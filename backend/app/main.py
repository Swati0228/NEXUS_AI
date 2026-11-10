from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="NexusAI API",
    description="Backend API for NexusAI - Autonomous Multi-Agent Research Copilot",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "NexusAI Backend",
        "version": "0.1.0",
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
