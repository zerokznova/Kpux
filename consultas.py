from telegram import Update
from telegram.ext import ContextTypes
from api.consultas_api import consultar_api

comandos = [
    "cpf", "cnpj", "nome", "rg", "cpfsimpl", "rgsimpl", "pis", "titulo",
    "telefone", "email", "cns", "mae", "pai", "placa", "chassi", "renavam",
    "motor", "fotorj", "fotosp", "funcionarios", "razao"
]

for cmd in comandos:
    exec(f"""
async def {cmd}(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Use corretamente: /{cmd} <dado>")
        return
    termo = ' '.join(context.args)
    await update.message.reply_text(f"🔎 Consultando {cmd.upper()}...")
    resultado = consultar_api(base="{cmd}", info=termo)
    await update.message.reply_text(resultado)
    """)
