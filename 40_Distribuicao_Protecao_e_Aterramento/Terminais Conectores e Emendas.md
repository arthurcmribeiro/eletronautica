---
title: "Terminais Conectores e Emendas"
note_type: "technical-note"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "TERMINAIS, CONECTORES E EMENDAS 33a19734f7fb81518ee3f81d505d0439.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "66"
tier_fase_6: "A"
reviewed_on: "2026-04-21"
review_jurisdiction:
  - "Brasil"
  - "internacional"
review_level: "engineering-curated"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
normas_citadas:
  - "ABYC E-11 (AC and DC Electrical Systems on Boats) — §11.13 conexões"
  - "ABYC E-11 §11.13.1 — ring/spade terminals e connections"
  - "ABYC E-11 §11.13.1.1 — crimpagem, não torcimento"
  - "ABYC E-11 §11.13.1.9 — solda não permitida como único meio de conexão"
  - "ABYC E-11 §11.13.1.10 — solder/wire-nut proibido em aplicações principais"
  - "ABYC E-11 §11.14 — suporte mecânico e alívio de tração"
  - "UL 486A-486B (Wire Connectors)"
  - "UL 486C (Splicing Wire Connectors)"
  - "UL 486E (Equipment Wiring Terminals — AL-CU)"
  - "UL 310 (Electrical Quick-Connect Terminals)"
  - "UL 1426 (Electrical Cables for Boats)"
  - "MIL-T-7928 (Terminals, Lug; Crimp-Style)"
  - "MIL-DTL-22520 (Crimping Tools)"
  - "MIL-C-39029 (Contacts, Electrical Connector)"
  - "IEC 61238-1 (Compression and mechanical connectors for power cables)"
  - "IEC 60352-2 (Solderless connections — Crimped connections)"
  - "IEC 60352-6 (Solderless connections — Insulation displacement)"
  - "IEC 60529 (IP code — grau de proteção)"
  - "SAE J1127 / J1128 (Low Voltage Battery Cable / Primary Cable)"
  - "SAE AS-39029 (Contacts, Electrical — Aerospace crimp)"
  - "DIN 46234 / 46235 / 46237 (Terminais tubulares ring/spade)"
  - "DIN 46228 (Ponteiras/ferrules)"
  - "NFPA 70 (NEC) art. 110.14 — conexões elétricas"
  - "ABNT NBR 5410 §6.2.6 — conexões"
  - "ABNT NBR IEC 61238-1 — conectores de compressão"
  - "ABNT NBR 14039 §5.4 — MT conexões"
  - "ISO 10133:2012 — DC small craft"
  - "ISO 13297:2020 — AC small craft"
  - "NORMAM-05/DPC — Embarcações recreio"
family_clusters:
  - "ABYC-USCG (EUA náutico)"
  - "UL (EUA industrial)"
  - "IEC (internacional)"
  - "MIL-SAE (militar/aeroespacial/automotivo)"
  - "DIN (europeu industrial)"
  - "ABNT-NORMAM (Brasil)"
aliases:
  - "TERMINAIS, CONECTORES E EMENDAS"
  - "Terminais Conectores e Emendas"
  - "Ring / spade / ferrule"
  - "Crimpagem marine"
  - "Splice / emenda elétrica"
  - "Heat-shrink solder-seal"
seo_title: "Terminais conectores e emendas em embarcações: crimpagem, seleção e vedação"
seo_description: "Guia técnico sobre terminação elétrica marine: crimpagem ABYC, terminais ring/spade/ferrule, conectores destacáveis, emendas seladas, torque de borne, IP e diagnóstico."
seo_keywords:
  - "terminais elétricos marine"
  - "crimpagem ABYC"
  - "heat-shrink solder-seal"
  - "terminal náutico cobre estanhado"
geo_queries:
  - "Como fazer terminação elétrica profissional em embarcação?"
  - "Quais conectores e terminais usar em ambiente marinho?"
  - "Crimpagem ou solda em barco?"
related_notes:
  - "Cabeamento Náutico"
  - "Barramento DC - Bus Bar - Distribuição DC"
  - "Banco de Baterias"
  - "Inspeção de Cabos Terminais e Conexões"
  - "Fusíveis DC - Proteção Contra Sobrecorrente"
  - "Disjuntores (DC) e (AC)"
  - "Aterramento"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
---

# Terminais Conectores e Emendas

