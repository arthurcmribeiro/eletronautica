---
title: "Motor de Trim - Tilt"
note_type: "technical-note"
domain: "90_Revisao_Manual"
source_file: "MOTOR DE TRIM TILT 33a19734f7fb81b5b54bd17895f75160.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "48"
tier_fase_6: "A"
reviewed_on: "2026-04-21"
review_jurisdiction:
  - "Brasil"
  - "internacional"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
  - "https://www.quicksilver-products.com/"
  - "https://yamalube.com/"
  - "https://www.volvopenta.com/parts-service/"
review_level: "engineering-curated"
normas_citadas:
  - "ABYC P-22 - Marine Engines - Installation"
  - "ABYC P-24 - Electric Propulsion Systems (for electric trim integration)"
  - "ABYC A-16 - Electrical Safety (circuit protection)"
  - "ABYC E-11 - AC and DC Electrical Systems on Boats"
  - "ABYC P-4 - Marine Inboard Engines and Transmissions (reference for stern drives)"
  - "ISO 10133:2017 - Small craft - Extra-low-voltage DC installations"
  - "ISO 16147:2020 - Small craft - Inboard diesel engines - Engine-mounted fuel and electrical components"
  - "ISO 8665:2022 - Small craft - Marine propulsion reciprocating internal combustion engines - Power measurements and declarations"
  - "ISO 11591:2011 - Engine-driven small craft - Field of vision from helm position"
  - "IEC 60068-2-11 - Salt mist testing"
  - "IEC 60529:2013 - Degrees of protection provided by enclosures (IP Code)"
  - "ISO 8846:1990 - Electrical devices - Protection against ignition of flammable gases"
  - "UL 1500 - Ignition-Protected Marine Products"
  - "SAE J1171 - Marine Ignition Protection"
  - "ISO 3448:1992 - Industrial liquid lubricants - ISO viscosity classification"
  - "ISO 11158:2023 - Hydraulic fluids Family H"
  - "Dexron III / Dexron VI - GM Automatic Transmission Fluid Specification"
  - "Mercon V - Ford Automatic Transmission Fluid Specification"
  - "Mercury Quicksilver Power Trim & Steering Fluid - Mercury Marine OEM specification"
  - "Yamalube Power Trim & Steering Fluid - Yamaha OEM specification"
  - "Volvo Penta Power Trim Fluid - Volvo Penta OEM specification"
  - "SAE J1703 - Motor Vehicle Brake Fluid (reference for incompatibility - DO NOT USE)"
  - "NBR 11213:2020 - Óleos hidráulicos - Classificação e especificação"
  - "NBR 14134:2015 - Óleos lubrificantes - Terminologia"
  - "NORMAM-01/DPC - Embarcações empregadas na navegação em mar aberto"
  - "NORMAM-03/DPC - Embarcações empregadas na navegação interior"
aliases:
  - "MOTOR DE TRIM TILT"
  - "Trim and tilt"
  - "Power trim"
  - "PTT (Power Trim and Tilt)"
seo_title: "Motor de trim e tilt: eletro-hidráulica, ATF, relés, alívio manual e falhas"
seo_description: "Guia técnico sobre motor de trim/tilt em motor de popa e stern drive: conjunto eletro-hidráulico, relés, fluido ATF/trim, proteção, cilindros, válvula de alívio, queda de tensão e diagnóstico do sistema."
seo_keywords:
  - "trim tilt boat"
  - "motor de trim embarcação"
  - "power trim tilt"
  - "falha trim tilt"
  - "óleo trim tilt Mercury Yamaha"
  - "ATF trim hidráulico"
geo_queries:
  - "Por que o trim/tilt sobe devagar, não desce ou fica travado?"
  - "Como diferenciar falha elétrica de falha hidráulica no trim/tilt?"
  - "Qual fluido usar no trim/tilt Mercury, Yamaha ou Volvo Penta?"
