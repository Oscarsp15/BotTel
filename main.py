import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TOKEN
from handlers.user_handlers import start, track_interaction, nivel_command, welcome
from handlers.admin_handlers import erase
from models.database import create_tables


# Crear las tablas si no existen
create_tables()

# Configurar el log
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

def main():
    # Inicializar el bot
    application = Application.builder().token(TOKEN).build()

    # Registrar los manejadores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("nivel", nivel_command))
    application.add_handler(CommandHandler("erase", erase)) 
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))


    # Manejador de interacciones
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, track_interaction))

    # Manejar los nuevos miembros que se unen al grupo

    # Iniciar el bot
    application.run_polling()

if __name__ == "__main__":
    main()
