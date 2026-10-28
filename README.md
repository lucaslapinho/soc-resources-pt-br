# 🛡️ Recursos para SOC · PT-BR

<a id="inicio"></a>

**Ferramentas, bases de conhecimento e referências para apoiar o trabalho diário de um Security Operations Center.**

Da triagem ao encerramento do incidente: encontre recursos por atividade, entenda quando usá-los e conheça as dependências que precisam ser avaliadas. O catálogo reúne referências do material fornecido e complementos editoriais com links para os mantenedores.

**65 entradas · 11 categorias · Português brasileiro · Edição: 28/10/2026**

## Comece pela sua tarefa

| Preciso de ajuda para… | Começar por | Próximo passo |
|---|---|---|
| Investigar email ou URL suspeita | [Triagem](#triagem) | [Roteiro de phishing](docs/roteiros.md#phishing) |
| Consultar um hash, domínio ou IP | [Triagem](#triagem) e [CTI](#cti) | Correlacionar origem, tempo e contexto do indicador |
| Criar ou revisar uma detecção | [Detecção](#deteccao) | [Modelo de caso de uso](templates/caso-de-uso.md) |
| Investigar execução suspeita no Windows | [Endpoint e DFIR](#endpoint) e [Hunting](#hunting) | [Roteiro de endpoint](docs/roteiros.md#endpoint) |
| Investigar atividade Linux | [GTFOBins](https://gtfobins.org/) e [Hunting](#hunting) | Levantar comandos, usuário, privilégios e persistência |
| Examinar tráfego ou PCAP | [Rede](#rede) | Relacionar sessões, DNS e alertas com a timeline |
| Tratar um incidente | [Resposta](#resposta) | [Modelo de registro](templates/registro-incidente.md) |
| Automatizar uma tarefa repetitiva | [Plataformas](#plataformas) | Definir entradas, erros, permissões e efeitos das ações |
| Capacitar o time | [Capacitação](#treinamento) | [Trilha de quatro semanas](docs/capacitacao.md) |
| Estruturar processos e métricas | [Operação](#operacao) | Definir responsáveis, filas, escalonamento e critérios de qualidade |

## Como navegar

- [Catálogo por categoria](#catalogo)
- [Roteiros de investigação](docs/roteiros.md)
- [Capacitação do time](docs/capacitacao.md)
- [Critérios, fontes e verificação](docs/metodologia.md)
- [Como contribuir](CONTRIBUTING.md)
- [Catálogo JSON](data/recursos.json) · [Planilha CSV](data/recursos.csv)

Use os IDs `SOC-001` a `SOC-065` em tickets e procedimentos para manter a referência estável. As descrições resumem a finalidade do recurso; **“uso no SOC” é uma sugestão editorial**, que depende do ambiente.

## Orientações de uso

- **Consulta e envio são operações diferentes.** Antes de submeter emails, arquivos, URLs ou cabeçalhos a serviços externos, confira dados sensíveis, visibilidade da submissão e política interna. URLs podem conter tokens. Prefira consulta de hash quando ela atender à análise.
- **Valide detecções no seu ambiente.** Confira produto, versão, logs, campos, parsers, macros, lookups, janela temporal e falsos positivos. Uma regra publicada não implica execução imediata ou cobertura comprovada.
- **Interprete indicadores com contexto.** Binários legítimos, ferramentas RMM e drivers listados precisam de investigação. Presença em catálogo ou correspondência isolada não comprova comprometimento.
- **Preserve evidências.** Registre origem, horário/fuso, ferramenta, versão e integridade dos arquivos coletados. Use laboratório autorizado para amostras de malware e testes de emulação.
- **Confira condições de acesso.** Site público não significa que todos os dados, APIs ou recursos sejam gratuitos. Custos, licenças e limites não foram auditados.

<a id="catalogo"></a>
## Catálogo por categoria

| Categoria | Entradas |
|---|---:|
| [Descoberta e coleções](#descoberta) | 12 |
| [Operação e maturidade do SOC](#operacao) | 2 |
| [Triagem de phishing, URLs e indicadores](#triagem) | 6 |
| [Inteligência de ameaças e vulnerabilidades](#cti) | 7 |
| [Engenharia de detecção e consultas](#deteccao) | 5 |
| [Threat hunting e abuso de ferramentas legítimas](#hunting) | 6 |
| [Investigação de endpoints e DFIR](#endpoint) | 10 |
| [Análise e monitoramento de rede](#rede) | 4 |
| [Plataformas de monitoramento e automação](#plataformas) | 4 |
| [Resposta a incidentes e playbooks](#resposta) | 3 |
| [Capacitação, datasets e simulação](#treinamento) | 6 |

<a id="descoberta"></a>
## Descoberta e coleções

| ID / recurso | Finalidade | Uso no SOC | Observações e dependências |
|---|---|---|---|
| **SOC-001** · [A-poc / BlueTeam-Tools](https://github.com/A-poc/BlueTeam-Tools)<br><sub>agregador</sub> | Reunir ferramentas e técnicas para monitoramento, hunting, inteligência, resposta a incidentes, malware e forense. | Encontrar ferramentas conforme a atividade e ampliar o catálogo interno do SOC. | A coleção inclui recursos com diferentes condições de acesso e licenciamento. |
| **SOC-002** · [fabacab / Awesome Cybersecurity Blue Team](https://github.com/fabacab/awesome-cybersecurity-blueteam)<br><sub>agregador</sub> | Catalogar recursos defensivos, incluindo monitoramento, automação, segurança em nuvem, evidências e inteligência. | Descobrir projetos e comparar alternativas para capacidades da operação. | A preferência do mantenedor por software livre não comprova a manutenção de cada projeto listado. |
| **SOC-004** · [iw-sec / Awesome SOC Tools](https://github.com/iw-sec/awesome-soc-tools)<br><sub>agregador</sub> | Reunir ferramentas de inteligência e enriquecimento para triagem de indicadores. | Montar favoritos e selecionar fontes de consulta para IPs, domínios, URLs e hashes. | O catálogo identifica serviços que exigem conta para funcionalidades relevantes. |
| **SOC-005** · [LetsDefend / Awesome SOC Analyst](https://github.com/LetsDefend/awesome-soc-analyst)<br><sub>agregador</sub> | Reunir ferramentas, laboratórios, livros e referências de investigação e fontes de logs. | Construir trilhas para analistas e apoiar consultas sobre phishing, malware e eventos. | Consultar requisitos e condições atuais na fonte. |
| **SOC-006** · [st0pp3r / Awesome SOC Analyst](https://github.com/st0pp3r/awesome-soc-analyst)<br><sub>agregador</sub> | Organizar referências, ferramentas online, publicações e materiais relacionados ao trabalho do analista SOC. | Padronizar favoritos e fontes de consulta da equipe. | O projeto disponibiliza um arquivo de favoritos para importação no navegador. |
| **SOC-008** · [hslatman / Awesome Threat Intelligence](https://github.com/hslatman/awesome-threat-intelligence)<br><sub>agregador</sub> | Catalogar fontes, feeds, APIs, formatos, plataformas e referências de inteligência de ameaças. | Selecionar fontes de CTI e planejar integrações de enriquecimento. | Indicadores precisam de análise contextual para apoiar decisões. |
| **SOC-009** · [meirwah / Awesome Incident Response](https://github.com/meirwah/awesome-incident-response)<br><sub>agregador</sub> | Reunir ferramentas e referências de coleta, análise de logs e memória, timelines, gestão e resposta. | Selecionar recursos conforme a etapa da investigação. | O catálogo deve ser combinado com um procedimento adequado ao incidente. |
| **SOC-010** · [0x4D31 / Awesome Threat Detection and Hunting](https://github.com/0x4D31/awesome-threat-detection)<br><sub>agregador</sub> | Reunir ferramentas, regras, datasets, pesquisas, frameworks e laboratórios de detecção e hunting. | Encontrar referências para desenvolver casos de uso e identificar telemetria necessária. | Consultar requisitos e condições atuais na fonte. |
| **SOC-011** · [cugu / Awesome Forensics](https://github.com/cugu/awesome-forensics)<br><sub>agregador</sub> | Catalogar ferramentas e recursos de análise forense por especialidade. | Selecionar ferramentas para coleta, análise de artefatos e preparação de uma estação DFIR. | As marcações de manutenção e recomendação refletem os critérios do mantenedor. |
| **SOC-020** · [DFIR.Training / DFIR Tools](https://www.dfir.training/dfir-tools)<br><sub>diretorio ferramentas</sub> | Organizar ferramentas forenses por finalidade, tipo e desenvolvedor. | Encontrar ferramentas para uma necessidade específica de coleta ou análise. | A consulta pública ao diretório não implica gratuidade de todos os produtos listados. |
| **SOC-021** · [NIST / Computer Forensics Tools & Techniques Catalog](https://toolcatalog.nist.gov/)<br><sub>diretorio ferramentas</sub> | Permitir pesquisa de ferramentas e técnicas forenses por função e parâmetros técnicos. | Comparar alternativas de acordo com os requisitos da investigação. | O NIST informa que a presença no catálogo não implica teste do produto. |
| **SOC-022** · [OSINT Framework](https://osintframework.com/)<br><sub>diretorio fontes</sub> | Organizar ferramentas e fontes de investigação em fontes abertas. | Encontrar fontes complementares para investigação e enriquecimento. | Alguns recursos exigem cadastro ou cobram por funcionalidades adicionais. |

[↑ Voltar ao início](#inicio)

<a id="operacao"></a>
## Operação e maturidade do SOC

| ID / recurso | Finalidade | Uso no SOC | Observações e dependências |
|---|---|---|---|
| **SOC-003** · [cyb3rxp / Awesome SOC](https://github.com/cyb3rxp/awesome-soc)<br><sub>base conhecimento</sub> | Organizar referências para construir, operar e amadurecer um SOC. | Estruturar processos, engenharia de detecção, métricas, automação e procedimentos. | Inclui procedimentos sobre avaliação de comprometimento de Microsoft 365 e servidores web. |
| **SOC-030** · [SOC Brazil](https://socbrazil.com/)<br><sub>portal recursos</sub> | Reunir conteúdo em português, avaliações de maturidade, calculadoras, relatórios e recursos da comunidade. | Apoiar planejamento, dimensionamento e desenvolvimento da operação. | Consultar requisitos e condições atuais na fonte. |

[↑ Voltar ao início](#inicio)

<a id="triagem"></a>
## Triagem de phishing, URLs e indicadores

| ID / recurso | Finalidade | Uso no SOC | Observações e dependências |
|---|---|---|---|
| **SOC-027** · [abuse.ch / ThreatFox, URLhaus e MalwareBazaar](https://threatfox.abuse.ch/) · [Fonte 1](https://urlhaus.abuse.ch/) · [Fonte 2](https://bazaar.abuse.ch/)<br><sub>grupo bases cti</sub> | Reunir IOCs associados a malware, URLs de distribuição de malware e informações sobre amostras. | Consultar indicadores e avaliar integrações de enriquecimento. | ThreatFox, URLhaus e MalwareBazaar têm escopos distintos. URLhaus não é uma base geral de todo tipo de phishing. Confirmar condições de API. |
| **SOC-029** · [CyberChef](https://gchq.github.io/CyberChef/) · [Fonte 1](https://github.com/gchq/CyberChef)<br><sub>ferramenta</sub> | Combinar operações de codificação, decodificação, compressão, hashes e transformação de dados. | Tratar strings, logs e artefatos por meio de receitas reproduzíveis. | O projeto documenta execução local. Registrar a receita quando ela for parte relevante da análise. |
| **SOC-036** · [VirusTotal](https://www.virustotal.com/)<br><sub>servico</sub> | Consultar reputação e contexto de hashes, domínios, IPs e URLs. | Começar por consultas de hashes existentes durante a triagem. | Uploads e análises podem compartilhar conteúdo; consultar a política aplicável antes de enviar arquivos ou URLs internos. |
| **SOC-037** · [urlscan.io](https://urlscan.io/)<br><sub>servico</sub> | Pesquisar e analisar carregamento de páginas web. | Examinar redirecionamentos, requisições e infraestrutura de uma URL. | Verificar a visibilidade da submissão; URLs podem conter tokens ou dados pessoais. |
| **SOC-038** · [MXToolbox — Email Header Analyzer](https://mxtoolbox.com/EmailHeaders.aspx)<br><sub>servico</sub> | Auxiliar a leitura de cabeçalhos de mensagens. | Revisar saltos de entrega e indícios de problemas de autenticação de email. | Cabeçalhos podem expor endereços e infraestrutura; sanitizar dados antes da submissão externa. |
| **SOC-063** · [oletools](https://github.com/decalage2/oletools)<br><sub>ferramentas</sub> | Inspecionar documentos Microsoft Office e artefatos relacionados. | Analisar macros e estruturas suspeitas em documentos recebidos por email. | Preservar o arquivo original e usar ambiente de análise isolado. |

[↑ Voltar ao início](#inicio)

<a id="cti"></a>
## Inteligência de ameaças e vulnerabilidades

| ID / recurso | Finalidade | Uso no SOC | Observações e dependências |
|---|---|---|---|
| **SOC-025** · [MITRE ATT&CK](https://attack.mitre.org/)<br><sub>base conhecimento</sub> | Organizar conhecimento sobre táticas e técnicas adversárias e referências relacionadas. | Mapear comportamentos, estruturar hipóteses de hunting e analisar cobertura. | Mapeamento para uma técnica não demonstra, isoladamente, eficácia da detecção. |
| **SOC-026** · [Malpedia / Fraunhofer FKIE](https://malpedia.caad.fkie.fraunhofer.de/)<br><sub>base conhecimento</sub> | Apoiar identificação e contextualização de famílias de malware. | Pesquisar aliases, referências e contexto para investigação e hunting. | Parte dos dados, incluindo amostras e regras não públicas, depende de acesso por convite. |
| **SOC-028** · [The DFIR Report / Public Reports](https://thedfirreport.com/reports/)<br><sub>relatorios</sub> | Publicar análises de intrusões reais com evidências, sequência de atividades e mapeamentos ATT&CK. | Criar hipóteses de hunting, casos de uso e exercícios baseados em incidentes. | A coleção indicada é pública; o projeto também oferece conteúdo e serviços comerciais. |
| **SOC-039** · [MISP](https://www.misp-project.org/)<br><sub>plataforma</sub> | Organizar e compartilhar inteligência de ameaças. | Estruturar indicadores, eventos, contexto e fluxos de compartilhamento. | Definir taxonomias, distribuição, retenção e qualidade antes de automatizar o consumo. |
| **SOC-040** · [OpenCTI](https://docs.opencti.io/)<br><sub>plataforma</sub> | Organizar conhecimento e relacionamentos de CTI. | Conectar relatórios, entidades e contexto para apoiar investigação. | Conectores, feeds e implantação possuem requisitos próprios. |
| **SOC-041** · [CISA — Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)<br><sub>base conhecimento</sub> | Catalogar vulnerabilidades conhecidas por exploração em ataques. | Priorizar exposição junto com inventário, criticidade e controles existentes. | A ausência no catálogo não demonstra ausência de exploração; KEV não substitui gestão de vulnerabilidades. |
| **SOC-042** · [FIRST — EPSS](https://www.first.org/epss/)<br><sub>base conhecimento</sub> | Estimar a probabilidade de exploração de vulnerabilidades. | Complementar a priorização de CVEs com exposição e contexto do ativo. | Probabilidade estimada não é impacto, confirmação de exploração ou garantia de ausência de risco. |

[↑ Voltar ao início](#inicio)

<a id="deteccao"></a>
## Engenharia de detecção e consultas

| ID / recurso | Finalidade | Uso no SOC | Observações e dependências |
|---|---|---|---|
| **SOC-012** · [SigmaHQ / Sigma](https://github.com/SigmaHQ/sigma)<br><sub>regras consultas</sub> | Disponibilizar regras Sigma para detecção e hunting. | Desenvolver e adaptar lógicas de detecção e comparar cobertura. | Conversão e execução dependem do backend, dos campos e das fontes de logs. |
| **SOC-013** · [Microsoft Sentinel e Defender / Azure-Sentinel](https://github.com/Azure/Azure-Sentinel)<br><sub>regras consultas</sub> | Reunir detecções, consultas, hunting, workbooks, playbooks, parsers e conectores. | Apoiar operações com Sentinel e Defender e desenvolver conteúdo compatível com o ambiente. | Confirmar tabelas, conectores e diferenças de esquema entre os produtos. |
| **SOC-014** · [Splunk Security Content](https://github.com/splunk/security_content) · [Fonte 1](https://research.splunk.com/)<br><sub>regras consultas</sub> | Disponibilizar detecções, Analytic Stories, contexto de TTPs e conteúdo de investigação. | Criar e revisar casos de uso no Splunk. | Verificar fontes de dados, campos, macros, lookups e demais dependências da detecção. |
| **SOC-015** · [Elastic / Detection Rules](https://github.com/elastic/detection-rules)<br><sub>regras consultas</sub> | Manter regras do Elastic Security e recursos de desenvolvimento, teste e validação. | Desenvolver casos de uso e organizar o ciclo de vida de detecções. | Confirmar compatibilidade de versão, esquema e disponibilidade do conteúdo. |
| **SOC-043** · [YARA](https://github.com/VirusTotal/yara)<br><sub>ferramenta</sub> | Identificar padrões em arquivos por meio de regras. | Criar e revisar assinaturas para triagem e pesquisa de malware. | Validar regras contra amostras positivas e negativas e revisar custo de execução. |

[↑ Voltar ao início](#inicio)

<a id="hunting"></a>
## Threat hunting e abuso de ferramentas legítimas

| ID / recurso | Finalidade | Uso no SOC | Observações e dependências |
|---|---|---|---|
| **SOC-007** · [mthcht / Awesome Lists](https://github.com/mthcht/awesome-lists)<br><sub>listas referencia</sub> | Reunir listas de serviços, tarefas, named pipes, user agents, certificados, aplicações e outros artefatos. | Apoiar lookups, enriquecimento, consultas e hipóteses de hunting. | Uma correspondência precisa de contexto; as listas não devem ser interpretadas uniformemente como blocklists. |
| **SOC-016** · [LOLBAS](https://lolbas-project.github.io/)<br><sub>catalogo tecnico</sub> | Catalogar binários, scripts e bibliotecas Windows que podem ser utilizados de forma abusiva. | Contextualizar processos e comandos suspeitos e apoiar hunting. | A existência ou execução de um item listado não comprova uso malicioso. |
| **SOC-017** · [GTFOBins](https://gtfobins.org/)<br><sub>catalogo tecnico</sub> | Documentar funcionalidades de executáveis Unix/Linux que podem ser abusadas em sistemas mal configurados. | Investigar atividades relacionadas a permissões e uso suspeito de executáveis. | O catálogo não é uma lista de programas necessariamente vulneráveis. |
| **SOC-018** · [LOLDrivers](https://www.loldrivers.io/)<br><sub>catalogo tecnico</sub> | Catalogar drivers Windows vulneráveis ou maliciosos, hashes, evidências e recursos de detecção. | Investigar carregamento de drivers e possíveis cenários de BYOVD. | Diferenciar vulnerabilidade, classificação maliciosa e evidência de abuso no ambiente. |
| **SOC-019** · [LOLRMM](https://lolrmm.io/)<br><sub>catalogo tecnico</sub> | Catalogar ferramentas de gerenciamento e acesso remoto e seus artefatos. | Identificar acesso remoto não autorizado e investigar possível abuso de RMM. | Confrontar os achados com inventário, instalação, responsável e uso permitido. |
| **SOC-044** · [ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator)<br><sub>ferramenta</sub> | Visualizar camadas de técnicas ATT&CK. | Documentar hipóteses, prioridades e cobertura apoiada por evidências. | Uma técnica colorida não comprova cobertura; registrar dados e validações associados. |

[↑ Voltar ao início](#inicio)

<a id="endpoint"></a>
## Investigação de endpoints e DFIR

| ID / recurso | Finalidade | Uso no SOC | Observações e dependências |
|---|---|---|---|
| **SOC-024** · [Ultimate Windows Security / Security Log Encyclopedia](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/)<br><sub>base conhecimento</sub> | Documentar eventos de segurança Windows e disponibilizar referências de outras fontes. | Consultar Event IDs e apoiar a interpretação de eventos durante investigações. | É uma referência independente; não deve ser apresentada como documentação oficial da Microsoft. |
| **SOC-045** · [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/)<br><sub>ferramentas</sub> | Reunir utilitários de diagnóstico e investigação Windows. | Consultar processos, persistência e eventos com ferramentas como Autoruns e Sysmon. | Ferramentas podem exigir elevação; implantação de telemetria depende da política do ambiente. |
| **SOC-046** · [Velociraptor](https://docs.velociraptor.app/)<br><sub>ferramenta</sub> | Coletar e investigar artefatos de endpoints. | Realizar triagem e hunting com artefatos e consultas VQL. | Planejar acesso, escopo de coleta, impacto e retenção das evidências. |
| **SOC-047** · [Hayabusa](https://github.com/Yamato-Security/hayabusa)<br><sub>ferramenta</sub> | Analisar logs de eventos Windows e construir timelines. | Triar EVTX e revisar resultados de detecção durante investigações. | Conferir regras, versão e contexto dos eventos; alertas precisam de validação. |
| **SOC-048** · [Chainsaw](https://github.com/WithSecureLabs/chainsaw)<br><sub>ferramenta</sub> | Pesquisar artefatos forenses, incluindo logs Windows. | Buscar padrões em EVTX e apoiar hunting com regras e mapeamentos. | Confirmar formato dos dados e dependências dos mapeamentos utilizados. |
| **SOC-049** · [Eric Zimmerman Tools](https://ericzimmerman.github.io/)<br><sub>ferramentas</sub> | Disponibilizar utilitários de análise de artefatos Windows. | Examinar registros, execução e timelines conforme o artefato disponível. | Preservar o original, documentar versão da ferramenta e exportações. |
| **SOC-050** · [Volatility 3](https://github.com/volatilityfoundation/volatility3)<br><sub>ferramenta</sub> | Analisar imagens de memória. | Investigar processos e outros artefatos em uma aquisição de memória. | Compatibilidade e símbolos dependem da imagem; a aquisição é uma etapa separada. |
| **SOC-051** · [Plaso](https://plaso.readthedocs.io/)<br><sub>ferramenta</sub> | Extrair e processar eventos para análise de timelines. | Consolidar artefatos temporais e apoiar reconstrução de incidentes. | Registrar fuso horário, parsers, origem e limites das evidências. |
| **SOC-061** · [Mandiant capa](https://github.com/mandiant/capa)<br><sub>ferramenta</sub> | Identificar capacidades de programas a partir de regras. | Contextualizar uma amostra em uma estação de análise de malware. | Resultados precisam de interpretação; empacotamento e formato podem limitar a análise. |
| **SOC-062** · [Mandiant FLOSS](https://github.com/mandiant/flare-floss)<br><sub>ferramenta</sub> | Extrair strings de executáveis, incluindo formas ofuscadas suportadas. | Apoiar a pesquisa de indicadores e comportamento provável de uma amostra. | Executar a análise em ambiente adequado e correlacionar os achados com outras evidências. |

[↑ Voltar ao início](#inicio)

<a id="rede"></a>
## Análise e monitoramento de rede

| ID / recurso | Finalidade | Uso no SOC | Observações e dependências |
|---|---|---|---|
| **SOC-052** · [Wireshark](https://www.wireshark.org/)<br><sub>ferramenta</sub> | Capturar e analisar protocolos e pacotes de rede. | Investigar sessões, DNS, HTTP e outras comunicações em PCAP. | Capturas podem conter dados sensíveis; o conteúdo disponível depende de criptografia e ponto de captura. |
| **SOC-053** · [Zeek](https://zeek.org/)<br><sub>ferramenta</sub> | Produzir telemetria de segurança a partir do tráfego de rede. | Investigar conexões e protocolos usando logs estruturados. | Planejar posicionamento do sensor, capacidade, perda de pacotes e retenção. |
| **SOC-054** · [Suricata](https://suricata.io/)<br><sub>ferramenta</sub> | Inspecionar tráfego e gerar eventos de segurança de rede. | Correlacionar alertas e telemetria de protocolos com outros eventos. | Regras e modo de operação exigem tuning e dimensionamento no ambiente. |
| **SOC-055** · [Arkime](https://arkime.com/)<br><sub>plataforma</sub> | Indexar sessões e apoiar pesquisa de capturas de rede. | Pivotar de metadados de sessão para os pacotes disponíveis. | Dimensionar armazenamento e controlar acesso ao conteúdo das capturas. |

[↑ Voltar ao início](#inicio)

<a id="plataformas"></a>
## Plataformas de monitoramento e automação

| ID / recurso | Finalidade | Uso no SOC | Observações e dependências |
|---|---|---|---|
| **SOC-056** · [Wazuh](https://documentation.wazuh.com/)<br><sub>plataforma</sub> | Oferecer capacidades de monitoramento e análise de segurança. | Avaliar coleta de eventos e casos de uso de monitoramento de endpoints. | Validar arquitetura, agentes, integrações e manutenção antes da adoção. |
| **SOC-057** · [Security Onion](https://docs.securityonion.net/)<br><sub>plataforma</sub> | Integrar recursos de monitoramento de segurança e investigação. | Avaliar uma plataforma para visibilidade e análise de rede. | Conferir requisitos, licenciamento dos componentes e arquitetura de implantação. |
| **SOC-059** · [Shuffle](https://github.com/Shuffle/Shuffle)<br><sub>plataforma</sub> | Construir fluxos de automação de segurança. | Automatizar enriquecimento e tarefas repetitivas com revisão de efeitos. | Tratar credenciais, tratamento de erros e ações de contenção conforme o processo de mudança. |
| **SOC-060** · [Palo Alto Networks — Cortex XSOAR Content](https://github.com/demisto/content)<br><sub>integracoes playbooks</sub> | Reunir integrações, scripts e playbooks para Cortex XSOAR. | Pesquisar automações e dependências de pacotes antes de adaptá-los. | Compatibilidade com versão e produto deve ser confirmada; a presença no repositório não implica disponibilidade no tenant. |

[↑ Voltar ao início](#inicio)

<a id="resposta"></a>
## Resposta a incidentes e playbooks

| ID / recurso | Finalidade | Uso no SOC | Observações e dependências |
|---|---|---|---|
| **SOC-031** · [Microsoft / Incident Response Playbooks](https://learn.microsoft.com/en-us/security/operations/incident-response-playbooks)<br><sub>playbooks</sub> | Disponibilizar procedimentos para phishing, password spray e incidentes envolvendo aplicações. | Adaptar fluxos, checklists e etapas de investigação ao ambiente. | Conferir pré-requisitos de produtos, logs, funções e permissões de cada playbook. |
| **SOC-032** · [CERT Société Générale / Incident Response Methodologies](https://github.com/certsocietegenerale/IRM)<br><sub>playbooks</sub> | Reunir referências operacionais de tratamento de incidentes. | Elaborar ou revisar procedimentos internos de resposta. | O conteúdo consultado se apresenta como IRM 2022; adaptar às tecnologias e responsabilidades atuais. |
| **SOC-058** · [DFIR-IRIS](https://docs.dfir-iris.org/)<br><sub>plataforma</sub> | Organizar casos e informações de resposta a incidentes. | Registrar atividades, indicadores e evidências de uma investigação. | Definir papéis, acesso, retenção e integração com o processo interno. |

[↑ Voltar ao início](#inicio)

<a id="treinamento"></a>
## Capacitação, datasets e simulação

| ID / recurso | Finalidade | Uso no SOC | Observações e dependências |
|---|---|---|---|
| **SOC-023** · [SANS / Posters & Cheat Sheets](https://www.sans.org/posters)<br><sub>base conhecimento</sub> | Reunir referências rápidas sobre segurança, defesa, forense e resposta. | Organizar materiais de consulta para a wiki e a capacitação do SOC. | Consultar requisitos e condições atuais na fonte. |
| **SOC-033** · [OTRF / Security Datasets](https://github.com/OTRF/Security-Datasets)<br><sub>dataset</sub> | Disponibilizar datasets de atividades benignas e maliciosas para pesquisa e análise. | Testar consultas, exercitar investigações e avaliar lógicas de detecção. | Verificar compatibilidade de campos e contexto antes de reutilizar os dados. |
| **SOC-034** · [Malware Traffic Analysis](https://www.malware-traffic-analysis.net/)<br><sub>dataset treinamento</sub> | Compartilhar PCAPs, exercícios, tutoriais e materiais relacionados a tráfego de malware. | Treinar análise de tráfego, identificação de indicadores e reconstrução de atividades. | Distinguir capturas de tráfego, exercícios e arquivos que contenham amostras de malware. |
| **SOC-035** · [DFIR Diva / Training Directory](https://training.dfirdiva.com/)<br><sub>diretorio treinamento</sub> | Catalogar treinamentos de DFIR, blue team e áreas relacionadas. | Montar trilhas conforme função, experiência e lacunas da equipe. | O diretório reúne ofertas gratuitas e pagas. |
| **SOC-064** · [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)<br><sub>simulacao</sub> | Disponibilizar testes de comportamentos mapeados ao ATT&CK. | Exercitar coleta de telemetria e validar hipóteses em laboratório autorizado. | Testes podem alterar o sistema; revisar pré-requisitos, comandos e limpeza antes de executar. |
| **SOC-065** · [MITRE CALDERA](https://github.com/mitre/caldera)<br><sub>simulacao</sub> | Apoiar emulação de adversários e exercícios automatizados. | Planejar exercícios controlados para avaliar visibilidade e resposta. | Usar escopo autorizado, laboratório e plano de recuperação; não executar automaticamente em produção. |

[↑ Voltar ao início](#inicio)

## Glossário

| Sigla | Significado |
|---|---|
| CTI / IOC | Inteligência de ameaças / indicador de comprometimento |
| DFIR | Forense digital e resposta a incidentes |
| SIEM / SOAR | Gestão e correlação de eventos / orquestração e automação de segurança |
| EDR / XDR | Detecção e resposta em endpoints / detecção e resposta estendida |
| TTP | Táticas, técnicas e procedimentos |
| RMM / BYOVD | Gerenciamento e acesso remoto / abuso por introdução de driver vulnerável |
| PCAP / EVTX | Captura de pacotes / arquivo de eventos Windows |
| KQL / SPL / VQL | Linguagens de consulta de Microsoft, Splunk e Velociraptor, respectivamente |

## Fontes, atribuição e manutenção

Os 35 IDs iniciais vieram do catálogo fornecido pelo solicitante. Os demais são complementos editoriais. A referência inicial indicada no material foi [DXC-0 / soc-ressources](https://github.com/DXC-0/soc-ressources). Os links e créditos de cada projeto estão preservados; cada ferramenta e conteúdo externo mantém sua própria licença.

O arquivo de favoritos mencionado no pedido **não estava disponível no caminho fornecido** durante a elaboração. Esta edição não incorpora nem publica o HTML de favoritos. Veja o [registro de proveniência e verificação](docs/metodologia.md) para o escopo exato da revisão.

Sugestões e correções podem ser enviadas por issue ou pull request, seguindo [CONTRIBUTING.md](CONTRIBUTING.md). Não inclua credenciais, dados de clientes ou evidências reais de incidentes nas contribuições.

### Histórico

| Versão | Data editorial | Alterações |
|---|---|---|
| 1.0.0 | 2026-10-28 | Catálogo inicial categorizado, roteiros de investigação, modelos e trilha de capacitação. |