related_notes:
  - "Óleos Hidráulicos Marine — Guia Completo"
  - "Relés e Relés de Estado Sólido"
  - "Fusíveis DC — Proteção Contra Sobrecorrente"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
  - "Plataforma de Popa Elétrica - Hidráulica"
  - "Flap"
  - "Estabilizador"
---

# Motor de Trim - Tilt

> [!abstract] Resumo técnico
> O sistema de `trim/tilt` é um atuador eletro-hidráulico sujeito a corrente elevada, ambiente agressivo, vedação crítica e forte dependência de relés/contatores e condição hidráulica. O erro mais comum é tratar tudo como falha elétrica ou tudo como falha de bomba, quando o sistema exige leitura combinada. Fluido correto (ATF Dexron ou fluido específico do fabricante) e sangria adequada são decisivos.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Trim ≠ tilt** — `trim` é ajuste fino dentro da faixa de navegação; `tilt` é levantamento maior para manobra/reboque. Mudam esforço, velocidade e, às vezes, lógica de controle.
> 2. **Sistema é eletro-hidráulico** — motor DC aciona bomba hidráulica que move cilindro(s); falha pode estar no elétrico, no hidráulico ou em ambos.
> 3. **Corrente é alta e intermitente** — pico de 40-120 A em motores de popa médios; stall pode chegar a 200 A. Fusível por stall, não por corrente nominal.
> 4. **Relé/solenoide reversor é ponto de falha crítico** — "sobe mas não desce" (ou vice-versa) costuma ser contato oxidado/soldado.
> 5. **Queda de tensão degrada tudo** — cabo do motor é curto mas de alta corrente; pontos de massa e positivo precisam estar limpos.
> 6. **Fluido é crítico e volume é pequeno (150-500 ml)** — ATF Dexron III/VI ou fluido proprietário (Quicksilver, Yamalube, Volvo Penta Power Trim); NUNCA usar fluido de freio ou óleo de motor.
> 7. **Alívio manual é recurso de segurança** — parafuso/válvula permite mover conjunto em pane; procedimento específico por fabricante deve estar documentado.
> 8. **Perda de pressão em repouso indica vedação interna** — motor "desce sozinho" após desligar, possivelmente válvula de retenção ou pistão com vazamento interno.
> 9. **Dois lados do cilindro precisam ser sangrados** — sangria incompleta deixa sistema "esponjoso" e com perda de força.

> [!danger] Quando chamar um especialista (9 cenários)
> 1. **Conjunto descendo sozinho com motor desligado** — vedação de pistão ou válvula de retenção interna; risco de motor bater em rampa/cais/fundo em repouso.
> 2. **Óleo leitoso no reservatório** — água entrou; operação danifica bomba e corrói interior em curto prazo; parar e drenar.
> 3. **"Sobe e desce sozinho" em navegação** — comando elétrico fantasma (chicote comprometido) ou switch travado; desligar fusível e investigar antes de seguir operando.
> 4. **Cheiro de queimado no relé de trim** — contato soldado ou motor em stall; risco de incêndio em carenagem.
> 5. **Motor forçando contra fim de curso** — falha de corte; pode romper mangueira em alta pressão (até 200 bar).
> 6. **Falha após retrofit de fluido errado** — ATF em sistema que pede fluido de trim específico (ou vice-versa) causa falha progressiva; drenar e trocar conforme manual imediatamente.
> 7. **Vazamento de óleo na haste do pistão em operação** — vedação comprometida; risco de perda súbita de pressão e queda do conjunto.
> 8. **Trim/tilt não responde após tempestade/raio** — possibilidade de dano em módulo eletrônico de alguns sistemas; teste sistemático antes de operar em mar.
> 9. **Perícia pós-acidente (impacto com fundo, abalroamento)** — não acionar sistema; fotografar posição e estado; preservar evidências para investigação.

## O que é

O `trim/tilt` ajusta o ângulo do propulsor ou conjunto associado para:

- otimização de navegação (ângulo de trim muda atitude e consumo);
- controle de atitude e eficiência em planeio;
- recolhimento para manobra, atracação, reboque ou proteção em águas rasas.

