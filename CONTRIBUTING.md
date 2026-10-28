# Como contribuir

Sugira um recurso, corrija um link ou melhore um roteiro por issue ou pull request.

## Incluir um recurso

Informe nome, URL do mantenedor, categoria, tipo, finalidade, uso no SOC, dependências, condições de acesso conhecidas e data/escopo da revisão. Procure duplicatas antes de sugerir.

1. Edite `data/recursos.json` e atribua o próximo ID disponível; preserve todos os IDs existentes.
2. Atualize a categoria correspondente no `README.md`, o CSV e as contagens afetadas.
3. Registre o que foi realmente verificado e eventuais pendências em `docs/metodologia.md` e no registro de links.
4. Execute `python scripts/validate_catalog.py` e revise a renderização Markdown no GitHub.

## Qualidade das contribuições

- Priorize fontes primárias e descreva o uso concreto para o analista.
- Diferencie material histórico, agregador, regra, ferramenta e plataforma.
- Não afirme gratuidade, compatibilidade ou manutenção sem referência atual.
- Não inclua credenciais, dados de clientes, IPs internos, URLs com tokens ou evidências reais de incidentes.
- Exemplos devem usar dados sintéticos e informar o produto e as dependências.
- Mantenha créditos, links de origem e condições de licenciamento dos conteúdos externos.

## Correções e descontinuação

Um erro de acesso isolado pode ser temporário. Confira a fonte antes de marcar o recurso como descontinuado. Preserve o ID e documente a substituição ou mudança de endereço.
