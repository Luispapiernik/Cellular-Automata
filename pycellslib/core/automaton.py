from pycellslib.core.cell_information import CellInformation
from pycellslib.core.rule import Rule
from pycellslib.core.topology import Topology


class Automaton:
    """
    Un objeto de la clase Automaton encapsula la idea de automata, esta clase
    se encarga de coordinar las clases Cells, Topology y Rules, y ofrece
    metodos para la extraccion de informacion (densidades o de estados o de
    atributos, flujos, ...) del automata
    """

    def __init__(
        self,
        cell_information: CellInformation,
        rule: Rule,
        topology: Topology,
        name: str = "",
    ) -> None:
        self.cell_information = cell_information
        self.rule = rule
        self.topology = topology
        self.name = name

        neighborhood = self.rule.get_neighborhood()
        self.mask = neighborhood.get_mask()
        self.offset = neighborhood.get_offset()

    def load_configuration(self, directory):
        """
        Este metodo debe cargar la informacion del automata desde un directorio
        """

    def save_configuration(self, directory):
        """
        Este metodo debe guardar toda la informacion que permita la
        reinstanciacion del automata en cualquier sistema
        """

    def get_density_of_state(self, state):
        """
        Este metodo obtiene la densidad de algun estado en todo el espacio
        """

    def get_densities_of_states(self):
        """
        Este metodo obtiene las densidades de todos los estados en todo el
        espacio
        """

    def get_average_of_attribute(self, index):
        """
        Este metodo obtiene el promedio del atributo especificado (por medio
        del indice) en todo el espacio
        """

    def get_averages_of_attributes(self):
        """
        Este metodo obtiene el promedio de todos los atributos en todo el
        espacio
        """

    def next_step(self) -> None:
        """
        Este metodo itera un paso en la ejecucion del automata
        """
        # en el paso anterior, la nueva informacion se escribio en el buffer
        # de escritura, para usarla en el paso de actualizacion, el buffer
        # debe ser cambiado a uno de lectura
        self.topology.flip()

        for position in self.topology:
            mask_position = tuple(
                position[i] + self.offset[i] for i in range(len(position))
            )

            cells, attributes = self.topology.apply_mask(mask_position, self.mask)

            cell, attributes = self.rule.apply_rule(cells, attributes)

            self.topology.update_cell(position, cell, attributes)
