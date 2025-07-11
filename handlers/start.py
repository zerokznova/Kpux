async def start(update, context):
    await update.message.reply_text(
        "Olá! 👋\nUse /cpf, /nome, /placa e outros comandos para consultar.\n"
        "Exemplo: /nome Jair Messias Bolsonaro"
    )