Embora o uso pelo operador pareça simples, o sistema envolve:

- motor elétrico DC (tipicamente 12V em popa, 12/24V em stern drive);
- bomba hidráulica (palheta ou engrenagem, pressão 100-200 bar);
- cilindros ou atuadores hidráulicos (simples ou duplo cilindro);
- válvulas internas (retenção, alívio, bypass);
- relés/contatores de comando (reversor de polaridade);
- alívio manual (parafuso ou válvula manual), em muitos modelos.

## Diferença entre trim e tilt

Em termos práticos:

- `trim` é o ajuste funcional dentro da faixa de operação de navegação (tipicamente 0-20°);
- `tilt` é o levantamento maior para fora da condição normal (até 70-90° para reboque ou acesso à rabeta).

Essa diferença muda esforço, velocidade, curso e, às vezes, lógica de controle.

Em alguns sistemas, `trim` e `tilt` usam bombas ou circuitos distintos.

## Arquitetura eletro-hidráulica

O conjunto depende tanto do lado elétrico quanto do hidráulico.

Do lado elétrico:

- corrente alta por curto período (típico 40-120 A, stall até 200 A em motores grandes);
- sensibilidade a relés e quedas de tensão;
- proteção correta (fusível ou breaker dimensionado ao stall);
- integridade de chicote e comandos (switch no leme, console, ou comando no joystick).

Do lado hidráulico:

- fluido compatível (Dexron ou fluido proprietário);
- vedação íntegra (NBR ou Viton conforme sistema);
- ausência de ar e contaminação excessiva;
- válvulas internas funcionando como previsto (retenção, alívio, bypass manual).

## Relés e comando

Muitos sistemas dependem de relés ou solenoides reversores para alternar os sentidos de acionamento.

Isso significa que sintomas como:

- sobe e não desce;
- desce e não sobe;
- apenas "clica" sem movimentar;

podem nascer do circuito de comando, não do conjunto hidráulico.

Os relés são tipicamente contatores de alta corrente (80-200 A) montados na carenagem do motor em popa, ou próximo ao conjunto de bomba em stern drive.

Ver também:

- [[Relés e Relés de Estado Sólido]]

## Queda de tensão e desempenho

Como a corrente é alta, tensão insuficiente pode causar:

- movimento lento;
- aquecimento anormal;
- ruído sem força;
- diagnóstico errado de "bomba cansada".

Pontos críticos:

- ponto de massa do motor (quase sempre no bloco);
- cabo positivo da bateria até o relé de trim;
- conexões no próprio relé (oxidação é comum);
- chave geral e qualquer `bus bar` intermediário.

Ver também:

- [[Fusíveis DC — Proteção Contra Sobrecorrente]]

## Fluido e manutenção (crítico)

**Fluidos corretos por fabricante (validar sempre no manual):**

| Fabricante | Fluido recomendado | Alternativa aceita |
|---|---|---|
| Mercury / Mariner | Quicksilver Power Trim & Steering Fluid | ATF Dexron III |
| Yamaha | Yamalube Power Trim & Steering Fluid | ATF Dexron III |
| Suzuki | ATF Dexron III OU Suzuki Power Trim Fluid | — |
| Evinrude / Johnson (BRP) | ATF Dexron III | Fluido BRP específico |
| Volvo Penta (stern drive) | Volvo Penta Power Trim Fluid | ATF Dexron III (conforme manual) |
| Mercruiser (Bravo/Alpha stern drives) | Quicksilver Power Trim Fluid | ATF Dexron III |
| Honda Marine | Honda ATF DW-1 ou Dexron III | — |
| Tohatsu / Nissan | ATF Dexron III | — |

**O que NÃO usar (sob NENHUMA hipótese):**

- fluido de freio DOT 3/4/5.1 — ataca vedação de NBR;
- óleo de motor SAE 15W-40 — viscosidade errada, aditivação errada;
- óleo hidráulico industrial HLP 32 genérico — pode não ter compatibilidade com vedação e fricção;
- ATF Mercon V ou ATF+4 — formulação diferente do Dexron;
- fluido automotivo de direção hidráulica — pode funcionar em emergência mas degrada com tempo.

