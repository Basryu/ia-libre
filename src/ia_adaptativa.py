# IA Adaptativa Libre para Videojuegos
# Idea y diseño original por Ximena Gómez Lucero (2025)
# Asistencia técnica en prototipado por herramientas de IA
# Publicado como PRIOR ART bajo Licencia MIT

from collections import Counter

class SistemaIAAdaptativa:
    def __init__(self):
        self.historial_dificultad = []
        self.movimientos_usados = []
        self.prestigio = 0  # Antes 'prestigio'

    def registrar_pelea(self, dificultad, movimientos):
        """Registra el resultado de una pelea y los movimientos usados."""
        self.historial_dificultad.append(dificultad)
        self.movimientos_usados.extend(movimientos)

        # Ajuste de prestigio
        if dificultad == "fácil":
            self.prestigio += 10
        elif dificultad == "media":
            self.prestigio += 5
        else:
            self.prestigio += 2

    def ajustar_enemigo(self):
        """Devuelve configuración del próximo enemigo."""
        if self.historial_dificultad.count("fácil") > len(self.historial_dificultad) / 2:
            dificultad = "difícil"
        elif self.historial_dificultad.count("difícil") > len(self.historial_dificultad) / 2:
            dificultad = "media"
        else:
            dificultad = "media"

        # Movimiento más usado por el jugador
        mov_pref = Counter(self.movimientos_usados).most_common(1)
        if mov_pref:
            contra_estrategia = f"Defender contra {mov_pref[0][0]}"
        else:
            contra_estrategia = "Estrategia estándar"

        return {
            "dificultad": dificultad,
            "estrategia": contra_estrategia,
            "prestigio_jugador": self.prestigio
        }

# Ejemplo de uso
if __name__ == "__main__":
    ia = SistemaIAAdaptativa()
    ia.registrar_pelea("fácil", ["espada", "espada", "arco"])
    ia.registrar_pelea("fácil", ["espada", "magia"])
    ia.registrar_pelea("media", ["arco", "arco", "espada"])
    print(ia.ajustar_enemigo())
