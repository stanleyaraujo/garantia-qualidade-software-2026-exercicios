# 🔬 Projeto Integrador: **Auditoria de Qualidade**

**UC:** Garantia da Qualidade de Software — UNIFG 2026/2
**Professor:** Petros Barreto
**Peso:** 60% da média final (40% marcos + 20% apresentação)
**Entrega final:** Aula 40 — apresentação de 20 min + relatório de auditoria

---

## 🎯 O que você vai fazer

Você recebe um sistema **real e com defeitos** e constrói, ao longo do semestre,
o **programa completo de garantia da qualidade** em volta dele.

O sistema sob teste é o
[**`sistema-biblioteca-qa`**](https://github.com/petrosbarreto/sistema-biblioteca-qa):
uma aplicação Python de gestão de empréstimos de biblioteca, escrita de propósito
como um sistema legado plausível — com regras de negócio de verdade, sem testes,
com dívida técnica e **com defeitos plantados**.

```
┌─────────────────────────────────────────────────────────────────┐
│  sistema-biblioteca-qa   ← você NÃO escreveu, e é isso mesmo     │
│                                                                 │
│  • empréstimo e devolução de exemplares                          │
│  • cálculo de multa por atraso                                   │
│  • limite de empréstimos por tipo de usuário                     │
│  • reserva e fila de espera                                      │
│  • renovação com regras de bloqueio                              │
│  • relatórios e API HTTP                                         │
│                                                                 │
│  Sem testes. Com dívida técnica. Com defeitos.                  │
└─────────────────────────────────────────────────────────────────┘
```

> 💡 **Por que um sistema que você não escreveu:** porque é a situação real.
> Quase ninguém começa a carreira num projeto novo — você entra num sistema que
> já existe, ninguém documentou, e precisa decidir onde investir esforço de
> qualidade com informação incompleta. Escrever testes para o próprio código, que
> você acabou de escrever e já sabe que funciona, é um exercício muito mais
> fácil e muito menos parecido com o trabalho.

---

## ⚠️ A regra fundamental do projeto

> **Nenhum artefato pode ser fictício.**

Todo defeito relatado tem que existir de verdade, e vir acompanhado do **teste
que o expõe**. Toda métrica tem que ser medida, não estimada. Todo risco
apontado tem que se referir a um trecho identificável do código.

Um relatório de auditoria bem escrito mas com achados inventados vale **zero**.
Essa é a diferença entre garantia da qualidade e teatro de qualidade — e é o
ponto ético central desta UC.

---

## 📅 Marcos

Cada marco é um Pull Request com o título `[Auditoria MN] Seu Nome Completo`.

### M1 — Plano de Teste (Aula 10) · 15%

| Entregável | Conteúdo |
|---|---|
| `01-plano-de-teste.md` | Estruturado conforme ISO/IEC/IEEE 29119: escopo, itens de teste, abordagem, critérios de entrada e saída, ambiente, cronograma, riscos do projeto de teste |
| `02-criterios-aceitacao.md` | Critérios de aceitação para as 6 regras de negócio principais, escritos de forma **verificável** |
| `03-analise-de-risco.md` | Matriz risco = probabilidade × impacto, para no mínimo 10 áreas do sistema, com a **priorização de teste** decorrente |
| `04-matriz-rastreabilidade.md` | Requisito → critério de aceitação → caso de teste (os casos podem ficar como `TBD` neste marco) |

**O que separa uma nota alta:** a análise de risco tem que **justificar** a
priorização. Dizer "o cálculo de multa é de risco alto" não vale nada; dizer
"risco alto porque envolve dinheiro, tem 4 ramos condicionais, foi alterado 3
vezes no histórico do Git e não tem nenhum teste" vale tudo.

### M2 — Inspeção e Análise Estática (Aula 14) · 15%

| Entregável | Conteúdo |
|---|---|
| `05-relatorio-inspecao.md` | Inspeção formal de **2 módulos** escolhidos pelo risco do M1, com checklist e achados |
| `06-analise-estatica.md` | Saída de `ruff`, `mypy`, `radon` e `bandit`, **interpretada** — não colada |
| **GitHub Issues** | Cada defeito registrado como Issue, com template, severidade, prioridade e passos de reprodução |
| `07-defeitos.md` | Tabela consolidada, classificada por tipo (ODC) e severidade |

**O que separa uma nota alta:** a **qualidade do relatório de defeito**, não a
quantidade. Um relatório que outra pessoa consegue reproduzir sem te perguntar
nada vale mais que dez achados vagos. E: defeito encontrado por análise estática
tem que ser confirmado como defeito **real** — falso positivo de linter relatado
como bug desconta.

### M3 — Especificação de Casos de Teste (Aula 20) · 15%

| Entregável | Conteúdo |
|---|---|
| `08-casos-caixa-preta.md` | Partição de equivalência + valor limite + tabela de decisão para o cálculo de multa e o limite de empréstimos |
| `09-casos-caixa-branca.md` | Grafo de fluxo, complexidade ciclomática e conjunto de caminhos básicos de **2 funções** |
| `10-teste-exploratorio.md` | Registro de 2 sessões de teste exploratório com *charter*, achados e tempo |

**O que separa uma nota alta:** para **cada** conjunto de casos, a justificativa
da técnica escolhida. Por que tabela de decisão aqui e valor limite ali?

### M4 — Suíte Automatizada e TDD (Aula 26) · 20%

| Entregável | Conteúdo |
|---|---|
| `tests/unit/` | Testes de unidade dos módulos de maior risco, com dublês onde couber |
| `tests/integration/` | Testes de integração (persistência, camadas) |
| `tests/system/` | Testes de sistema via API |
| `tests/acceptance/` | Testes de aceitação em Gherkin (`behave` ou `pytest-bdd`) |
| `11-tdd-nova-funcionalidade.md` | Uma funcionalidade **nova** implementada por TDD, com o histórico de commits mostrando o ciclo red-green-refactor |
| Correção dos defeitos | Cada defeito do M2 corrigido, **com o teste que o pegou commitado antes da correção** |

**Requisito não negociável:** para cada defeito corrigido, o histórico do Git tem
que mostrar o **teste falhando antes** da correção. Corrigir e depois escrever o
teste não conta — e é verificável no histórico.

### M5 — Painel de Métricas (Aula 31) · 15%

| Entregável | Conteúdo |
|---|---|
| `12-metricas.md` | Cobertura (linha, ramo), complexidade ciclomática, acoplamento, densidade de defeitos, DRE, dívida técnica estimada |
| `13-analise-metricas.md` | Interpretação: o que cada número **significa** e o que fazer a respeito |
| Painel | Gerado por script (`scripts/metricas.py`), reproduzível, com histórico entre os marcos |

**O que separa uma nota alta:** mostrar uma métrica que **enganaria** um gestor
desatento e explicar por quê. Exemplo: um módulo com 100% de cobertura e
nenhuma asserção significativa.

### M6 — CI com Quality Gates e Parecer Ético (Aula 39) · 15%

| Entregável | Conteúdo |
|---|---|
| `.github/workflows/qa.yml` | Pipeline com estágios: lint → tipos → unidade → integração → cobertura → segurança → mutação |
| Quality gates | Limiares que **reprovam** o build, com justificativa de cada limiar escolhido |
| `14-parecer-etico.md` | Parecer sobre os defeitos encontrados: impacto no usuário, dever de comunicação, o que você faria se a gerência pedisse para liberar assim |
| `15-relatorio-desempenho.md` | Teste de carga com `locust` e análise |

### M7 — Apresentação (Aula 40) · 5%

| Tempo | Conteúdo |
|---|---|
| 3 min | O sistema, o escopo da auditoria e como você priorizou |
| 7 min | Os achados: os 3 defeitos mais graves, com demonstração ao vivo do teste que os expõe |
| 5 min | As métricas: antes e depois, com a evolução |
| 3 min | O parecer ético e sua recomendação (liberar / não liberar / liberar com ressalvas) |
| 2 min | Perguntas |

---

## 📁 Estrutura da entrega

```
auditoria-biblioteca/
├── README.md                      resumo executivo da auditoria
├── relatorio/
│   ├── 01-plano-de-teste.md ... 15-relatorio-desempenho.md
├── tests/
│   ├── unit/ · integration/ · system/ · acceptance/
│   └── conftest.py
├── scripts/
│   └── metricas.py                gera o painel, reproduzível
├── .github/workflows/qa.yml
└── evidencias/
    ├── cobertura/ · analise-estatica/ · carga/
    └── prints/
```

---

## 🎚️ Níveis de escopo

Escolha na Aula 06 e declare no `README.md` da sua auditoria.

| Nível | Escopo | Nota máxima |
|---|---|---|
| **1 — Essencial** | Todos os marcos, cobrindo os **3 módulos de maior risco** | 8,5 |
| **2 — Completo** | + *mutation testing* com `mutmut`, testes de contrato de API, cobertura de ramo ≥ 80% nos módulos auditados | 10,0 |
| **3 — Avançado** | + *property-based testing* com `hypothesis`, teste de carga com análise de gargalo, refatoração guiada por métricas com antes/depois medido | 10,0 + bônus |

**Bônus (+0,25 cada, máx. +1,5):**

- Relatório de auditoria publicado como site (GitHub Pages)
- *Fuzzing* da API com `schemathesis`
- Análise de histórico do Git para achar módulos "quentes" (muitas alterações + muitos defeitos)
- Comparação da mesma suíte implementada em **JUnit 5** para um módulo
- Teste de acessibilidade da interface, se você implementar uma
- *Chaos testing*: o sistema se comporta bem com o banco indisponível?

---

## ✅ Rubrica de cada marco

| Critério | Pontos |
|---|---|
| **Corretude técnica** — os artefatos estão tecnicamente certos | 35 |
| **Rigor do raciocínio** — as escolhas estão justificadas | 30 |
| **Qualidade dos artefatos** — reprodutíveis, legíveis, completos | 25 |
| **Clareza e comunicação** | 10 |

### O que zera um marco

- Achado, defeito ou métrica **fictício**
- Teste que não roda, ou suíte quebrada
- Métrica reportada sem o comando que a produziu
- Artefato que você não consegue explicar
- Correção de defeito sem o teste que o expõe commitado antes

---

## 💡 Conselhos de quem já corrigiu auditorias

**Não tente testar tudo.** O sistema é maior do que 160 horas permitem cobrir. O
M1 existe justamente para você **decidir onde não investir** — e defender essa
decisão. Uma auditoria focada nos 3 módulos críticos, bem feita, vale mais que
uma varredura rasa em 15 módulos.

**Leia o histórico do Git antes de escolher.** `git log --format= --name-only |
sort | uniq -c | sort -rn` mostra os arquivos mais alterados. Arquivo que muda
muito e não tem teste é onde os defeitos moram.

**Escreva o relatório de defeito pensando em quem vai corrigir.** Título que
descreve o **sintoma**, não a sua teoria da causa. Passos numerados. Resultado
esperado e resultado obtido, separados. Versão e ambiente.

**O parecer ético do M6 não é redação escolar.** É a parte da auditoria em que
você assume uma posição técnica com consequências. Se você encontrar um defeito
que cobra multa indevida do usuário, a recomendação "não liberar" precisa estar
escrita, com fundamento — porque é isso que um profissional faz.

---

**Dúvidas?** Abra uma Issue no repositório de exercícios ou pergunte em sala.
