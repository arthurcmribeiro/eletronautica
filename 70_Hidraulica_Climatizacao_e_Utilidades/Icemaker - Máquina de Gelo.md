---
title: "Icemaker - Máquina de Gelo"
note_type: "technical-note"
domain: "70_Hidraulica_Climatizacao_e_Utilidades"
source_file: "ICEMAKER MÁQUINA DE GELO 33a19734f7fb81df9a98d1565b2937ad.md"
status: "fase-5-reescrita-premium"
fase_6_reescrita: "50"
tier_fase_6: "A"
reviewed_on: "2026-04-21"
review_jurisdiction:
  - "Brasil"
  - "internacional"
source_urls:
  - "https://www.marinha.mil.br/dpc/normas-autoridade-maritima-brasileira"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
  - "https://www.epa.gov/snap"
  - "https://www.epa.gov/section608"
  - "https://www.fda.gov/food/retail-food-protection"
review_level: "engineering-curated"
normas_citadas:
  - "ABYC A-16 - Electrical Safety (low-voltage DC circuits)"
  - "ABYC E-11 - AC and DC Electrical Systems on Boats"
  - "ABYC A-31 - Battery Chargers and Inverters"
  - "ABYC H-23 - Installation of Potable Water Systems"
  - "ABYC H-28 - Greywater Systems (drainage)"
  - "ISO 10133:2017 - Small craft - Extra-low-voltage DC installations"
  - "ISO 13297:2020 - Small craft - AC installations"
  - "ISO 15748:2002 - Ships and marine technology - Potable water supply on ships and marine structures"
  - "ISO 8846:1990 - Small craft - Electrical devices - Protection against ignition of flammable gases"
  - "ISO 9094:2015 - Small craft - Fire protection"
  - "ISO 17899:2018 - Ships and marine technology - Marine potable water purification"
  - "IEC 60335-2-24:2020 - Household refrigerating appliances"
  - "IEC 60335-2-89:2019 - Commercial refrigerating appliances"
  - "UL 563 - Icemaking Equipment"
  - "UL 471 - Commercial Refrigerators and Freezers"
  - "UL 60335-2-24 - Safety of Household Refrigerating Appliances"
  - "NSF/ANSI 12:2023 - Automatic Ice Making Equipment"
  - "NSF/ANSI 18:2023 - Manual Food and Beverage Dispensing Equipment"
  - "NSF/ANSI 61:2022 - Drinking Water System Components - Health Effects"
  - "NSF/ANSI 372:2020 - Drinking Water System Components - Lead Content"
  - "FDA Food Code 2022 - Retail and Food Service Operations"
  - "EN 378:2016 - Refrigerating systems and heat pumps - Safety and environmental requirements"
  - "AHRI 810:2016 - Performance Rating of Automatic Commercial Ice-Makers"
  - "Protocolo de Montreal (1987) - Substances that Deplete the Ozone Layer"
  - "Emenda de Kigali (2016) - Montreal Protocol HFC phase-down"
  - "EPA SNAP (Significant New Alternatives Policy) - 40 CFR Part 82 Subpart G"
  - "EPA Section 608 - Stratospheric Ozone Protection (40 CFR Part 82 Subpart F)"
  - "AIM Act 2020 (American Innovation and Manufacturing Act) - HFC phase-down"
  - "EU F-gas Regulation 517/2014 - Fluorinated greenhouse gases"
  - "CONAMA 267/2000 - Proibição de substâncias que destroem a camada de ozônio"
  - "CONAMA 340/2003 - Cilindros para envasamento de gases refrigerantes"
  - "IN IBAMA 207/2008 - Cadastro de importadores de gases refrigerantes"
  - "Portaria MCT 86/2013 - Certificação de técnicos em refrigeração"
  - "ISO 817:2014 - Refrigerants - Designation and safety classification"
  - "ASHRAE 34-2022 - Designation and Safety Classification of Refrigerants"
  - "ASHRAE 15-2022 - Safety Standard for Refrigeration Systems"
  - "NBR 13971:2014 - Sistemas de refrigeração - Manutenção programada"
  - "NBR 15960:2019 - Gases refrigerantes - Classificação"
  - "NBR 5410:2004 - Instalações elétricas de baixa tensão"
  - "NBR 15975:2017 - Requisitos para elaboração de projeto executivo de instalações de AVAC"
  - "Portaria MS 2.914/2011 - Procedimentos de controle e vigilância da qualidade da água para consumo humano"
  - "NORMAM-01/DPC - Embarcações empregadas na navegação em mar aberto"
  - "NORMAM-03/DPC - Embarcações empregadas na navegação interior"
