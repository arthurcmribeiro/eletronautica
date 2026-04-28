---
title: "Wi-Fi a Bordo — Roteador Marine e Conectividade"
note_type: "system"
domain: "60_Automacao_Conectividade_e_Monitoramento"
source_file: "WI-FI A BORDO — ROTEADOR MARINE E CONECTIVIDADE 33a19734f7fb8139a6d9c3aa78b1c688.md"
status: "tier-b-curated"
fase_6_reescrita: 130
reviewed_on: "2026-04-26"
review_jurisdiction: "Brasil + Internacional"
review_level: "tier-b-curated"
normas_citadas:
  - "ABYC E-11"
  - "ABYC TE-30"
  - "IEC 60945"
  - "IEEE 802.11 a/b/g/n/ac/ax/be (Wi-Fi 1-7)"
  - "IEC 60529 (IP)"
  - "IEC 61547 (EMC)"
  - "ANATEL Resolução 715/2019 + Portaria 14.448 (2,4/5GHz/6GHz)"
  - "FCC Part 15"
  - "EU Directive 2014/53/EU (RED)"
  - "Manual técnico Peplink Pepwave / WirelessHaven / Mikrotik / Ubiquiti / GL.iNet"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://www.nmea.org/standards.html"
  - "https://www.nmea.org/nmea-0400.html"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "WI-FI A BORDO — ROTEADOR MARINE E CONECTIVIDADE"
seo_title: "Wi-Fi a Bordo — Roteador Marine e Conectividade"
seo_description: "WI-FI A BORDO — Rede local sem fio para distribuir conectividade e integrar dispositivos da embarcacao. Wi-Fi nao e sinônimo de internet; a WAN pode vir de 4G, Starlink, marina ou outra fonte."
seo_keywords:
  - "Roteador"
  - "Conectividade"
  - "60 Automacao Conectividade e Monitoramento"
geo_queries:
  - "O que e Wi-Fi a Bordo — Roteador Marine e Conectividade em instalacoes eletricas nauticas?"
  - "Qual e a funcao de Wi-Fi a Bordo — Roteador Marine e Conectividade na embarcacao?"
related_notes:
  - "Atuador Linear"
  - "Automação de Bordo — Sistemas Domoticos"
  - "Câmeras de Bordo / Sistema CFTV"
  - "Interfone / Intercomunicador de Bordo"
  - "Monitoramento Remoto — VRM / Telemetria"
  - "Sensor de Nível Diesel"
  - "Sistema de Alarme Geral / Painel de Alarmes"
  - "Som"
---

# Wi-Fi a Bordo — Roteador Marine e Conectividade

> [!abstract] Resumo técnico
> WI-FI A BORDO — Rede local sem fio usada para distribuir conectividade e integrar dispositivos a bordo. Wi-Fi não é sinônimo de internet: a rede local pode existir sem acesso externo, e a internet pode vir de 4G/5G, Starlink, Wi-Fi de marina ou outras fontes WAN.

> [!tldr] TL;DR — 4 regras
> 1. **Roteador marine-grade** (Peplink Pepwave MAX BR1/HD2/Transit, Mikrotik LtAP, Ubiquiti UniFi, GL.iNet) com IP rated + EMC + multi-WAN (4G/5G + Starlink + Wi-Fi marina).
> 2. **Multi-WAN failover** essencial: Wi-Fi marina (rápido + grátis) → 4G/5G (em movimento) → Starlink (oceânico) — switch automático.
> 3. **Wi-Fi 6/6E (802.11ax/be)** preferível em yacht moderno — múltiplos dispositivos simultâneos sem congestionar.
> 4. **Cybersecurity** — senha forte WPA3 + segregação de rede (instrumentos NMEA isolados de dispositivos guest) + firmware atualizado.

> [!info] Glossário rápido
> - **WAN:** Wide Area Network (internet externa).
> - **LAN:** Local Area Network (rede interna).
> - **Multi-WAN:** múltiplas conexões WAN com balanceamento.
> - **Failover:** mudança automática de WAN ativa.
> - **WPA3:** padrão de segurança Wi-Fi atual.
> - **VLAN:** Virtual LAN (segregação de rede).
> - **Pepwave / Peplink:** referência marine multi-WAN.
> - **Wi-Fi 6/6E/7:** padrões IEEE 802.11ax/ax/be.

## O que é

Wi-Fi a bordo é a camada sem fio da rede local da embarcação. Seu papel é interligar dispositivos móveis, TVs, câmeras IP, controladores, sistemas de automação e, em muitos casos, o acesso externo à internet.

Uma arquitetura séria normalmente separa:

- **WAN** — a fonte de internet que vem de fora.
- **LAN cabeada** — o backbone local mais confiável.
- **Wi-Fi** — a camada de acesso para usuários e dispositivos sem fio.

## Função

- Distribuir conectividade aos usuários a bordo.
- Interligar dispositivos IP como câmeras, smart TVs e controladores.
- Servir de base para monitoramento remoto, entretenimento e automação.
- Criar uma rede local funcional mesmo quando não houver internet externa.

