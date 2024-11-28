from fastapi import HTTPException
from src.services import project_service, history_service

async def get_history(project_id: str):
    try:
        # Get project information
        result = await project_service.get_project(project_id = project_id)

        # Extract necessary information
        project_info = {
            "name": result.name,
            "one_liner": result.oneLiner,
            "description": result.description,
        }

        # Get submission history
        result = await history_service.get_submission_history(project_id = project_id)
        
        # Extract necessary information
        submission_history = []
        for submission in result:
            submission_history.append({
                "week": submission.week,
                "progress_comment": submission.progressComment,
                "output_url": submission.outputUrl,
                "feedback": [
                    {
                        "user_name": feedback.User.name if feedback.User else None,
                        "evaluation_rate": feedback.evaluationRate,
                        "evaluation_comment": feedback.evaluationComment,
                    }
                    for feedback in submission.Feedback
                ]
            })

        # Organize the data
        data = {
            "project_info": project_info,
            "submission_history": submission_history
        }
        
        return data
    except Exception as e:
        print("history_controller.py" ,{e})
        raise HTTPException(status_code = 500, detail="Error fetching progress history (Controller)")

