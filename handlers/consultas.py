from api.consultas_api import buscar_dados

def consulta_generica(update, context, base, comando):
    query = ' '.join(context.args).strip()
    if not query:
        update.message.reply_text(f"❌ Use corretamente: /{comando} <dado>")
        return
    update.message.reply_text(f"🔎 Consultando {comando.upper()}...")
    resultado = buscar_dados(base, query)
    update.message.reply_text(resultado)

def cpf(update, context):
    consulta_generica(update, context, "cpf", "cpf")

def cnpj(update, context):
    consulta_generica(update, context, "cnpj", "cnpj")

def placa(update, context):
    consulta_generica(update, context, "placa", "placa")

def nome(update, context):
    consulta_generica(update, context, "nome", "nome")
