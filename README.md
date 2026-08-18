# ✅ Exercícios — Garantia da Qualidade de Software

**UNIFG 2026/2** · Prof. Petros Barreto · **160h** — 40 aulas de 4h
**Área:** Computação e TIC · **Nível:** Intermediário

Repositório **público** da UC. Aqui ficam as listas semanais, a especificação do
projeto de **Auditoria de Qualidade** e a validação automática dos Pull Requests.

> Os **slides** ficam em repositório separado. O link é distribuído em sala e no
> ambiente virtual.

---

## 🚀 Começando (uma vez no semestre)

```bash
# 1. Faça FORK deste repositório

# 2. Clone o SEU fork
git clone https://github.com/SEU-USUARIO/garantia-qualidade-software-2026-exercicios.git
cd garantia-qualidade-software-2026-exercicios

# 3. Aponte para o original, para receber as listas novas
git remote add upstream https://github.com/petrosbarreto/garantia-qualidade-software-2026-exercicios.git

# 4. Ambiente
curl -LsSf https://astral.sh/uv/install.sh | sh
uv init && uv python pin 3.13
uv add --dev pytest pytest-cov pytest-mock ruff mypy radon bandit

# 5. Confira
uv run pytest --version && uv run ruff --version
```

### Antes de cada lista nova

```bash
git switch main && git pull upstream main && git push origin main
```

---

## 📤 Entregando

```bash
git switch -c aula07
# resolva em exercicios/aula07/
uv run pytest exercicios/aula07/ -v
uv run ruff check exercicios/aula07/
git add exercicios/aula07 && git commit -m "Aula 07: matriz de rastreabilidade"
git push -u origin aula07
# PR com o título EXATO: [Aula 07] Seu Nome Completo
```

⚠️ **PR com título fora do padrão não é corrigido.** Formato:
`[Aula NN] Nome Completo`. Para o projeto: `[Auditoria M3] Nome Completo`.

### 🤖 Validação automática

| Verificação | Se falhar |
|---|---|
| `pytest` nas pastas alteradas | ❌ comentário com a saída |
| `ruff check` (lint) | ⚠️ aviso com os achados |
| Presença de `RESPOSTAS.md` | ❌ comentário pedindo o arquivo |
| Título do PR no padrão | ⚠️ aviso |
| Cobertura reportada | ℹ️ informativo — **não** é critério de aprovação |

> 💡 **Por que a cobertura é apenas informativa:** porque cobertura mede
> **execução**, não verificação. Transformá-la em critério de aprovação seria
> criar exatamente a Lei de Goodhart que estudamos na Aula 01. O critério de
> qualidade dos seus testes é a **rubrica**, avaliada por pessoa.

---

## 📂 Estrutura de cada entrega

```
exercicios/aulaNN/
├── RESPOSTAS.md          # análises, justificativas, tabelas, pareceres
├── *.py                  # código sob teste (quando houver)
├── test_*.py             # seus testes
└── evidencias/           # saídas de comandos, prints, relatórios
```

**Regras não negociáveis:**

1. `RESPOSTAS.md` com as seções nomeadas **como no enunciado** (`## Parte A`, `### A1`).
2. **Toda métrica reportada vem com o comando que a produziu.** Número sem comando
   não conta.
3. **Toda escolha de técnica vem justificada.** Aplicar sem justificar perde
   pontos no critério de rigor.
4. `ruff check` sem erros; código formatado (`ruff format`).
5. `pytest` verde no seu fork antes do PR.

---

## 📊 Rubrica padrão de todas as listas

| Critério | Pontos | O que se avalia |
|---|---|---|
| **Corretude técnica** | 35 | as respostas e o código estão certos |
| **Rigor do raciocínio** | 30 | as escolhas estão **justificadas** |
| **Qualidade dos artefatos** | 25 | reprodutíveis, legíveis, completos |
| **Clareza e comunicação** | 10 | estrutura e redação |

⚠️ **"Rigor do raciocínio" vale 30 pontos.** Nesta UC, **escolher** uma técnica
de teste é mais importante que aplicá-la. Em várias questões **não existe resposta
única** — existe resposta fundamentada e resposta sem fundamento.

### Prazos

| | |
|---|---|
| Entrega | até a véspera da aula seguinte, 23h59 |
| Atraso até 7 dias | −20 pontos |
| Atraso acima de 7 dias | não corrigido (conta como descartada) |

Nota de exercícios = média das 40 listas, **descartando as 2 piores**.

---

## 🧮 Composição da nota final

| Instrumento | Peso |
|---|---|
| Listas semanais (40) | 30% |
| Marcos do projeto de auditoria (M1–M6) | 40% |
| Revisão por pares | 10% |
| Apresentação final do relatório (M7) | 20% |