aliases:
  - "ICEMAKER MÁQUINA DE GELO"
  - "Ice maker"
  - "Máquina de gelo marítima"
  - "Commercial ice maker marine"
seo_title: "Icemaker em embarcações: água, energia, drenagem, refrigerante e sanidade"
seo_description: "Guia técnico sobre icemaker em embarcações: carga AC/DC, qualidade da água, drenagem, ventilação, produção real, limpeza sanitária, refrigerantes regulados (Montreal/Kigali/EPA/CONAMA) e integração com galley."
seo_keywords:
  - "icemaker barco"
  - "máquina de gelo embarcação"
  - "ice maker marine"
  - "carga ac galley barco"
  - "refrigerante icemaker R-134a R-290"
  - "NSF 12 ice equipment"
geo_queries:
  - "Vale a pena instalar icemaker na embarcação?"
  - "Por que a máquina de gelo do barco produz pouco ou dá problema sanitário?"
  - "Qual refrigerante usa o icemaker marine e como é regulado?"
related_notes:
  - "Ar-Condicionado Marine — Sistema Completo"
  - "Ar-Condicionado Marine 12V DC"
  - "Geladeira - Freezer de Bordo"
  - "Bomba de Água Pressurizada"
  - "Caixa de Água Cinza"
  - "Gerador (AC)"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Troubleshooting — Diagnóstico de Falhas Elétricas"
---

# Icemaker - Máquina de Gelo

> [!abstract] Resumo técnico
> O `icemaker` é um consumidor utilitário que combina refrigeração, água pressurizada, drenagem e exigência sanitária. Embarcações que o instalam sem pensar em energia, água de alimentação, ventilação e limpeza costumam ganhar um equipamento caro e pouco confiável. Refrigerantes são regulados (Montreal/Kigali/EPA/CONAMA); descarte e recarga exigem técnico certificado. Sanidade é ponto subestimado — gelo é alimento, sujeito à Food Code 2022 (EUA) e Portaria MS 2.914/2011 (Brasil).

> [!tip] TL;DR — Regra de decisão em 30 segundos
> 1. **Icemaker é carga AC pesada, não DC (geralmente)** — 400-1500 W em regime, 2000-3500 W em partida; tratar como circuito dedicado de gerador ou shore power.
> 2. **Não existe "icemaker DC pequeno" confiável** — algumas linhas Isotherm/Vitrifrigo 12V produzem 3-6 kg/dia mas são exceção; produção/consumo razoável é AC.
> 3. **Produção catalogada é em condição ideal (21°C ambiente, 10°C água alimentação)** — barco tropical pode produzir 40-60% do catálogo.
> 4. **Qualidade da água importa mais que o equipamento** — água dura entope, água salobra danifica, água clorada altera sabor; pré-filtro é mandatório.
> 5. **Dreno é parte do projeto, não detalhe** — água de degelo + purga contínua precisa escoar sem sifonagem, sem retorno e preferencialmente sem conexão com esgoto (risco sanitário).
> 6. **Refrigerantes modernos: R-134a (saindo), R-290 (propano, A3 inflamável), R-404A (comercial, em phase-down)** — recarga/descarte só com técnico certificado EPA 608 ou MCT 86/2013.
> 7. **Gelo é alimento, sujeito a regulação sanitária** — NSF/ANSI 12/18/61 nos EUA, FDA Food Code 2022, Portaria MS 2.914/2011 no Brasil; biofilme e contaminação são riscos reais.
> 8. **Limpeza sanitária a cada 3-6 meses é mandatória em charter** — desmontar bin, limpar com solução NSF-aprovada, desinfetar, enxaguar com água potável.
> 9. **Ventilação do condensador é igual à geladeira** — nicho fechado sem fluxo de ar reduz produção em 50% e mata compressor.

