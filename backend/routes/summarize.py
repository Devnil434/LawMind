from fastapi import APIRouter, HTTPException
from ..services import report_service

router = APIRouter(prefix="/summarize", tags=["summarize"])

@router.post("/")
async def summarize_document(request: dict):
    text = request.get("text", "")
    if not text:
        raise HTTPException(status_code=400, detail="No text provided for summarization")
    
    try:
        # Use report service for summarization
        summary = await report_service.generate_summary(text)
        return {"message": "Document summarized successfully", "summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during summarization: {str(e)}")