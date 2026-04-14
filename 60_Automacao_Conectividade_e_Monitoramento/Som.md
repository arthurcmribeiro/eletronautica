---
title: "Som"
note_type: "system"
domain: "60_Automacao_Conectividade_e_Monitoramento"
source_file: "SOM 99519734f7fb82afa0ef81e230098bb2.md"
status: "technical-review-l1"
aliases:
  - "SOM"
seo_title: "Som"
seo_description: "SISTEMA DE SOM A BORDO — Arquitetura de audio para entretenimento que exige cuidado com energia, protecao, EMC, corrosao, zonas de uso e convivencia com sistemas de navegacao."
seo_keywords:
  - "Som de bordo"
  - "Audio marinho"
  - "Amplificador nautico"
  - "60 Automacao Conectividade e Monitoramento"
geo_queries:
  - "Como projetar sistema de som a bordo?"
  - "Quais sao as falhas comuns de audio em embarcacoes?"
related_notes:
  - "TV a Bordo / Entretenimento"
  - "Wi-Fi a Bordo — Roteador Marine e Conectividade"
  - "VHF"
  - "Inversora (DC To AC)"
  - "Banco de Baterias"
  - "Bússola Eletrônica (Compass / HDG Sensor)"
---

# Som

> [!abstract] Resumo técnico
> Sistema de som a bordo é uma instalação de entretenimento que convive com vibração, névoa salina, restrição energética e forte sensibilidade a EMC. O erro recorrente é tratar áudio como acessório isolado, sem considerar banco de baterias, proteção, cabeamento, zonas de uso e impacto sobre equipamentos de navegação.

## O que é

Um sistema de som de bordo normalmente combina:

- fonte ou head unit;
- processador ou controle por zonas, quando aplicável;
- amplificador;
- alto-falantes e, às vezes, subwoofer;
- infraestrutura elétrica e de sinal.

Em projetos maiores, o ponto central não é "ter mais potência", e sim distribuir áudio com coerência entre zonas internas e externas sem degradar energia, confiabilidade ou segurança operacional.

## Função na embarcação

- entretenimento em fundeio, marina e navegação compatível com a operação;
- distribuição de áudio por zonas;
- integração com TV, streaming e, em alguns casos, sistemas de anúncio.

## Fundamentos mínimos

### Potência anunciada não é critério suficiente

Potência de marketing e potência útil não são a mesma coisa. Em engenharia de áudio embarcado, o que importa é a combinação entre:

- potência contínua aplicável;
- impedância compatível;
- sensibilidade do alto-falante;
- volume desejado no ambiente real;
- capacidade do sistema elétrico de sustentar a carga.

### Energia e autonomia precisam entrar na conta

Áudio de alta potência, especialmente com subwoofer e múltiplas zonas, pode virar carga relevante do banco de serviço. Em uso prolongado, o impacto no balanço energético é real.

### EMC e ruído são parte do projeto

Cabos de alimentação, cabos de sinal e pontos de retorno mal definidos geram zumbido, ruído de alternador, distorção e comportamento errático.

### Segurança operacional prevalece sobre entretenimento

O sistema não deve mascarar alarmes, chamadas operacionais ou percepção situacional quando a navegação exigir atenção.

## Arquiteturas comuns

### Sistema simples

- head unit com amplificação interna;
- poucas zonas;
- menor complexidade;
- adequado para embarcações pequenas e uso moderado.

### Sistema com amplificador dedicado

- maior controle de potência e qualidade;
- exige projeto sério de alimentação, proteção e ventilação;
- adequado para cockpit aberto ou múltiplas zonas.

### Sistema multizona

- distribuição independente por áreas;
- útil em embarcações maiores;
- aumenta exigência de controle, cabeamento e governança de consumo.

## Projeto e instalação

### O que precisa ser definido

1. zonas de escuta e prioridade de uso;
2. nível de exposição à umidade, UV e spray;
3. potência real requerida por zona;
4. forma de alimentação e proteção do circuito;
5. separação física entre sinal, potência e navegação;
6. distância de componentes magnéticos em relação a bússolas e sensores.

