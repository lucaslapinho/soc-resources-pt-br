# Metodologia, proveniência e verificação

## Origem e seleção

- **SOC-001 a SOC-035:** derivados do catálogo de referência fornecido pelo solicitante, com IDs e URLs preservados.
- **SOC-036 a SOC-065:** complementos editoriais para cobrir triagem prática, análise de endpoints, rede, plataformas e validação em laboratório.
- **Favoritos HTML:** o arquivo `favoritos_28_10_2026.html` não foi localizado no caminho informado nem nas buscas por nome nas pastas de Downloads, anexos e Documents. Nenhum favorito desse arquivo foi incorporado. O original não foi publicado.
- A referência inicial citada no documento é [DXC-0/soc-ressources](https://github.com/DXC-0/soc-ressources). A organização deste repositório foi preparada para consulta por atividade do SOC.

O documento recebido é material de referência. Suas instruções de operação do Codex não foram adotadas como instruções deste projeto nem copiadas para arquivos de configuração de agentes.

## Critérios editoriais

1. Finalidade relacionada a uma atividade defensiva ou à capacitação do SOC.
2. URL do mantenedor ou da publicação original sempre que identificada.
3. Descrição concisa e aplicação operacional concreta.
4. Distinção entre agregador, ferramenta, plataforma, dataset e base de conhecimento.
5. Registro de dependências e limitações materiais, sem prometer eficácia, gratuidade ou compatibilidade universal.

Um projeto aparece uma vez no catálogo principal. A entrada SOC-027 reúne três serviços da abuse.ch e outras entradas podem possuir mais de uma fonte. A contagem de entradas não é uma contagem de ferramentas individuais.

## Verificação realizada

Data editorial: **28/10/2026**. Cada consulta técnica tem seu horário UTC registrado no JSON.

- Total: **65 entradas**, **69 URLs distintas**.
- Respostas HTTP obtidas pelo verificador: **67**.
- URLs pendentes de revisão manual: **2**.
- Arquivo completo: [verificação de links](../data/verificacao-links.json).
- O verificador efetuou requisições GET, seguiu redirecionamentos e registrou status, destino e título quando disponível. Não fez login, não executou ferramentas nem baixou amostras.
- Uma resposta HTTP 200 indica acessibilidade técnica naquele momento. Ela não comprova qualidade, segurança, manutenção, licença ou adequação do conteúdo. Bloqueios HTTP, timeouts e erros de certificado foram mantidos como pendências, sem contornar validação TLS.
- As páginas de Sigma, Azure-Sentinel, DXC-0 e do antigo Microsoft-365-Defender-Hunting-Queries também foram consultadas como referências documentais durante a elaboração.
- As descrições dos 35 IDs originais foram adaptadas do material recebido. A checagem automática de links não equivale a uma nova revisão técnica integral de cada projeto.
- **Não houve teste funcional**, teste de detecções, auditoria de licenças ou levantamento de preços e limites de API.

## Referência histórica Microsoft

O antigo [Microsoft-365-Defender-Hunting-Queries](https://github.com/microsoft/Microsoft-365-Defender-Hunting-Queries) está arquivado. Para pesquisar conteúdo atual, comece por [Azure-Sentinel](https://github.com/Azure/Azure-Sentinel) (SOC-013) e confira os requisitos do produto, das tabelas e dos conectores da consulta selecionada.

## URLs para revisão manual

| URL | Resultado da consulta |
|---|---|
| [https://attack.mitre.org/](https://attack.mitre.org/) | HTTP não obtido; TimeoutError — requer revisão |
| [https://www.cisa.gov/known-exploited-vulnerabilities-catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | HTTP 403; HTTPError — requer revisão |

## Manutenção sugerida

Revise os links periodicamente e sempre que um analista reportar mudança. Preserve os IDs: um recurso descontinuado deve ter seu histórico registrado, sem reutilização do ID. Documente redirecionamentos, projetos arquivados, mudanças de escopo e as revisões efetivamente feitas. Uma periodicidade sugerida é trimestral; este repositório não cria uma rotina agendada.

Para verificar consistência local, execute `python scripts/validate_catalog.py` na raiz. Essa validação não acessa serviços externos. Atualizações no catálogo precisam ser refletidas no README, JSON e CSV na mesma contribuição.
