class PyCellsLibError(Exception):
    """
    Esta clase solo tiene la intencion de renombrar (se crea un sinonimo), para
    hacer mas claro que errores son creados en la libreria, todas las
    excepciones deben heredar de esta clase
    """


class InitializationWithoutParametersError(PyCellsLibError):
    """
    Esta excepcion debe ser lanzada cuando se intente instanciar un objeto
    sin pasar los parametros requeridos a la clase
    """

    def __init__(self, class_name):
        msg = f"No se puede instanciar {class_name} sin parametros"
        super().__init__(msg)


class InvalidParameterError(PyCellsLibError):
    """
    Esta excepcion debe ser lanzada cuanto se pase un argumento invalido, esto
    es, no esta en el rango requerido, no tenga el tipo adecuado, ...
    """

    def __init__(self, reason_msg):
        msg = f"Parametro invalido, {reason_msg}"
        super().__init__(msg)
