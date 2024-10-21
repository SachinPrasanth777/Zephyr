from fastapi import APIRouter, UploadFile, File, HTTPException
from utilities.admin import supabase
from fastapi.responses import JSONResponse
from middleware.bucket import bucket_exists

bucket_router = APIRouter()


@bucket_router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        bucket_name = "testbucket"
        bucket_exists(bucket_name)

        path = f"{file.filename}"
        file_content = await file.read()

        response = supabase.storage.from_(bucket_name).upload(
            path=path,
            file=file_content,
            file_options={"content-type": file.content_type},
        )

        if response:
            return JSONResponse(
                content={
                    "message": "File uploaded successfully",
                    "path": path,
                },
                status_code=200,
            )
        else:
            raise HTTPException(
                status_code=500, detail="Failed to upload file to Supabase"
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@bucket_router.get("/retrieve")
async def retrieve():
    try:
        response = supabase.storage.list_buckets()
        buckets = [
            {
                "id": bucket.id,
                "name": bucket.name,
                "public": bucket.public,
                "created_at": bucket.created_at.isoformat(),
                "updated_at": bucket.updated_at.isoformat(),
                "file_size_limit": bucket.file_size_limit,
                "allowed_mime_types": bucket.allowed_mime_types,
            }
            for bucket in response
        ]
        return JSONResponse(status_code=200, content={"message": buckets})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@bucket_router.get("/retrieve/{bucket_name}")
async def retrieve_files(bucket_name: str):
    try:
        response = supabase.storage.get_bucket(bucket_name)
        files = supabase.storage.from_(bucket_name).list()
        if response:
            bucket = {
                "id": response.id,
                "name": response.name,
                "public": response.public,
                "created_at": response.created_at.isoformat(),
                "updated_at": response.updated_at.isoformat(),
                "file_size_limit": response.file_size_limit,
                "allowed_mime_types": response.allowed_mime_types,
                "files": files
            }
            return JSONResponse(status_code=200, content={"message": bucket})
        else:
            raise HTTPException(status_code=404, detail="Bucket not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
