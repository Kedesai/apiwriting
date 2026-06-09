from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Deployment(Base):
    __tablename__ = "deployments"

    deployment_id = Column(String, primary_key=True, index=True)
    app_name = Column(String)
    project_id = Column(Integer)
    version = Column(String)
    environment = Column(String)
    initiated_by = Column(String)
    status = Column(String)
    created_at = Column(String)