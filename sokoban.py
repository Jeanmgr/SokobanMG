import os

class Sokoban:
    def __init__(self):
        self.elementos = {
            "personaje": 0,
            "caja": 1,
            "pared": 2,
            "meta": 3,
            "camino": 4,
            "caja_meta": 5,
            "personaje_meta": 6,
        }

        # Mapa fijo: paredes y caminos.
        self.mapaInicial = [
            [2, 2, 2, 2, 2, 2, 2],
            [2, 4, 4, 4, 4, 4, 2],
            [2, 4, 4, 4, 4, 4, 2],
            [2, 4, 4, 4, 4, 4, 2],
            [2, 2, 2, 2, 2, 2, 2],
        ]

        # Posiciones iniciales .
        self.personajeInicial = (2, 3)
        self.cajasIniciales = {(2, 4), (3,4)}
        self.metasIniciales = {(2, 2), (3,2)}

        self.juegoActivo = True
        self.reiniciarNivel()

        # FUNCIONES GENERALES

    def limpiarPantalla(self):
        """Borra la pantalla antes de mostrar el nuevo tablero."""
        comando = "cls" if os.name == "nt" else "clear"
        resultado = os.system(comando)

        if resultado != 0:
            print("\033[2J\033[H", end="")

    def reiniciarNivel(self):
        """Restaura el único nivel a su estado original."""
        self.mapa = [fila[:] for fila in self.mapaInicial]
        self.personaje = self.personajeInicial
        self.cajas = set(self.cajasIniciales)
        self.metas = set(self.metasIniciales)
        self.movimientos = 0
        self.juegoActivo = True

    def posicionValida(self, fila, columna):
        """Comprueba que una posición esté dentro del mapa."""
        if fila < 0 or fila >= len(self.mapa):
            return False

        if columna < 0 or columna >= len(self.mapa[fila]):
            return False

        return True

    def esPared(self, posicion):
        """Comprueba si la posición contiene una pared."""
        fila, columna = posicion

        if not self.posicionValida(fila, columna):
            return True

        return self.mapa[fila][columna] == self.elementos["pared"]

    def esMeta(self, posicion):
        """Comprueba si una posición es una meta."""
        return posicion in self.metas

    def esCaja(self, posicion):
        """Comprueba si una posición contiene una caja."""
        return posicion in self.cajas

    # IMPRESIÓN DEL MAPA

    def obtenerElemento(self, posicion):
        """Obtiene el número que debe mostrarse en una casilla."""
        fila, columna = posicion

        if posicion == self.personaje:
            if posicion in self.metas:
                return self.elementos["personaje_meta"]

            return self.elementos["personaje"]

        if posicion in self.cajas:
            if posicion in self.metas:
                return self.elementos["caja_meta"]

            return self.elementos["caja"]

        if posicion in self.metas:
            return self.elementos["meta"]

        return self.mapa[fila][columna]

    def construirMapaVisible(self):
        """Construye una matriz con las posiciones actuales."""
        mapaVisible = []

        for fila in range(len(self.mapa)):
            filaVisible = []

            for columna in range(len(self.mapa[fila])):
                posicion = (fila, columna)
                elemento = self.obtenerElemento(posicion)
                filaVisible.append(elemento)

            mapaVisible.append(filaVisible)

        return mapaVisible

    def imprimirMapa(self):
        """Imprime el tablero con sus valores numéricos."""

        print("          SOKOBAN")
        print("-" * 29)

        mapaVisible = self.construirMapaVisible()

        for fila in mapaVisible:
            print(" ".join(str(elemento) for elemento in fila))

        print("-" * 29)
        print("Movimientos:", self.movimientos)
        print("Total de cajas en el mapa:", len(self.cajas))
        print("Cajas sobre metas:", len(self.cajas & self.metas))
        print("Metas disponibles:", len(self.metas))
        print("-" * 29)

    # LECTURA Y EVALUACIÓN DEL MOVIMIENTO

    def leerMovimiento(self):
        """Solicita una tecla al usuario."""
        print("W: arriba | A: izquierda")
        print("S: abajo  | D: derecha")
        print("R: reiniciar | Q: salir")

        movimiento = input("Movimiento: ")
        return movimiento.strip().lower()

    def evaluarMovimiento(self, movimiento):
        """Ejecuta el movimiento correspondiente a la tecla."""
        if movimiento == "d":
            self.derecha()

        elif movimiento == "a":
            self.izquierda()

        elif movimiento == "w":
            self.arriba()

        elif movimiento == "s":
            self.abajo()

        elif movimiento == "r":
            self.reiniciarNivel()

        elif movimiento == "q":
            self.juegoActivo = False
            self.mensaje = "Saliste del juego."

        else:
            self.mensaje = "Tecla no válida."

    # CÁLCULO DE POSICIONES

    def calcularDestino(self, cambioFila, cambioColumna):
        """Calcula la casilla que está delante del personaje."""
        fila, columna = self.personaje

        nuevaFila = fila + cambioFila
        nuevaColumna = columna + cambioColumna

        return (nuevaFila, nuevaColumna)

    def calcularDestinoCaja(
        self, posicionCaja, cambioFila, cambioColumna
    ):
        """Calcula la siguiente posición de una caja."""
        fila, columna = posicionCaja

        nuevaFila = fila + cambioFila
        nuevaColumna = columna + cambioColumna

        return (nuevaFila, nuevaColumna)

    def destinoLibre(self, posicion):
        """Comprueba si una casilla está libre para una caja."""
        if self.esPared(posicion):
            return False

        if posicion in self.cajas:
            return False

        return True

    # --------------------------------------------------
    # ACTUALIZACIÓN DEL PERSONAJE Y LAS CAJAS
    # --------------------------------------------------

    def moverPersonaje(self, nuevaPosicion):
        """Actualiza la posición del personaje."""
        self.personaje = nuevaPosicion
        self.movimientos += 1

    def moverCaja(self, posicionActual, posicionNueva):
        """Mueve una caja sin borrar las metas."""
        self.cajas.remove(posicionActual)
        self.cajas.add(posicionNueva)

    def validarEmpuje(
        self, posicionCaja, cambioFila, cambioColumna
    ):
        """Comprueba si una caja puede ser empujada."""
        destinoCaja = self.calcularDestinoCaja(
            posicionCaja,
            cambioFila,
            cambioColumna
        )

        if not self.posicionValida(
            destinoCaja[0], destinoCaja[1]
        ):
            self.mensaje = "No puedes sacar una caja del mapa."
            return False

        if self.esPared(destinoCaja):
            self.mensaje = "No puedes empujar una caja contra la pared."
            return False

        if destinoCaja in self.cajas:
            self.mensaje = "No puedes empujar dos cajas a la vez."
            return False

        return True

    def mover(self, cambioFila, cambioColumna, direccion):
        """Procesa el movimiento del personaje y, si es necesario, una caja."""
        destino = self.calcularDestino(
            cambioFila,
            cambioColumna
        )

        # Verificar los límites del mapa.
        if not self.posicionValida(destino[0], destino[1]):
            self.mensaje = "Movimiento fuera del mapa."
            return False

        # No se permite atravesar paredes.
        if self.esPared(destino):
            self.mensaje = "Hay una pared."
            return False

        # Si existe una caja, intentar empujarla.
        if self.esCaja(destino):
            puedeEmpujar = self.validarEmpuje(
                destino,
                cambioFila,
                cambioColumna
            )

            if not puedeEmpujar:
                return False

            destinoCaja = self.calcularDestinoCaja(
                destino,
                cambioFila,
                cambioColumna
            )

            # Primero se actualiza la caja.
            self.moverCaja(destino, destinoCaja)

            # Después, el personaje ocupa la posición de la caja.
            self.moverPersonaje(destino)

            self.mensaje = "Caja empujada hacia " + direccion + "."
            return True

        # Si no hay caja, el personaje puede caminar.
        self.moverPersonaje(destino)

        if self.esMeta(destino):
            self.mensaje = "El personaje está sobre una meta."
        else:
            self.mensaje = "Movimiento hacia " + direccion + "."

        return True
    
    # MOVIMIENTOS INDIVIDUALES

    def derecha(self):
        """Mueve al personaje una casilla hacia la derecha."""
        return self.mover(0, 1, "la derecha")

    def izquierda(self):
        """Mueve al personaje una casilla hacia la izquierda."""
        return self.mover(0, -1, "la izquierda")

    def arriba(self):
        """Mueve al personaje una casilla hacia arriba."""
        return self.mover(-1, 0, "arriba")

    def abajo(self):
        """Mueve al personaje una casilla hacia abajo."""
        return self.mover(1, 0, "abajo")

    # CONDICIÓN DE VICTORIA

    def verificarMeta(self):
        """Comprueba si todas las metas tienen una caja."""
        return self.metas.issubset(self.cajas)

    def nivelCompletado(self):
        """Muestra el mensaje de victoria si se completa el nivel."""
        if self.verificarMeta():
            self.mensaje = "¡Felicidades! Completaste el nivel."
            return True

        return False

    # CICLO PRINCIPAL DEL JUEGO

    def mostrarInstrucciones(self):
        """Explica los controles y los elementos del tablero."""
        print("INSTRUCCIONES DE SOKOBAN")
        print("0 = personaje")
        print("1 = caja")
        print("2 = pared")
        print("3 = meta")
        print("4 = camino")
        print("5 = caja sobre meta")
        print("6 = personaje sobre meta")
        print("No puedes atravesar paredes.")
        print("No puedes empujar dos cajas al mismo tiempo.")

    def procesarTurno(self):
        """Muestra el tablero, lee el movimiento y lo procesa."""
        self.limpiarPantalla()
        self.imprimirMapa()

        if self.nivelCompletado():
            self.juegoActivo = False
            return

        movimiento = self.leerMovimiento()
        self.evaluarMovimiento(movimiento)

    def jugar(self):
        """Repite el juego hasta completar el nivel o salir."""
        self.mostrarInstrucciones()

        while self.juegoActivo:
            self.procesarTurno()

        self.limpiarPantalla()
        self.imprimirMapa()

        if self.verificarMeta():
            print("¡Ganaste!")
        else:
            print(self.mensaje)

