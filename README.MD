# SOKOBAN

## 1. Objetivo

### 1.1 General

Programar el juego Sokoban en una versión retro para consola.

### 1.2 Específicos

- Aplicar los conocimientos básicos de programación orientada a objetos con Python (Clases, Objetos, Métodos, Variables, Arrays, Bucles, Leer desde teclado, Decisiones, etc.).

- Utilizar ingeniería de software para analizar, diseñar y desarrollar el juego.

- Utilizar Kanban para dar seguimiento a las actividades a realizar ToDo, Doing, Done.

- Utilizar Hitos (Milestones) para cada una de las etapas del desarrollo.

- Documentar el código generado.

## 2. Reglas del juego

El juego sokoban consiste en recorrer un mapa en forma de laberinto para empujar cajas que estan repartidas en el mapa, hacia puntos determinados por las metas, y tiene las siguientes reglas:

1. El personaje se puede mover hacia arriba, abajo, izquierda y derecha.
2. El personaje solo puede empujar 1 caja hacia arriba, abjo, izquierda o derecha.
3. El personaje se moverá en un mapa predefinido.
4. Para terminar el nivel se tienen que acomodar todas las cajas sobre las metas.
5. El nivel de dificultad no está determinado necesariamente por la cantidad de cajas y metas.

## 3. Elementos del juego

Sokoban tiene 2 partes principales de juego, el mapa donde se va jugar y los elementos (personaje, cajas, metas, paredes y piso).

### 3.1 Mapa de juego

Cada nivel del juego se colocará dentro de una array bidimensional, colocando números para representar los elementos de juego, a continuación se tiene un ejemplo básico de nivel.

````code
self.mapa = [
            [2, 2, 2, 2, 2, 2, 2],
            [2, 4, 4, 4, 4, 4, 2],
            [2, 4, 4, 0, 4, 4, 2],
            [2, 4, 4, 4, 4, 4, 2],
            [2, 2, 2, 2, 2, 2, 2],
        ]
````

### 3.2 Lista de elementos

Para esta versión del sokoban se utilizarán numeros para representar cada uno de los elementos del juego.

"personaje":0,
            "caja":1,
            "pared":2,
            "meta":3,
            "camino":4,
            "caja_meta":5,
            "personaje_meta":6

| Número | Interpretación |
| --- | --- |
| 0 | Personaje |
| 1 | Caja |
| 2 | Pared |
| 3 | Meta |
| 4 | Camino |
| 5 | Caja_meta |
| 6 | Personaje_meta |

## 4. Controles

Para moverse en el juego el usuario utilizará alguna de las siguientes letras para indicar hacia adonde se quiere mover:

| Letra | Dirección del movimiento |
| -- | -- |
| a | Izquierda |
| d | Derecha |
| w | Arriba |
| s | Abajo |

## 5. Modo de juego

El juego consiste mostrar el mapa y solicitar al usuario que escriba la letra hacia donde se quiere mover, despúes de colocar la letra se presiona enter, se evalua el moviento, si es un movimiento valido se realiza el cambio en el array, es decir se actualiza el mapa, y se repite este proceso forma infinita, hasta que se hayan terminado de acomodar todas las cajas sobre las metas.

## 6. Funciones a implementar

| Actividad | Estado | Inicio | Fin | Fecha de terminación |
|---|---|---|---|---|
| Crear la clase Sokoban | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Definir los elementos numéricos | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Crear el mapa inicial | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Definir las posiciones iniciales | Done | 08/10/2026 | 08/10/2026 | 08/10/2026 |
| Implementar el reinicio del nivel | Done | 09/10/2026 | 09/10/2026 | 09/10/2026 |
| Validar las posiciones del mapa | Done | 09/10/2026 | 09/10/2026 | 09/10/2026 |
| Construir el mapa visible | Done | 09/10/2026 | 09/10/2026 | 09/10/2026 |
| Imprimir el tablero en la terminal | Done | 09/10/2026 | 09/10/2026 | 09/10/2026 |
| Leer y evaluar los movimientos | Done | 09/10/2026 | 09/10/2026 | 09/10/2026 |
| Implementar los cuatro movimientos | Done | 09/10/2026 | 09/10/2026 | 09/10/2026 |
| Implementar el movimiento de cajas | Done | 09/10/2026 | 09/10/2026 | 09/10/2026 |
| Conservar las metas | Done | 09/10/2026 | 09/10/2026 | 09/10/2026 |
| Implementar la condición de victoria | Done | 09/10/2026 | 09/10/2026 | 09/10/2026 |
| Mostrar instrucciones y mensajes | Done | 09/10/2026 | 09/10/2026 | 09/10/2026 |
| Probar los escenarios de movimiento |Done| 09/10/2026 | 12/10/2026 | 12/10/2026 |
| Revisar la documentación final | Done | 09/10/2026 | 12/10/2026 | 12/10/2026 |
| Cargar niveles desde archivos externos | ToDo | — | — | — |
| Avanzar automáticamente a otro nivel | ToDo | — | — | — |


### 6.2 Funciones generales

| Función | Descripción | Estado |
|---|---|---|
| __init__() | Inicializa los elementos, el mapa y las posiciones. | Done |
| limpiarPantalla() | Limpia la terminal. | Done |
| reiniciarNivel() | Restaura las posiciones iniciales. | Done |
| posicionValida() | Comprueba los límites del mapa. | Done |
| esPared() | Verifica si una casilla es una pared. | Done |
| esMeta() | Comprueba si una posición es una meta. | Done |
| esCaja() | Comprueba si una posición contiene una caja. | Done |
| iniciarJuego() | Crea el objeto e inicia la partida. | Done |

