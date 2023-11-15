
# Bot para alterar o tipo de filial

Este é um programinha simples que desenvolvi em um fim de semana simplesmente por tédio. Recentemente havia aprendido a utilizar o o telegram para enviar comandos para um projeto de automação que eu estava desenvolvendo utilizando ESP32. Aproveitei o embalo e achei interessante a ideia de usar o telegram para se conectar à um banco de dados e fazer alterações nele a partir de comandos. Não foi uma ideia super inovadora (e por razões internas o programa nem chegou a ser utilizado na empresa, apenas testado), mas obviamente serviu de bastante aprendizado, portanto, tempo bem investido!


## Objetivo desta aplicação

Esta aplicação tem por objetivo tornar mais fácil a alteração do tipo e filial no sitema winthor. Esta alteração é feita para que a equipe de compras da empresa possa fazer transferências entre as filiais.

##
Existem apenas dois tipos de filiais no sistema, CD (Centro de Distribuição) e Loja. De acorddo com as regras do sistema WinThor, somente pode ser feito transferências entre lojas e do CD para a loja, nunca no sentido inverso. Em situações em que é necessário realizar uma transferência de uma loja para o CD, é preciso alterar o tipo da filial de destino para loja no cadastro da mesma. A rotina que contém o cadastro dessas informações é bem complexa e possui muitas abas e informações, de forma que leva-se um certo tempo até chegar até esse cadastro específico e seja feito a alteração. Uma vez alterado, é feito a transferênciade mercadoria, e ao fim da transferência, é necessário alterar o tipo de filial para a informação original. Ao utilizar o telegram esse procedimento específico é facilitado, tendo em vista que basta apenas pegar o celular e enviar uma mensagem com o comando específico. 

## Bibliotecas utilizadas

Para este projeto foram utilizadas apenas duas bibliotecas: 
```bash
import telebot
import cx_Oracle
```
A biblioteca 'telebot' é responsável por interpretar os comandos enviados via telegram e executar as funções relacionadas à cada comando. Já a biblioteca 'cx_Oracle' é responsável por fazer a conexão com o banco de dados.

## Conectando ao banco de dados
Essa parte já foi uma dor de cabeça gigante quando eu tentei conectar uma aplicação à um banco oracle pela primeira vez. Sobre todos os problemas enfrentados relacionados à essa parte, vou deixar o link do repositório onde precisei aprender a fazer essa conexão.https://github.com/Sipauba/rotina-winthor-status-requisicao-material-de-consumo/blob/main/README.md

##
Primeiramente foi criado variáveis com todas as informações necessárias para fazer a conexão com o banco, como IP, nome do serviço, login  e senha.
```bash
host = 'x'
servico = 'x'
usuario = 'x'
senha = 'x'

# Encontra o arquivo que aponta para o banco de dados
cx_Oracle.init_oracle_client(lib_dir="./instantclient_21_10")

# Faz a conexão ao banco de dados
conecta_banco = cx_Oracle.connect(usuario, senha, f'{host}/{servico}')

# Cria um cursor no banco para que seja possível fazer consultas e alterações no banco de dados
cursor = conecta_banco.cursor()

```
É necessário baixar o client oracle (instantclient_21_10) no site da oracle e deixar na pasta junto com o arquivo deste programa.

## Aplicando o Bot ao telegram
Existem diversos tutoriais na internet que ensinam como criar o bot e configura-lo. Basicamente adicionei o BotFather no meu telegram e apartir dele eu criei o meu bot. A partir disso apenas precisei do token gerado na criação do Bot. Este token é como uma chave única que identifica o bot especificamente.
```bash
# Este token é específico do bot criado
TOKEN = '6418781436:AAE8hyxEjX-TjZec0ghGQVArNXAv6Vulcaw'
```
Em seguida é criado uma variável para conectar o bot ao telegram. Esta variável será utilizada em cada função no código

```bash
# Crie uma instância do bot
bot = telebot.TeleBot(TOKEN)
```
Para esta aplicação, o bot foi incluido em um grupo com os integrantes que enviariam os comandos. Os comandos só funcionam no grupo em que o Bot está inserido.

## Criando os comandos

A função abaixo é um exemplo das funções criadas para todo o código. A única diferença é o valor contido entre os colchetes, que será o gatilho para executar o comando (exatamente o que precisa ser digitado após a / no telegram), e o código em SQL que será executado no banco.

```bash
# Comando /6cd
@bot.message_handler(commands=['6cd'])
def cd6(message):
    cursor.execute('update pcfilial set tipofilial = 1 where codigo = 6')
    cursor.execute('commit')
    bot.send_message(message.chat.id, "Filial 6 configurada como CD.")
```
## Instruções aos usuários e traatamento de erros

Ao iniciar o bot é informado aos usuários do grupo que o comando /help  possui as informações sobre como dar os comandos so bot.
```bash
# Comando /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Bot iniciado. Digite /help para ver os comandos.")
```
```bash
# Comando /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Aqui estão os comandos disponíveis:\n\n"
                                      "O comando consiste em digitar / seguido do número da filial e o tipo, se Loja ou CD \n"
                                      "Exemplos: /6loja /4cd /20loja \n"
                                      "/start - Iniciar o bot\n"
                                      "/help - Exibir esta mensagem de ajuda\n"
                                      "/info - Exibir informações do usuário")
```
Se o usuário inserir um comando errado ou inexistente, ele ativará uma função que irá informar que o comando digitado é inexistente.

```bash
# Lidar com mensagens de texto não comandos
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.send_message(message.chat.id, "Comando inexistente. Digite /help para ver os comandos disponíveis.")
```

# Conclusão
Com esta aplicação é possível salvar um pouco de tempo no processo de alteração do tipo de filial, tendo em vista que pelo próprio sistema o prcesso é um pouco mais oneroso. Também é possível atribuir essa atividade de trocar o tipo de filial para um grupo seleto de pessoas, já que pelo sistema não é possível restringir a rotina de cadastro de filiais para que o usuário faça apenas a alteração do tipo de filial.
