"""Padrao de Projeto STRATEGY: regras intercambiaveis de progressao de carga."""
from abc import ABC, abstractmethod


class EstrategiaProgressao(ABC):
    """Contrato comum: toda estrategia calcula a proxima carga."""

    @abstractmethod
    def proxima_carga(self, carga_atual: float) -> float:
        ...


class ProgressaoLinear(EstrategiaProgressao):
    """Soma um valor fixo (kg) a cada ciclo. Ideal para iniciantes."""

    def __init__(self, incremento_kg: float = 2.0):
        self.incremento_kg = incremento_kg

    def proxima_carga(self, carga_atual: float) -> float:
        return round(carga_atual + self.incremento_kg, 2)


class ProgressaoPercentual(EstrategiaProgressao):
    """Aumenta um percentual da carga atual. Ideal para intermediarios."""

    def __init__(self, percentual: float = 5.0):
        self.percentual = percentual

    def proxima_carga(self, carga_atual: float) -> float:
        return round(carga_atual * (1 + self.percentual / 100), 2)


class ProgressaoDeload(EstrategiaProgressao):
    """Reduz a carga para recuperacao (semana de descarga)."""

    def __init__(self, reducao_percentual: float = 10.0):
        self.reducao_percentual = reducao_percentual

    def proxima_carga(self, carga_atual: float) -> float:
        return round(carga_atual * (1 - self.reducao_percentual / 100), 2)
