# FastAPI app
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import upload, analyze, summarize, extract

app = FastAPI(title="LawMind Backend")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(analyze.router)
app.include_router(summarize.router)
app.include_router(extract.router)