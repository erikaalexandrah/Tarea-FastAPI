from fastapi import APIRouter

router = APIRouter(prefix="/register", tags=["Registro"])

@router.get("/")
def show_register():
    return {
        "page": "Registro de Usuario",
        "description": (
            "Para participar en **Empire of Wagers**, cada jugador debe crear una cuenta de usuario. "
            "El registro permite guardar tu progreso, tus estadísticas y tus resultados en las partidas. "
            "El proceso de registro se realiza desde la interfaz web oficial del juego, donde deberás ingresar un nombre de usuario y una contraseña. "
            "Una vez completado, podrás acceder al sistema, crear o unirte a partidas y utilizar tus modificadores personalizados. "
            "Actualmente, el formulario de registro solo está disponible desde el cliente web. "
            "Pronto se habilitará el enlace oficial de acceso."
        )
    }
