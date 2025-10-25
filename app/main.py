from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import register, terms, video, installation, usage

app = FastAPI(title="FastAPI SDD Project")

# Include routers
app.include_router(register.router)
app.include_router(terms.router)
app.include_router(video.router)
app.include_router(installation.router)
app.include_router(usage.router)

# Mount static directory (for videos, images, etc.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def root():
    return {"message": "Welcome to the main API"}