> [!abstract] Resumo técnico
> Terminais, conectores e emendas são a **interface eletromecânica** entre cabo, equipamento e circuito — e, estatisticamente, o **ponto único mais frequente** de falha elétrica em embarcação. Em bordo, grande parte das falhas não nasce no condutor, mas na terminação: crimpagem ruim (ferramenta errada, dimensão incompatível), material incompatível (cobre nu em ambiente salino, pares galvânicos), vedação insuficiente (heat-shrink sem adesivo, borne exposto), esforço mecânico mal resolvido (cabo balançando sem alívio de tração) e corrosão progressiva (meses ou anos de sal + umidade). ABYC E-11 §11.13 é explícito: **crimpagem é o método primário; solda como único meio não é permitida; wire-nut e emenda torcida proibidos em aplicações principais**. IEC 61238-1 e UL 486 normalizam conectores de compressão. Uma terminação correta é um **conjunto ferramenta + terminal + cabo + método + ambiente** — trocar um elemento sem ajustar os outros degrada o resultado.

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Crimpagem é o padrão, não solda** — ABYC E-11 §11.13.1.9 não permite solda como único meio de conexão; solda torna a emenda rígida, quebra em vibração, oxida e esconde defeito.
> 2. **Terminal + ferramenta + cabo formam um conjunto** — crimpar terminal Thomas & Betts com alicate chinês de R$20 resulta em crimpe decorativo; cada família (T&B, Ancor, Burndy, Hilti) tem ferramenta calibrada específica.
> 3. **Cobre estanhado marine, sempre** — cobre nu oxida em 3-12 meses em ar salino; terminal estanhado + cabo BC5W2 (UL 1426) + heat-shrink com adesivo.
> 4. **Ponteira (ferrule) para cabo em borne parafuso** — fio flexível solto em borne de disjuntor estraga os fios individuais; ponteira DIN 46228 resolve.
> 5. **Heat-shrink solder-seal** (Ancor, 3M Scotchlok) em emenda em chicote — derrete solda no meio + adesivo termofundido nas pontas; emenda selada IP67 em 20 s.
> 6. **Alívio de tração obrigatório** — cabo chegando no terminal não pode tensionar o crimpe; ABYC E-11 §11.14 exige suporte ≤ 450 mm do terminal + braçadeira ≤ 150 mm do conector.
> 7. **Torque de aperto calibrado** — cada borne tem torque especificado (0,5-8 N·m típico); aperto excessivo amassa filamento, aperto insuficiente gera ponto quente.
> 8. **Nunca compartilhar dois cabos em um mesmo olhal-borne** se o fabricante não permitir — empilhar olhais é comum mas só funciona com olhal duplo ou barramento de distribuição.
> 9. **Emenda é exceção, não estratégia** — minimizar emendas no projeto; onde for inevitável, documentar em diagrama com coordenada física e data.
> 10. **Validação: tração manual + inspeção visual + termografia em carga** — terminal que passa no "puxão firme", não mostra cabo saindo do crimpe, e não esquenta em carga nominal está bom.