> ⚠️ **A revisão por pares é avaliada nas duas direções.** A qualidade da revisão
> que você **faz** no código do colega vale tanto quanto o código que você
> entrega. Revisão agressiva perde nota. Revisão vazia ("LGTM") também.

---

## 🔬 Projeto Integrador: Auditoria de Qualidade

Você recebe um sistema real **com defeitos plantados** e constrói o programa
completo de QA em volta dele.

**Sistema sob teste:** [`sistema-biblioteca-qa`](https://github.com/petrosbarreto/sistema-biblioteca-qa)
— aplicação Python de empréstimo de livros, sem testes, com dívida técnica.

| Marco | Aula | Entrega | Peso |
|---|---|---|---|
| M1 | 10 | Plano de teste + análise de risco + critérios de aceitação | 15% |
| M2 | 14 | Relatório de inspeção e análise estática + defeitos registrados | 15% |
| M3 | 20 | Especificação de casos de teste (caixa-preta e caixa-branca) | 15% |
| M4 | 26 | Suíte nos 4 níveis + TDD de funcionalidade nova | 20% |
| M5 | 31 | Painel de métricas com análise | 15% |
| M6 | 39 | CI com quality gates + parecer ético | 15% |
| M7 | 40 | Apresentação do relatório de auditoria | 5% |

> ⚠️ **A regra fundamental:** nenhum artefato pode ser fictício. Todo defeito
> relatado tem que existir de verdade, com o **teste que o expõe**. Toda métrica
> tem que ser medida, não estimada. Relatório bem escrito com achado inventado
> vale **zero**.

Especificação completa em [`projeto/README.md`](projeto/README.md).

---

## 📚 Índice das listas — 8 Unidades de Aprendizagem

| UA | Aulas | Tema |
|---|---|---|
| **1** | [01](exercicios/aula01) · 02 · 03 · 04 · 05 | Fundamentos da qualidade |
| **2** | 06 · 07 · 08 · 09 · 10 | Planejamento da qualidade |
| **3** | 11 · 12 · 13 · 14 | Inspeção e revisão |
| **4** | 15 · 16 · 17 · 18 · 19 · 20 | Técnicas de teste |
| **5** | 21 · 22 · 23 · 24 · 25 · 26 | Estratégias de teste |
| **6** | 27 · 28 · 29 · 30 · 31 | Métricas de qualidade |
| **7** | 32 · 33 · 34 | Ética e boas práticas |
| **8** | 35 · 36 · 37 · 38 · 39 · 40 | Integração e automação |

As listas são publicadas **na semana da aula correspondente**.

---

## 🧰 Ferramentas

| Uso | Ferramenta |
|---|---|
| Testes | `pytest`, `pytest-cov`, `pytest-mock` |
| BDD / aceitação | `behave` ou `pytest-bdd` |
| API | `httpx`, `schemathesis` |
| Análise estática | `ruff`, `mypy`, `radon`, `bandit` |
| *Mutation testing* | `mutmut` |
| Carga | `locust` |
| *Property-based* | `hypothesis` |
| Comparação Java | JUnit 5 + JaCoCo (aulas 22 e 28) |

---

## 📖 Bibliografia

**Básica**
- PRESSMAN, R.; MAXIM, B. *Engenharia de Software: uma abordagem profissional*. 9ª ed.
- DELAMARO, M.; MALDONADO, J.; JINO, M. *Introdução ao Teste de Software*. 2ª ed.
- SOMMERVILLE, I. *Engenharia de Software*. 10ª ed.

**Complementar**
- BECK, K. *Test-Driven Development: By Example*
- CRISPIN, L.; GREGORY, J. *Agile Testing*
- MYERS, G. *The Art of Software Testing*. 3ª ed.
- ISO/IEC 25010 · ISO/IEC/IEEE 29119
- Syllabus **CTFL do ISTQB** (gratuito, em português) — <https://bstqb.org.br>
- SOFTEX. *Guia Geral MPS de Software* — <https://softex.br/mpsbr>

---

## 🤝 Colaboração e integridade

✅ **Permitido:** discutir ideias com colegas; consultar normas, livros e internet;
usar assistentes de IA **desde que** você declare o uso no `RESPOSTAS.md` e
**entenda** cada linha entregue.

❌ **Não permitido:** copiar análise ou código de outro aluno; **inventar achados,
defeitos ou métricas**; entregar artefato que você não consegue explicar.

> ⚠️ **Nesta UC, inventar um achado é a falta mais grave** — mais grave que
> errar. É exatamente o comportamento que a UA 7 estuda como violação de
> responsabilidade técnica. Achado fictício zera a entrega.

---

**Dúvidas?** Abra uma [Issue](../../issues) ou pergunte em sala.
