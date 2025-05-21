from fastapi import FastAPI

from src.controllers.product import product_router
from src.controllers.users import user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(product_router)