> [!danger] Quando chamar um especialista (9 cenários)
> 1. **Gelo com sabor, cor ou odor estranho** — contaminação sanitária; parar consumo, investigar linha de água, filtro, bin; pode haver biofilme ou fonte externa.
> 2. **Cheiro de gás (especialmente doce/adocicado)** — vazamento de refrigerante R-290 (propano) em icemaker moderno; HC é inflamável A3, ventilar e parar sistema.
> 3. **Água acumulada no fundo do barco / sob o icemaker** — dreno obstruído ou descolado; risco elétrico, biológico e estrutural (se úmido prolongado em madeira/compensado).
> 4. **Compressor não desliga / produção caindo gradualmente** — refrigerante baixo, condensador sujo ou termostato ruim; compressor queima se ignorado.
> 5. **Gelo saindo mole/derretendo rapidamente** — ciclo de colheita (harvest) degradado; pode ser válvula solenoide com falha ou aquecedor de colheita queimado.
> 6. **Icemaker recebendo água de tanque de popa não tratada** — risco sanitário grave; gelo entra em contato direto com consumo humano; exige filtragem/UV.
> 7. **Descarte de icemaker antigo** — refrigerante DEVE ser recuperado antes do descarte (CONAMA 267/EPA 608); entregar a empresa certificada.
> 8. **Produção caindo após troca de filtro** — filtro errado (não-potável ou com retenção excessiva de pressão); gelo pode não formar ou formar irregularmente.
> 9. **Perícia sanitária pós-incidente (intoxicação alimentar em charter)** — não operar, preservar bin e amostras; NSF/ANSI 12 e Food Code aplicam-se à investigação.

## O que é

É o equipamento que produz gelo automaticamente a bordo a partir de água de alimentação e ciclo frigorífico próprio.

Pode fazer sentido para:

- uso intensivo de lazer (festa, drinks);
- charter (convidados esperam gelo disponível);
- pesca esportiva ou profissional (dependendo do tipo de gelo: clear cube, nugget, flake);
- embarcações com padrão elevado de serviço de galley.

Não faz sentido em:

- embarcação pequena sem gerador nem shore power contínuo;
- barco de uso esporádico (equipamento parado acumula biofilme);
- quando não há espaço para ventilação e dreno adequados.

## Tipos de gelo e equipamentos

| Tipo de gelo | Aplicação típica | Equipamento marine comum |
|---|---|---|
| Clear cube (cubo transparente) | Drinks premium | Scotsman CU50/CU0515, U-Line 2115B, Raritan Ice-Er-Ate |
| Half dice / full dice (cubo padrão) | Uso geral bebidas | Manitowoc QY-0204, Hoshizaki KM-50 |
| Nugget / chewable | Iate lounge, médica, pesca | Scotsman Brilliance, Hoshizaki FM-80 |
| Flake (raspas) | Pesca profissional, exposição de peixe | Scotsman AFE400, Hoshizaki FM-150 |
| Gourmet (esfera/forma) | Bar premium | U-Line H70, Sub-Zero UC-15IP |

Em recreio típico, clear cube ou half dice dominam. Flake é comum em pesca esportiva para preservar captura.

## O que ele exige do barco

Antes de instalar, é preciso verificar:

- disponibilidade de energia AC (maioria precisa de 115/230 V AC, 5-15 A dedicado);
- capacidade térmica de ventilação do nicho (30-50 mm livre em cada face mínimo);
- qualidade da água de alimentação (dureza, cloro, sedimento);
- drenagem correta (sem sifonagem, sem retorno);
- rotina de higienização (bin, evaporador, linha de água).

Sem isso, o equipamento tende a ter baixa produção, mau cheiro, biofilme e baixa confiabilidade.

## Produção nominal versus produção real

A produção indicada em catálogo depende de condições de ensaio (AHRI 810 típico):

- 21°C temperatura ambiente;
- 10°C temperatura da água de alimentação;
- tensão nominal;
- ciclo não-compartilhado.

Na prática, ela varia com:

- temperatura ambiente (trópico 30-35°C reduz 30-50%);
- temperatura da água de alimentação (água a 25°C reduz 15-25%);
- qualidade da ventilação;
- limpeza do sistema;
- estado do condensador e do circuito de água.