**Procedimento de troca e sangria:**

1. Posicionar motor em tilt máximo (haste totalmente estendida);
2. Drenar pelo bujão inferior (se existir) ou pelo bujão superior usando bomba de sucção;
3. Inspecionar fluido drenado — cor âmbar clara (novo), rosa/vermelho (Dexron), leitoso = água;
4. Encher pelo bujão de reposição com fluido correto;
5. Ciclar up/down várias vezes com motor em posição normal;
6. Completar nível e repetir ciclagem até nível estabilizar (sinal de sistema sangrado);
7. Verificar ausência de vazamentos após 24 h em repouso.

Ver também:

- [[Óleos Hidráulicos Marine — Guia Completo]]

## Parte hidráulica

O circuito hidráulico precisa manter:

- estanqueidade (vedações, mangueiras, conexões);
- pressão (bomba íntegra, válvulas de retenção funcionais);
- fluido apropriado (ver tabela acima);
- ausência de contaminação relevante (partículas, ar, água);
- retenção estável quando o conjunto está em posição.

Se a unidade sobe e depois cede sem comando, por exemplo, o problema pode estar mais em retenção hidráulica (válvula interna ou vedação do pistão) do que em comando elétrico.

## Alívio manual e contingência

Muitos conjuntos possuem forma de alívio manual para permitir movimentação em contingência.

Esse recurso é crítico para:

- recolher ou baixar o motor em pane elétrica;
- permitir transporte em rampa ou retorno seguro;
- evitar dependência absoluta do acionamento elétrico.

O procedimento exato é específico do fabricante e deve constar da documentação da embarcação. Tipicamente envolve:

- parafuso de alívio (1-3 voltas para liberar fluxo interno);
- manipulação manual do conjunto (peso significativo, geralmente duas pessoas);
- retorno do parafuso à posição original após manobra.

## Falhas mais comuns

As falhas recorrentes são:

- relé/solenoide defeituoso (contato soldado, solenoide queimado);
- baixa tensão no acionamento (queda em cabo/massa/conexão);
- motor elétrico fatigado (escovas gastas, coletor oxidado);
- contaminação ou nível inadequado de fluido;
- vedação degradada (pistão, haste, válvulas internas);
- retenção hidráulica ruim (válvula de retenção interna pingando);
- comando do leme com mau contato (switch gasto, chicote em curto);
- ar no sistema após manutenção (sangria incompleta).

## Diagnóstico profissional

Perguntas essenciais:

1. O comando está chegando corretamente ao conjunto (tensão medida no relé sob carga)?
2. A tensão no motor de acionamento é adequada sob carga (medir no próprio motor, não apenas na bateria)?
3. O conjunto hidráulico gera e mantém pressão (observar se haste se move contra carga externa)?
4. O problema é simétrico nos dois sentidos ou só em um?
5. Existe recurso manual e ele funciona (teste sem comando elétrico)?
6. O nível e aparência do fluido estão normais?

Ensaios úteis:

- medir tensão no acionamento (bateria, relé, motor — três pontos);
- confirmar atuação dos relés/solenoides (ouvir click, ver escovilhar em circuito com multímetro);
- inspecionar nível e estado do fluido conforme fabricante;
- observar ruído, velocidade e retenção do movimento;
- comparar comportamento `up` e `down` (diferenças revelam qual lado do circuito tem problema);
- testar alívio manual para confirmar integridade mecânica do conjunto.

## Boas práticas

- manter o procedimento de alívio manual documentado e acessível;
- inspecionar relés, cabos e pontos de massa semestralmente;
- usar o fluido especificado pelo fabricante (jamais "equivalente genérico");
- incluir o sistema na rotina de teste, não só quando falhar;
- investigar lentidão como possível problema elétrico E hidráulico ao mesmo tempo;
- registrar no plano de manutenção a marca e volume de fluido usado na última troca;
- testar alívio manual pelo menos uma vez por temporada.

