from app.controllers.treino_controller import TreinoController
from app.services.progressao import ProgressaoLinear, ProgressaoPercentual
from app.views.cli import mostrar_treino


def main():
    ctrl = TreinoController()
    aluno = ctrl.cadastrar_aluno("Marina Souza", "Hipertrofia")
    treino = ctrl.criar_treino(aluno.nome, "Treino A - Peito e Triceps")
    ctrl.adicionar_exercicio(treino, "Supino reto", 4, 10, 40)
    ctrl.adicionar_exercicio(treino, "Triceps corda", 3, 12, 20)

    mostrar_treino(aluno, treino)

    print("\n>> Ciclo seguinte (progressao linear +2 kg)")
    ctrl.aplicar_progressao(treino, ProgressaoLinear(2))
    mostrar_treino(aluno, treino)

    print("\n>> Ciclo seguinte (progressao percentual 5%)")
    ctrl.aplicar_progressao(treino, ProgressaoPercentual(5))
    mostrar_treino(aluno, treino)


if __name__ == "__main__":
    main()
