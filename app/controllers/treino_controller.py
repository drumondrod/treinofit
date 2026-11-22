"""Camada Controller: orquestra Model e Services, sem conhecer a interface."""
from app.models.entidades import Aluno, Exercicio, Treino
from app.services.progressao import EstrategiaProgressao


class TreinoController:
    def __init__(self):
        self._alunos = {}  # repositorio em memoria (simples para 2 semanas)

    def cadastrar_aluno(self, nome: str, objetivo: str) -> Aluno:
        if not nome.strip():
            raise ValueError("O nome do aluno e obrigatorio.")
        aluno = Aluno(nome=nome.strip(), objetivo=objetivo)
        self._alunos[aluno.nome] = aluno
        return aluno

    def obter_aluno(self, nome: str) -> Aluno:
        if nome not in self._alunos:
            raise KeyError(f"Aluno '{nome}' nao encontrado.")
        return self._alunos[nome]

    def listar_alunos(self):
        return list(self._alunos.values())

    def criar_treino(self, nome_aluno: str, nome_treino: str) -> Treino:
        treino = Treino(nome=nome_treino)
        self.obter_aluno(nome_aluno).treinos.append(treino)
        return treino

    def adicionar_exercicio(self, treino: Treino, nome: str,
                            series: int, repeticoes: int, carga_kg: float) -> Exercicio:
        exercicio = Exercicio(nome, series, repeticoes, carga_kg)
        treino.adicionar(exercicio)
        return exercicio

    def aplicar_progressao(self, treino: Treino, estrategia: EstrategiaProgressao) -> None:
        """Atualiza todas as cargas do treino usando a estrategia escolhida."""
        for exercicio in treino.exercicios:
            exercicio.carga_kg = estrategia.proxima_carga(exercicio.carga_kg)
