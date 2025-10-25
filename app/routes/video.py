from fastapi import APIRouter

router = APIRouter(prefix="/video", tags=["Video del Proyecto"])

@router.get("/")
def show_video():
    return {
        "page": "Video del Proyecto",
        "description": (
            "Este es el video oficial de presentación del proyecto **Empire of Wagers**, "
            "donde se explica la idea general, la mecánica del juego y los objetivos académicos del desarrollo."
        ),
        "video_url": "https://youtu.be/tXID7xGFH6c"
    }
