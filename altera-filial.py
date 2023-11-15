import telebot
import cx_Oracle

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

# Este token é específico do bot criado
TOKEN = '6418781436:AAE8hyxEjX-TjZec0ghGQVArNXAv6Vulcaw'

# Crie uma instância do bot
bot = telebot.TeleBot(TOKEN)

# Comando /6cd
@bot.message_handler(commands=['6cd'])
def cd6(message):
    cursor.execute('update pcfilial set tipofilial = 1 where codigo = 6')
    cursor.execute('commit')
    bot.send_message(message.chat.id, "Filial 6 configurada como CD.")

# Comando /6loja
@bot.message_handler(commands=['6loja'])
def cd6(message):
    cursor.execute('update pcfilial set tipofilial = 2 where codigo = 6')
    cursor.execute('commit')
    bot.send_message(message.chat.id, "Filial 6 configurada como LOJA.")
    
# Comando /3cd
@bot.message_handler(commands=['3cd'])
def cd6(message):
    cursor.execute('update pcfilial set tipofilial = 1 where codigo = 3')
    cursor.execute('commit')
    bot.send_message(message.chat.id, "Filial 3 configurada como CD.")
    
# Comando /3loja
@bot.message_handler(commands=['3loja'])
def cd6(message):
    cursor.execute('update pcfilial set tipofilial = 2 where codigo = 3')
    cursor.execute('commit')
    bot.send_message(message.chat.id, "Filial 3 configurada como LOJA.")
    
# Comando /4cd
@bot.message_handler(commands=['4cd'])
def cd6(message):
    cursor.execute('update pcfilial set tipofilial = 1 where codigo = 4')
    cursor.execute('commit')
    bot.send_message(message.chat.id, "Filial 4 configurada como CD.")
    
# Comando /4loja
@bot.message_handler(commands=['4loja'])
def cd6(message):
    cursor.execute('update pcfilial set tipofilial = 2 where codigo = 4')
    cursor.execute('commit')
    bot.send_message(message.chat.id, "Filial 4 configurada como LOJA.")
    
# Comando /5cd
@bot.message_handler(commands=['5cd'])
def cd6(message):
    cursor.execute('update pcfilial set tipofilial = 1 where codigo = 5')
    cursor.execute('commit')
    bot.send_message(message.chat.id, "Filial 5 configurada como CD.")
    
# Comando /5loja
@bot.message_handler(commands=['5loja'])
def cd6(message):
    cursor.execute('update pcfilial set tipofilial = 2 where codigo = 5')
    cursor.execute('commit')
    bot.send_message(message.chat.id, "Filial 5 configurada como LOJA.")
    
# Comando /20cd
@bot.message_handler(commands=['20cd'])
def cd6(message):
    cursor.execute('update pcfilial set tipofilial = 1 where codigo = 20')
    cursor.execute('commit')
    bot.send_message(message.chat.id, "Filial 20 configurada como CD.")
    
# Comando /20loja
@bot.message_handler(commands=['20loja'])
def cd6(message):
    cursor.execute('update pcfilial set tipofilial = 2 where codigo = 20')
    cursor.execute('commit')
    bot.send_message(message.chat.id, "Filial 20 configurada como LOJA.")
    
# Comando /70cd
@bot.message_handler(commands=['70cd'])
def cd6(message):
    cursor.execute('update pcfilial set tipofilial = 1 where codigo = 70')
    cursor.execute('commit')
    bot.send_message(message.chat.id, "Filial 70 configurada como CD.")
    
# Comando /70loja
@bot.message_handler(commands=['70loja'])
def cd6(message):
    cursor.execute('update pcfilial set tipofilial = 2 where codigo = 70')
    cursor.execute('commit')
    bot.send_message(message.chat.id, "Filial 70 configurada como LOJA.")

# Comando /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Bot iniciado. Digite /help para ver os comandos.")

# Comando /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Aqui estão os comandos disponíveis:\n\n"
                                      "O comando consiste em digitar / seguido do número da filial e o tipo, se Loja ou CD \n"
                                      "Exemplos: /6loja /4cd /20loja \n"
                                      "/start - Iniciar o bot\n"
                                      "/help - Exibir esta mensagem de ajuda\n"
                                      "/info - Exibir informações do usuário")

# Comando /info
@bot.message_handler(commands=['info'])
def handle_info(message):
    user = message.from_user
    bot.send_message(message.chat.id, f"Nome: {user.first_name}\n"
                                      f"Sobrenome: {user.last_name}\n"
                                      f"ID do usuário: {user.id}")

# Lidar com mensagens de texto não comandos
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.send_message(message.chat.id, "Comando inexistente. Digite /help para ver os comandos disponíveis.")

# Iniciar o bot
if __name__ == "__main__":
    bot.polling(none_stop=True)
