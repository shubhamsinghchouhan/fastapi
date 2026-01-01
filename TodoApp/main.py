# root file

from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

# Create new Database in FastApi
models.Base.metadata.create_all(bind=engine)