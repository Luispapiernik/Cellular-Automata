import curses as c
import numpy as np


class TestAutomata(object):
    """docstring for TestAutomata"""
    def __init__(self):
        self.states = [np.zeros((13, 13), dtype=np.int),
                       np.zeros((13, 13), dtype=np.int)]

        self.states[0][5:8, 5:8] = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
        self.states[0][5:8, 5:8] = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]

        self.index = 0

    def get_state(self):
        index = (self.index + 1) % 2
        return self.states[self.index]


class CursesVisualizer:
    """
    Esta clase se encarga de coordinar todos los objetos necesarios para
    realizar la visualizacion de un automata en pantalla
    """

    def __init__(self, automata):
        self.automata = automata
        self.stdscr = self.initialize()

        self.quit = False

    def initialize(self):
        """
        Este metodo realiza la inicializacion de recursos
        """
        # se inicializa curses y se obtiene una referencia a la ventana
        # principal
        stdscr = c.initscr()

        # para manejar colores
        c.start_color()

        # se delega el trabajo de codificar el codigo de teclas especiales
        # a curses
        stdscr.keypad(True)
        # se desabilita el mostrar en pantalla cada vez que se presione una
        # tecla (con esto se controlara que se muestra en pantalla)
        c.noecho()
        # se habilita la lectura de entrada del teclado sin tener que
        # presionar la tecla ENTER
        c.cbreak()

        # se oculta el cursor de la pantalla
        c.curs_set(0)

        # inicializacion de colores
        # c.init_pair(COLOR_SELECTED_ELEMENT, c.COLOR_RED, c.COLOR_BLACK)
        # c.init_pair(COLOR_SELECTED_PANEL, c.COLOR_GREEN, c.COLOR_BLACK)
        return stdscr

    def loop(self):
        """
        Este metodo coordina el ciclo de vida del visualizador
        """
        # se limpia la pantalla
        self.stdscr.erase()

        # se dibuja un borde para toda la ventana
        self.stdscr.box()

        # se cargan los cambios
        self.stdscr.refresh()
        while not self.quit:
            # se obtiene entrada del usuario
            char = self.stdscr.getch()

            # se presiono la letra q
            if char == 113:
                self.quit = True

    def end(self):
        """
        Este metodo libera recursos una vez se ha terminado la ejecucion
        """
        c.endwin()


if __name__ == '__main__':
    visualizer = CursesVisualizer(TestAutomata())

    visualizer.loop()
    visualizer.end()
