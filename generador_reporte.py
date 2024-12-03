from abc import ABC, abstractmethod
from Planta import Planta  # Asegúrate de tener la clase Planta definida

# Clase abstracta GeneradorReporte
class GeneradorReporte(ABC):
    def __init__(self, plantas=None):
        # Si no se pasa ninguna lista de plantas, inicializamos una lista vacía
        self.plantas = plantas if plantas is not None else []

    @abstractmethod
    def generar_reporte(self, filename):
        """ Método para generar el reporte """
        pass

    @abstractmethod
    def guardar_reporte(self, filename):
        """ Método para guardar el reporte generado """
        pass
