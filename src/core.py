from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from conf.settings import TELEGRAM_TOKEN, HTTP_CATS_URL


def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Oi " + update.message.chat.first_name + " tudo bem?"
    )
    bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open('./quem.jpg','rb')
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text="eu sou o Bruce, sou um doguinho aqui de Bauru, digite /help para a lista de comandos"
    )


def unknown(bot, update):
    response_message = "Desculpe, não te entendi! :/"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )
    bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open('./ops.jpg','rb')
    )

def help(bot, update): 
    response_message = "Lista de comandos disponiveis: \n\n\
    /historia para saber um pouco sobre mim"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def historia(bot, update): 
    response_message = "Eu nasci no natal de 2017, e sou a mistura de um pastor e um vira lata, segue a minha foto"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )
    bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open('./lindo.jpg','rb')
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Minha mãe infelizmente já morreu! E o meu é pai está na foto comigo, e ele é muito ciumento!!'
    )
    bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open('./familia.jpg','rb')
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Os meus donos são o Leo (meu favorito), a Carol, o Paulo e a Andreia, vou mostrar eles pra vocês também'
    )
    bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open('./donos.jpg','rb')
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text='E eu adoro passear!!'
    )

def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('help', help)
    )
    dispatcher.add_handler(
        CommandHandler('historia', historia)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()