# Exercício — Aula 01: O que é Qualidade de Software e por que ela Falha

**UC:** Garantia da Qualidade de Software — UNIFG 2026/2
**UA 1:** Fundamentos da Qualidade de Software
**Entrega:** até a véspera da Aula 02 — PR `[Aula 01] Seu Nome Completo`

> ⚠️ Em várias questões desta lista **não existe resposta única**. O que é
> avaliado é a **justificativa**. "Rigor do raciocínio" vale 30 dos 100 pontos.

---

## Parte A — Erro, defeito e falha (25 pontos)

Para cada situação, preencha a tabela identificando **erro**, **defeito** e
**falha**. Quando um dos três não estiver descrito, escreva "não descrito" e
diga **o que seria preciso investigar** para descobri-lo.

| # | Situação |
|---|---|
| A1 | A pessoa entendeu que "mês" começa em 0, como em algumas APIs, e escreveu `mes = data.month - 1`. Relatórios de janeiro saem vazios. |
| A2 | O sistema aceita CPF com 10 dígitos. Nenhum usuário reclamou. |
| A3 | Clicar duas vezes rapidamente em "Salvar" registra o empréstimo em duplicidade. |
| A4 | O requisito dizia "campo obrigatório". A tela permite salvar vazio. O banco tem 4.000 registros nulos. |
| A5 | Uma função tem complexidade ciclomática 31 e nenhum teste. Nunca deu problema em produção. |
| A6 | A senha do banco de dados está escrita no código-fonte, que está num repositório público. |
| A7 | Ao migrar para a versão nova da biblioteca de datas, o cálculo de multa passou a errar em 1 dia nos meses de 31 dias. |
| A8 | O sistema funciona perfeitamente, mas o requisito estava errado: a regra de multa aprovada pela diretoria não é a que a lei exige. |

*(3 pontos cada, 1 ponto pelo formato)*

**A9 (bônus dentro da parte).** Nos casos **A5** e **A8**, responda:

(a) No A5, **existe** um defeito? E existe um **problema de qualidade**? São a
mesma coisa? Justifique com as definições da aula.
(b) No A8, onde está o defeito — no código, no requisito, ou em nenhum dos dois?
O que essa resposta diz sobre o alcance do teste como técnica?

---

## Parte B — Definições de qualidade aplicadas (20 pontos)

Considere este requisito real de um sistema de biblioteca:

> *"O sistema deve calcular a multa por atraso na devolução."*

**B1 (8 pts).** Avalie o requisito pelas **quatro definições clássicas** de
qualidade (Crosby, Juran, ausência de deficiências, Weinberg). Para cada uma,
diga o que ela ilumina e o que ela deixa escapar **neste caso concreto**.

**B2 (7 pts).** Reescreva o requisito de forma **verificável**. Ele precisa
permitir que alguém escreva um caso de teste sem fazer nenhuma pergunta a
ninguém. Liste também as **necessidades implícitas** que você teve que tornar
explícitas.

**B3 (5 pts).** Liste **cinco** partes interessadas neste requisito e, para cada
uma, o que ela chamaria de "multa calculada com qualidade". Aponte pelo menos
**um conflito** real entre duas delas.

---

## Parte C — Implementação: a cobertura enganosa (30 pontos)

Você vai reproduzir, com código rodando, a demonstração do slide 4.3.

### Setup

```bash
cd exercicios/aula01
uv init --no-workspace . 2>/dev/null || true
uv add --dev pytest pytest-cov
```

**C1 (5 pts).** Crie `multa.py`:

```python
def calcular_multa(dias_atraso: int, valor_diario: float) -> float:
    """Multa por atraso na devolução. Sem atraso, sem multa."""
    if dias_atraso <= 0:
        return 0.0
    return dias_atraso * valor_diario
```

**C2 (7 pts).** Crie `test_multa_ruim.py` — um teste **sem nenhuma asserção** que
atinja **100% de cobertura**. Cole a saída de:

```bash
uv run pytest --cov=multa --cov-report=term-missing test_multa_ruim.py
```

**C3 (6 pts).** **Sabote** o `multa.py`: troque `*` por `+`. Rode o mesmo comando
e cole a saída. O teste passou? A cobertura mudou? Explique.

**C4 (8 pts).** Crie `test_multa_bom.py` com asserções de verdade, cobrindo no
mínimo:

- o caso de fronteira (`dias_atraso == 0`)
- um caso de atraso positivo
- um caso de `dias_atraso` negativo
- um caso com `valor_diario` fracionário

Demonstre que ele **falha** no código sabotado e **passa** no correto. Cole as
duas saídas.

**C5 (4 pts).** Escreva a tabela de casos que você usou em C4, com uma coluna
explicando **por que** cada caso está lá. *(Você acabou de fazer, informalmente,
partição de equivalência e análise de valor limite — as técnicas da Aula 15.)*

### 🤔 Reflexão obrigatória (sem pontos, mas zera a Parte C se ausente)

