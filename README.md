# Cellular-Automata

PyCellsLib es una librería para la simulación y visualización de autómatas celulares arbitrarios.

## Instalación
Para realizar la instalación de la libreria primero se debe clonar localmente el repositorio con el comando `git clone https://github.com/computational-group-the-golden-ticket/Cellular-Automata.git`, luego debera aceder a la carpeta del repositorio y ejecutar el comando `python3 -m pip install -e .` o `pip3 install -e .`.

Para la desinstalación de la libreria ejecute el comando `python3 -m pip uninstall pycellslib` o `pip3 uninstall pycellslib`

## Autómata celular

### Definición
Un **autómata celular** (A.C.) es un modelo matemático para un sistema dinámico que evoluciona en pasos discretos. No existe una definición formal y matemática aceptada de autómata celular; sin embargo, se puede describir a un A.C. como una tupla, es decir, un conjunto ordenado de objetos caracterizado por los siguientes componentes:

- Una *rejilla* o *cuadriculado* (lattice) de enteros infinitamente extendida, y con dimensión d un número natural. Cada celda de la cuadrícula se conoce como célula.
- Cada célula puede tomar un valor en los enteros a partir de un *conjunto finito de estados* ***k***.
- Cada célula, además, se caracteriza por su vecindad, un conjunto finito de células en las cercanías de la misma.
- De acuerdo con esto, se aplica a todas las células de la cuadrícula una *función de transición* (***f***) que toma como argumentos los valores de la célula en cuestión y los valores de sus vecinos, y regresa el nuevo valor que la célula tendrá en la siguiente etapa de tiempo. Esta función ***f*** se aplica, como ya se dijo, de forma homogénea a todas las células, por cada paso discreto de tiempo.

### Condiciones de frontera
Por definición, un A.C. consiste en una retícula infinita de enteros. Sin embargo, para cuestiones prácticas (como en modelos de sistemas físicos llevados a cabo en ordenadores de memoria finita), se requiere tomar ciertas consideraciones a la hora de implementar un A.C. Por ello, la definición original se modifica para dar cabida a retículas finitas en las que las células del A.C. interactúen. Esto conlleva la consideración extra de lo que debe suceder con aquellas células que se encuentren en los bordes de la retícula. A la implementación de una o varias consideraciones específicas se le conoce como *condición de frontera*.

