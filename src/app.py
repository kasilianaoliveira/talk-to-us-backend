from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse

from src.controllers.product import product_router
from src.controllers.users import user_router
from src.schemas.responses_messages import StandardErrorResponse

app = FastAPI()


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Handles HTTP exceptions to return a standardized error response.
    """
    error_response = StandardErrorResponse(
        code=exc.status_code,
        message=exc.detail,
        details=(
            {"path": request.url.path}
            if exc.status_code >= status.HTTP_500_INTERNAL_SERVER_ERROR
            else None
        ),
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=error_response.model_dump(exclude_none=True),
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """
    Handles any other uncaught exceptions, returning a standardized 500 error.
    """
    error_response = StandardErrorResponse(
        code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        message="Ocorreu um erro inesperado no servidor.",
        details={"error_type": type(exc).__name__, "message": str(exc)},
    )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=error_response.model_dump(exclude_none=True),
    )


app.include_router(user_router)
app.include_router(product_router)
