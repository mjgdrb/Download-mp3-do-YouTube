import yt_dlp


print('''
\t====  MP3 DOWN! ====
''')

url = input("INSIRA A URL: ")

ydl_opcoes = {
    'js_runtimes': {'node': {}},
    'format' : 'bestaudio/best',
    'postprocessors' : 
    [
        {
        'key':'FFmpegExtractAudio',
        'preferredcodec':'mp3',
        'preferredquality': '192',
        }
    ],
    'outtmpl':'pasta_musicas/%(title)s.%(ext)s'
            }

with yt_dlp.YoutubeDL(ydl_opcoes) as ydl:
    ydl.download([url])

print("\nDownload finalizado!")