### 6.3 Funciones de impresión del mapa

| Función | Descripción | Estado |
|---|---|---|
| obtenerElemento() | Determina el número que se muestra en cada casilla. | Done |
| construirMapaVisible() | Construye la matriz con las posiciones actuales. | Done |
| imprimirMapa() | Imprime el tablero y los contadores. | Done |

### 6.4 Funciones de entrada y control

| Función | Descripción | Estado |
|---|---|---|
| leerMovimiento() | Solicita una tecla al usuario. | Done |
| evaluarMovimiento() | Ejecuta la acción correspondiente. | Done |
| procesarTurno() | Actualiza la pantalla y procesa una jugada. | Done |
| jugar() | Controla el ciclo principal del juego. | Done |
| mostrarInstrucciones() | Explica los controles y elementos. | Done |

### 6.5 Funciones para calcular posiciones

| Función | Descripción | Estado |
|---|---|---|
| calcularDestino() | Calcula la siguiente posición del personaje. | Done |
| calcularDestinoCaja() | Calcula la siguiente posición de una caja. | Done |
| destinoLibre() | Comprueba si una casilla está libre para una caja. | Done |

**Observación:** destinoLibre() está implementada, aunque no se utiliza directamente en el flujo actual de movimiento.

### 6.6 Funciones de movimiento

| Función | Descripción | Estado |
|---|---|---|
| moverPersonaje() | Actualiza la posición del personaje y cuenta el movimiento. | Done |
| moverCaja() | Actualiza la posición de una caja. | Done |
| validarEmpuje() | Verifica si una caja puede desplazarse. | Done |
| mover() | Centraliza las validaciones y actualiza las posiciones. | Done |
| derecha() | Mueve al personaje a la derecha. | Done |
| izquierda() | Mueve al personaje a la izquierda. | Done |
| arriba() | Mueve al personaje hacia arriba. | Done |
| abajo() | Mueve al personaje hacia abajo. | Done |

### 6.7 Funciones de victoria

| Función | Descripción | Estado |
|---|---|---|
| verificarMeta() | Comprueba si todas las metas tienen cajas. | Done |
| nivelCompletado() | Detecta la victoria y establece el mensaje correspondiente. | Done |

## 7. Casos de movimiento

Los siguientes escenarios están documentados en los comentarios del código y deben comprobarse durante las pruebas.

| Caso | Escenario | Estado |
|---|---|---|
| 1 | Personaje hacia un camino libre. | Done |
| 2 | Personaje hacia una meta. |  Done |
| 3 | Personaje empuja una caja hacia un camino libre. |  Done  |
| 4 | Personaje empuja una caja hacia una meta. |  Done  |
| 5 | Personaje sale de una meta. |  Done  |
| 6 | Personaje se mueve entre posiciones con metas. |  Done  |
| 7 | Caja sale de una meta y esta se conserva. | Done |
| 8 | Caja se mueve hacia otra meta libre. | Done |
| 9 | Personaje intenta empujar una caja contra una pared. | Done |
| 10 | Personaje intenta empujar una caja contra otra caja. |  Done  |
| 11 | Personaje intenta salir de los límites del mapa. |  Done |
| 12 | Personaje sobre una meta se representa con el valor 6. |  Done  |

## 8. Hitos del desarrollo (Milestones)

| Hito | Actividades | Estado |
|---|---|---|
| Hito 1: Estructura inicial | Crear la clase, el mapa y los elementos. | Done |
| Hito 2: Representación del tablero | Construir e imprimir el mapa visible. | Done |
| Hito 3: Movimientos del personaje | Implementar direcciones y validar posiciones. | Done |
| Hito 4: Movimiento de cajas | Implementar empujes y evitar movimientos inválidos. | Done |
| Hito 5: Condición de victoria | Comprobar las metas y finalizar el nivel. | Done |
| Hito 6: Pruebas y documentación | Verificar escenarios y registrar resultados. | Doing |
| Hito 7: Niveles adicionales | Cargar mapas externos y avanzar entre niveles. | ToDo |

## 9. Pruebas funcionales

| Prueba | Resultado esperado | Estado |
|---|---|---|
| Mover al personaje hacia un camino libre | El personaje cambia de posición. | Done |
| Intentar atravesar una pared | El movimiento se cancela. | Done |
| Empujar una caja hacia una casilla libre | La caja se mueve y el personaje ocupa su lugar anterior. | Done |
| Empujar una caja contra una pared | La caja no se mueve. | Done |
| Empujar una caja contra otra caja | El movimiento se cancela. | Done |
| Mover una caja hacia una meta | La caja se representa con el valor 5. | Done |
| Intentar salir del mapa | El movimiento se cancela. | Done |
| Reiniciar con la tecla r | Se recuperan las posiciones iniciales. | Done |
| Salir con la tecla q | El juego termina. | Done |
| Completar todas las metas | Se muestra el mensaje de victoria. | Done |

## 10. Conclusión

El desarrollo de Sokoban permitió organizar el código mediante una clase y diferentes métodos para controlar los movimientos, representar el tablero y validar las acciones del jugador. También se implementaron el movimiento de las cajas, la conservación de las metas, el reinicio de la partida y la condición de victoria.

El tablero Kanban permite identificar las actividades realizadas y las tareas pendientes. Como mejora futura, se propone implementar la carga de niveles desde archivos externos y el avance automático entre diferentes mapas.
  
  **Elaborado por:** Jean Marco Galeano Ramos.