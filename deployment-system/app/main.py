from fastapi import FastAPI
from app.routes import deployments, users, projects
from app.db.database import engine
from app.models import db_models
#Create DB tables
db_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#include routes
app.include_router(deployments.router)
app.include_router(users.router)
app.include_router(projects.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Deployment System API!"}