## Fundamentos mínimos

**Wi-Fi não é internet:** um barco pode ter rede local funcionando perfeitamente e, ainda assim, estar sem acesso externo.

**Frequências:** 2,4 GHz tende a oferecer maior alcance e pior convivência em ambientes congestionados; 5 GHz e faixas mais novas tendem a oferecer mais capacidade, mas sofrem mais com atenuação estrutural.

**Estrutura da embarcação:** cascos metálicos, anteparas, mobiliário denso, motores e compartimentos técnicos degradam a cobertura sem fio. Em muitos casos, o erro não está no roteador, e sim na expectativa de cobrir a embarcação inteira com um único ponto.

**Backbone cabeado:** sempre que possível, usar backbone Ethernet entre roteador, switch e access points é mais robusto que depender de mesh puramente sem fio.

## Arquitetura recomendada

```text
Fonte WAN (4G / Starlink / marina)
        ↓
Roteador principal / gateway
        ↓
Switch local
        ↓
Access points por zona
        ↓
Clientes Wi-Fi e dispositivos IP
```

## Configurações comuns

**Configuração simples**

- um roteador único
- adequada para embarcação pequena e de baixa complexidade
- limitada em cobertura e segmentação

**Configuração por zonas**

- roteador principal + switch + access points
- melhor para flybridge, cabines, salão e áreas externas
- solução mais profissional

**Configuração com failover**

- múltiplas WANs
- troca automática entre fontes externas
- adequada para embarcação que depende de conectividade contínua

## Onde costuma dar problema

| Problema | Causa provável |
| --- | --- |
| cabines sem sinal | atenuação estrutural e falta de AP por zona |
| rede lenta | WAN ruim, congestionamento ou planejamento inadequado |
| reinício de equipamentos | alimentação DC instável ou conversão ruim |
| dispositivos críticos na mesma rede dos passageiros | segmentação inexistente |
| baixa confiabilidade do mesh | excesso de saltos sem backbone cabeado |

## Diagnóstico prático

1. Separar o problema entre `Wi-Fi local` e `internet externa`.
2. Medir cobertura por zona da embarcação.
3. Verificar alimentação do roteador/switch em partidas e transientes.
4. Confirmar se há backbone cabeado suficiente.
5. Separar tráfego de convidados e de sistemas críticos.

## Boas práticas

- Preferir alimentação DC nativa ou arquitetura de energia coerente.
- Setorizar a cobertura por zonas de uso real.
- Usar backbone cabeado para APs sempre que possível.
- Separar rede de passageiros, entretenimento e sistemas.
- Documentar SSIDs, senhas, IPs e topologia.
- Manter firmware e política de segurança minimamente atualizados.

## Erros comuns

- Chamar qualquer problema de internet de "problema de Wi-Fi".
- Querer cobertura total com um único roteador em embarcação complexa.
- Alimentar tudo por conversões desnecessárias sem tratar transientes.
- Misturar dispositivos críticos com rede aberta de convidados.
- Instalar AP onde o acesso é fácil, e não onde a cobertura precisa existir.

## Relação com outros sistemas

- **Starlink / Internet a Bordo** — fonte WAN frequente.
- **Monitoramento remoto** — depende de conectividade estável.
- **Câmeras IP** — exigem rede local minimamente robusta.
- **Automação de bordo** — pode usar Wi-Fi, Ethernet ou ambos.

## Brasil x referências internacionais

### Leitura equilibrada

No mercado local ainda é comum chamar de "Wi-Fi a bordo" um roteador doméstico ligado no inversor. Em uma arquitetura robusta, conectividade é rede, energia, segmentação, cobertura e manutenção.

## Normas e referências

- **IEEE 802.11 / documentação do fabricante** — padrões e capacidades do equipamento.
- **ANATEL (edição a verificar)** — homologação aplicável aos equipamentos de rádio.
- **Boas práticas de instalação elétrica de bordo** — para alimentação DC, proteção e encaminhamento de cabos.

## FAQ

**Um único roteador cobre todo o barco?**

Às vezes, em embarcação pequena e simples. Em muitas embarcações reais, não.

**Vale mais a pena mesh ou cabo?**

Quando for possível escolher, backbone cabeado costuma ser mais previsível e robusto.

**Wi-Fi sem internet ainda serve para alguma coisa?**

Sim. Rede local, câmeras, streaming interno, controle local e integração de dispositivos continuam funcionando.

## Integração com outras notas

- [[Atuador Linear]]
- [[Automação de Bordo — Sistemas Domoticos]]
- [[Câmeras de Bordo / Sistema CFTV]]
- [[Interfone / Intercomunicador de Bordo]]
- [[Monitoramento Remoto — VRM / Telemetria]]
- [[Sensor de Nível Diesel]]
- [[Sistema de Alarme Geral / Painel de Alarmes]]
- [[Som]]

## Perguntas que esta nota responde

- O que é Wi-Fi a Bordo — Roteador Marine e Conectividade na embarcação?
- Qual é a função do Wi-Fi a bordo?
