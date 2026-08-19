# Parte A — Erro, defeito e falha

## A1

- **Erro:** a pessoa interpretou incorretamente a representação dos meses.
- **Defeito:** o código `mes = data.month - 1` realiza um cálculo incorreto.
- **Falha:** os relatórios de janeiro ficam vazios.

A sequência causal é erro humano → defeito no código → falha observável.

## A2

- **Erro:** não descrito.
- **Defeito:** não descrito.
- **Falha:** não descrita.

É necessário investigar o requisito ou a regra de negócio que define o formato válido do CPF. Não é possível afirmar que 10 dígitos constituem um defeito sem essa evidência.

## A3

- **Erro:** não descrito.
- **Defeito:** o sistema não trata adequadamente solicitações duplicadas.
- **Falha:** o empréstimo é registrado em duplicidade.

O clique duplo é uma ação possível do usuário; o problema está no comportamento do sistema diante de duas solicitações.

## A4

- **Erro:** não descrito.
- **Defeito:** a implementação não garante o requisito de campo obrigatório.
- **Falha:** a tela permite salvar o campo vazio e são gerados registros nulos no banco.

## A5

- **Erro:** não descrito.
- **Defeito:** não há defeito funcional demonstrado apenas pelas informações fornecidas.
- **Falha:** não há falha observada.

Entretanto, existe um problema de qualidade e risco técnico: a complexidade ciclomática 31 dificulta a manutenção e os testes, e a ausência de testes reduz a capacidade de detectar defeitos.

## A6

- **Erro:** não descrito.
- **Defeito:** a senha do banco está exposta no código-fonte de um repositório público.
- **Falha:** não há falha de execução descrita, embora exista uma exposição de segurança.

## A7

- **Erro:** não descrito.
- **Defeito:** existe um problema na implementação/compatibilidade após a migração da biblioteca de datas.
- **Falha:** o cálculo da multa fica incorreto em um dia nos meses de 31 dias.

## A8

- **Erro:** houve um erro na definição/aprovação do requisito.
- **Defeito:** o requisito está incorreto, pois não corresponde à exigência legal.
- **Falha:** não há falha de execução descrita, pois o sistema funciona de acordo com o requisito fornecido.

## A9

### (a)

No caso A5, não é possível afirmar que existe um defeito funcional apenas pelas informações fornecidas, pois nenhum comportamento incorreto foi apresentado. Porém, existe um problema de qualidade e um risco técnico devido à alta complexidade e à ausência de testes.

Defeito e problema de qualidade não são necessariamente a mesma coisa. Um problema de qualidade pode representar um risco ou característica indesejável sem que exista uma falha funcional comprovada.

### (b)

No caso A8, o defeito está no requisito, pois a regra especificada não corresponde à exigência legal. O código pode estar funcionando corretamente em relação ao requisito fornecido.

Isso demonstra que testes não garantem, sozinhos, que os requisitos estejam corretos. Um teste pode verificar se o sistema implementa uma regra, mas, se a própria regra estiver errada, os testes podem passar e o produto continuar inadequado.
