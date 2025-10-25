from fastapi import APIRouter

router = APIRouter(prefix="/terms", tags=["Términos y Condiciones"])

@router.get("/")
def show_terms():
    return {
        "page": "Términos y Condiciones",
        "message": (
            "Bienvenido/a a *Empire of Wagers*, un juego académico inspirado en la dinámica del blackjack. "
            "Antes de continuar, te pedimos que leas atentamente y aceptes los siguientes Términos y Condiciones, "
            "los cuales describen las normas, responsabilidades y propósitos de este proyecto.\n\n"

            "1. **Naturaleza del juego**: *Empire of Wagers* es un desarrollo universitario con fines educativos, "
            "orientado al estudio de sistemas distribuidos, el diseño interactivo y la toma de decisiones estratégicas. "
            "El juego no involucra apuestas reales, dinero, premios materiales ni ningún tipo de intercambio económico. "
            "Todas las partidas, resultados y recompensas son puramente simbólicos y tienen un propósito académico y recreativo.\n\n"

            "2. **Mecánica general**: La base de *Empire of Wagers* se inspira en la lógica del blackjack clásico. "
            "El objetivo principal es sumar cartas para acercarse lo más posible a un valor límite (21) sin superarlo. "
            "Durante cada ronda, el jugador deberá decidir si tomar nuevas cartas, mantenerse o arriesgar, "
            "ponderando la suerte y la estrategia. Aunque existe un componente de azar, las decisiones racionales "
            "influyen directamente en el curso y resultado de cada enfrentamiento.\n\n"

            "3. **Uso de datos**: Este proyecto no recopila información personal sensible ni realiza almacenamiento permanente "
            "de datos fuera del entorno académico. Los nombres de usuario, puntuaciones o progresos generados "
            "serán utilizados exclusivamente con fines de evaluación o demostración dentro del curso correspondiente.\n\n"

            "4. **Conducta y ética**: Al participar en *Empire of Wagers*, el usuario se compromete a actuar de forma justa y responsable. "
            "Está prohibido manipular el código, alterar las probabilidades del juego o intentar obtener ventajas indebidas. "
            "El objetivo es fomentar la integridad académica, la comprensión del azar controlado y el respeto por las reglas del sistema.\n\n"

            "5. **Aceptación de los términos**: Al presionar 'Jugar' o continuar dentro del sistema, declaras haber leído, comprendido "
            "y aceptado íntegramente estos Términos y Condiciones. Reconoces que tu participación es voluntaria y que entiendes "
            "la finalidad académica y experimental del proyecto.\n\n"

            "Si no estás de acuerdo con alguno de los puntos aquí descritos, te recomendamos no continuar. "
            "Tu participación en *Empire of Wagers* implica la aceptación total de estos Términos y Condiciones."
        )
    }
