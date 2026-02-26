import yt_dlp


def download_youtube_content():
    url = input("Ссылка на ютуб видео: ")

    print("\n Выбираем в каком формате нам нужно скачать")
    print("1 - оригинальное видео с ютуба")
    print("2 - только аудио файл")
    print("3 - только видео(без звука!)")

    choice = input("\n вводим цифру, под которой указан нужный формат(1, 2 или 3): ")

    #настройки
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  #имя файла ютуб
        'quiet': False,  #полоска загрузки
    }

    if choice == '1':
        #скачивает видео+аудио и упаковывает в мп4
        ydl_opts.update({
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'merge_output_format': 'mp4',
        })
    elif choice == '2':
        #извлекает аудио и конвертирует в мп3
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '0',
            }],
        })
    elif choice == '3':
        #скачивает только видео в мп4 без звука
        ydl_opts.update({
            'format': 'bestvideo[ext=mp4]/bestvideo',
            'merge_output_format': 'mp4',
        })
    else:
        print("ошибка:неверный выбор")
        return

    try:
        print("\n начало загрузи")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n выполнено успешно, файл в папке проекта")
    except Exception as e:
        print(f"\n ошибка при скачивании: {e}")


if __name__ == "__main__":
    download_youtube_content()