## Erros comuns

- trocar relé sem verificar a causa do sobreesforço;
- usar fluido inadequado (fluido de freio, óleo de motor, ATF errado);
- ignorar queda de tensão;
- forçar mecanicamente o conjunto sem entender a posição hidráulica;
- operar até a pane e só então pensar em contingência manual;
- misturar fluidos de marcas/tipos diferentes sem fazer drenagem prévia;
- sangrar apenas um ciclo e considerar "pronto".

## Normas aplicáveis

### 1. Padrão primário de motor marine (ABYC)

- **ABYC P-22** — Marine Engines — Installation (integração do sistema de trim);
- **ABYC P-4** — Marine Inboard Engines and Transmissions (stern drives);
- **ABYC P-24** — Electric Propulsion Systems (quando trim integra com propulsão elétrica);
- **ABYC A-16** — Electrical Safety (proteção de circuito);
- **ABYC E-11** — AC and DC Electrical Systems on Boats (dimensionamento).

### 2. Padrão internacional (ISO)

- **ISO 10133:2017** — Extra-low-voltage DC installations;
- **ISO 16147:2020** — Inboard diesel engines — engine-mounted fuel and electrical components;
- **ISO 8665:2022** — Marine propulsion engines — power measurements;
- **ISO 11591:2011** — Field of vision from helm position (interação com trim afeta visibilidade).

### 3. Proteção e ambiente

- **IEC 60529:2013** — IP Code (tipicamente IP67 para conjunto);
- **IEC 60068-2-11** — Salt mist testing;
- **ISO 8846:1990** — Protection against ignition of flammable gases;
- **UL 1500** — Ignition-Protected Marine Products;
- **SAE J1171** — Marine Ignition Protection.

### 4. Fluidos e lubrificantes

- **ISO 3448:1992** — Viscosity classification;
- **ISO 11158:2023** — Hydraulic fluids Family H;
- **Dexron III/VI** (GM) — ATF specification;
- **Mercon V** (Ford) — ATF specification (raramente usado em trim);
- **SAE J1703** — Motor Vehicle Brake Fluid (referência de incompatibilidade);
- **NBR 11213:2020** — Óleos hidráulicos (Brasil);
- **NBR 14134:2015** — Lubrificantes — Terminologia.

### 5. Brasil (Marinha)

- **NORMAM-01/DPC** — Embarcações em mar aberto;
- **NORMAM-03/DPC** — Embarcações em navegação interior.

### Tabela comparativa por jurisdição

| Aspecto | EUA (ABYC/OEM) | Internacional (ISO) | Brasil (Marinha/ABNT) |
|---|---|---|---|
| Instalação motor | ABYC P-22, P-4 | ISO 16147, ISO 8665 | NORMAM (referencia) |
| Proteção DC | ABYC E-11, A-16 | ISO 10133 | NORMAM |
| Fluido trim | Quicksilver / Yamalube / Volvo Penta (OEM) | ISO 11158 / ATF OEM | NBR 11213 (referência) |
| Ignition protection | UL 1500, SAE J1171 | ISO 8846 | NORMAM |

## Glossário rápido

