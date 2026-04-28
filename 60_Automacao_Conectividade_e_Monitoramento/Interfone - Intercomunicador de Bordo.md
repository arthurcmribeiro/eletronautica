---
title: "Interfone / Intercomunicador de Bordo"
note_type: "system"
domain: "60_Automacao_Conectividade_e_Monitoramento"
source_file: "INTERFONE INTERCOMUNICADOR DE BORDO 33a19734f7fb8108897aec76ca245eb2.md"
status: "tier-b-curated"
fase_6_reescrita: 124
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil + Internacional"
review_level: "tier-b-curated"
normas_citadas:
  - "ABYC E-11"
  - "ABYC TE-30"
  - "IEC 60945"
  - "IEC 60529 (IP)"
  - "IEC 61010-1"
  - "ISO 9009 (HDMI/audio)"
  - "ABNT NBR 14728"
  - "ANATEL Resolução 715/2019"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://www.nmea.org/standards.html"
  - "https://www.nmea.org/nmea-0400.html"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "INTERFONE INTERCOMUNICADOR DE BORDO"
  - "INTERFONE / INTERCOMUNICADOR DE BORDO"
seo_title: "Interfone / Intercomunicador de Bordo"
seo_description: "INTERFONE A BORDO — Sistema de comunicacao interna que melhora seguranca operacional, coordenacao de manobras e comunicacao entre ponte, popa, cabines e casa de maquinas."
seo_keywords:
  - "Interfone maritimo"
  - "Intercomunicador de bordo"
  - "Comunicacao interna"
  - "60 Automacao Conectividade e Monitoramento"
geo_queries:
  - "O que e interfone de bordo em instalacoes nauticas?"
  - "Como projetar intercomunicacao interna em embarcacoes?"
related_notes:
  - "Wi-Fi a Bordo — Roteador Marine e Conectividade"
  - "Câmeras de Bordo / Sistema CFTV"
  - "Sistema de Alarme Geral / Painel de Alarmes"
  - "Som"
  - "TV a Bordo / Entretenimento"
  - "VHF"
---

# Interfone / Intercomunicador de Bordo

> [!abstract] Resumo técnico
> Interfone de bordo é um sistema de comunicação interna entre estações fixas ou móveis da embarcação. O valor técnico está em permitir coordenação clara em manobras, operação de máquinas e atendimento interno sem depender de celular, grito ou do uso indevido do VHF.

> [!tldr] TL;DR — 4 regras
> 1. **Distinguir interfone vs VHF:** VHF é regulado (ITU-R / ANATEL) e usado para fora; interfone é uso interno + manobra (ponte ↔ casa de máquinas ↔ popa ↔ cabines).
> 2. **Casa de máquinas → ponte é o ramal mais crítico** — em emergência, comunicação clara salva equipamento e vida. Cabo blindado + alto-falante de alta intensidade IP67.
> 3. **Tecnologias:** PoE (Power over Ethernet, Cisco SPA-Series, Grandstream, Yealink) × wireless DECT (Panasonic) × analog clássico marine (Phontech, Vingtor-Stentofon).
> 4. **Intelligibilidade > volume** — alto-falante calibrado para Speech Transmission Index (STI) >0,55 em casa de máquinas barulhenta.

> [!info] Glossário rápido
> - **PA (Public Address):** sistema de notificação geral.
> - **PABX:** central telefônica.
> - **PoE:** Power over Ethernet (IEEE 802.3af/at).
> - **DECT:** Digital Enhanced Cordless Telecommunications.
> - **STI (Speech Transmission Index):** métrica de inteligibilidade.
> - **Vingtor-Stentofon / Phontech:** referências marine commercial.

## O que é

Interfone é a infraestrutura de comunicação interna por voz da embarcação. Pode ser:

- analógico cabeado;
- digital cabeado;
- IP/VoIP;
- sem fio dedicado em aplicações específicas.

O tipo correto depende menos de moda e mais de:

- tamanho da embarcação;
- zonas que precisam se comunicar;
- ruído ambiente;
- necessidade ou não de integração com rede, câmeras e PA;
- criticidade operacional da comunicação.

## Função na embarcação

- coordenar manobras entre comando, proa, popa e plataforma;
- comunicar ponte e casa de máquinas durante testes ou ocorrência;
- facilitar rotina de tripulação e atendimento interno;
- reduzir improvisação com celular ou rádio portátil fora de contexto.

## Fundamentos mínimos

### Nem toda necessidade pede sistema IP

Para duas ou três estações fixas, um sistema cabeado simples e robusto costuma ser mais confiável que uma solução dependente de rede sem fio.

### Comunicação interna não deve ocupar canal de segurança

VHF é equipamento de comunicação marítima externa e de segurança. Não deve ser tratado como substituto rotineiro de interfone.

### Ruído ambiente muda a especificação

