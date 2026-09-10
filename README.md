# Trabalho Prático 1 — Análise inicial de webtoons e manhwa

Sistema orientado a objetos desenvolvido para a disciplina de Programação / Algoritmos e Estruturas de Dados na **Universidade Federal de Lavras (UFLA)**.

Permite organizar, consultar, filtrar e extrair estatísticas de uma base de dados contendo os 250 webtoons e manhwa mais bem avaliados.

## Funcionalidades

- **Cadastro de obras** com recálculo dinâmico de rankings
- **Estatísticas** — médias, máximos, mínimos e contagens por situação
- **Filtros** por nota, ranking, capítulos, situação e gênero
- **Tratamento de dados incompletos** — completar campos faltantes de obras já cadastradas
- **Listagem** de todas as obras com dados formatados

## Como executar

```bash
python main.py
```

## Estrutura do projeto

```
├── main.py          → Ponto de entrada (classe Aplicacao)
├── modelos.py       → Modelo de dados (classe Webtoon)
├── gerenciador.py   → Lógica de negócio (classe GerenciadorWebtoons)
├── repositorio.py   → Persistência em CSV (classe RepositorioCSV)
├── interface.py     → Interação via terminal (classe InterfaceUsuario)
├── validacoes.py    → Validação de dados (classe Validador)
├── constantes.py    → Constantes do sistema
└── dados.csv        → Arquivo de dados gerado automaticamente
```

## Autor

**Diego Alves** — UFLA, 2026