class Tateti():
    def __init__(self):
        self.tablero = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        self.es_turno_jugador_cruz = True

    def aplicar_jugada(self, numero_casillero):
        if self.es_turno_jugador_cruz:
            self.tablero[numero_casillero] = 'X'
        else:
            self.tablero[numero_casillero] = 'O'

        self.es_turno_jugador_cruz = not self.es_turno_jugador_cruz

        return self.tablero[numero_casillero]

    def termino_el_juego(self):
        alguna_fila = self.tablero[0] == self.tablero[1] == self.tablero[2] or self.tablero[3] == self.tablero[4] == self.tablero[5] or self.tablero[6] == self.tablero[7] == self.tablero[8]
        alguna_columna = self.tablero[0] == self.tablero[3] == self.tablero[6] or self.tablero[1] == self.tablero[4] == self.tablero[7] or self.tablero[2] == self.tablero[5] == self.tablero[8]
        diagonal_izq = self.tablero[0] == self.tablero[4] == self.tablero[8]
        diagonal_der = self.tablero[2] == self.tablero[4] == self.tablero[6]

        return alguna_fila or alguna_columna or diagonal_izq or diagonal_der

    def resetear_juego(self):
        self.tablero = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        self.es_turno_jugador_cruz = True

    def devolver_ganador(self):
        # Verificar filas
        for i in range(0, 9, 3):
            if self.tablero[i] != '' and self.tablero[i] == self.tablero[i + 1] == self.tablero[i + 2]:
                return self.tablero[i]

        # Verificar columnas
        for i in range(3):
            if self.tablero[i] != '' and self.tablero[i] == self.tablero[i + 3] == self.tablero[i + 6]:
                return self.tablero[i]

        # Verificar diagonales
        if self.tablero[0] == self.tablero[4] == self.tablero[8]:
            return self.tablero[0]
        if self.tablero[2] == self.tablero[4] == self.tablero[6]:
            return self.tablero[2]

        # No hay ganador
        return None