Logo, comparar equipamentos só por "kg/dia" é tecnicamente fraco.

## Água de alimentação

A máquina depende de água de qualidade coerente com o padrão de uso.

Pontos críticos:

- **pressão de alimentação** — tipicamente 1-5 bar; bomba pressurizada ou linha direta de tanque alto;
- **baixa carga de sedimento** — filtro 5 µm mínimo, idealmente 1 µm + carvão ativado;
- **controle de sabor e odor** — filtro de carvão ativado remove cloro, cloraminas, compostos orgânicos voláteis;
- **dureza da água** — acima de 150 ppm CaCO₃ exige softener (trocador iônico) para evitar entupimento;
- **compatibilidade com a rotina de sanitização** do sistema de água doce do barco.

**Antipadrão:** conectar icemaker em linha comum com bomba de chuveiro sem filtro dedicado. Equipamento dura 1-2 temporadas.

Ver também:

- [[Bomba de Água Pressurizada]]

## Drenagem e descarte

O dreno do equipamento precisa ser tratado como parte do projeto.

Ele não deve:

- criar retorno (sifonagem reversa é contaminação);
- gerar sifão indesejado (air gap mandatório em NSF 12);
- derramar em compartimento inadequado (porão fechado gera biofilme);
- dificultar limpeza (acesso para desentupir).

Dependendo da arquitetura da embarcação, a drenagem pode conversar com:

- **sistema de água cinza** — via air gap para evitar refluxo;
- **saída de casco dedicada** — acima da linha d'água, acima da linha de churrasco;
- **bomba de esgoto auxiliar** — quando gravidade não resolve.

Ver também:

- [[Caixa de Água Cinza]]

## Ventilação do nicho

Como todo equipamento frigorífico, o `icemaker` precisa rejeitar calor.

Sem ventilação adequada:

- a produção cai (até 50% em clima tropical);
- o compressor trabalha mais;
- a confiabilidade piora;
- o consumo sobe.

**Regras práticas:**

- mínimo 30-50 mm livre em cada face ventilada;
- entrada de ar em altura baixa, saída em altura alta;
- exaustor/ventilador auxiliar em nicho fechado;
- limpeza anual da serpentina do condensador (película de sal/pó reduz troca);
- em algumas linhas premium, water-cooled (água do mar) é alternativa — requer trocador de calor e bomba dedicada.

## Higiene e sanidade

Esse é um ponto frequentemente subestimado.

Como o gelo entra em contato direto com consumo humano, a máquina precisa de:

- **limpeza periódica** (a cada 3-6 meses em uso contínuo, anual em uso esporádico);
- **controle de biofilme** — limpeza com solução NSF-aprovada (ácido cítrico alimentar, Nickel-Safe, ou produto do fabricante);
- **atenção à qualidade da água** (pré-filtragem, substituição de cartucho conforme especificação);
- **bin de armazenamento bem mantido** (limpo, drenado, sem gelo acumulado "velho");
- **descalcificação** quando há sinal de resíduo branco (water scale);
- **desinfecção UV** em linhas profissionais de charter.

Equipamento aparentemente funcional pode produzir gelo inadequado sanitariamente (biofilme invisível na linha).

**Regulação sanitária aplicável:**

- **NSF/ANSI 12:2023** — Automatic Ice Making Equipment;
- **NSF/ANSI 61:2022** — Drinking Water System Components;
- **NSF/ANSI 372:2020** — Lead content (< 0.25%);
- **FDA Food Code 2022** — Retail and Food Service Operations (EUA, charter);
- **Portaria MS 2.914/2011** — Qualidade da água para consumo humano (Brasil).

## Integração elétrica

O `icemaker` deve entrar no projeto como carga AC relevante e não como tomada improvisada.

Analisar:

- **circuito dedicado** — breaker individual, não compartilhado com cafeteira/torradeira;
- **proteção compatível** — breaker 10-15 A típico para 115V AC, 6-10 A para 230V AC;
- **fator de simultaneidade** com outras cargas da galley (geladeira, fogão elétrico, microondas);
- **dependência de gerador ou shore power** — avaliar se banco de baterias + inversor cobre em fundeio (tipicamente não cobre em icemaker convencional);
- **queda de tensão** — menos crítica que em DC, mas ainda relevante em cabo longo até a popa.

