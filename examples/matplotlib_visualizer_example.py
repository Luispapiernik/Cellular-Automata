from pycellslib import Automaton
from pycellslib.cells import LifeLikeCell
from pycellslib.twodimensional.rules import BSNotationRule
from pycellslib.twodimensional.topologies import FinitePlaneTopology

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def randomGrid(N):
 
    """returns a grid of NxN random values"""
    return np.random.choice([0, 1], N*N, p=[0.5, 0.5]).reshape(N, N)


def main():
    N = 40
    cell_information = LifeLikeCell()
    topology = FinitePlaneTopology(0, N, N, 3, 3)
    rule = BSNotationRule([3], [2, 3], radius=1)

    automaton = Automaton(cell_information, rule, topology)
    automaton.topology.set_values_from_configuration(randomGrid(N), None)

    def update(frameNum, img):
        automaton.next_step()
        img.set_data(255 * automaton.topology.get_states())
        return img,

    fig, ax = plt.subplots()
    automaton.topology.flip()
    img = ax.imshow(255 * automaton.topology.get_states(), interpolation='nearest')
    automaton.topology.flip()
    updateInterval = 50
    ani = animation.FuncAnimation(fig, update, fargs=(img, ),
                                  frames = 1000,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show()


if __name__ == '__main__':
    main()
