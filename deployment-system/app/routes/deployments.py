from fastapi import APIRouter
from app.models.schemas import DeploymentRequest
from app.services import deployment_service
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter(prefix="/deployments", tags=["deployments"])

@router.post("/")
def create_deployment(request: DeploymentRequest, db: Session = Depends(get_db)):
    return deployment_service.create_deployment(request, db)


@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return deployment_service.list_deployments(db)

@router.get("/{deployment_id}")
def get_one(deployment_id: str, db: Session = Depends(get_db)):
    deployment = deployment_service.get_deployment(deployment_id, db)
    if not deployment:
        raise HTTPException(status_code=404, detail="Deployment not found")
    return deployment


@router.delete("/{deployment_id}")
def delete(deployment_id: str, db: Session = Depends(get_db)):
    if not deployment_service.delete_deployment(deployment_id, db):
        raise HTTPException(status_code=404, detail="Deployment not found")
    return {"message": f"Deployment {deployment_id} deleted successfully"}

#@router.get("/{deployment_id}/logs") - Uncomment to use DB instead of in-memory storage
#def get_logs(deployment_id: str, db: Session = Depends(get_db)  ):
#    return deployment_service.get_deployment_logs(deployment_id, db)