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

# Comando /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Olá! Eu sou um bot de exemplo. Digite /help para ver os comandos disponíveis.")

# Comando /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Aqui estão os comandos disponíveis:\n\n"
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
    bot.send_message(message.chat.id, "Eu só respondo a comandos. Digite /help para ver os comandos disponíveis.")

# Iniciar o bot
if __name__ == "__main__":
    bot.polling(none_stop=True)
