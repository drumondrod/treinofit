"""Camada View: apresentacao em terminal (poderia ser trocada por Web/Mobile)."""


def mostrar_treino(aluno, treino) -> None:
    print(f"\nAluno: {aluno.nome} | Objetivo: {aluno.objetivo}")
    print(f"{treino.nome}")
    print("-" * 52)
    for e in treino.exercicios:
        print(f"{e.nome:<22} {e.series}x{e.repeticoes:<3} {e.carga_kg:>6.1f} kg")
    print("-" * 52)
    print(f"Volume total: {treino.volume_total():.1f} kg")
