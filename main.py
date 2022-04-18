from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.responses import JSONResponse

from models import Item

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


@app.post("/items/")
async def create_item(item: Item):
    """Creates items"""
    return NotImplementedError()


@app.get("/items/")
async def get_items():
    """Returns items."""
    return NotImplementedError()


@app.get("/items/search/")
async def get_items(value: str):
    """Search items by given value."""
    return NotImplementedError()
