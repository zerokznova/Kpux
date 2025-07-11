from telegram import Update
from telegram.ext import ContextTypes
from api.consultas_api import buscar_dados

async def processar_consulta(update: Update, context: ContextTypes.DEFAULT_TYPE, comando: str):
    if not context.args:
        await update.message.reply_text(f"❌ Use corretamente: /{comando} <dado>")
        return

    valor = " ".join(context.args)
    await update.message.reply_text(f"🔎 Consultando {comando.upper()}...")

    resultado = buscar_dados(comando, valor)

    if isinstance(resultado, dict):
        if "error" in resultado:
            await update.message.reply_text(f"🔹 error: {resultado['error']}")
        else:
            mensagem = "\n".join(f"{k}: {v}" for k, v in resultado.items())
            await update.message.reply_text(f"🔍 Resultado:\n\n{mensagem}")
    else:
        await update.message.reply_text("⚠️ Erro ao processar a resposta.")

# Handlers específicos
async def cpf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await processar_consulta(update, context, "cpf")

async def nome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await processar_consulta(update, context, "nome")

async def placa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await processar_consulta(update, context, "placa")

async def cnpj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await processar_consulta(update, context, "cnpj")
