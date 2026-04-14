---
title: "Chaves Seletoras (AC)"
note_type: "technical-note"
domain: "40_Distribuicao_Protecao_e_Aterramento"
source_file: "CHAVES SELETORAS (AC) 2c919734f7fb83078ff601354dc25bca.md"
status: "technical-review-l1"
reviewed_on: "2026-04-14"
review_jurisdiction: "Brasil"
source_urls:
  - "https://www.gov.br/pt-br/servicos/solicitar-inscricao-transferencia-de-propriedade-e-ou-jurisdicao-titulos-e-certidoes-de-embarcacoes"
  - "https://www.marinha.mil.br/dpc/normas"
  - "https://abycinc.org/standards/"
  - "https://www.iso.org/standard/83643.html"
aliases:
  - "CHAVES SELETORAS (AC)"
seo_title: "Chaves Seletoras (AC)"
seo_description: "CHAVES SELETORAS AC — Dispositivos de transferencia e selecao de fonte para shore power, gerador e inversor, com foco em intertravamento, topologia de neutro e seguranca da comutacao."
seo_keywords:
  - "Chave seletora AC"
  - "Transfer switch"
  - "Selecao de fonte"
  - "40 Distribuicao Protecao e Aterramento"
geo_queries:
  - "Como especificar chave seletora AC em embarcacao?"
  - "Como funciona a transferencia entre shore power, gerador e inversor?"
related_notes:
  - "CAIS (Pier) (AC)"
  - "Gerador (AC)"
  - "Inversora (DC To AC)"
  - "Proteção Dr"
  - "Quadro Elétrico e Painel de Distribuição AC-DC"
  - "Transformador Entrada"
---

# Chaves Seletoras (AC)

> [!abstract] Resumo técnico
> Chave seletora AC, manual ou automática, é o elemento que escolhe qual fonte de corrente alternada alimenta o sistema da embarcação. Sua função crítica é impedir paralelismo indevido entre fontes não sincronizadas e preservar a coerência elétrica entre shore power, gerador, inversor e o painel AC.

## O que é

É o dispositivo de transferência ou seleção de fonte entre:

- energia de cais;
- gerador de bordo;
- inversor/carregador;
- eventualmente outras entradas AC previstas no projeto.

Nem toda solução é uma "chave giratória simples". Dependendo da arquitetura, a seleção pode ocorrer por:

- chave manual;
- disjuntores intertravados;
- ATS externo;
- lógica interna de inversor/carregador.

## Função na embarcação

- impedir que duas fontes incompatíveis alimentem o mesmo barramento simultaneamente;
- organizar a prioridade entre fontes;
- permitir comutação controlada entre energia externa, geração local e inversão;
- sustentar segurança operacional e integridade dos equipamentos.

## Fundamentos mínimos

### Fonte AC não pode ser tratada como se fosse apenas "mais uma tomada"

Shore power, gerador e inversor têm comportamentos diferentes de tensão, frequência, neutro e aterramento. A comutação precisa preservar essa topologia.

### Paralelismo entre fontes não é manobra trivial

Duas fontes AC só podem operar em paralelo quando o sistema foi projetado para sincronização e compartilhamento. Fora desse cenário, a regra é seleção exclusiva com intertravamento.

### Break-before-make é a lógica mais comum

Na maior parte das embarcações de recreio, a chave ou o sistema de transferência deve abrir uma fonte antes de fechar a outra. Isso evita backfeed e paralelismo indevido.

### Neutro e PE exigem leitura arquitetural

A forma como neutro e proteção se relacionam depende da topologia da fonte selecionada e da arquitetura do barco. Uma chave seletora fisicamente simples pode induzir erro sério se a topologia de neutro não for entendida.

## Projeto e instalação

### O que precisa ser definido

1. quais fontes existem e em que ordem de prioridade;
2. se a comutação será manual, automática ou híbrida;
3. como neutro, PE e proteção diferencial se comportam em cada fonte;
4. qual é a corrente máxima do sistema;
5. quais cargas podem tolerar a interrupção de transferência;
6. como a operação será documentada para o usuário e para manutenção.