> [!danger] Quando chamar um especialista
> Estes 9 cenários exigem eletricista naval ou rigger especializado:
> 1. **Terminal de cabo de bateria ≥ 2/0 AWG (50 mm²+)** — exige crimpadora hidráulica 12-16 t calibrada + terminal tubular pesado marine (Ancor, T&B, Burndy); errar cria pontos quentes que derretem em 300-500 A.
> 2. **Conexão alumínio-cobre (retrofit de embarcação antiga)** — par galvânico forte; exige Burndy KVSU, Penetrox e terminal bi-metal certificado AL-CU (UL 486E); mau bimetal corrói em meses.
> 3. **Conector MIL / aerospace quick-disconnect** (MIL-C-39029) em sistema de navegação crítica — crimpagem com MIL-DTL-22520 + gold-plated contacts + ensaio de pull strength documentado.
> 4. **Emenda em cabo submerso ou fundeado** (bomba de porão, sensor de nível externo) — vulcanizado 3M 2228 + fita + heat-shrink adhesive + encapsulante; qualquer falha = água no sistema elétrico.
> 5. **Retrofit de barco antigo com terminais torcidos ou solda antiga** — cada terminal precisa ser refeito com crimpagem apropriada; adesivo errado pode contaminar cabo BC5W2; trabalho de tempo completo em barco 40+ pés.
> 6. **Barco elétrico ou híbrido com banco 48V ≥ 400 Ah** — cabos 4/0 ou 300 MCM; terminal exige crimpador 20-30 t + calibração por lote; inspeção milimétrica após crimpe.
> 7. **Conexão de shore-power inlet high-amp** (50 A 240 V, 100 A 240 V) — terminal Furrion/Hubbell/Marinco + torque 6-10 N·m + vedação IP65+; deslize de aperto gera ponto quente em 1-3 meses.
> 8. **Sistema classificado (SOLAS, DNV, Lloyd's)** — registros de crimpe com número serial, fotos do antes/depois, ensaio de pull, rastreabilidade de lote; ensaio destrutivo por amostragem.
> 9. **Diagnóstico de queda de tensão anômala** (ΔV > 5% entre bateria e carga) sem causa óbvia — termografia + medição 4-fios ponto a ponto + abertura de terminais suspeitos para inspeção visual interna.

## O que são

Terminais, conectores e emendas são os elementos usados para:

- **terminar um condutor** em borne, barramento ou equipamento;
- **conectar e desconectar** circuitos (plugue-tomada, conector destacável);
- **unir condutores** de forma permanente ou semi-permanente (emenda/splice);
- **garantir continuidade elétrica e retenção mecânica** compatíveis com o ambiente marinho.

Do ponto de vista técnico, uma terminação boa precisa atender simultaneamente:

- **baixa resistência de contato** — tipicamente μΩ por junta; cada falha adiciona 10-100 mΩ e gera calor em carga;
- **retenção mecânica adequada** — suportar tensão de pull (ABYC E-11.13 sugere ≥ 20 lbf / 90 N em 18-14 AWG);
- **compatibilidade eletroquímica** — mesmo metal ou par galvânico controlado;
- **proteção ambiental coerente** — IP adequado ao local, vedação contra sal/umidade/vibração.

## Função na embarcação

- **viabilizar conexão confiável** de cabos e equipamentos;
- **reduzir risco de aquecimento localizado** (cada mΩ extra em 100 A = 10 W de calor);
- **permitir manutenção e substituição** quando aplicável (conector destacável vs. emenda permanente);
- **preservar integridade** do circuito em ambiente de vibração, umidade e sal.

## Fundamentos mínimos

### A terminação precisa ser pensada como conjunto

**Não existe "terminal bom" isoladamente**. O resultado depende da combinação entre:

- **cabo** — bitola, material, número de fios, isolação;
- **terminal ou conector** — tipo, material, acabamento, especificação;
- **ferramenta** — crimpadora calibrada para aquele terminal + cabo;
- **método de instalação** — sequência, torque, vedação, inspeção;
- **ambiente de serviço** — temperatura, vibração, umidade, exposição.

Trocar um desses elementos sem ajustar os outros degrada o resultado. Exemplo: cabo BC5W2 marine 16 mm² + terminal estanhado Ancor + crimpador manual de US$ 15 = crimpe decorativo (não há pressão suficiente para cold-weld). Mesmo cabo + mesmo terminal + crimpador hidráulico calibrado = conexão com resistência μΩ duradoura.

### Crimpagem correta costuma ser preferível a solda em bordo

Em muitas aplicações de bordo, **crimpagem bem executada e selada é a solução mais estável**:

| Técnica | Vantagens | Desvantagens | ABYC E-11 §11.13 |
| --- | --- | --- | --- |
| **Crimpagem** | resistência baixa μΩ, retenção mecânica, tolerante a vibração, rápida | exige ferramenta certa; sem inspeção interna | **método primário** (§11.13.1.1) |
| **Solda** | pode ser baixa resistência; visualmente clara | enrijece junta (quebra em vibração), oxida, esconde defeito | **não permitida como único meio** (§11.13.1.9) |
| **Crimpe + solda** | redundância, menos crítico em ferramenta | enrijece; solda mascara crimpe ruim; debate técnico | tolerada se bem executada |
| **Emenda torcida + fita** | fácil, sem ferramenta | oxidação imediata, zero tolerância a vibração | **proibida** em aplicações principais (§11.13.1.10) |
| **Wire-nut** | rápida em AC residencial | não aguenta vibração marine; oxida | **proibida** em aplicações principais |
| **Heat-shrink solder-seal** | emenda selada em chicote, rápida, IP67 | exige heat-gun calibrado; não substitui terminal | permitida como emenda de chicote |

### Emenda é exceção, não filosofia de projeto

O melhor chicote é aquele que **minimiza pontos intermediários de falha**. Emenda só deve existir quando houver **justificativa técnica e execução compatível**:

- **extensão de cabo existente** sem espaço para cabo novo;
- **conexão em meio de chicote** onde terminar nos dois lados é impraticável;
- **reparo em campo** de cabo danificado;
- **derivação** de ramal a partir de tronco existente.

Em todos os casos: **documentar em diagrama** (coordenada física, data, técnico), **selar adequadamente** ao ambiente, **aliviar tração** mecânica, e **deixar acessível** para inspeção futura.

### Corrente alta pede conexão séria

Em banco, motor de partida, inversor, bow-thruster e barramentos principais, **a qualidade da terminação impacta diretamente** queda de tensão, aquecimento e segurança:

- cabo 4/0 AWG (107 mm²) conduzindo 400 A sob 10 mΩ extra no terminal = **4 V caídos** + **1.600 W de calor** → terminal derrete em minutos;
- mesmo cabo com conexão correta (μΩ) = dezenas de mV caídos + dezenas de W → zero problema.

## Tipos mais comuns

### Terminais de compressão (não-destacáveis)

| Tipo | Aplicação | Padrão |
| --- | --- | --- |
| **Olhal (ring)** | borne parafusado (barramento, disjuntor, chave) | DIN 46234, MIL-T-7928 |
| **Forquilha (spade/fork)** | borne acessível, troca rápida | DIN 46237 |
| **Ponteira (ferrule) single** | cabo flexível em borne de disjuntor DIN | DIN 46228-1, -4 |
| **Ponteira duplo (twin-ferrule)** | dois fios em mesmo borne | DIN 46228 |
| **Terminal tubular pesado** | cabos ≥ 25 mm², alta corrente | DIN 46235 |
| **Quick-connect Faston (AMP)** | conexão destacável baixa corrente | UL 310 |
| **Pin / bullet** | emenda destacável automotivo | SAE J928 |

**Cores AMP/PIDG padrão** (ISO 7591 / DIN 46234):
- **vermelho** — 0,5-1,5 mm² (AWG 22-16);
- **azul** — 1,5-2,5 mm² (AWG 16-14);
- **amarelo** — 4-6 mm² (AWG 12-10).

### Conectores destacáveis

| Família | Aplicação | Padrão |
| --- | --- | --- |
| **Multipino Deutsch DT / DTM / DTP** | chicote automotivo e marine | IP67-IP69K |
| **Anderson Powerpole / SB** | conexão de potência destacável 15-350 A | |
| **MIL-C-5015 / 38999** | aviação/militar, instrumentação crítica | |
| **Phoenix Contact COMBICON** | conector pluggable painel DIN | IEC 61984 |
| **Wago 221 / 222** | conector de chicote sem ferramenta | |
| **NMEA 2000 Micro / Mini** | rede de dados náutica | ISO 11898 |
| **Shore-power (Hubbell, Marinco, Furrion)** | entrada AC do cais | UL 817 |
| **SAE trailer** (7-pin / 4-pin) | reboques, fora-de-borda leve | SAE J560 |

### Emendas

| Tipo | Aplicação | Vedação |
| --- | --- | --- |
| **Luva de compressão (butt splice)** | emenda linear pela crimpagem | heat-shrink adesivo |
| **Heat-shrink solder-seal** (Ancor, 3M) | emenda rápida com solda integrada | adesivo integrado, IP67 |
| **Wago 221** (conector de emenda) | emenda rápida sem ferramenta | requer caixa IP |
| **Conector de derivação (tap)** | derivar ramal sem cortar tronco | heat-shrink + adesivo |
| **Emenda selada por vulcanização** | cabo submerso/underwater | fita 3M 2228 + cola + encapsulante |
| **Emenda em caixa estanque** | junção múltipla | caixa IP66 + prensa-cabo |

## Projeto e instalação

### O que precisa ser definido

1. **tipo de cabo e seção** — BC5W2 marine classe 5, seção coerente com corrente;
2. **corrente e esforço mecânico** esperados — nominal + inrush + tração;
3. **ambiente de instalação** — IP necessário, temperatura, vibração;
4. **necessidade de desconexão futura** — se sim, conector destacável; se não, terminal permanente;
5. **método de vedação e alívio de tração** — heat-shrink adesivo, caixa, braçadeira;
6. **ferramenta correta** para execução — calibrada, com matriz específica.

### Diretrizes práticas

- **usar terminal compatível** com o cabo (bitola, flex vs. rígido) e com o borne real (tamanho do parafuso, geometria);
- **evitar mistura desnecessária** de metais e acabamentos (aço inox em circuito DC, cobre nu em ar salino);
- **prever alívio de tração** e proteção mecânica (ABYC §11.14: suporte ≤ 450 mm do terminal);
- **selar adequadamente** quando o ambiente exigir (heat-shrink adesivo 3:1 com Hotmelt SB350, 3M EPS-400, Raychem SCL);
- **validar visualmente e mecanicamente** cada terminação crítica (pull test + inspeção);
- **usar aresta limpa** no corte do cabo (ferramenta de corte, não alicate mal ajustado);
- **respeitar comprimento de desencapamento** (lstrip) indicado pelo fabricante do terminal — 3-12 mm típico;
- **aplicar inibidor de oxidação** (Penetrox A-13, Noalox) em conexão AL-CU ou em ambiente especialmente salino.

### Passo a passo correto de crimpagem de olhal em cabo marine

```
1. Cortar cabo com alicate de corte (não alicate comum) — aresta reta.
2. Desencapar comprimento exato (Lstrip = comprimento do canudo do terminal + 1-2 mm).
3. Retorcer levemente os filamentos (se multifilar) — manter integridade.
4. Inserir no canudo do terminal até que fique visível na janela de inspeção.
5. Posicionar crimpador na matriz correta (cor ou tamanho).
6. Acionar crimpe até fim de curso (ratchet com trava).
7. Inspecionar visualmente — não deve haver filamento solto fora, terminal deve abraçar canudo.
8. Teste de pull — puxar com força moderada (20-40 lbf / 90-180 N); cabo não pode sair.
9. Aplicar heat-shrink adesivo 3:1 cobrindo canudo + 10 mm do isolamento; aquecer uniformemente.
10. Aguardar esfriar + inspecionar vedação (heat-shrink deve estar liso, sem bolhas).
```

### Ferramentas de crimpagem por calibre de cabo

| Bitola (AWG / mm²) | Crimpadora recomendada | Referência típica |
| --- | --- | --- |
| 22-18 AWG / 0,5-1,0 mm² | crimpadora ratchet PIDG | Paladin 1300, Knipex 97 53 04 |
| 16-14 AWG / 1,5-2,5 mm² | crimpadora ratchet AMP | Klein 1005, Paladin 1345 |
| 12-10 AWG / 4-6 mm² | crimpadora hidráulica/ratchet pesada | Paladin 1388, AMP 59250 |
| 8-6 AWG / 10-16 mm² | ratchet pesada ou hidráulica 4-6 t | Anvil, Ancor 702005 |
| 4-2 AWG / 25-35 mm² | hidráulica 6-10 t | FEC Crimper, T&B TBM-8 |
| 2/0-4/0 AWG / 50-120 mm² | hidráulica 12-16 t | Burndy Y35, Greenlee 1981 |
| 300-500 MCM / 150-240 mm² | hidráulica 20-30 t + matriz | Burndy Y46, Greenlee PS600 |

**Ponteiras (ferrules)** exigem crimpadora quadrangular ou hexagonal:
- cabo 0,5-16 mm²: Knipex 97 43 200, Phoenix Contact CRIMPFOX, Weidmüller PZ;
- cabo 10-50 mm²: Klauke K1050;
- cabo 25-150 mm²: Cembre ND-12, Haupa 216900.

### Torque de aperto por borne

| Tamanho do parafuso | Torque típico (N·m) | Aplicação |
| --- | --- | --- |
| M3 / #6 | 0,5-0,8 | borne pequeno DIN |
| M4 / #8 | 1,0-2,0 | borne disjuntor 6-32 A |
| M5 / #10 | 2,5-4,0 | borne disjuntor 40-63 A |
| M6 / 1/4" | 4,0-7,0 | barramento pequeno |
| M8 / 5/16" | 6,0-12 | barramento médio |
| M10 / 3/8" | 10-20 | barramento grande |
| M12 / 1/2" | 20-40 | polo de bateria, shunt pesado |

Usar **torquímetro calibrado** — aperto excessivo amassa filamento de cobre (reduz seção efetiva, gera ponto quente); aperto insuficiente gera resistência crescente por vibração.

## Onde costuma dar problema

| Problema | Causa provável | Mitigação |
| --- | --- | --- |
| **aquecimento localizado** | contato ruim, terminal inadequado, aperto deficiente | termografia + re-crimpe |
| **falha intermitente** | crimpagem ruim, vibração, cabo mal suportado | inspeção + braçadeira |
| **corrosão acelerada** | vedação insuficiente, materiais incompatíveis | heat-shrink adesivo, cobre estanhado |
| **quebra perto do terminal** | rigidez excessiva, esforço mecânico mal resolvido | alívio de tração, conduíte flexível |
| **diagnóstico confuso** | emenda escondida, conector sem identificação | documentar, etiquetar |
| **crimpe decorativo** | ferramenta errada (alicate comum em vez de crimpador ratchet) | crimpador calibrado |
| **solda em ambiente de vibração** | tentativa de "melhorar" crimpe | refazer com crimpe apropriado |
| **par galvânico** | terminal de latão em cabo de cobre ou AL em Cu | terminal estanhado + Penetrox |
| **cabo rígido em borne flexível** | cabo THHN classe 3 em conector PIDG de flex | ferrule (ponteira) |
| **dois olhais no mesmo borne** | tentativa de compartilhar parafuso | barramento ou olhal duplo |

## Diagnóstico prático

1. **Inspecionar visualmente** corrosão, folga, deformação e selagem — luz + espelho dental em pontos ocultos;
2. **Medir queda de tensão na conexão sob carga** — método 4-fios (Kelvin) com clamp + voltímetro µV;
3. **Verificar aquecimento anormal** — termografia ou toque com dorso da mão (nunca palma em corrente alta);
4. **Testar retenção mecânica** e alívio de tração — puxão firme sem dano ao crimpe;
5. **Confirmar** se o terminal usado corresponde ao cabo e ao borne — caliper + datasheet.

**Ferramentas úteis**:
- **termocâmera** (FLIR C5, Hikmicro B20) — hot spot em carga nominal;
- **multímetro 4-fios (Kelvin)** (Fluke 88V, Keithley 2450) — μΩ em conexão;
- **torquímetro de bancada** (Wera 7440, 7441) — verificar torque após ensaio;
- **lente ampliadora** 10-20× + lanterna LED — inspeção de crimpe;
- **alicate de pull test** (Paladin PT-200) — medir 10-200 lbf com calibração.

## Boas práticas profissionais

- **usar ferramentas e terminais adequados** à aplicação — não improvisar com alicate comum ou solda;
- **tratar a terminação como ponto crítico** do circuito, especialmente em alta corrente;
- **preferir conexões seladas** (heat-shrink adesivo, caixa IP, boot) em ambientes agressivos;
- **evitar emenda escondida** sem registro em diagrama unifilar;
- **revisar terminais de banco, barramento e alimentação crítica** periodicamente (anual em barco recreio, semestral em comercial);
- **manter coerência** entre a terminação, o esforço mecânico e a exposição ambiental;
- **etiquetar cabo** com heat-shrink printed (Brady, Dymo Rhino) em cada extremidade — sobrevive 15+ anos;
- **manter kit de peças de reposição** (terminais, heat-shrink, conectores) a bordo em barco de cruzeiro longo;
- **treinamento periódico** da tripulação/técnico — vídeo + simulação + supervisão.

## Erros que fragilizam a base técnica

- **compensar crimpagem ruim com solda improvisada** — piora mecanicamente;
- **usar terminal que "quase serve"** — resistência maior, risco de solto;
- **esconder emenda em local inacessível** e sem documentação — herança para o próximo proprietário;
- **ignorar alívio de tração** em cabo sujeito a vibração — quebra a 15-30 mm do terminal;
- **focar no brilho do terminal** e esquecer a qualidade elétrica do contato;
- **empilhar 3-4 olhais num mesmo borne** sem barramento — oxidação entre olhais e aquecimento;
- **alicate comum para crimpar** — não há cold-weld; crimpe "decorativo" que solta em 6-18 meses;
- **heat-shrink sem adesivo** (heat-shrink simples) — não veda, permite infiltração de sal;
- **reutilizar terminal já crimpado** — metal deformado, resistência imprevisível;
- **conector de chicote automotivo (Faston)** em aplicação marine externa sem IP — oxida rápido.

## Relação com outros sistemas

- **[[Cabeamento Náutico]]** — base do conjunto cabo-terminação.
- **[[Barramento DC - Bus Bar - Distribuição DC]]** — pontos críticos de conexão.
- **[[Banco de Baterias]]** — terminais de alta corrente e baixa tolerância a erro.
- **[[Inspeção de Cabos Terminais e Conexões]]** — manutenção e auditoria.
- **[[Fusíveis DC — Proteção Contra Sobrecorrente]]** e **[[Disjuntores (DC) e (AC)]]** — consequências de mau contato na proteção.
- **[[Aterramento]]** — terminais do PE exigem mesma disciplina.
- **[[Quadro Elétrico e Painel de Distribuição AC-DC]]** — onde a maior parte dos terminais convive.
- **[[Chaves Gerais (DC)]]**, **[[Chaves Seletoras (AC)]]**, **[[Relés e Relés de Estado Sólido]]**, **[[Contatores (AC)]]** — bornes de saída exigem terminais adequados.

## Normas e referências

### Por família e jurisdição

| Família | Norma | Escopo |
| --- | --- | --- |
| **ABYC (EUA)** | E-11 §11.13 | conexões marine |
| ABYC | E-11 §11.13.1.1 | crimpagem (não torcimento) |
| ABYC | E-11 §11.13.1.9 | solda não-único-meio |
| ABYC | E-11 §11.13.1.10 | wire-nut proibido |
| ABYC | E-11 §11.14 | alívio de tração |
| **UL (EUA)** | UL 486A-486B | wire connectors |
| UL | UL 486C | splicing |
| UL | UL 486E | AL-CU terminals |
| UL | UL 310 | quick-connect |
| UL | UL 1426 | cables for boats |
| **MIL (EUA)** | MIL-T-7928 | terminals lug |
| MIL | MIL-DTL-22520 | crimping tools |
| MIL | MIL-C-39029 | contacts |
| **IEC (internacional)** | IEC 61238-1 | compression connectors |
| IEC | IEC 60352-2 | crimped connections |
| IEC | IEC 60352-6 | insulation displacement |
| IEC | IEC 60529 | IP code |
| **ISO (internacional)** | ISO 10133 / 13297 | small craft DC / AC |
| **SAE (EUA)** | SAE J1127 / J1128 | battery / primary cable |
| SAE | SAE AS-39029 | aerospace crimp |
| **DIN (Europa)** | DIN 46234/46235/46237 | olhais / tubulares / forquilhas |
| DIN | DIN 46228 | ponteiras |
| **NFPA (EUA)** | NFPA 70 art. 110.14 | conexões elétricas |
| **ABNT (Brasil)** | NBR 5410 §6.2.6 | conexões |
| ABNT | NBR IEC 61238-1 | conectores compressão |
| ABNT | NBR 14039 §5.4 | MT conexões |
| **NORMAM (Brasil)** | NORMAM-05 | recreio |

### Comparação prática entre jurisdições

- **EUA (ABYC + UL)**: ABYC E-11 §11.13 é a referência de bordo — crimpagem como método primário, solda proibida como único meio, wire-nut e emenda torcida proibidas em aplicações principais; UL 486 detalha terminais; MIL-T-7928 padroniza terminais militares.
- **Internacional (IEC)**: IEC 61238-1 e IEC 60352-2 estabelecem ensaio de crimpe (pull-out, mV drop, resistência); IEC 60529 para IP; ISO 10133/13297 para náutica.
- **Europa (DIN + CENELEC)**: DIN 46234/46235/46237 padronizam terminais em mm² e colorem cores (PIDG/AMP); CE/RCD exige conformidade.
- **Brasil (ABNT + NORMAM)**: NBR 5410 §6.2.6 cobre conexões em BT; NBR IEC 61238-1 (tradução direta); mercado usa extensivamente terminais DIN-padrão + AMP (Tyco/TE Connectivity); NORMAM-05 remete a ABYC/ISO em náutica.
- **Militar/aeroespacial (MIL-SAE)**: MIL-T-7928 + MIL-DTL-22520 + SAE AS-39029 exigem ferramentas calibradas com número serial, rastreabilidade de lote, ensaio destrutivo por amostragem.

## Glossário rápido

1. **Alívio de tração (strain relief)** — suporte mecânico do cabo próximo ao terminal.
2. **Amalgamação** — junção metálica por cold-weld na crimpagem.
3. **AMP / PIDG** — famílias Tyco/TE Connectivity de terminais com isolamento.
4. **Anderson Powerpole** — conector destacável modular de potência.
5. **Barril (barrel)** — parte do terminal que abraça o cabo.
6. **Boot** — luva flexível de proteção de terminal.
7. **Braçadeira (cable tie)** — amarração do chicote ao suporte.
8. **Butt splice** — emenda linear em luva.
9. **BC5W2** — cabo marine flexível estanhado UL 1426.
10. **CAT cable** — categoria de cabo de dados (CAT 5e, 6, 7).
11. **Classe de flexibilidade (IEC 60228)** — 1 (rígido) a 6 (muito flexível).
12. **Cold weld** — união metálica por pressão (sem calor).
13. **Compound inibidor** — pasta antioxidante (Penetrox, Noalox).
14. **Conector pluggable** — destacável/removível.
15. **Contato banhado** — camada de outra liga (Au, Ni, Sn) sobre base.
16. **Crimpagem** — compressão mecânica do terminal no cabo.
17. **Crimpador ratchet** — ferramenta com trava de fim de curso.
18. **DeoxIT** — produto de limpeza e proteção de contato (Caig).
19. **Deutsch DT / DTM / DTP** — conectores automotivos IP67.
20. **Die (matriz)** — inserto da crimpadora para tamanho específico.
21. **Dielétrico** — isolamento elétrico.
22. **Emenda (splice)** — união de dois cabos em meio de chicote.
23. **Epoxi encapsulante** — resina para vedação definitiva.
24. **Faston (quick-connect)** — terminal push-on 6,3 mm.
25. **Ferrule (ponteira)** — tubo que termina cabo flexível para borne.
26. **Gage (calibre)** — seção do cabo (AWG ou mm²).
27. **Gold-plated contact** — contato banhado a ouro (baixa corrente, baixa resistência).
28. **Heat-gun** — soprador térmico (350-600 °C).
29. **Heat-shrink** — tubo termorretrátil.
30. **Heat-shrink adesivo (dual-wall)** — com adesivo termofundido interno.
31. **Hot-melt** — adesivo fusível que veda sob calor.
32. **IP code (IEC 60529)** — grau de proteção (IP20 a IP69K).
33. **Isolation displacement (IDC)** — conector que perfura isolação (Scotchlok).
34. **Knife-edge** — corte afiado do desencapamento (padrão ABYC).
35. **Lug (olhal)** — terminal com furo para parafuso.
36. **Marinco / Hubbell / Furrion** — fabricantes de shore-power inlets.
37. **MIL-spec** — padrão militar.
38. **Par galvânico** — combinação de metais com potencial diferente.
39. **Penetrox** — compound inibidor para AL-CU.
40. **PIDG (Pre-Insulated Diamond Grip)** — terminal AMP pré-isolado.
41. **Polaridade marcada** — identificação + ou − no conector.
42. **Pull test** — ensaio de tração do crimpe.
43. **Quick-disconnect (QD)** — conector rápido destacável.
44. **Ratchet** — mecanismo de trava progressiva.
45. **Solder-seal** — heat-shrink com solda e adesivo integrados.
46. **Spade / fork** — terminal em garfo.
47. **Terminal tubular pesado** — lug de cabo grosso (DIN 46235).
48. **Tin-plated** — banhado a estanho (marine standard).
49. **Vulcanizado** — fita que se auto-solda sob pressão (3M 2228).
50. **Wire-nut** — conector em espiral para AC residencial (proibido marine).

## FAQ

**Todo terminal precisa ser soldado depois de crimpar?**

**Não**. Isso **não é regra de boa prática** e pode até prejudicar o comportamento mecânico em certas aplicações. ABYC E-11 §11.13.1.9 é explícito: solda não é permitida como único meio de conexão; §11.13.1.10 proíbe wire-nut em aplicações principais. Crimpagem bem executada com ferramenta calibrada + heat-shrink adesivo é o padrão profissional em embarcação. Solda adicional sobre crimpe bom é debatida — alguns profissionais usam em baixa vibração (painel interno seco), muitos evitam por enrijecer a junta e mascarar defeito interno.

**Posso reutilizar terminal ou conector já deformado?**

Em geral, **não é a abordagem profissional**. A confiabilidade da conexão cai e o defeito volta mascarado. O metal do terminal sofre deformação plástica na crimpagem inicial — forma geometria específica que não é recuperável. Reutilizar resulta em: (a) aperto insuficiente (resistência elétrica maior); (b) risco de desalojar; (c) possível crack interno invisível. Terminais são baratos; custo de um retorno ao estaleiro por terminal falho é ordens de magnitude maior.

**Toda emenda é ruim?**

**Não**. Emenda bem especificada e bem executada pode ser aceitável, mas não deve virar estratégia de projeto por conveniência. Emenda aceitável: heat-shrink solder-seal profissional em chicote protegido, documentada no diagrama, acessível para inspeção. Emenda ruim: fita isolante em chicote escondido atrás de forro, sem coordenação documental. Regra prática: cada emenda adicionada = mais um ponto de falha; projeto maduro minimiza emendas no desenho inicial.

**Por que usar cobre estanhado (tin-plated) em barco?**

Cobre nu exposto a ar salino oxida formando **óxido de cobre (preto esverdeado)** — isolante, aumenta resistência, acelera corrosão do restante do cabo/terminal. Cobre estanhado tem camada de estanho (5-15 µm) que age como sacrificial e corrosão-resistente. Em barco: cabo BC5W2 (UL 1426) com filamentos estanhados + terminal estanhado + heat-shrink adesivo dá 15-25 anos de vida útil; mesmo sistema em cobre nu dura 3-8 anos.

**Qual a diferença entre heat-shrink simples e adesivo (dual-wall)?**

**Heat-shrink simples** (adesive-free) é polyolefin que encolhe ao aquecer — veda poeira e impede contato acidental, mas **não impede água**. **Heat-shrink adesivo (dual-wall)** tem camada interna de adesivo termofundido (hot-melt) que derrete no aquecimento e se molda ao cabo + terminal — gera vedação IP67 contra água, sal e vapor. Em barco, **apenas heat-shrink adesivo** em conexões externas ou úmidas; simples em chicote interno seco.

**Quando usar ponteira (ferrule) em vez de crimpar direto o cabo no borne?**

Sempre que o cabo for **flexível classe 5 ou 6 (multifilar fino)** e o borne for do tipo **parafuso de disjuntor/contator DIN**. O parafuso do borne esmaga e "pica" filamentos individuais do cabo flexível solto — reduz seção efetiva, pontos quentes, risco de quebra. Ponteira DIN 46228 isola os filamentos em um tubo metálico, oferece superfície sólida ao parafuso e distribui a pressão. Regra: cabo flexível + borne parafuso = ponteira crimpada; cabo rígido + borne parafuso = direto; cabo qualquer + borne mola DIN = direto (mola distribui).

**Posso empilhar 3 olhais num mesmo parafuso de barramento?**

**Evitar**. Empilhar olhais gera: (a) torque desigual entre as lâminas; (b) oxidação entre contatos; (c) dificuldade de remoção de um sem soltar os outros. Soluções corretas: (1) usar **barramento de distribuição** (Blue Sea bus bar) em vez de parafuso único; (2) usar **olhal duplo** (ring + extension tab) Ancor/T&B; (3) **crimpar vários cabos em um mesmo terminal** (só quando o terminal permitir essa seção total — verificar datasheet). Para alimentação crítica (polo de bateria, barramento principal), sempre barramento dedicado, não empilhamento.

**Qual a melhor emenda para cabo submerso (bomba de porão externa)?**

Três camadas em sequência: (1) **crimpagem** com butt splice estanhado Ancor ou equivalente; (2) **vulcanizado** 3M Scotch 2228 ou 130C em 2-3 camadas (estica ~50% ao aplicar; se auto-solda em 24 h); (3) **heat-shrink adesivo** de tamanho correto sobre vulcanizado + 20 mm de cada lado. Para aplicação crítica (sensor submerso permanente), adicionar encapsulante de epoxi (3M Scotchcast 40) em caixa pequena. Evitar emenda em cabo que fica continuamente submerso — preferir cabo contínuo até caixa estanque IP68.

## Integração com outras notas

- [[Cabeamento Náutico]]
- [[Barramento DC - Bus Bar - Distribuição DC]]
- [[Banco de Baterias]]
- [[Inspeção de Cabos Terminais e Conexões]]
- [[Fusíveis DC — Proteção Contra Sobrecorrente]]
- [[Disjuntores (DC) e (AC)]]
- [[Aterramento]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]
- [[Chaves Gerais (DC)]]
- [[Relés e Relés de Estado Sólido]]

## Perguntas que esta nota responde

- Como fazer terminações elétricas confiáveis em embarcações?
- Quais falhas nascem em terminais, conectores e emendas?
- Quando uma emenda ou conexão deixa de ser aceitável em bordo?
- Por que usar cobre estanhado (tin-plated) em barco?
- Quando usar ponteira (ferrule) em vez de crimpar direto?
- Qual a melhor emenda para cabo submerso?
- Posso empilhar olhais no mesmo parafuso?