### Diretrizes práticas

- preferir alimentação pelo banco de serviço, não pelo banco de partida;
- proteger cada ramal de potência conforme cabo e carga;
- manter retorno elétrico coerente para evitar ruído;
- instalar amplificador em local ventilado e acessível;
- escolher equipamento adequado ao ambiente de exposição real, não ao marketing.

## Onde costuma dar problema

| Problema | Causa provável |
| --- | --- |
| chiado ou zumbido | retorno ruim, laço de terra, EMI ou roteamento inadequado |
| distorção em volume alto | clipping, falante incompatível ou alimentação insuficiente |
| desligamento aleatório | queda de tensão, aquecimento ou proteção entrando |
| oxidação precoce | conectores e equipamentos inadequados ao ambiente |
| leitura errada de bússola | proximidade excessiva de ímãs e componentes magnéticos |

## Diagnóstico prático

1. Confirmar tensão no equipamento sob carga real.
2. Medir queda de tensão no ramal do amplificador.
3. Verificar impedância e integridade dos alto-falantes.
4. Isolar ruído entre alimentação, sinal e equipamento.
5. Validar posicionamento físico em relação a sensores de navegação.

## Boas práticas profissionais

- documentar zonas, fusíveis, bitolas e pontos de retorno;
- tratar cabo de potência e cabo de sinal como circuitos distintos;
- não dimensionar amplificador e banco "no limite";
- escolher alto-falantes e equipamentos compatíveis com o ambiente real;
- prever comando simples para desligamento total quando o barco estiver parado;
- manter o sistema subordinado à segurança operacional e aos alarmes do barco.

## Erros comuns

- usar equipamento automotivo em área exposta como se fosse equivalente marinho;
- alimentar sistema potente pela bateria de partida;
- misturar retorno de sinal e potência sem critério;
- instalar alto-falantes perto demais de bússola ou heading sensor;
- projetar potência sem olhar autonomia e dissipação térmica.

## Relação com outros sistemas

- **[[TV a Bordo / Entretenimento]]** — integração de áudio e vídeo.
- **[[Wi-Fi a Bordo — Roteador Marine e Conectividade]]** — streaming local e internet.
- **[[Inversora (DC To AC)]]** — quando parte do sistema depender de equipamentos AC.
- **[[Banco de Baterias]]** — impacto energético do entretenimento.
- **[[VHF]]** e **[[Bússola Eletrônica (Compass / HDG Sensor)]]** — convivência eletromagnética e espacial.

## Normas e referências

- documentação elétrica e ambiental do fabricante;
- boas práticas de instalação DC, EMC e proteção de circuitos;
- critérios de montagem compatíveis com o ambiente marinho real da embarcação.

## FAQ

**Equipamento automotivo sempre é inadequado?**

Não em qualquer contexto, mas em áreas expostas ou em uso severo normalmente traz durabilidade e confiabilidade inferiores às de soluções adequadas ao ambiente marinho.

**Sistema de som deve ficar no banco de partida?**

Em regra, não é a arquitetura preferível. O consumo de entretenimento deve ficar no banco de serviço, salvo projeto muito específico.

**Ruído de alternador no áudio é sempre culpa do alternador?**

Não. Muitas vezes o problema está no roteamento de cabos, retorno elétrico, filtragem ou instalação do amplificador.

## Integração com outras notas

- [[TV a Bordo / Entretenimento]]
- [[Wi-Fi a Bordo — Roteador Marine e Conectividade]]
- [[VHF]]
- [[Inversora (DC To AC)]]
- [[Banco de Baterias]]
- [[Bússola Eletrônica (Compass / HDG Sensor)]]

## Perguntas que esta nota responde

- Como projetar sistema de som a bordo sem comprometer a elétrica?
- Quais são os erros mais comuns em áudio embarcado?
- Como evitar ruído, distorção e interferência em sistema de som náutico?
