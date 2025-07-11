from telegram.ext import Updater, CommandHandler
from handlers.start import start
from handlers.consultas import cpf, cnpj, placa, nome

TOKEN ="7794910663:AAFvwakiaQ3muTSClhDfNa3rRN78YTD-ArU"

def main():
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))  
dp.add_handler(CommandHandler("cpf", cpf))  
dp.add_handler(CommandHandler("cnpj", cnpj))  
dp.add_handler(CommandHandler("placa", placa))  
dp.add_handler(CommandHandler("nome", nome))  

print("🤖 Bot rodando...")  
updater.start_polling()  
updater.idle()

if name == "main":
main()