Ver também:

- [[Gerador (AC)]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]

## Refrigerantes

### Tipos em uso marine

- **R-134a (HFC)** — padrão 2000-2020; GWP 1430; em phase-down global (Kigali/AIM Act/EU F-gas);
- **R-290 (propano)** — HC; GWP 3; classe A3 (inflamável); carga máxima em eletrodoméstico residencial 150 g (IEC 60335-2-24); em icemaker compacto com carga ≤ 150 g já é padrão;
- **R-404A (HFC blend)** — comercial, freezer/icemaker industrial; GWP 3922; em phase-down acelerado;
- **R-452A, R-448A** — blends modernos que substituem R-404A em aplicação comercial; GWP menor;
- **R-600a (isobutano)** — usado em icemaker residencial; carga pequena.

### Regulação ambiental (DEC-26)

Igual a geladeira/freezer:

| Jurisdição | Norma principal | Aplicação a icemaker |
|---|---|---|
| EUA | EPA SNAP + AIM Act 2020 + Section 608 | Certificação de técnico obrigatória; recuperação pré-descarte |
| UE | EU F-gas Regulation 517/2014 | Cronograma phase-down; registro de equipamento por carga |
| Internacional | Montreal + Kigali | Base regulatória global |
| Brasil | CONAMA 267/2000 + 340/2003 + Portaria MCT 86/2013 | Técnico certificado obrigatório; descarte via empresa credenciada |

### Prática marine

- equipamento novo em 2026: R-290 ou R-452A/R-448A dominam;
- recarga **nunca** em campo sem técnico certificado;
- descarte: recuperar gás, entregar a coletor credenciado.

## Onde costuma falhar

As falhas mais frequentes são:

- baixa produção por ambiente quente ou ventilação ruim;
- falha de alimentação de água (pressão baixa, filtro entupido);
- dreno mal resolvido (entupido, sifonado, invertido);
- biofilme e qualidade sanitária ruim;
- carga elétrica mal acomodada no sistema AC (disjuntor desarmando, queda de tensão);
- falsa expectativa de produção em uso tropical intenso;
- escala (scale) de cálcio/magnésio em evaporador;
- aquecedor de colheita (harvest heater) queimado — gelo não solta;
- válvula solenoide de água com defeito — ciclo não completa.

## Diagnóstico profissional

Perguntas obrigatórias:

1. A água chega com qualidade e pressão adequadas?
2. O equipamento tem ventilação suficiente?
3. O dreno está correto (sem sifonagem, sem retorno)?
4. A energia disponível suporta operação normal (tensão sob carga, breaker correto)?
5. O problema é de refrigeração, de água, de colheita ou de higiene?
6. O filtro de água foi substituído na periodicidade correta?

Ensaios úteis:

- medir pressão da água de alimentação em operação;
- medir tensão no equipamento durante partida e regime;
- observar tempo de ciclo (tipicamente 15-25 min por lote de cubos);
- inspecionar condensador e medir temperatura de saída do ar;
- verificar sabor, odor e aparência do gelo produzido;
- limpar sanitariamente e observar melhora em produção/qualidade.

## Boas práticas

- instalar apenas quando o perfil operacional justificar;
- prever filtro/qualidade de água coerentes (5 µm + carvão ativado mínimo);
- garantir ventilação e acesso de manutenção;
- incluir o equipamento na rotina sanitária da embarcação (trimestral ou semestral);
- tratar a produção nominal como valor condicionado, não promessa absoluta;
- documentar ciclo de manutenção (filtro, limpeza, inspeção) no manual da embarcação;
- respeitar regulação de refrigerante em qualquer intervenção.

## Erros comuns

- instalar em nicho quente e fechado;
- drenar de forma improvisada (mangueira sem air gap em porão);
- esquecer que gelo é item sanitário;
- subestimar o consumo e a dependência de AC;
- comparar modelos só pela produção de catálogo;
- não trocar filtro de água no prazo (perda de produção + sabor);
- ignorar biofilme porque "está funcionando";
- recarregar refrigerante sem certificação (ilegal).