### Diretrizes práticas

- prever intertravamento real entre fontes;
- identificar claramente entradas e saída;
- não confiar em "memória do operador" como barreira de segurança;
- integrar a lógica de transferência com o painel AC e a proteção diferencial;
- evitar gambiarras com tomadas, plugues e backfeed improvisado.

## Onde costuma dar problema

| Problema | Causa provável |
| --- | --- |
| fonte errada energizando o barramento | chave mal operada ou arquitetura confusa |
| comutação falha ou intermitente | componente degradado, tensão fora da janela ou lógica ruim |
| disparos ou comportamento estranho após troca de fonte | topologia de neutro/PE mal tratada |
| dano em inversor, gerador ou entrada de cais | paralelismo indevido ou backfeed |
| usuário não sabe qual fonte está ativa | painel e chave mal identificados |

## Diagnóstico prático

1. Confirmar qual fonte deveria estar alimentando o sistema.
2. Verificar a posição ou o estado do sistema de transferência.
3. Medir presença de tensão na entrada e na saída da seletora.
4. Conferir se a topologia elétrica prevista para a fonte ativa está coerente com o restante do sistema.
5. Em ATS ou lógica automática, validar critérios de detecção, temporização e prioridade.

## Boas práticas profissionais

- usar transferência com intertravamento inequívoco;
- documentar operação normal e operação de contingência;
- tratar neutro, PE e DR em conjunto com a chave seletora;
- prever manutenção e teste funcional do sistema de transferência;
- desenhar a operação para minimizar erro humano.

## Erros comuns

- assumir que qualquer chave "serve" para transferir fontes AC;
- ligar duas fontes no mesmo barramento sem estratégia de sincronização;
- ignorar implicações de neutro e aterramento ao trocar a fonte;
- deixar a transferência dependente de procedimento informal não documentado;
- achar que inversor com relé interno resolve sozinho uma arquitetura mal pensada.

## Relação com outros sistemas

- **[[CAIS (Pier) (AC)]]** — fonte externa frequentemente priorizada.
- **[[Gerador (AC)]]** — fonte local com comportamento próprio.
- **[[Inversora (DC To AC)]]** — fonte alternativa e, muitas vezes, elemento de transferência.
- **[[Proteção Dr]]** — coerência da proteção diferencial conforme a fonte ativa.
- **[[Quadro Elétrico e Painel de Distribuição AC-DC]]** — ponto de distribuição a jusante.
- **[[Transformador Entrada]]** — influencia a topologia de entrada AC.

## Normas e referências

- documentação do transfer switch ou do inversor/carregador;
- critérios aplicáveis de transferência de fonte, seccionamento e proteção AC;
- diagrama unifilar real da embarcação.

## FAQ

**Posso transferir diretamente de uma fonte para outra sem passar por OFF?**

Depende do equipamento específico e da lógica de transferência prevista. Em muitos sistemas simples, a filosofia segura é break-before-make.

**Todo inversor já substitui chave seletora externa?**

Não. Isso depende da arquitetura, da quantidade de fontes e do que o equipamento realmente gerencia.

**Se a tensão está presente, a transferência está correta?**

Não necessariamente. Pode haver presença de tensão com topologia incorreta, fonte errada ou risco de backfeed.

## Integração com outras notas

- [[CAIS (Pier) (AC)]]
- [[Gerador (AC)]]
- [[Inversora (DC To AC)]]
- [[Proteção Dr]]
- [[Quadro Elétrico e Painel de Distribuição AC-DC]]
- [[Transformador Entrada]]

## Perguntas que esta nota responde

- Como selecionar fontes AC em embarcações com segurança?
- Qual a função real de uma chave seletora ou transfer switch?
- Quais erros de topologia e operação aparecem na comutação AC de bordo?