Se você fosse gestor e visse "cobertura: 100%" no painel, **qual segunda pergunta
você faria** antes de aprovar a liberação? Responda em 3 frases.

---

## Parte D — QA, QC e Teste (15 pontos)

Classifique cada atividade como **QA** (processo, preventivo), **QC** (produto,
detectivo) ou **Teste** (uma técnica de QC). Justifique em uma linha cada.

| # | Atividade |
|---|---|
| D1 | Exigir que todo PR tenha ao menos um revisor aprovando |
| D2 | Rodar `pytest` antes do merge |
| D3 | Definir que a equipe usará TDD em módulos de cálculo financeiro |
| D4 | Inspecionar o documento de requisitos antes de começar a codificar |
| D5 | Executar o roteiro de teste de aceitação com o cliente |
| D6 | Treinar a equipe em análise de valor limite |
| D7 | Rodar `ruff` e `mypy` no pipeline |
| D8 | Escolher o modelo de ciclo de vida do projeto |
| D9 | Medir a densidade de defeitos por release e discutir a tendência |
| D10 | Fazer teste exploratório por 2 horas numa funcionalidade nova |
| D11 | Escrever o template de relatório de defeito que a equipe usará |
| D12 | Verificar se a tela funciona no Firefox |

**D13 (3 pts).** Uma empresa tem uma equipe de 5 testadores que recebe o sistema
na última semana antes da entrega e executa roteiros manuais. A empresa chama
isso de "área de QA".

(a) Do ponto de vista da terminologia da aula, o que essa área faz de fato?
(b) Cite **duas** consequências previsíveis desse arranjo.
(c) Sugira **uma** mudança de baixo custo que moveria a organização na direção de
QA de verdade.

---

## Parte E — Análise de caso com parecer (10 pontos)

Retome o cenário da Prática em Sala 3: o aplicativo de agendamento de consultas
da rede pública, com os cinco problemas conhecidos (P1 a P5).

**E1 (4 pts).** Ordene os cinco por gravidade e **declare explicitamente o
critério** que você usou. O critério é o que vale nota, não a ordem.

**E2 (3 pts).** Para cada problema, indique a parte interessada prejudicada.

**E3 (3 pts).** Escreva o **parecer** de 5 a 8 linhas para a diretoria: liberar,
não liberar, ou liberar com ressalvas — com fundamento. Se recomendar liberar com
ressalvas, diga **quais** ressalvas e **qual prazo** para correção.

⚠️ Escreva como um profissional escreveria para a diretoria: sem drama, sem
jargão desnecessário, e **assumindo uma posição**. Parecer que não recomenda nada
não é parecer.

---

## Parte F — Bônus: primeiro contato com o sistema sob teste (+10 pontos)

O sistema que você vai auditar o semestre inteiro é o
[`sistema-biblioteca-qa`](https://github.com/petrosbarreto/sistema-biblioteca-qa).

```bash
git clone https://github.com/petrosbarreto/sistema-biblioteca-qa.git
cd sistema-biblioteca-qa
cat README.md
```

**F1.** Sem escrever nenhum teste ainda, apenas **lendo** o código e o histórico:

(a) Rode e cole:
```bash
git log --format= --name-only | sort | uniq -c | sort -rn | head -10
uv run radon cc . -s -a
uv run ruff check . | tail -20
```

(b) Liste os **3 módulos** que você suspeita serem os mais arriscados, com a
justificativa baseada nas evidências acima (frequência de alteração, complexidade,
achados de lint).

(c) Escolha **uma** função e escreva, em prosa, o que ela deveria fazer segundo o
nome e o código. Você consegue afirmar com certeza? O que está ambíguo?

> 💡 Isto é o embrião do **M1** da auditoria (Aula 10). Fazer agora te adianta.

---

## Entrega

```
exercicios/aula01/
├── RESPOSTAS.md            # Partes A, B, C5, D, E e F
├── multa.py                # Parte C
├── test_multa_ruim.py
├── test_multa_bom.py
└── evidencias/
    ├── cobertura-teste-ruim.txt
    ├── cobertura-sabotado.txt
    ├── teste-bom-falhando.txt
    └── teste-bom-passando.txt
```

## Rubrica

| Critério | Pontos |
|---|---|
| Corretude técnica | 35 |
| **Rigor do raciocínio** (justificativas) | 30 |
| Qualidade dos artefatos (reprodutíveis, com os comandos) | 25 |
| Clareza e comunicação | 10 |
| **Bônus F** | +10 |

---

## 🆘 Dicas

**Travou na Parte A?** Volte ao diagrama da cadeia causal e pergunte, em ordem:
houve ação humana equivocada? ela deixou marca no artefato? essa marca foi
executada e produziu comportamento errado observável?

**Travou na Parte C?** O truque do teste sem asserção é chamar a função e
**descartar** o retorno. O pytest só falha se houver `assert` falso ou exceção.

**Não sabe se seu parecer da Parte E está bom?** Leia em voz alta imaginando que
a diretoria está na sala. Se soar como reclamação, reescreva. Se não disser o que
fazer, reescreva.