## Normas aplicáveis

### 1. Padrão elétrico de recreio (ABYC/ISO)

- **ABYC A-16** — Electrical Safety;
- **ABYC E-11** — AC and DC Electrical Systems on Boats;
- **ABYC A-31** — Battery Chargers and Inverters (se operar via inversor);
- **ABYC H-23** — Installation of Potable Water Systems (alimentação);
- **ABYC H-28** — Greywater Systems (drenagem);
- **ISO 10133:2017** — Extra-low-voltage DC installations;
- **ISO 13297:2020** — AC installations;
- **ISO 15748:2002** — Potable water supply on ships.

### 2. Equipamento de refrigeração (IEC/UL/EN)

- **IEC 60335-2-24:2020** — Household refrigerating appliances;
- **IEC 60335-2-89:2019** — Commercial refrigerating appliances;
- **UL 563** — Icemaking Equipment;
- **UL 471** — Commercial Refrigerators and Freezers;
- **UL 60335-2-24** — Safety of Household Refrigerating Appliances;
- **EN 378:2016** — Refrigerating systems — Safety and environmental;
- **AHRI 810:2016** — Performance Rating of Automatic Commercial Ice-Makers.

### 3. Sanidade (NSF/FDA/MS)

- **NSF/ANSI 12:2023** — Automatic Ice Making Equipment;
- **NSF/ANSI 18:2023** — Manual Food and Beverage Dispensing Equipment;
- **NSF/ANSI 61:2022** — Drinking Water System Components;
- **NSF/ANSI 372:2020** — Drinking Water System Components — Lead Content;
- **FDA Food Code 2022** — Retail and Food Service;
- **Portaria MS 2.914/2011** — Água para consumo humano (Brasil);
- **ISO 17899:2018** — Marine potable water purification.

### 4. Refrigerantes — Regulação ambiental (DEC-26)

- **Protocolo de Montreal (1987)**;
- **Emenda de Kigali (2016)**;
- **EPA SNAP + EPA Section 608 + AIM Act 2020** (EUA);
- **EU F-gas Regulation 517/2014**;
- **CONAMA 267/2000 + 340/2003** (Brasil);
- **IN IBAMA 207/2008** (cadastro importadores);
- **Portaria MCT 86/2013** (certificação de técnicos);
- **ISO 817:2014** (classificação);
- **ASHRAE 34-2022 + ASHRAE 15-2022**.

### 5. Brasil (Marinha/ABNT)

- **NBR 13971:2014** — Manutenção programada de sistemas de refrigeração;
- **NBR 15960:2019** — Gases refrigerantes — Classificação;
- **NBR 5410:2004** — Instalações elétricas de baixa tensão;
- **NORMAM-01/DPC** — Mar aberto;
- **NORMAM-03/DPC** — Navegação interior.

### Tabela comparativa por jurisdição

| Aspecto | EUA (ABYC/EPA/UL/NSF) | Internacional (ISO/IEC/ASHRAE) | Europa (EN/EU) | Brasil (ABNT/CONAMA/MS) |
|---|---|---|---|---|
| Segurança elétrica | ABYC E-11 | ISO 13297 | EN 60335 | NBR 5410 |
| Equipamento ice | UL 563 | IEC 60335-2-24/89, AHRI 810 | EN 378 | NBR 13971 |
| Sanidade ice | NSF 12, FDA Food Code | ISO 17899 | EU regulation | MS 2.914/2011 |
| Refrigerante phase-down | EPA SNAP + AIM | Montreal + Kigali | EU F-gas 517 | CONAMA 267 |
| Manuseio refrigerante | EPA Section 608 | ISO 817, ASHRAE 34 | EU F-gas cert | Portaria MCT 86/2013 |

## Glossário rápido

