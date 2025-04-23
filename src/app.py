from fastapi import FastAPI

from src.routes.products import product_router
from src.routes.users import user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(product_router)
