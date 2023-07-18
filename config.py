import os
# token and urls
TOKEN = '5673447297:AAECWAeluUYYCt01FdilVwhz8jvJpu3Wp2s'
SELFIE_URL = 'https://ibb.co/YZLhP4n'
HIGH_SCHOOL = 'https://ibb.co/PWq2pvL'
REP_URL = 'https://github.com/jokkojja/yandex_testovoe'

#paths
VOICE_PATH = 'voice_data'
BABUSHKA = os.path.join(VOICE_PATH, 'babushka.ogg')
SQL = os.path.join(VOICE_PATH, 'sql.ogg')
LOVE_STORY = os.path.join(VOICE_PATH, 'love_story.ogg')

#texts
START_MESSAGE = ''.join(("Привет! Я помогу тебе познакомиться со мной поближе.",
                 "Если хочешь увидеть мое последнее селфи: напиши 'Селфи'.\n",
                 "Если фото из старшей школы: 'Старшая школа'.\n",
                 "Если хочешь узнать о моем главном увлечении: 'Увлечение'.\n",
                 "Также есть вариант выбрать что-нибудь из меню. Для этого просто тыкни сюда -----> /menu"))
HOBBY_TEXT = ''.join(('Мое главное увлечение - игра на гитаре. ' \
              'Это отличный способ расслабиться, отдонуть, выплеснуть все эмоции после тяжелого дня. ' \
              'К тому же это сильно помогает с утра разогнать свой мозг, просто начинаю лучше думать. ' \
              'Играйте на гитаре :)'))
HIGHT_SCHOOL_TEXT = 'Все фото со старшей школы были утеряны вместе со старым жестким диском, поэтому тут фотка в супер крутом малиновом пиджаке'
CHOOSE_VOICE_TEXT = 'Выбирай о чем хочешь послушать войс:'
NEXT_STEP_TEXT = 'Что-то про следующий шаг'
BABUSHKA_TEXT = 'Сказ про бабушку и ChatGPT'
SQL_TEXT = 'История противостояние SQL и NoSQL'
LOVE_TEXT = 'Лав стори'
REP_TEXT = 'Ссылка на реп к этому супер боту'
