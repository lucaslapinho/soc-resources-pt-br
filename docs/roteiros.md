# Roteiros de investigação

Procedimentos de apoio para adaptação ao processo do time. Registre o que foi observado, a hipótese, a evidência e o resultado. Ações de contenção seguem as responsabilidades e autorizações do ambiente.

<a id="phishing"></a>
## Email ou URL suspeita

1. Preserve a mensagem original e seus anexos. Registre remetente, destinatários, horário e identificador da mensagem.
2. Examine remetente de envelope, From, Reply-To, Received e Authentication-Results. Interprete SPF, DKIM e DMARC junto com o caminho de entrega e os logs disponíveis.
3. Extraia URLs e hashes sem abrir o conteúdo na estação de trabalho. Use CyberChef (SOC-029) para transformação reproduzível e oletools (SOC-063) para documentos Office quando pertinente.
4. Consulte fontes existentes antes de submeter conteúdo novo: abuse.ch (SOC-027), VirusTotal (SOC-036) e pesquisas do urlscan.io (SOC-037). Confira a política de compartilhamento para cada submissão.
5. Correlacione entrega, clique, download, execução e autenticações no ambiente. Diferencie uma tentativa bloqueada de um incidente com impacto demonstrado.
6. Documente escopo, evidências, confiança, lacunas e escalonamento. Use os playbooks Microsoft (SOC-031) apenas após conferir os requisitos aplicáveis.

**Saída esperada:** classificação fundamentada, ativos e usuários afetados, timeline e próximos passos com responsáveis.

<a id="endpoint"></a>
## Processo ou comando suspeito em endpoint

1. Registre hostname, usuário, horário/fuso, processo pai e filho, linha de comando, caminho, hash e assinatura quando disponíveis.
2. Compare o comportamento com o papel do ativo e o uso autorizado. Consulte LOLBAS (SOC-016), GTFOBins (SOC-017), LOLDrivers (SOC-018) ou LOLRMM (SOC-019) conforme o caso.
3. Busque persistência, conexões, movimentação lateral e eventos de identidade correlacionados. Documente os eventos ausentes em vez de presumir que não ocorreram.
4. Se houver EVTX, avalie Hayabusa (SOC-047) ou Chainsaw (SOC-048). Para outros artefatos, selecione Sysinternals (SOC-045), Velociraptor (SOC-046) ou Eric Zimmerman Tools (SOC-049).
5. Construa a timeline preservando o fuso e a precisão das fontes. Imagens de memória podem ser examinadas com Volatility 3 (SOC-050), quando disponíveis e compatíveis.
6. Registre a hipótese, alternativas benignas, evidências e decisão de escalonamento. Preserve os artefatos antes de ações que possam alterá-los.

**Saída esperada:** cadeia de eventos, escopo afetado, hipótese sustentada e lacunas de coleta.

<a id="deteccao"></a>
## Nova detecção ou hipótese de hunting

1. Defina comportamento, risco e resultado esperado. Relacione ATT&CK (SOC-025) quando houver evidências para o mapeamento.
2. Liste telemetria necessária e valide exemplos de eventos reais ou de laboratório. Identifique produto, linguagem, campos e normalização.
3. Consulte Sigma (SOC-012), Sentinel/Defender (SOC-013), Splunk (SOC-014) ou Elastic (SOC-015) conforme a plataforma.
4. Adapte a lógica e explique as dependências. Sigma exige backend e mapeamento; conteúdo de um produto pode não funcionar em outro.
5. Valide casos positivos e negativos, custo da consulta, volume, exceções e agrupamento. Datasets OTRF (SOC-033) apoiam testes dentro dos limites do cenário simulado.
6. Use o [modelo de caso de uso](../templates/caso-de-uso.md) para registrar versão, proprietário, rollback e critérios de revisão.

**Saída esperada:** lógica documentada, testes reproduzíveis e indicação explícita do que ainda depende do ambiente.

## Triagem de tráfego de rede

1. Identifique origem da captura, janela temporal, fuso, ativos e eventuais perdas de pacotes.
2. Examine sessões e protocolos com Wireshark (SOC-052) e, conforme a infraestrutura, Zeek (SOC-053), Suricata (SOC-054) ou Arkime (SOC-055).
3. Correlacione DNS, conexões, certificados e alertas com logs de endpoint e identidade. Considere limitações de visibilidade por criptografia e posicionamento do sensor.
4. Documente a sequência, indicadores observados, alternativas benignas e lacunas.

**Saída esperada:** timeline correlacionada com evidências de rede e contexto dos ativos.
