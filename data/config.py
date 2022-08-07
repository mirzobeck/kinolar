from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "Bot_token"  # Bot toekn
ADMINS = [adminning telegram id]  # adminlar ro'yxati
CHANNELS = []
