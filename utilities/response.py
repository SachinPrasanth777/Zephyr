from fastapi import Response
from json import dumps


class JSONResponse(Response):
    def __init__(
        self,
        content: dict,
        status_code=200,
        media_type="application/json",
        *args,
        **kwargs
    ):
        super().__init__(
            content=dumps(content),
            status_code=status_code,
            media_type=media_type,
            *args,
            **kwargs
        )
