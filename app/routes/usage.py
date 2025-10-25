from fastapi import APIRouter

router = APIRouter(prefix="/usage", tags=["Uso del Juego"])

@router.get("/")
def usage_instructions():
    return {
        "page": "Instrucciones de Uso y Reglas del Juego",
        "details": [
            "**Empire of Wagers** es un juego de cartas inspirado en el blackjack clásico, "
            "diseñado para partidas cortas y dinámicas donde la estrategia y el azar se combinan.",
            "",
            "**Objetivo principal:** acercarte lo más posible al valor de 21 sin superarlo. "
            "Si te pasas, pierdes la ronda automáticamente. El oponente también buscará acercarse a 21.",
            "",
            "**Sistema de vida:** cada jugador comienza con 60 puntos de vida (HP). "
            "Cada vez que pierdes una ronda, pierdes una cantidad de vida igual al valor total de tu mano. "
            "Por ejemplo, si terminas con 24 puntos, pierdes 24 de vida. "
            "Si terminas con 18 puntos y el oponente tiene 20, pierdes 18 de vida. "
            "Si empatan, nadie pierde vida.",
            "",
            "**Duración estimada:** una partida típica dura entre 3 y 4 rondas, "
            "dependiendo de las decisiones del jugador y del uso de los modificadores.",
            "",
            "**Derrota:** si tu vida llega a 0, pierdes inmediatamente.",
            "**Victoria:** ganas cuando todos los oponentes llegan a 0 HP.",
            "",
          "**Reglas básicas del turno:**",
            "1. Cada jugador comienza con dos cartas visibles solo para sí mismo.",
            "2. Durante tu turno puedes elegir entre Pedir (draw) o Plantarte (stand).",
            "3. Las decisiones de cada jugador se mantienen en secreto hasta que ambos hayan actuado, "
            "de modo que el oponente no puede saber si pediste o te plantaste.",
            "4. Una vez que ambos jugadores confirman su decisión, se revelan los valores totales de las manos. "
            "El más cercano a 21 gana la ronda.",
            "5. En caso de empate, ninguno pierde vida.",
            "",
          "**Modificadores del juego (10 en total):**",
            "1. **Suerte del Novato:** una vez por partida, si tu total supera 21, se ajusta automáticamente a 20 y se marca como usado.",
            "2. **Robo Preciso:** al activarse, la siguiente carta que tomes tendrá un valor fijo entre 2 y 6. Luego se desactiva.",
            "3. **Escudo de Hierro:** reduce el daño recibido en la próxima derrota en un 50%. Se activa una sola vez cada tres rondas.",
            "4. **Doble Riesgo:** al activarlo, duplicas tu daño potencial. Si ganas, curas 6 HP; si pierdes, el daño se duplica.",
            "5. **Golpe Crítico:** si logras exactamente 21, infliges 8 puntos adicionales de daño al oponente.",
            "6. **Reinicio de Mano:** puedes descartar todas tus cartas y recibir una nueva mano una sola vez por partida.",
            "7. **Vista Parcial:** una vez por ronda, puedes ver el valor de una carta aleatoria del oponente.",
            "8. **Recuperación:** si pierdes por una diferencia menor o igual a 5 puntos, recuperas 5 HP al final de la ronda.",
            "9. **Bloqueo de Efecto:** impide que el oponente use su modificador en la siguiente ronda.",
            "10. **Última Apuesta:** cuando tu vida sea menor o igual a 15 HP, comienzas cada mano con un As adicional.",
            "",
            "**Consejos estratégicos:**",
            "- Plantarte en el momento justo es más importante que perseguir siempre el 21.",
            "- Usa tus modificadores con inteligencia: una activación bien empleada puede cambiar el resultado de la partida.",
            "- Los oponentes agresivos suelen pasarse; observa sus patrones antes de arriesgarte.",
            "",
            "**Resumen general:**",
            "- Límite de puntos: 21",
            "- Vida inicial: 60 HP",
            "- Pierdes vida igual al valor de tu mano si pierdes.",
            "- Duración media: 3–4 rondas por partida.",
            "- No se gana vida por victoria directa (solo con modificadores).",
            "- 10 modificadores activos equilibrados para partidas rápidas.",
            "",
            "*Empire of Wagers* combina probabilidad, riesgo y cálculo rápido. "
            "Pensar antes de pedir una carta puede ser la diferencia entre la victoria y la derrota."
        ]
    }
