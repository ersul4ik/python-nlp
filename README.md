The simple app to learn NLP with python and MongoDB.

How to run:

1. make sure you have installed python (at least 3.8 version)
2. python -m pip install -r requirements.txt
3. set environment variable: MONGO_URL
4. uvicorn main:app --reload
5. open API spec: http://127.0.0.1:8000/docs


The app should have:
- [x] API to handle requests
- [x] API should have ability to receive data from the requester payload
- [x] API should have ability to split received data before storing it on DB
- [x] API should have ability to search by world.
