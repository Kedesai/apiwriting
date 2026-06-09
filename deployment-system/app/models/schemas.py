from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DeploymentRequest(BaseModel):
    app_name: str
    project_id: int
    version: str
    environment: str
    initiated_by: str

class DeploymentResponse(BaseModel):
    deployment_id: int
    project_id: int
    version: str
    environment: str
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class DeploymentStatus(BaseModel):
        status: str
        message: Optional[str] = None
        PENDING: str = "pending"
        IN_PROGRESS: str = "in_progress"
        COMPLETED: str = "completed"
        FAILED: str = "failed"