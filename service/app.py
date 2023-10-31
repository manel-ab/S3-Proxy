"""Main for all the services"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

from service.utils.types import ServiceResponse
from service.routes import upload_file

app = FastAPI()


@app.exception_handler(Exception)
async def handle_internal_server_error(*_args) -> JSONResponse:
    """Handles an internal server error."""
    service_response: ServiceResponse = {
        "statusCode": 500,
        "body": {"message": "Internal server error"},
    }
    return JSONResponse(
        status_code=service_response["statusCode"],
        content=service_response,
    )


app.include_router(upload_file.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
