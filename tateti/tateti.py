class Tateti():
    def __init__(self):
        self.tablero = ['', '', '', '', '', '', '', '', '']
        self.es_turno_jugador_cruz = True

    def aplicar_jugada(self, numero_casillero):
        if self.es_turno_jugador_cruz:
            self.tablero[numero_casillero] = 'X'
        else:
            self.tablero[numero_casillero] = 'O'

        self.es_turno_jugador_cruz = not self.es_turno_jugador_cruz

        return self.tablero[numero_casillero]

    def termino_el_juego(self):
        pass