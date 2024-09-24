```
telegram_bot/
│
├── main.py                      # Archivo principal que inicia el bot
├── config.py                    # Configuraciones generales y variables de entorno
├── handlers/
│   ├── __init__.py              # Hace que el directorio se considere un paquete Python
│   ├── admin_handlers.py        # Comandos y funcionalidades específicas para administradores
│   ├── user_handlers.py         # Comandos generales y funcionalidades para usuarios
│   ├── level_handlers.py        # Comandos y funcionalidades específicas para niveles avanzados (ej: Pollito Aventurero)
├── models/
│   ├── __init__.py              # Hace que el directorio se considere un paquete Python
│   ├── database.py              # Configuración y conexión con SQLite
│   ├── user_model.py            # Operaciones CRUD para la tabla de usuarios
│   ├── level_model.py           # Operaciones relacionadas con los niveles y roles
├── assets/
│   ├── level0.gif               # Archivo GIF u otros recursos estáticos que uses
│   ├── ...                      # Otros recursos como imágenes, audios, etc.
└── README.md                    # Instrucciones sobre cómo configurar y usar el bot

´´´