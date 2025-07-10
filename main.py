from telegram.ext import Application, CommandHandler
from handlers.start import start
from handlers.consultas import (
    cpf, cnpj, nome, rg, cpfsimpl, rgsimpl, pis, titulo,
    telefone, email, cns, mae, pai, placa, chassi,
    renavam, motor, fotorj, fotosp, funcionarios, razao
)

TOKEN = "7794910663:AAFvwakiaQ3muTSClhDfNa3rRN78YTD-ArU"

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cpf", cpf))
    app.add_handler(CommandHandler("cnpj", cnpj))
    app.add_handler(CommandHandler("nome", nome))
    app.add_handler(CommandHandler("rg", rg))
    app.add_handler(CommandHandler("cpfsimpl", cpfsimpl))
    app.add_handler(CommandHandler("rgsimpl", rgsimpl))
    app.add_handler(CommandHandler("pis", pis))
    app.add_handler(CommandHandler("titulo", titulo))
    app.add_handler(CommandHandler("telefone", telefone))
    app.add_handler(CommandHandler("email", email))
    app.add_handler(CommandHandler("cns", cns))
    app.add_handler(CommandHandler("mae", mae))
    app.add_handler(CommandHandler("pai", pai))
    app.add_handler(CommandHandler("placa", placa))
    app.add_handler(CommandHandler("chassi", chassi))
    app.add_handler(CommandHandler("renavam", renavam))
    app.add_handler(CommandHandler("motor", motor))
    app.add_handler(CommandHandler("fotorj", fotorj))
    app.add_handler(CommandHandler("fotosp", fotosp))
    app.add_handler(CommandHandler("funcionarios", funcionarios))
    app.add_handler(CommandHandler("razao", razao))

    print("🤖 Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