Casa de máquinas, cockpit aberto e áreas externas pedem transdutores, microfones e níveis de sinalização diferentes dos usados em cabines silenciosas.

### Cabeamento e EMC importam

Linhas de áudio e dados são sensíveis a ruído de alternador, inversor, motores e cargas comutadas. Projeto ruim gera chiado, baixa inteligibilidade e falsa percepção de defeito do equipamento.

## Arquiteturas comuns

### Sistema analógico simples

- 2 a 4 estações;
- lógica direta;
- boa confiabilidade;
- baixa complexidade de diagnóstico.

### Sistema digital dedicado

- mais recursos de chamada e gerenciamento;
- ainda preserva arquitetura de comunicação interna independente.

### Sistema IP

- integra voz, vídeo e rede local;
- faz sentido quando há backbone de dados consistente;
- aumenta dependência de switch, energia de rede e configuração.

## Projeto e instalação

### O que precisa ser definido

1. quais pontos realmente precisam de comunicação;
2. se a comunicação deve ser simultânea, seletiva ou por chamada;
3. se o sistema precisa sobreviver a perda de internet;
4. nível de ruído de cada ambiente;
5. se haverá integração com câmeras, PA ou rede IP;
6. estratégia de alimentação e proteção do circuito.

### Diretrizes práticas

- separar cabos de áudio e dados dos cabos de potência;
- prever estação adequada para casa de máquinas, se aplicável;
- escolher microfone e alto-falante compatíveis com o ambiente;
- documentar claramente zona, estação e alimentação;
- não esconder sistema crítico dentro de rede mal gerida.

## Onde costuma dar problema

| Problema | Causa provável |
| --- | --- |
| chiado ou zumbido | interferência eletromagnética ou aterramento ruim |
| baixa inteligibilidade | microfone inadequado, ruído ambiente alto ou instalação ruim |
| estação muda | falha de alimentação, cabo rompido ou conector degradado |
| falha intermitente | vibração, umidade ou terminal mal crimpado |
| sistema IP instável | energia ruim, endereçamento confuso ou rede saturada |

## Diagnóstico prático

1. Confirmar alimentação em cada estação ou nó de rede.
2. Isolar se a falha está em uma estação, em uma zona ou no sistema inteiro.
3. Testar comunicação com bypass temporário do cabeamento suspeito.
4. Verificar proximidade com fontes de EMI.
5. Em sistemas IP, checar switch, VLAN, IP e latência local antes de culpar o terminal.

## Boas práticas profissionais

- usar solução simples quando a aplicação é simples;
- manter comunicação de manobra independente de internet;
- especificar componentes e conectores compatíveis com umidade e vibração;
- separar tecnicamente comunicação interna, PA e comunicação externa;
- testar clareza de áudio com motor, vento e ruído real da operação;
- treinar usuários para reconhecer chamada, prioridade e resposta esperada.

## Erros comuns

- improvisar com celular como solução "definitiva";
- usar VHF para rotina interna de bordo;
- instalar equipamento predial em área náutica exposta sem critério;
- passar áudio junto com cabos de alta corrente;
- escolher sistema IP sem ter rede minimamente robusta.

## Relação com outros sistemas

- **[[Wi-Fi a Bordo — Roteador Marine e Conectividade]]** — suporte para soluções IP quando aplicável.
- **[[Câmeras de Bordo / Sistema CFTV]]** — integração voz/vídeo em certas arquiteturas.
- **[[Sistema de Alarme Geral / Painel de Alarmes]]** — pode compartilhar lógica de anúncio, mas não é a mesma coisa.
- **[[Som]]** — alguns sistemas usam amplificação ou zonas de áudio relacionadas.
- **[[VHF]]** — comunicação externa e de segurança, não substituto do interfone.

## Normas e referências

- documentação do fabricante do sistema;
- boas práticas de cabeamento e EMC da embarcação;
- requisitos de operação específicos quando a embarcação estiver sob regime comercial ou classe.

## FAQ

**Sistema IP precisa de internet para funcionar?**

Não. Ele pode funcionar localmente sem internet, desde que a rede local esteja operacional.

**Vale a pena instalar interfone em barco pequeno?**

Depende da operação. Se houver manobra com tripulação distribuída, flybridge, popa distante ou casa de máquinas separada, pode agregar muito.

**Walkie-talkie resolve?**

Como contingência, às vezes. Como solução fixa e profissional, normalmente não.

## Integração com outras notas

- [[Wi-Fi a Bordo — Roteador Marine e Conectividade]]
- [[Câmeras de Bordo / Sistema CFTV]]
- [[Sistema de Alarme Geral / Painel de Alarmes]]
- [[Som]]
- [[TV a Bordo / Entretenimento]]
- [[VHF]]

## Perguntas que esta nota responde

- O que é interfone de bordo?
- Quando vale usar intercomunicador dedicado em embarcações?
- Como evitar falhas de inteligibilidade e ruído em sistemas de interfone?
