from sqlmodel import Session, select
from app.models.project import Project

class ProjectCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create(self, project: Project):
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def list(self):
        return self.db.exec(select(Project)).all()

    def get(self, project_id: int):
        return self.db.get(Project, project_id)
