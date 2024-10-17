# module_5_hard.py
import time
import hashlib


class User:
    '''Каждый объект класса User должен обладать следующими атрибутами и методами:
Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)'''

    def __init__(self, nickname, password, age):
        # имя пользователя, строка
        self.nickname = str(nickname)

        # Пароль в хэшированном виде
        self.password = int(hash(password))

        # Возраст, число
        self.age = int(age)

    def __str__(self):
        return f'{self.nickname}'


class Video:
    '''Каждый объект класса Video должен обладать следующими атрибутами и методами:
Атрибуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
adult_mode(ограничение по возрасту, bool (False по умолчанию))'''

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        # Заголовок видео, строка
        self.title = str(title)

        # Продолжительность, секунды
        self.duration = int(duration)

        # Время просмотра, число
        self.time_now = int(time_now)

        # Ограничение по возрасту, логическое значение
        self.adult_mode = bool(adult_mode)

    def __str__(self):
        return f'{self.title} {self.duration} {self.time_now} {self.adult_mode}'


class UrTube:
    '''Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
 Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)'''

    def __init__(self):
        # Список объектов User
        self.users = []

        # Список объектов Video
        self.videos = []

        # Текущий пользователь
        self.current_user = None

    def log_in(self, nickname, password):
        '''Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users
        с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу.'''
        for user in self.users:
            if user.nickname == nickname and hash(user.password) == hash(password):
                self.current_user = User
        return self.current_user.nickname

    def register(self, nickname, password, age):
        '''Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
        если пользователя не существует (с таким же nickname). Если существует, выводит на экран:
        "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.'''
        if nickname not in [user.nickname for user in self.users]:
            self.users.append(User(nickname, password, age))
            self.current_user = User(nickname, password, age)
            return self.current_user.nickname
        else:
            print(f"Пользователь {nickname} уже существует")
        # for user_i in self.users:
        #     if nickname == user_i.nickname:
        #         print(f'Пользователь {nickname} уже существует')
        # if self.current_user is None:
        #     self.users.append(User(str(nickname), hash(password), int(age)))
        #     self.current_user = self.users[-1]
        #     return self.current_user.nickname

    def log_out(self):
        '''Метод log_out для сброса текущего пользователя на None.'''
        self.current_user = None
        return self.current_user.nickname

    def add(self, *Video):
        '''Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с
        таким же названием видео ещё не существует. В противном случае ничего не происходит.'''
        for video_i in Video:
            if video_i.title not in [v.title for v in self.videos]:
                self.videos.append(video_i)
        return self.videos

    def get_videos(self, search_word):
        '''Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
        содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best'
        (не учитывать регистр).'''
        list_video = []
        for video_seach in self.videos:
            if search_word.lower() in video_seach.title.lower():
                list_video.append(video_seach.title)
        return list_video

    def watch_video(self, title):
        '''Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
        то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается.
        Для метода watch_video так же учитывайте следующие особенности:
        Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
        Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль
        надпись: "Войдите в аккаунт, чтобы смотреть видео"
        Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
        Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
        После воспроизведения нужно выводить: "Конец видео"'''
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if self.current_user.age < 18 and video.adult_mode:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for second in range(video.time_now, video.duration + 1):
                    time.sleep(1)
                    print(second, end=' ')
                video.time_now = 0
                print("Конец видео")
                return
        print("Видео не найдено")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user) #Изменено от контрольного примера

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
