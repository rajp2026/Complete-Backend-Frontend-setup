from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database import get_session
from app.models.project import Project
from app.crud.project import ProjectCRUD

router = APIRouter(prefix="/projects", tags=["Projects"])

def get_project_crud(db: Session = Depends(get_session)):
    return ProjectCRUD(db)

@router.post("/")
def create_project(project: Project, crud: ProjectCRUD = Depends(get_project_crud)):
    return crud.create(project)

@router.get("/")
def list_projects(crud: ProjectCRUD = Depends(get_project_crud)):
    return crud.list()

@router.get("/{project_id}")
def get_project(project_id: int, crud: ProjectCRUD = Depends(get_project_crud)):
    return crud.get(project_id)
