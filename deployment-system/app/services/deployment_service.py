import uuid
import time
from datetime import datetime
from threading import Thread
#from app.db.database import deployments, deployment_logs - commented so that it can be used with DB instead of in-memory storage
from app.utils.logger import logger
from sqlalchemy.orm import Session
from app.models.db_models import Deployment

#Create a deployment
def create_deployment(data, db: Session):
    deployment_id = str(uuid.uuid4())
    
    new_deployment = Deployment(
        deployment_id=deployment_id,
        app_name=data.app_name,
        project_id=data.project_id,
        version=data.version,
        environment=data.environment,
        initiated_by=data.initiated_by,
        status="pending",
        created_at=datetime.utcnow()
    )
    db.add(new_deployment)
    db.commit()
    db.refresh(new_deployment)

    #deployment_logs[deployment_id] = [ - Uncomment to use DB instead of in-memory storage
    #    f"Deployment created at {datetime.utcnow()}"
    #]

    logger.info(f"Deployment {deployment_id} created")

#Start Backgroung Process

    Thread(target=process_deployment, args=(deployment_id,)).start()
    return new_deployment

# Background Processing
def process_deployment(deployment_id: str):
    from app.db.database import SessionLocal
    db = SessionLocal()


    try:
        deployment = db.query(Deployment).filter(
            Deployment.deployment_id == deployment_id
        ).first()

        if not deployment:
            db.close()
            return

        #  Set to running
        deployment.status = "running"
        db.commit()

        time.sleep(5)

        #  Mark success
        deployment.status = "success"
        deployment.updated_at = datetime.utcnow().isoformat()
        db.commit()

    except Exception as e:
        #  Handle failure correctly
        deployment = db.query(Deployment).filter(
            Deployment.deployment_id == deployment_id
        ).first()

        if deployment:
            deployment.status = "failed"
            deployment.updated_at = datetime.utcnow().isoformat()
            db.commit()

        logger.error(f"Deployment failed {deployment_id}: {str(e)}")

    finally:
        db.close()

    #try:
    #    deployments[deployment_id]["status"] = "running"
    #    deployment_logs[deployment_id].append(f"Deployment started at {datetime.utcnow()}")
    #    logger.info(f"Deployment {deployment_id} started")

        # Simulate deployment time
    #    time.sleep(5)

    #    deployments[deployment_id]["status"] = "deployed"
    #    deployment_logs[deployment_id].append(f"Deployment completed at {datetime.utcnow()}")
    #    logger.info(f"Deployment {deployment_id} completed")

    #except Exception as e:
    #    #deployments[deployment_id]["status"] = "failed" - commented to use DB instead of in-memory storage
    #    deployment_logs[deployment_id].append(f"Deployment failed at {datetime.utcnow()}: {str(e)}")
    #    logger.error(f"Deployment {deployment_id} failed: {str(e)}")


#Get deployment by ID
def get_deployment(deployment_id: str, db: Session):
    return db.query(Deployment).filter(Deployment.deployment_id == deployment_id).first()


#List all deployments
def list_deployments(db: Session):
    return db.query(Deployment).all()

#Delete Deployment
def delete_deployment(deployment_id: str, db: Session):
    deployment = get_deployment(deployment_id, db)
    if not deployment:
        return False
    db.delete(deployment)
    db.commit()
    logger.info(f"Deployment {deployment_id} deleted")
    return True


#Get deployment logs - Uncomment to use DB instead of in-memory storage
#def get_deployment_logs(deployment_id: str, db: Session):
#    return db.query(DeploymentLog).filter(DeploymentLog.deployment_id == deployment_id).all()
