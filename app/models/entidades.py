"""Camada Model: entidades do dominio e suas regras basicas."""
from dataclasses import dataclass, field
from typing import List


@dataclass
class Exercicio:
    nome: str
    series: int
    repeticoes: int
    carga_kg: float

    def __post_init__(self):
        if self.series <= 0 or self.repeticoes <= 0:
            raise ValueError("Series e repeticoes devem ser maiores que zero.")
        if self.carga_kg < 0:
            raise ValueError("A carga nao pode ser negativa.")

    def volume(self) -> float:
        """Volume de treino = series x repeticoes x carga (kg)."""
        return self.series * self.repeticoes * self.carga_kg


@dataclass
class Treino:
    nome: str
    exercicios: List[Exercicio] = field(default_factory=list)

    def adicionar(self, exercicio: Exercicio) -> None:
        self.exercicios.append(exercicio)

    def volume_total(self) -> float:
        return sum(e.volume() for e in self.exercicios)


@dataclass
class Aluno:
    nome: str
    objetivo: str
    treinos: List[Treino] = field(default_factory=list)
