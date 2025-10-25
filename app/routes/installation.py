from fastapi import APIRouter

router = APIRouter(prefix="/installation", tags=["Instalación"])

@router.get("/")
def installation_instructions():
    return {
        "page": "Guía de Instalación",
        "message": (
            "El juego **Empire of Wagers** se ejecuta directamente en el navegador web. "
            "No es necesario realizar ninguna instalación adicional en tu dispositivo. "
            "Pronto podrás acceder al juego a través del enlace oficial del frontend. "
            "Actualmente, el enlace aún no está disponible."
        )
    }