# INICIO DEL PROGRAMA

def iniciarJuego():
    """Crea el objeto y comienza la partida."""
    juego = Sokoban()
    juego.jugar()


if __name__ == "__main__":
    iniciarJuego()

# DOCUMENTACIÓN DE LOS CASOS DE MOVIMIENTO

# Caso 1: personaje y camino.
# El personaje avanza y la casilla anterior vuelve a mostrar 4.

# Caso 2: personaje y meta.
# El personaje avanza y la meta permanece registrada.

# Caso 3: personaje, caja y camino.
# El personaje empuja la caja si la siguiente casilla está libre.

# Caso 4: personaje, caja y meta.
# La caja puede avanzar hasta una meta.

# Caso 5: personaje sobre una meta y camino.
# El personaje sale y la casilla anterior muestra 3.

# Caso 6: personaje sobre una meta y otra meta.
# El personaje cambia de meta y ambas metas se conservan.

# Caso 7: caja sobre una meta y camino.
# La caja puede salir de la meta y esta vuelve a mostrar 3.

# Caso 8: caja sobre una meta y otra meta.
# La caja puede moverse a otra meta libre.

# Caso 9: personaje frente a una caja y una pared.
# El movimiento se cancela y ninguna posición cambia.

# Caso 10: personaje frente a dos cajas.
# El movimiento se cancela porque no se empujan cajas en cadena.

# Caso 11: personaje frente al límite del mapa.
# El movimiento se cancela para evitar salir de la matriz.

# Caso 12: personaje sobre meta.
# El mapa muestra 6 hasta que el personaje abandona esa posición.

# Las posiciones se actualizan mediante las variables de estado.
# El método obtenerElemento decide qué número se debe imprimir.
# El método construirMapaVisible crea la representación actual del mapa.
# El autoborrado se realiza al principio de cada turno.
# El reinicio restaura las posiciones iniciales del nivel.
# La clase Sokoban agrupa los datos y las funciones del juego.