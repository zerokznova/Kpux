from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! 👋\nUse /cpf, /nome, /placa e outros comandos para consultar.\nExemplo: /nome Jair Messias Bolsonaro")