- **Trim** — ajuste fino de ângulo do propulsor dentro da faixa de navegação (0-20° típico).
- **Tilt** — levantamento maior fora da navegação (até 70-90°), para atracação/reboque.
- **PTT (Power Trim and Tilt)** — conjunto eletro-hidráulico integrado.
- **Motor de popa (outboard)** — motor removível instalado no espelho de popa; trim/tilt ajusta ângulo do conjunto completo.
- **Stern drive / inboard-outboard** — motor interno + rabeta externa; trim/tilt ajusta rabeta.
- **Rabeta** — caixa de transmissão externa em stern drive; inclui hélice, cone de saída e atuadores de trim.
- **Cilindro de trim** — cilindro hidráulico que move o conjunto; tipicamente dois em outboard, um ou dois em stern drive.
- **Bomba hidráulica de trim** — bomba de palheta ou engrenagem, pressão 100-200 bar.
- **Reservatório de fluido** — tipicamente 150-500 ml, integrado à bomba.
- **Válvula de retenção (check valve)** — retém pressão com motor desligado.
- **Válvula de alívio (relief valve)** — limita pressão máxima (típico 160-210 bar).
- **Parafuso de alívio manual** — permite mover conjunto em pane elétrica.
- **Relé reversor** — contator que alterna polaridade do motor para subir/descer.
- **Solenoide up/down** — em alguns sistemas, válvulas eletro-hidráulicas em vez de reversão de polaridade do motor.
- **Stall current** — corrente máxima com motor bloqueado (pode atingir 200 A em motores grandes).
- **Corrente de pico** — corrente de partida (40-120 A típico).
- **Fusível slow-blow** — fusível que tolera pico mas desarma em stall sustentado.
- **Breaker DC** — disjuntor rearmável; substituto preferido em sistemas modernos.
- **Escovas do motor** — contatos de grafite que conduzem corrente ao rotor.
- **Coletor (comutador)** — anel segmentado no rotor; desgasta com escovas.
- **Queda de tensão** — ABYC recomenda ≤ 3% em circuitos não-críticos, ≤ 10% em pico de stall.
- **Ponto de massa** — conexão ao bloco do motor; oxidação é falha comum.
- **Bus bar** — barra condutora que distribui positivo ou negativo.
- **ATF (Automatic Transmission Fluid)** — fluido para transmissão automática; uso em trim/tilt.
- **Dexron III / VI** — especificações GM de ATF (III obsoleta, VI atual).
- **Mercon V / LV** — Ford ATF (raro em trim).
- **Quicksilver Power Trim Fluid** — Mercury OEM.
- **Yamalube Power Trim Fluid** — Yamaha OEM.
- **Volvo Penta Power Trim Fluid** — Volvo Penta OEM.
- **NBR (Buna-N)** — elastômero de vedação; padrão em sistemas com fluido mineral e ATF.
- **Viton (FKM)** — elastômero de alta resistência térmica/química.
- **Sangria** — remoção de ar do circuito hidráulico.
- **Cavitação** — formação/colapso de bolhas de vapor; destrói bomba rapidamente.
- **Aeração** — ar dissolvido/arrastado no fluido; gera espuma e perda de resposta.
- **Emulsão** — mistura óleo + água; aparência leitosa, sinal crítico de problema.
- **Fim de curso (end stop)** — limite mecânico; sistema precisa de corte elétrico antes de atingir.
- **IP67** — grau de proteção; imersão até 1 m por 30 min (IEC 60529).
- **Ignition-protected** — componente certificado para não inflamar gases combustíveis.
- **Carenagem (cowling)** — capô do motor de popa; abriga relés e chicote.
- **Retenção hidráulica** — capacidade do sistema de manter posição com bomba desligada.
- **Haste do pistão** — parte cromada do cilindro; arranhão grave = vedação comprometida em pouco tempo.
- **Anodo do trim** — anodo sacrificial específico do conjunto de trim; proteção galvânica.

## Integração com outras notas

- [[Óleos Hidráulicos Marine — Guia Completo]]
- [[Relés e Relés de Estado Sólido]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Troubleshooting — Diagnóstico de Falhas Elétricas]]
- [[Plataforma de Popa Elétrica - Hidráulica]]
- [[Flap]]
- [[Estabilizador]]

## Perguntas que esta nota responde

- Como o sistema de trim/tilt realmente funciona?
- Onde separar falha elétrica de falha hidráulica?
- Como diagnosticar conjunto lento, travado ou que perde posição?
- Qual fluido usar em Mercury, Yamaha, Volvo Penta, Suzuki, Mercruiser, Honda Marine?
- Quando e como usar o alívio manual em pane?
- Quais são os erros de manutenção que destroem vedação ou bomba do trim?
