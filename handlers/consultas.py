from api.consultas_api import buscar_dados

async def consulta_generica(update, context, base, comando):
    query = ' '.join(context.args).strip()
    if not query:
        await update.message.reply_text(f"❌ Use corretamente: /{comando} <dado>")
        return
    await update.message.reply_text(f"🔎 Consultando {comando.upper()}...")
    resultado = buscar_dados(base, query)
    await update.message.reply_text(resultado)

async def cpf(update, context):
    await consulta_generica(update, context, "cpf", "cpf")

async def cnpj(update, context):
    await consulta_generica(update, context, "cnpj", "cnpj")

async def placa(update, context):
    await consulta_generica(update, context, "placa", "placa")

async def nome(update, context):
    await consulta_generica(update, context, "nome", "nome")
