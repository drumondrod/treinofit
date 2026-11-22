import pytest

from app.controllers.treino_controller import TreinoController
from app.models.entidades import Exercicio, Treino
from app.services.progressao import (
    ProgressaoDeload,
    ProgressaoLinear,
    ProgressaoPercentual,
)


def test_volume_do_exercicio():
    # 4 series x 10 repeticoes x 40 kg = 1600 kg
    assert Exercicio("Supino reto", 4, 10, 40).volume() == 1600


def test_exercicio_invalido_levanta_erro():
    with pytest.raises(ValueError):
        Exercicio("Agachamento", 0, 10, 60)


def test_volume_total_do_treino():
    treino = Treino("Treino A")
    treino.adicionar(Exercicio("Supino", 4, 10, 40))   # 1600
    treino.adicionar(Exercicio("Triceps", 3, 12, 20))  # 720
    assert treino.volume_total() == 2320


def test_progressao_linear():
    assert ProgressaoLinear(2).proxima_carga(40) == 42


def test_progressao_percentual():
    assert ProgressaoPercentual(5).proxima_carga(40) == 42


def test_progressao_deload():
    assert ProgressaoDeload(10).proxima_carga(50) == 45


def test_controller_aplica_estrategia_em_todos_os_exercicios():
    ctrl = TreinoController()
    aluno = ctrl.cadastrar_aluno("Marina", "Hipertrofia")
    treino = ctrl.criar_treino(aluno.nome, "Treino A")
    ctrl.adicionar_exercicio(treino, "Supino", 4, 10, 40)
    ctrl.adicionar_exercicio(treino, "Remada", 4, 10, 30)
    ctrl.aplicar_progressao(treino, ProgressaoLinear(2.5))
    assert [e.carga_kg for e in treino.exercicios] == [42.5, 32.5]


def test_aluno_sem_nome_e_rejeitado():
    with pytest.raises(ValueError):
        TreinoController().cadastrar_aluno("   ", "Emagrecimento")
