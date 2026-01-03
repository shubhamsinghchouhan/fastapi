# root file

from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos, admin, users

app = FastAPI()

# Create new Database in FastApi
models.Base.metadata.create_all(bind=engine)

# routers
# to include other python server files
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)