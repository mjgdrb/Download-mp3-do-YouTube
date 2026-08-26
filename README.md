Aqui está uma versão do seu **README.md** totalmente reformatada em Markdown moderno, estruturada e visualmente atraente para o GitHub:

---

# 🎵 MP3DOWN

Uma ferramenta em Python para download e conversão de áudios do YouTube para formato **MP3**, com opção de linha de comando (CLI) ou interface gráfica (GUI).

---

## ⚠️ Isenção de Responsabilidade (Disclaimer)

* 🚨 **Fins Educacionais:** Este software foi desenvolvido exclusivamente para fins de estudo, aprendizado de programação e backup pessoal de conteúdos aos quais o usuário já possui direito de acesso ou que estejam sob licenças livres (como *Creative Commons* ou domínio público).
* 🚨 **Direitos Autorais:** O autor não apoia, incentiva ou tolera a pirataria ou a violação de direitos autorais.
* 🚨 **Responsabilidade do Usuário:** O uso desta ferramenta é de total e exclusiva responsabilidade do usuário, cabendo a este respeitar os **Termos de Serviço** das plataformas e as leis de propriedade intelectual vigentes em seu país.

---

## 🛠️ Pré-requisitos

Para que o projeto funcione corretamente, você precisará ter os seguintes utilitários instalados no seu sistema operacional:

* **Python 3.x**
* **[FFmpeg](https://ffmpeg.org/)** (necessário para a conversão de áudio para `.mp3`)
* **[Node.js](https://nodejs.org/)** (necessário para a execução de rotinas JS do YouTube pelo `yt-dlp`)

---

## 📦 Dependências do Python

Instale as bibliotecas necessárias executando o comando abaixo no seu terminal:

```bash
pip install yt-dlp customtkinter

```

---

## 🚀 Como Usar

O projeto possui duas formas de execução:

### 1. Linha de Comando (`main.py`)

Execução simples via terminal.

```bash
python main.py

```

> **Nota:** O script criará automaticamente uma pasta chamada `pasta_musicas` no mesmo diretório para salvar seus arquivos MP3.

### 2. Interface Gráfica (`interface01.py`)

Execução com interface visual intuitiva desenvolvida em CustomTkinter.

```bash
python interface01.py

```

> **Nota:** Os arquivos baixados através da interface gráfica também serão salvos automaticamente na pasta `pasta_musicas`.

---

## 🧰 Tecnologias Utilizadas

* **[Python](https://www.python.org/)** — Linguagem principal
* **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** — Download e extração das mídias
* **[FFmpeg](https://ffmpeg.org/)** — Processamento e conversão dos arquivos de áudio
* **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** — Interface gráfica moderna