Dentro del ámbito de los A.C., se pueden implementar numerosas condiciones de frontera, en función de lo que el problema real requiera para su modelado. ([para mas información](https://es.wikipedia.org/wiki/Aut%C3%B3mata_celular#Condiciones_de_frontera))

### Variaciones
Los A.C. pueden variar en alguna de las características antes mencionadas, derivando en autómatas celulares no *estándar*.

Por ejemplo, un A.C. estándar tiene una cuadrícula donde se asume que las células son cuadros; es decir, que la retícula tiene una geometría cuadrada. Esto no es necesariamente un requisito, y se puede variar el A.C. para presentar una geometría triangular o hexagonal (en A.C. de 2 dimensiones, el cuadrado, el triángulo y el hexágono son las únicas figuras geométricas que llenan el plano).

También puede variarse el conjunto de estados ***k*** que cada célula puede tomar, la función de transición ***f*** de forma que ya no sea homogénea, utilizar elementos estocásticos (aleatoriedad) en ***f*** (lo que se conoce como A.C. *probabilístico*), variar las vecindades de cada célula, etc.

## Sobre la libreria
Esta librería pretende ofrecer herramientas para la simulación y visualización de autómatas celulares arbitrarios (es decir, con los parámetros para la geometría, vecindad, tipos de celulas, funciones de transicion, ... todos especificados por el usuario). De acuerdo a esto, se han abstraido de la definicion de **automata celular** unos objetos primarios, que exhiben los siguientes comportamientos respectivamente:

- Un objeto que encapsula la informacion de las celulas, esto es, los posibles estados, numero de atributos (los atributos son una variacion que se permite en la libreria, la cual agrega a cada celula la capacidad de guardar numeros reales para especificar cosas como, densidades, flujos, alturas, ... y estas pueden ser usadas en las funciones de transición), ...
- Un objeto que encapsula la informacion espacial (geometrica) del automata, como, dimensiones, el como funciona la frontera, maneja la logica de actualización de las celulas, ...
- Un objeto que encapsula la idea de vecindad y funciones de transición.
- Un objeto que coordina la comunicacion entre los objetos mencionados anteriormente y ademas brinda informacion general del autama (densidad de determinado estado o atributo, flujo de esas mismas variables, ...)

Dadas las restricciones anteriores se realizo la definicion de 5 clases base, que son **CellInformation**, **Topology**, **Neighborhood**, **Rule** y **Automaton** y cuyas definiciones son:

Para visualización de ejemplos en los que se use cada clase [visitar](https://github.com/computational-group-the-golden-ticket/Cellular-Automata/tree/main/examples)

### CellInformation
```python
class CellInformation(metaclass=ABCMeta):
    """
    Una celula es una entidad que puede tener n estados representados por
    numeros enteros, y que tienen algun nombre, adicionalmente, la celula tiene
    atributos asociados, que son tambien valores numericos con nombre, estos se
    pueden usar para representar variables fisicas (velocidad, ...), variables
    demograficas, ...

    Esta es la clase base de las que deben heredar aquellas clases que brindan
    informacion de los parametros asociados a las celulas de algun automata.
    """

    @abstractmethod
    def get_states(self):
        """
        Este metodo retorna una tupla, lista o arreglo de los posibles estados
        que puede tener una celula

        Returns
        -------
        out(tuple(int)|list(int)|ndarray(int)): Posibles estados que puede
            tener una celula
        """

    @abstractmethod
    def get_number_of_attributes(self):
        """
        Este metodo retorna el numero de atributos que tiene una celula. En
        caso de que la celula no tenga atributos se retorna 0

        Returns
        -------
        out(int): numero de atributos de una celula
        """

    @abstractmethod
    def get_default_state(self):
        """
        Este metodo retorna el valor del estado que tienen las celulas por
        defecto

        Returns
        -------
        out(int): valor del estado por defecto de la celula
        """

    @abstractmethod
    def get_default_value_of_attributes(self):
        """
        Este metodo retorna los valores que tiene una celula por defecto en
        cada atributo. En caso de que la celula no tenga atributos, se retorna
        None

        Returns
        -------
        out(list|ndarray|None): valores por defecto de los atributos de la
            celula.
        """
    # con el objetivo de obtener y mostrar informacion del automata, como
    # densidad o flujo de celulas en un estado, ... se nombran los estados
    @abstractmethod
    def get_name_of_state(self, state):
        """
        Este metodo retorna el nombre asociado a un estado.

        Params
        ------
        state(int): valor del estado del que se desea conocer el nombre

        Returns
        -------
        out(str): nombre del estado, puede ser un string vacio
        """

    # con el objetivo de obtener y mostrar informacion del automata, como
    # densidad, flujos, ... se nombran los atributos, los cuales tienen un
    # orden fijo
    @abstractmethod
    def get_name_of_attributes(self, index):
        """
        Este metodo retorna el nombre del atributo asociado a un indice, el
        indice cuenta desde cero. Se retorna None en caso de que la celula no
        tenga atributos

        Params
        ------
        index(int): indice que corresponde al atributo

        Returns
        -------
        out(str|None): nombre del atributo, puede ser un string vacio
        """
```

### Topology
```python
class Topology(metaclass=ABCMeta):
    """
    La topologia representa la informacion espacial de una automata, esto es,
    tiene encapsulada las dimensiones, la distribucion de las celulas, los
    valores de estados y atributos en cada parte del espacio, metodos
    que extraen y asignan valores a subregiones del espacio...

    Internamente la clase Topology debe manejar 2 estructuras de datos para
    poder implementar la logica de actualizacion de las celulas (porque esta
    actualizacion se debe realizar en paralelo, es decir, en una de las
    estructuras de datos se van leyendo los valores, para poder calcular cual
    sera el nuevo valor en la siguiente iteracion, y en la otra estructura
    de datos se va escribiendo el nuevo valor de las celulas), por tanto en
    cada una de las estructuras se podra solo realizar una de dos, o escribir
    o leer (este comportamiento se puede modificar con el metodo flip, que
    invierte los papeles de lectura-escritura en las estructuras de datos).
    Ademas estas estructuras deben tener el cuenta el como la clase maneja
    las fronteras (las celulas de la frontera son no actualizables, su unico
    objetivo es el de hacer que todas las celulas actualizables tengan la
    misma condicion para las vecindades)
    """
    @abstractmethod
    def get_offset(self):
        """
        Este metodo debe retornar el offset que se le hacen a las posiciones
        en la matrix para no considerar las celulas de las fronteras en el
        proceso de actualizacion
        """

    @abstractmethod
    def __iter__(self):
        """
        La clase Topology debe brindar una interfaz por la cual se pueda
        iterar por cada celula para realizar el proceso de actualizacion, este
        metodo retorna un iterador sobre las posiciones de las celulas que son
        actualizables (esto es, las que no estan en la frontera)

        Returns
        -------
        out(iter(int)): iterador que recorre cada uno de los indices de las
            celulas que son actualizables
        """

    @abstractmethod
    def flip(self):
        """
        Este metodo cambia el papel (ser de lectura o ser de escritura) que
        cumplen las 2 estructuras de datos en las que se almacenan la
        informacion de estados y atributos de las celulas
        """

    @abstractmethod
    def get_cell(self, position):
        """
        Este metodo obtiene la informacion de una celula, tanto los estados
        como los atributos. Este metodo no permite obtener una celula que esta
        en la frontera

        Params
        ------
        position(tuple(int)|list(int)|ndarray(int)): representan la posicion de
            la celula

        Returns
        -------
        outs(tuple): tupla cuya primera componente es un entero con el valor
            del estado de la celula asociada a la posicion dada, y la segunda
            componente es un array con el valor de los atributos, o None, en
            caso de que las celulas no tenga atributos
        """

    @abstractmethod
    def get_states(self):
        """
        Este metodo retorna los estados de las celulas, no se tiene en cuenta
        la frontera

        Returns
        -------
        out(list(int)|tuple(int)|ndarray(int)): estados de las celulas
        """

    @abstractmethod
    def get_attributes(self):
        """
        Este metodo retorna los atributos de las celulas, no se tiene en cuenta
        la frontera

        Returns
        -------
        out(list(float)|tuple(float)|ndarray(float)): atributos de las celulas
        """

    @abstractmethod
    def update_cell(self, position, cell_state, cell_attributes):
        """
        Este metodo actualiza la informacion de una celula, tanto estados como
        atributos

        Params
        ------
        position(tuple|list): representa la posicion de la celula que sera
            actualizada
        cell_state(int): entero con el valor del estado de la celula
        cell_attributes(list(float)|ndarray(float)|None): lista o arreglo con
            los valores de los atributos. Si las celulas no tienen atributos
            se pasa None
        """

    @abstractmethod
    def set_border_values(self, cell_state, cell_attributes):
        """
        Este metodo establece el valor en los bordes

        Params
        ------
        state_value(int): especifica el valor de los estados en los bordes
        attributes_values(list): especifica el valor de los atributos en los
            bordes, cada elemento de la lista especifica un atributo
        """

    @abstractmethod
    def set_values_from(self, cell_state, cell_attributes):
        """
        Este metodo establece el valor de las celulas usando los mismos
        parametros tanto para los estados, como para los atributos

        Params
        ------
        cell_state(int): entero con el valor de los estados de las celulas
        cell_attributes(list|None): lista o arreglo con los valores de
            los atributos. Si las celulas no tienen atributos se pasa None
        """

    @abstractmethod
    def set_values_from_configuration(self, cell_states, cell_attributes):
        """
        Este metodo establece el valor de las celulas desde un arreglo de
        estados y un arreglo de atributos

        Params
        ------
        cell_states(ndarray(int)): arreglo con los valores de los estados de
            cada celula
        cell_attributes(ndarray(float)|None): arreglo con los valores de los
            atributos de cada celula. Si las celulas no tienen atributos se
            pasa None
        """

    @abstractmethod
    def apply_mask(self, position, mask):
        """
        Este metodo retorna la vecindad de una celula mediante la aplicacion
        de la mascara que representa la vecindad

        Params
        ------
        position(tuple(int)|list(int)): posicion en la que se ubica la mascara
        mask(ndarray): arreglo que representa alguna vecindad

        Returns
        ------
        out(tuple): Tupla donde la primera componente son los estados de las
            celulas que representan la vecindad, y la segunda componente
            representa los atributos de cada celula, si las celulas no tienen
            atributos se retorna None
        """
```

### Neighborhood
```python
class Neighborhood(metaclass=ABCMeta):
    """
    El vecindario de una celula define que celulas condicionan como cambia de
    estado cuando se aplica la funcion de transicion. La vecindad de una celula
    se representa como una mascara (array de numpy de tipo bool), False indica
    que la celula no afecta, y True indica que la celula si afecta. Esta
    mascara se superpone en el array que contiene las celulas (en la clase
    Topology) usando como coordenadas la posicion de la celula en cuestion mas
    un offset (una translacion)
    """

    @abstractmethod
    def get_mask(self):
        """
        Este metodo retorna la mascara que define la vecindad de una celula

        Returns
        -------
        out(ndarray(bool)): mascara
        """

    @abstractmethod
    def get_offset(self):
        """
        Este metodo retorna el offset de la mascara

        Returns
        -------
        out(tuple(int)|list(int)|ndarray(int)): valor que indica el offset en
            cada eje de la mascara
        """
```

### Rule
```python
class Rule(metaclass=ABCMeta):
    """
    Una regla representa el como cambia el estado de cada celula, esto es,
    representa la vecindad y la funcion de transicion que se aplica a la
    vecindad
    """

    @abstractmethod
    def get_neighborhood(self):
        """
        Este metodo retorna la vecindad asociada a la regla

        Returns
        -------
        out(Neighborhood): Objeto que representa la vecindad
        """

    @abstractmethod
    def apply_rule(self, cell_states, cell_attributes):
        """
        Este metodo aplica las reglas de transicion a una vecindad de la
        celula

        Params
        ------
        cell_states(ndarray(int)): arreglo que representa los estados de la
            vecindad de una celula (es retornado por el metodo apply_mask de
            la clase topology)
        cell_attributes(ndarray(float)): arreglo que representa los atributos
            de la vecindad de una celula (es retornado por el metodo apply_mask
            de la clase topology)

        Returns
        -------
        out(int|ndarray|list): representa el valor del estado de la celula y
            posiblemente el valor de los atributos de la celula. En caso de
            retornar valor de tipo ndarray o list, entonces la primera
            componente debe ser el valor del estado y las demas componentes,
            los valores de los atributos
        """
```

### Automaton
```python
class Automaton:
    """
    Un objeto de la clase Automaton encapsula la idea de automata, esta clase
    se encarga de coordinar las clases Cells, Topology y Rules, y ofrece
    metodos para la extraccion de informacion (densidades o de estados o de
    atributos, flujos, ...) del automata
    """

    def __init__(self, cell_information, rule, topology, name=''):

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

    def next_step(self):
        """
        Este metodo itera un paso en la ejecucion del automata
        """
```
