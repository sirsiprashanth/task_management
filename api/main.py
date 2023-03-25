from fastapi import FastAPI
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from database_config import database
from router import ConfigureRoutes

origins = [
    "*",
]

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(
    middleware=middleware,
    docs_url="/docs",
    redoc_url="/redocs",
    title="TaskMGMT API",
    version="1.0.0",
    openapi_url="/openapi.json",
)


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return await request_validation_exception_handler(request, exc)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

ConfigureRoutes.__init__(app)


@app.get("/", include_in_schema=False)
async def read_root():
    return {"message": "Hello World"}
