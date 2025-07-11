from telegram.ext import ApplicationBuilder, CommandHandler
from handlers.start import start
from handlers.consultas import cpf, cnpj, placa, nome

TOKEN = "7794910663:AAFvwakiaQ3muTSClhDfNa3rRN78YTD-ArU"

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cpf", cpf))
    app.add_handler(CommandHandler("cnpj", cnpj))
    app.add_handler(CommandHandler("placa", placa))
    app.add_handler(CommandHandler("nome", nome))

    print("🤖 Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
