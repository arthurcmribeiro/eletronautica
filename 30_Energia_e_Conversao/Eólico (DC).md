---
title: "Eólico (DC)"
note_type: "technical-note"
domain: "30_Energia_e_Conversao"
source_file: "EÓLICO (DC) d0b19734f7fb8218b70581ee7f081bf3.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
review_level: "engineering-curated"
aliases:
  - "EÓLICO (DC)"
  - "Gerador eólico náutico"
seo_title: "Eólico DC em embarcações: quando vale a pena, limites e integração"
seo_description: "Guia técnico sobre geração eólica DC em embarcações: produção real, turbulência, controlador, dump load, ruído, instalação e integração com solar e banco de baterias."
seo_keywords:
  - "eólico DC embarcação"
  - "gerador eólico náutico"
  - "dump load turbina barco"
  - "solar e eólico veleiro"
geo_queries:
  - "Gerador eólico vale a pena em embarcação?"
  - "Quais cuidados técnicos existem na instalação de turbina eólica náutica?"
related_notes:
  - "Bancos de Bateria"
  - "Inversora (DC To AC)"
  - "Monitor de Bateria - BMV - Shunt"
  - "Placa Solar (DC)"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Relés e Relés de Estado Sólido"
  - "Tipos de Bateria"
---

# Eólico (DC)

> [!abstract] Resumo técnico
> Geração eólica DC em embarcação é solução de nicho, útil sobretudo quando há vento consistente, longos períodos fundeado e perfil de consumo noturno relevante. Não substitui automaticamente o solar e não faz sentido universal em qualquer barco.

## O que é

É a geração elétrica proveniente de turbina eólica de pequeno porte integrada ao sistema DC da embarcação. Em geral, a máquina gera energia variável que precisa ser condicionada e controlada antes de chegar ao banco de baterias.

Em sistemas pequenos, a saída final é tratada como geração DC para carga do banco e alimentação do barramento.

## Quando faz sentido

Faz mais sentido em:

- veleiros e embarcações de cruzeiro com permanência longa em fundeio;
- cenários com vento noturno ou persistente;
- arquiteturas híbridas em que o [[Placa Solar (DC)|solar]] não cobre bem o período sem sol;
- perfis operacionais em que ruído e ocupação de espaço são aceitáveis.

Faz menos sentido em:

- lanchas de uso ocasional;
- barcos com perfil de marina e shore power frequente;
- embarcações em locais de vento muito turbulento ou inconsistente;
- projetos em que ruído, vibração e visual são críticos.

## O maior problema de expectativa

Potência nominal de catálogo não equivale a produção diária real.

Em geração eólica pequena, a produção é fortemente afetada por:

- distribuição real de vento;
- turbulência criada pelo próprio barco, mastro, radar, hardtop e superestrutura;
- altura de instalação;
- estratégia de controle;
- necessidade de frenagem e dump load.

Muita decepção com eólico nasce de expectativa irreal, não necessariamente de defeito.

## Integração elétrica correta

O sistema precisa considerar:

- característica elétrica da turbina;
- controlador compatível;
- estratégia de frenagem ou carga de desvio, quando exigida;
- proteção da linha até o banco;
- comportamento do banco ao se aproximar do estado cheio;
- química da bateria.

Nem toda turbina aceita ser conectada a um controlador genérico. Eólico pede arquitetura própria.

## Relação com o banco de baterias

O comportamento do banco muda muito o aproveitamento do sistema:

- chumbo limita aceitação de carga ao avançar o SOC;
- lítio aproveita melhor geração variável, mas exige coordenação com BMS e controlador;
- banco inadequado ou já saturado reduz o benefício prático do eólico.

## Relação com o solar

O melhor uso do eólico costuma ser complementar ao solar:

- solar domina em dias claros;
- eólico pode contribuir em vento noturno, tempo fechado e fundeio prolongado.

Se o barco já tem área boa para solar e perfil diurno, normalmente o primeiro investimento racional continua sendo fotovoltaico.

## Instalação mecânica

A parte mecânica é tão importante quanto a elétrica. Entram aqui:

- altura;
- rigidez do suporte;
- transmissão de vibração;
- segurança física das pás;
- acesso para manutenção;
- compatibilidade com mastreação, toldos e antenas.

Instalação mal posicionada gera:

- ruído excessivo;
- fadiga estrutural;
- turbulência e baixa geração;
- risco operacional para tripulação.

## Falhas típicas

As mais frequentes são:

- produção muito abaixo da expectativa;
- ruído e vibração tornando o sistema inutilizável;
- desgaste prematuro de rolamentos;
- suporte flexível ou mal ancorado;
- falha de frenagem ou de dump load;
- corrosão em conectores, controlador ou partes móveis.

## Diagnóstico profissional

O diagnóstico deve responder:

1. Há vento útil no local e na altura de instalação?
2. A turbina está operando na janela prevista pelo fabricante?
3. O banco está apto a receber a energia naquele momento?
4. O controlador está adequado à máquina?
5. O gargalo é aerodinâmico, mecânico ou elétrico?

Medições úteis:

- tensão e corrente entregues em diferentes ventos;
- estado do banco;
- temperatura do controlador e da carga de desvio;
- vibração estrutural do suporte;
- histórico de produção comparado ao ambiente real.

## Boas práticas

- dimensionar o eólico para complementar, não para sustentar fantasia energética;
- instalar em local de melhor vento e menor turbulência possível;
- tratar ruído e vibração como critérios de projeto, não como detalhe;
- manter proteção anticorrosiva e rotina de inspeção;
- integrar geração eólica ao monitoramento do sistema;
- revisar se o perfil operacional do barco realmente justifica essa solução.

## Erros comuns

Os mais recorrentes são:

- comprar pela potência de catálogo;
- instalar atrás de superestrutura, mastro ou radar;
- tratar o sistema como se fosse "igual a solar";
- ignorar dump load, frenagem e controle próprio;
- achar que eólico resolve sozinho um balanço energético ruim.

## Integração com outras notas

- [[Bancos de Bateria]]
- [[Inversora (DC To AC)]]
- [[Monitor de Bateria - BMV - Shunt]]
- [[Placa Solar (DC)]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]
- [[Tipos de Bateria]]

## Perguntas que esta nota responde

- Quando geração eólica realmente faz sentido em embarcação?
- Por que potência nominal de turbina pequena costuma enganar?
- Quais limites mecânicos e elétricos definem se o sistema vai funcionar bem ou virar ruído caro?
