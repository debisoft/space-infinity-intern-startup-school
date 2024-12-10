from fastapi import APIRouter, Form
from src.controllers import submission_controller as controller

router = APIRouter()

# Get application project information
@router.post("/submission/project/{project_id}")
async def get_project(project_id: str):
    result = await controller.get_project(project_id = project_id)
    return result

# Update submission records when submitting progress
@router.post("/submission/complete/{project_id}")
async def register_progress_complete(
    project_id: str,
    progress_score: int = Form(...),
    progress_comment: str = Form(...),
    upload_link: str = Form(...)
):
    submission_status = "Reviewing"
    is_registered =  await controller.register_progress(
        project_id = project_id,
        progress_score = progress_score,
        progress_comment = progress_comment,
        upload_link = upload_link,
        submission_status = submission_status,
    )
    print("submission_router.py completed result:", is_registered)

    if is_registered:
        message = "Submission registered successfully!"
    else:
        message = "Submission registration failed!"

    return JSONResponse(content={"result": is_registered, "message": message})


# Update submission records when not submitting progress
@router.post("/submission/incomplete/{project_id}")
async def register_progress_incomplete(
    project_id: str,
):
    submission_status = "Incomplete"
    is_registered =  await controller.register_progress(
        project_id = project_id,
        progress_score = None,
        progress_comment = None,
        upload_link = None,
        submission_status = submission_status,
    )
    print("submission_router.py incomplete result:", is_registered)
    
    if is_registered:
        message = "Submission registered successfully! (Incomplete)"
    else:
        message = "Submission registration failed! (Incomplete)"

    return JSONResponse(content={"result": is_registered, "message": message})