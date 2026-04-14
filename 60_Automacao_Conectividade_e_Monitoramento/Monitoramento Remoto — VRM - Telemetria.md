---
title: "Monitoramento Remoto — VRM / Telemetria"
note_type: "system"
domain: "60_Automacao_Conectividade_e_Monitoramento"
source_file: "MONITORAMENTO REMOTO — VRM TELEMETRIA 33a19734f7fb8100b1c2cbedc98aedd6.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://abycinc.org/standards/"
  - "https://www.nmea.org/standards.html"
  - "https://www.nmea.org/nmea-0400.html"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "MONITORAMENTO REMOTO — VRM TELEMETRIA"
  - "MONITORAMENTO REMOTO — VRM / TELEMETRIA"
  - "VRM / Monitoramento Remoto"
seo_title: "Monitoramento Remoto — VRM / Telemetria"
seo_description: "MONITORAMENTO REMOTO — VRM / TELEMETRIA — Plataforma de monitoramento e gestao remota de sistemas Victron conectados a internet, com alertas, diagnostico e alguns controles remotos."
seo_keywords:
  - "Monitoramento"
  - "Remoto"
  - "VRM"
  - "Telemetria"
  - "60 Automacao Conectividade e Monitoramento"
geo_queries:
  - "O que e Monitoramento Remoto — VRM / Telemetria em instalacoes eletricas nauticas?"
  - "Qual e a funcao de Monitoramento Remoto — VRM / Telemetria na embarcacao?"
related_notes:
  - "Atuador Linear"
  - "Automação de Bordo — Sistemas Domoticos"
  - "Câmeras de Bordo / Sistema CFTV"
  - "Interfone / Intercomunicador de Bordo"
  - "Sensor de Nível Diesel"
  - "Sistema de Alarme Geral / Painel de Alarmes"
  - "Som"
  - "Starlink / Internet a Bordo"
---

# Monitoramento Remoto — VRM / Telemetria

> [!abstract] Resumo técnico
> MONITORAMENTO REMOTO — VRM / TELEMETRIA — Plataforma de monitoramento remoto da Victron para sistemas conectados a um GX device com internet. Permite monitorar, alertar, diagnosticar e, em certos casos, controlar dispositivos compatíveis remotamente.

## O que é

VRM (Victron Remote Monitoring) é a plataforma remota da Victron Energy para supervisão, diagnóstico e gestão de sistemas conectados. Segundo a documentação oficial, o VRM é gratuito e funciona com um GX device com acesso à internet; em sistemas menores, também pode operar com GlobalLink 520.

O ponto técnico importante é que o VRM não é "mais um display". Ele é a camada remota de um ecossistema que inclui:

- equipamentos Victron ou integrados;
- um dispositivo GX;
- conectividade com internet;
- regras de alarme e acesso de usuários.

## O que está confirmado em fonte oficial

Segundo o manual oficial do VRM:

- o portal oferece monitoramento remoto, alertas, controle, gestão e otimização;
- o dashboard e o app exibem estado da instalação e dados históricos;
- o VRM oferece **Remote Console**;
- o VRM permite **remote firmware update** em equipamentos compatíveis;
- o VRM oferece **Remote VEConfigure** para Multi/Quattro compatíveis;
- o VRM pode oferecer controles remotos para ESS, inverter/charger, relés GX, gerador e EV charging, quando suportados e com conexão em tempo real.

## Função na embarcação

- acompanhar estado energético e eventos críticos sem estar a bordo;
- receber alarmes e detectar problemas cedo;
- apoiar diagnóstico remoto antes de visita técnica;
- registrar histórico de operação;
- viabilizar gestão técnica mais madura da embarcação.

## Requisitos mínimos

1. Equipamentos compatíveis ou parcialmente integrados.
2. Dispositivo GX adequadamente alimentado e conectado.
3. Conexão com internet.
4. Cadastro e configuração correta da instalação no portal.

## Limites reais

**Sem internet:** o sistema local continua operando, mas o VRM não recebe dados em tempo real até a conectividade voltar.

**Sem ecossistema compatível:** a visibilidade e o nível de controle podem ser limitados.

**Sem parametrização correta:** alerta demais vira ruído; alerta de menos vira falsa sensação de segurança.

## Problemas mais frequentes

| Problema | Causa provável |
| --- | --- |
| VRM offline | perda de internet, GX desligado ou falha local |
| dados ausentes ou incompletos | integração parcial ou configuração incorreta |
| alarmes inúteis | parametrização ruim e histerese mal definida |
| falsa confiança no remoto | ausência de rotina local e de verificação operacional |

## Diagnóstico prático

1. Confirmar se o GX está alimentado e operacional localmente.
2. Verificar se a instalação tem internet funcional.
3. Conferir cadastro e acesso à instalação.
4. Validar se os equipamentos aparecem corretamente no ecossistema GX.
5. Revisar regras de alarme, histerese e perfis de notificação.

## Boas práticas

- configurar alarmes com critério técnico e histerese coerente;
- separar alerta crítico de evento meramente informativo;
- revisar o portal periodicamente, mesmo sem alarme;
- documentar usuários, permissões e responsabilidades;
- usar o histórico para manutenção preditiva, não só para reação a falhas.

## Erros comuns

- instalar VRM e nunca ajustar regras de alarme;
- achar que telemetria substitui inspeção e rotina operacional;
- abrir acesso excessivo a usuários sem governança;
- depender de internet frágil sem estratégia de redundância.

## Relação com outros sistemas

- **Banco de baterias / monitor de bateria** — telemetria energética.
- **Inversor/carregador** — estado, modos e eventos.
- **Gerador / relés / cargas controladas** — quando a arquitetura suportar controle remoto.
- **Starlink / Wi-Fi / 4G** — base de conectividade para o portal remoto.

## Normas e referências

- **Manual oficial VRM Portal**: [victronenergy.com/media/pg/VRM_Portal_manual/en/index-en.html](https://www.victronenergy.com/media/pg/VRM_Portal_manual/en/index-en.html)
- **Introdução oficial VRM**: [victronenergy.com/media/pg/VRM_Portal_manual/en/introduction.html](https://www.victronenergy.com/media/pg/VRM_Portal_manual/en/introduction.html)
- **Controles no VRM**: [victronenergy.com/media/pg/VRM_Portal_manual/en/control-your-devices-in-vrm.html](https://www.victronenergy.com/media/pg/VRM_Portal_manual/en/control-your-devices-in-vrm.html)

## FAQ

**VRM funciona sem internet?**

O sistema local pode continuar operando, mas o portal remoto depende de conectividade.

**VRM é pago?**

A documentação oficial informa que o VRM é gratuito; recursos e serviços específicos devem sempre ser conferidos na documentação vigente.

**VRM substitui display local?**

Não. Ele complementa a operação local com camada remota, histórica e de gestão.

## Integração com outras notas

- [[Atuador Linear]]
- [[Automação de Bordo — Sistemas Domoticos]]
- [[Câmeras de Bordo / Sistema CFTV]]
- [[Interfone / Intercomunicador de Bordo]]
- [[Sensor de Nível Diesel]]
- [[Sistema de Alarme Geral / Painel de Alarmes]]
- [[Som]]
- [[Starlink / Internet a Bordo]]

## Perguntas que esta nota responde

- O que é Monitoramento Remoto — VRM / Telemetria em instalações elétricas náuticas?
- Qual é a função de Monitoramento Remoto — VRM / Telemetria na embarcação?
