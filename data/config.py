# from environs import Env

# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()

# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili

# ADMINS=['486178287']
# BOT_TOKEN='5382365025:AAEulPbA2A2yHPD-2iXRDYBAaSt2oKtlTk0'
# ip='localhost'


import os

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))  # Bot token
ADMINS = list(os.environ.get("ADMINS"))  # adminlar ro'yxati
IP = str(os.environ.get("ip"))  # Xosting ip manzili
