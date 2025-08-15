# IA Adaptativa Libre para Videojuegos

Idea y diseño original por Ximena Gómez Lucero (2025)   
Asistencia técnica en documentación y prototipado por herramientas de IA.  

Este sistema propone una **IA adaptativa libre de patentes** que ajusta la dificultad y el comportamiento de enemigos y NPCs según el historial del jugador.  
Se publica como *prior art* para impedir patentes abusivas y permitir que cualquier desarrollador la implemente.

---

##Objetivo 
Crear una IA que:
- Aumente la dificultad si el jugador derrota enemigos fácilmente.
- Adapte estrategias enemigas según los movimientos favoritos del jugador.
- Ajuste la actitud de NPCs según el prestigio ganado.

---

##Componentes principales 

### Jugador
Atributos:
1. **Salud**
2. **Estamina**
3. **Hechizos**
4. **Lista de enemigos derrotados** con dificultad (fácil, media, difícil).
5. **Prestigio** (gana derrotando enemigos o eligiendo diálogos específicos). 

### Enemigos
- Recuerdan si enemigos similares fueron derrotados fácil/media/difícil.
- Ajustan fuerza y estrategia en base a esa memoria.

### NPCs
- Reaccionan al respeto del jugador con actitudes amistosa, neutral o hostil.

---

##Flujo básico 
1. El jugador derrota a un enemigo → se registra dificultad y movimientos usados.
2. El sistema ajusta prestigio y guarda datos en el historial. 
3. Futuros enemigos usan el historial para decidir:
   - Dificultad.
   - Estrategia (contraataque a movimientos frecuentes).
4. NPCs adaptan su actitud según el respeto actual.

---

## Ejemplo de uso 

Ver archivo [`src/ia_adaptativa.py`](src/ia_adaptativa.py)

---

##Licencia 
Se publica bajo Licencia MIT para uso libre y con atribución. 
