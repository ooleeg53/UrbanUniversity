from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title.lower()
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None
        self.word = None
        self.nickname = None
        self.password = None
        self.age = None

    def log_in(self, nickname, password):
        for key in self.users.keys():
            if key == nickname:
                for value in self.users.values():
                    if hash(value) == hash(password):
                        self.nickname = nickname
                        self.password = password
                        self.current_user = self.nickname

    def register(self, nickname, password, age):
        if nickname in self.users.keys():
            print(f'Пользователь {nickname} уже существует.')
        else:
            self.nickname = nickname
            self.password = password
            self.age = age
            self.users[self.nickname] = {self.password, self.age}
            self.current_user = self.nickname

    def log_out(self):
        self.current_user = None
        self.password = None
        self.age = None

    def add(self, *video):
        for i in video:
            if i not in self.videos:
                self.videos[i.title] = {'duration': i.duration, 'time_now': i.time_now, 'adult_mode': i.adult_mode}
            else:
                continue

    def get_videos(self, word):
        self.word = word.lower()
        list_video = []
        for video in self.videos:
            if self.word in video:
                list_video.append(video)
        return list_video

    def watch_video(self, name):
        if name.lower() not in self.videos.keys():
            return
        else:
            if self.current_user is None:
                return print('войдите в аккаунт, чтобы смотреть видео')
            elif name.lower() in self.videos.keys():
                if self.videos[name.lower()]["adult_mode"] is True and self.age < 18:
                    return print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for i in range(1, self.videos[name.lower()]['duration'] + 1):
                        print(i, end=' ')
                        sleep(1)
                    print('конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
