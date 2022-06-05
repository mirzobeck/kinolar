from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5345828167:AAFq3eqtoqZUsbNJCZ26M4TstZKCO54OB10"  # Bot toekn
ADMINS = [1361526026,833102457]  # adminlar ro'yxati
CHANNELS = []
# try:
#     for i in db.get_channel():
#         CHANNELS.append(i[0])
# except:
#     pass
