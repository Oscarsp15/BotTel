from telegram import Update
from telegram.ext import ContextTypes

async def erase(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Borra los últimos 100 mensajes en el chat o en el tema específico."""
    chat_id = update.effective_chat.id
    message_id = update.message.message_id
    
    # Asegúrate de que el bot tiene los permisos necesarios
    bot_member = await context.bot.get_chat_member(chat_id, context.bot.id)
    if bot_member.can_delete_messages:
        try:
            # Elimina un rango de mensajes recientes (por ejemplo, los últimos 100 mensajes)
            for msg_id in range(message_id, message_id - 100, -1):
                try:
                    await context.bot.delete_message(chat_id, msg_id)
                except Exception as e:
                    # Algunos mensajes podrían no ser eliminables, ignora esos errores y continúa
                    print(f"No se pudo eliminar el mensaje {msg_id}: {e}")
            
            await update.message.reply_text("¡Los últimos 100 mensajes han sido borrados!")
        except Exception as e:
            await update.message.reply_text(f"Error al intentar borrar los mensajes: {e}")
    else:
        await update.message.reply_text("No tengo permisos para borrar mensajes en este chat.")

