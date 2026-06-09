from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import time
from fastapi import HTTPException
import threading
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ENV = os.getenv("ENV", "dev")

class DeploymentRequest(BaseModel): # Define Data Model for Deployment Request
    app_name: str
    version: str

app = FastAPI() # Create FastAPI instance

deployments = {} # In-memory storage for deployments



@app.post("/deployments") # Define POST endpoint for creating deployments
def create_deployment(request: DeploymentRequest):
    deployment_id = str(uuid.uuid4()) # Generate unique deployment ID

    logger.info(f"Creating deployment: {request.app_name} version {request.version} with ID {deployment_id}")
    deployments[deployment_id] = {
        "app_name": request.app_name,
        "version": request.version,
        "status": "pending"
    }
   

@app.get("/deployments/{deployment_id}") # Define a GET endpoint for retrieving deployment status
def get_deployment(deployment_id: str): #Add GET by ID endpoint
    if deployment_id not in deployments:
        raise HTTPException(status_code=404, detail={"error": "Deployment not found"}) 
    return deployments[deployment_id]

@app.get("/deployments") # Define a GET endpoint for retrieving all deployments
def list_deployments():
    return deployments

@app.get("/home") # Define a GET endpoint for the home page
def home():
    return {"message": "Welcome to the Deployment API!", "environment": ENV 
    }

@app.delete("/deployments/{deployment_id}") # Define a DELETE endpoint for deleting a deployment
def delete_deployment(deployment_id: str):
    if deployment_id not in deployments:
        raise HTTPException(status_code=404, detail={"error": "Deployment not found"}) 
    del deployments[deployment_id]
    return {"message": "Deployment deleted successfully"}    
def process_deployment(deployment_id: str): # Simulate deployment processing
    logger.info(f"Processing deployment ID {deployment_id}")
    time.sleep(5) # Simulate time-consuming deployment process
    deployments[deployment_id]["status"] = "deployed" # Update deployment status to deployed   
    threading.Thread(target=process_deployment, args=(deployment_id,)).start() # Start deployment processing in a separate thread
    #return {"deployment_id": deployment_id, "status": "pending"}