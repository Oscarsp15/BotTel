from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from models.user_model import get_user, create_user, update_interactions, update_level
from models.level_model import get_role
import asyncio
import random

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not get_user(user.id):
        create_user(user.id, user.full_name)
    await update.message.reply_text(f"¡Hola {user.full_name}! ¡Bienvenido al bot de niveles!")

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for new_user in update.message.new_chat_members:
        # Verificar si el usuario tiene un username
        if new_user.username:
            mention = f"@{new_user.username}"
        else:
            # Si no tiene username, mencionarlo por su nombre sin @
            mention = new_user.full_name or new_user.first_name

        # Elegir una imagen de bienvenida aleatoriamente
        image_filename = f"assets/welcome_images/welcome{random.choice([1, 2, 3, 4, 5])}.jpg"
        
        # Envía la imagen de bienvenida
        with open(image_filename, 'rb') as photo:
            await context.bot.send_photo(
                chat_id=update.message.chat_id, 
                photo=photo, 
                caption=f"¡Bienvenido {mention}, esperamos que disfrutes tu estancia aquí!",
                parse_mode=ParseMode.HTML  # Usamos HTML para permitir menciones correctas
            )


async def track_interaction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_name = update.effective_user.full_name
    
    user = get_user(user_id)
    
    if not user:
        create_user(user_id, user_name)
        user = (user_id, user_name, 1, 0)
    
    interactions = user[3] + 1
    level = user[2]
    
    # Subir un nivel cada 10 interacciones
    if interactions % 10 == 0:
        level += 1
        update_level(user_id, level)
        update_interactions(user_id, interactions)
        
        # Cambiar de rol cada 10 niveles
        if level % 10 == 0:
            role_name, _ = get_role(level)  # Extrae solo el nombre del rol
            await update.message.reply_text(f"¡Felicidades {user_name}! ¡Has alcanzado el nivel {level} y ahora eres {role_name}!")
        else:
            await update.message.reply_text(f"¡Felicidades {user_name}! ¡Has alcanzado el nivel {level}!")
    else:
        update_interactions(user_id, interactions)



    # Log de la interacción
    print(f"User {user_name} has {interactions} interactions and is at level {level}.")



async def nivel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = get_user(user_id)

    if not user:
        await update.message.reply_text("¡Aún no tienes nivel! Comienza a interactuar para subir de nivel.")
        return

    level = user[2]
    role, _ = get_role(level)
    
    # Crear el texto de nivel
    caption = f"Estás en el nivel {level} y eres un {role}."
    
    # Si el rol es "Pollito Bebé", enviar el GIF con el texto como caption
    if role == "Pollito Bebé":
        gif_path = "assets/user_levels/level0.gif"
        try:
            message = await update.message.reply_animation(animation=open(gif_path, 'rb'), caption=caption)
            # Esperar 5 segundos antes de eliminar el mensaje
            await asyncio.sleep(5)
            await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=message.message_id)
        except Exception as e:
            await update.message.reply_text(f"Error al enviar el GIF: {e}")
    else:
        # Si no es "Pollito Bebé", solo envía el mensaje de texto
        message = await update.message.reply_text(caption)
        # Esperar 5 segundos antes de eliminar el mensaje
        await asyncio.sleep(10)
        await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=message.message_id)