- **Icemaker** — equipamento que produz gelo automaticamente.
- **Ice maker portátil** — equipamento independente, sem instalação fixa; produção 10-20 kg/dia.
- **Built-in ice maker** — embutido em gabinete da galley; produção 15-40 kg/dia.
- **Commercial ice maker** — uso profissional, produção 50-300 kg/dia.
- **Clear cube** — cubo transparente, formação lenta, drinks premium.
- **Half dice / full dice** — cubo padrão de bar.
- **Nugget / chewable** — gelo pequeno quebradiço, tipo Sonic.
- **Flake ice** — raspa de gelo, pesca e exposição.
- **Bin** — reservatório de armazenamento do gelo produzido.
- **Harvest cycle** — ciclo de colheita; gelo é liberado da placa evaporadora.
- **Harvest heater** — aquecedor que descola o gelo no ciclo de colheita.
- **Evaporador** — placa/molde onde o gelo se forma; fria por refrigerante.
- **Condensador** — trocador que rejeita calor; ar (air-cooled) ou água (water-cooled).
- **Water-cooled ice maker** — variante marine premium; usa água do mar em trocador.
- **Air-cooled** — padrão; ar ambiente rejeita calor do condensador.
- **Bomba de purga** — bomba que expulsa a água residual de cada ciclo.
- **Bin thermostat / sensor** — detecta bin cheio e para a produção.
- **Solenoid valve (água)** — válvula eletromagnética que admite água no ciclo.
- **Pré-filtro de sedimento** — 5 µm típico; remove partículas.
- **Filtro de carvão ativado** — remove cloro, cloraminas, gosto/odor.
- **Softener / trocador iônico** — remove cálcio/magnésio em água dura.
- **Scale / incrustação** — depósito de cálcio/magnésio em evaporador/linha.
- **Descalcificador** — produto químico (ácido cítrico alimentar ou equivalente NSF) que remove scale.
- **Air gap** — separação física que impede refluxo de esgoto para água limpa; mandatório NSF 12.
- **Biofilme** — camada de microrganismos em superfície úmida; contaminação sanitária.
- **NSF/ANSI 12** — norma de equipamento automático de gelo.
- **NSF/ANSI 61** — componentes em contato com água potável.
- **FDA Food Code 2022** — código alimentar dos EUA; aplica-se a charter.
- **Portaria MS 2.914/2011** — qualidade da água para consumo humano (Brasil).
- **R-134a (HFC)** — refrigerante dominante 2000-2020; em phase-down.
- **R-290 (propano, HC)** — A3 inflamável; padrão moderno em equipamento pequeno.
- **R-404A (HFC blend)** — comercial; em phase-down acelerado.
- **R-452A / R-448A** — blends modernos de baixo GWP.
- **GWP** — Global Warming Potential relativo ao CO₂.
- **ODP** — Ozone Depletion Potential.
- **A1/A2L/A3** — classes de segurança de refrigerante (ASHRAE 34 / ISO 817).
- **EPA SNAP** — Significant New Alternatives Policy (EUA).
- **EPA Section 608** — manuseio/recuperação de refrigerante (EUA).
- **AIM Act 2020** — phase-down HFC nos EUA.
- **EU F-gas 517/2014** — regulamento europeu.
- **CONAMA 267/2000** — proíbe substâncias que destroem ozônio (Brasil).
- **Portaria MCT 86/2013** — certificação de técnicos (Brasil).
- **Técnico certificado EPA 608** — habilitação para manuseio (EUA).
- **Recuperação** — remover refrigerante para recipiente; obrigatória antes do descarte.
- **Duty cycle** — tempo ligado / tempo total.
- **AHRI 810** — norma de performance de icemaker comercial.
- **Shore power** — alimentação AC de marina.
- **Charter** — operação comercial; regulação sanitária mais rigorosa.
- **Galley** — cozinha da embarcação.

## Integração com outras notas

- [[Ar-Condicionado Marine — Sistema Completo]]
- [[Ar-Condicionado Marine 12V DC]]
- [[Geladeira - Freezer de Bordo]]
- [[Bomba de Água Pressurizada]]
- [[Caixa de Água Cinza]]
- [[Gerador (AC)]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]

## Perguntas que esta nota responde

- Quando o icemaker faz sentido técnico na embarcação?
- Por que esse equipamento produz menos do que o esperado?
- Como integrar água, drenagem, energia e higiene na máquina de gelo de bordo?
- Qual refrigerante usa o icemaker marine e como ele é regulado?
- Quais normas sanitárias aplicam-se a gelo em embarcação comercial/charter?
- Como dimensionar carga elétrica do icemaker sem desarmar o gerador?
