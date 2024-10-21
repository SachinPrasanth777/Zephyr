from utilities.admin import supabase


def bucket_exists(bucket_name: str):
    try:
        existing_buckets = supabase.storage.list_buckets()
        if not any(bucket["name"] == bucket_name for bucket in existing_buckets):
            supabase.storage.create_bucket(bucket_name)
    except Exception:
        pass
