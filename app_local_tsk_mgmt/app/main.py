from fastapi import FastAPI
from database import engine
import models
from schemas import Users
from routers import Authentication, Users



app = FastAPI()
app.include_router(Authentication.router)
app.include_router(Users.router)

models.Base.metadata.create_all(bind=engine)

