from os import getenv

import nltk
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.responses import JSONResponse
import motor.motor_asyncio

from models import Text
from services import get_words, company_helper

app = FastAPI()
nltk.download('punkt')
MONGO_DETAILS = getenv('MONGO_URL')
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.parser


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


@app.post("/companies/")
async def create_company(payload: Text):
    """Creates companies"""
    words = get_words(payload.description)
    company_collection = database.get_collection("companies")
    company_collection.insert_one({'company_name': payload.company_name, 'description_key_words': words})
    return {'company_name': payload.company_name}


@app.get("/companies/")
async def get_companies():
    """Returns companies."""
    companies = []
    async for company in database.get_collection("companies").find():
        companies.append(company_helper(company))
    return {'companies': companies}


@app.get("/companies/search/")
async def search_company(value: str):
    """Search companies by given value."""
    companies = []
    company_collection = database.get_collection("companies")
    results = company_collection.find({'description_key_words': value})
    async for company in results:
        companies.append(company_helper(company))
    return {'results': companies}
