# Desafio Teste
Olá, queremos convidá-lo a participar de nosso desafio de seleção. Pronto para participar? Seu trabalho será visto por nosso time e você receberá ao final um feedback sobre o que achamos do seu trabalho. Não é legal?

## Sobre a Oportunidade
A vaga é para Analista de Sistemas/Programador, se você for aprovado nesta etapa, será convidado para uma entrevista com nosso time de especialistas. Orientações:

* Você pode utilizar alguma das seguintes linguagens (Ruby on Rails, PHP, Python ou Java);
* Você pode utilizar algum dos seguintes bancos de dados (SQLite, PostgreSQL, MySQL)

## Desafio Técnico
A empresa especializada na prestação de serviços, e nada melhor que um bom sistema de gestão de serviços executados:

### Pré-Requisitos
Criar um sistema para cadastro de ordem de serviço que possua:

* Criação, edição, exclusão e listagem de serviços;
* Criação, edição, exclusão e listagem de ordens de serviço;
* Relatório para contabilização dos serviços realizados e respectivos valores.

#### Campo para Serviço
| Campo   | Tipo    | Obrigatório | Observação |
| --------|---------|-------|-------|
| descricao | Texto   |  Sim | Descrição do serviço |
| valor | Monetário   |  Sim | Valor cobrado pela unidade do serviço |


#### Campo para Ordem de Serviço
Obs.: Uma ordem de serviço possui apenas um único serviço

| Campo           | Tipo     | Obrigatório | Observação |
| -------- |--------- |------- |------- |
| serviço         | Serviço  | Sim         | Serviço executado na ordem de serviço |
| quantidade      | Numérico | Sim         | Quantidade do serviço executado. Mínimo 1 |
| nomeFuncionario | Texto    | Sim         | Nome do funcionário que executou a ordem de serviço |
| data            | Data     | Sim         | Data da execução da ordem de serviço |
| horaInicio      | Hora     | Sim         | Hora de início da execução da ordem de serviço |
| horaFim         | Hora     | Sim         | Hora de término da execução da ordem de serviço |
| detalhe         | Texto    | Não         | Detalhes adicionais sobre a ordem de serviço |


#### Relatório de Contabilização dos Serviços
Página que deve exibir uma tabela que agrupe todos os serviços executados nas ordens de serviço e as respectivas quantidades e valores. 
A contabilização dos serviços possuem as regras:

1. A cada 10 unidades de um serviço, esse serviço recebe 10% de desconto.
2. O desconto máximo que um serviço pode receber é de 30%

Exemplo tabela:

| Serviço | Valor Unitário | Qtd | Valor Total | Desconto | Valor Final|
| -------- |--------- |------- |------- |------- |------- |
| Corte de energia     | R$45,00 | 15 |   R$675,00 | 10% |   R$607,50 |
| Inspeção             | R$20,00 |  8 |   R$160,00 |  0% |   R$160,00 |
| Religação de energia | R$30,00 | 50 | R$1,500,00 | 30% | R$1.050,00 |
| TOTAL                |         |    | R$2.335,00 |     | R$1.817,50 |


### Escopo Mínimo

* Listagem de serviços cadastrados
* Criação e edição de serviços
* Exclusão de serviços
* Listagem das ordens de serviços cadastradas
* Criação e edição de ordem de serviço
* Exclusão de ordem de serviço
* Exibição do relatório de contabilização dos serviços
* Testes automatizados
* Elaborar um manual de execução da aplicação


### Diferenciais

* Utilização de algum framework de layout (bootstrap, materialize, etc)
* Implementar autenticação


### Instruções

1. Faça o fork do desafio;
2. Crie um repositório privado no bitbucket para o projeto e adicione como colaborador o usuário sistemas_teste;
3. Desenvolva no prazo combinado;
4. Após concluir seu trabalho faça um push; 
5. Responda ao e-mail enviado do desafio, adicionando cópia para sistemas@teste.com.br notificando a finalização do desafio para validação.

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Entre no diretório
* Instale as dependências.
* Rode as migrações.

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
