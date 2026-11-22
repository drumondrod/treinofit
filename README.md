# TreinoFit - Gestao de treinos para Personal Trainer

Projeto academico de Engenharia de Software (Rodrigo Drumond).
Permite ao personal trainer cadastrar alunos, montar treinos, calcular o volume
de treino e aplicar regras de progressao de carga (padrao Strategy).

## Arquitetura (MVC / camadas)
- `app/models` - entidades (Aluno, Treino, Exercicio)
- `app/controllers` - regras de orquestracao
- `app/services` - Strategy de progressao de carga
- `app/views` - interface (terminal)

## Como executar
```bash
pip install -r requirements.txt
python main.py     # demonstracao
pytest -v          # testes unitarios
```
A cada `push` no GitHub, o workflow `.github/workflows/main.yml` roda os testes.
