"""
Docs
"""

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import FuncAnimation


class PaletteCreator():
    """docstring for PaletteCreator"""
    def __init__(self, colors, name=''):
        max_color = max(i for i, _ in colors)
        self.colors = [(0, 0, 0)] * (max_color + 1)

        for index, color in colors:
            self.colors[index] = color

        self.cmap = LinearSegmentedColormap.from_list(name, self.colors)

    def set_color(self, state, color):
        """
        Docs
        """
        if state >= len(self.colors):
            self.colors.append(color)

        self.colors[state] = color


class GameOfLifeLikePalette(PaletteCreator):
    def __init__(self, invert=False):
        colors = [[0, 'white'], [1, 'black']]

        if invert:
            colors[0][0] = 1
            colors[1][0] = 0

        super().__init__(colors, 'Game Of Life')


def update_function(_, axes, palette, interpolation, automaton):
    """
    Docs
    """
    automaton.next_step()
    img = axes.imshow(255 * automaton.topology.get_states(),
                      cmap=palette, aspect='equal',
                      interpolation=interpolation)
    return (img, )


def configure_animation(title, fontdict={'color': 'white',
                                         'family': 'sans-serif',
                                         'fontweight': 'bold',
                                         'fontsize':16},
                        figsize=(5, 5), backgroud_color='black'):
    """
    Docs
    """
    fig = plt.figure(figsize=figsize, facecolor=backgroud_color)
    axes = fig.add_subplot()

    axes.set_title(title, fontdict=fontdict)
    axes.set_xticks([])
    axes.set_yticks([])

    return fig, axes


def animate(automaton, fig, axes, palette=GameOfLifeLikePalette().cmap,
            interpolation='sinc', frames=None, time_per_frame=50,
            save_count=None):
    """
    Docs
    """
    axes.imshow(255 * automaton.topology.get_states(), cmap=palette,
                interpolation=interpolation)
    animation = FuncAnimation(fig, update_function, frames=frames,
                              fargs=(axes, palette, interpolation, automaton),
                              interval=time_per_frame,
                              save_count=save_count)
    plt.show()

    return animation
