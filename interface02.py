import yt_dlp
import customtkinter as ctk
from tkinter import filedialog
import os


def mp3down():
    
    url = campo_url.get()

    pasta = filedialog.askdirectory()

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
        'outtmpl': os.path.join(pasta, '%(title)s.%(ext)s')
                }

    with yt_dlp.YoutubeDL(ydl_opcoes) as ydl:
        ydl.download([url])

    resultado_download.configure(text='Download finalizado', text_color='green')


# Aparência 
ctk.set_appearance_mode('dark') # coloca no modo dark

# Criação da janela

app = ctk.CTk()         # Cria a janela
app.title("MP3 DOWN")   # Título da janela
app.geometry('300x350') # Tamanho da janela

# Criação dos campos

# Label mp3down
label_mp3down = ctk.CTkLabel(app,text='MP3 DOWN')
label_mp3down.pack(pady=10)

# Label url
label_url = ctk.CTkLabel(app, text='URL:')
label_url.pack(pady=10)

# Campo url
campo_url = ctk.CTkEntry(app,placeholder_text="Insira a URL")
campo_url.pack(pady=10)

# Botão baixar
botao_baixar = ctk.CTkButton(app,text='Baixar', command=mp3down)
botao_baixar.pack(pady=10)

# Campo feedback
resultado_download = ctk.CTkLabel(app, text='')
resultado_download.pack(pady=10)

app.mainloop() #Inicia a janela

