# Video Downloader 📹

Este é um script simples em Python, projetado para **baixar vídeos da internet** (YouTube, TikTok, Instagram etc.), através da biblioteca [YT-DLP](https://github.com/yt-dlp/yt-dlp). Um adendo! Tenha consciência de que tais vídeos podem estar protegidos por direitos autorais. Use este script com responsabilidade - *ou não, caso prefira se aventurar pelos "sete mares" da internet!* 🏴‍☠️

<br />

## 🚀 Funcionalidades

- **Video Downloader 📥**: Baixe vídeos de diversas plataformas, como YouTube, TikTok, Instagram, entre outras.
- **Melhor Qualidade ✨**: Download feito com a melhor qualidade disponível para o vídeo (1080p, 720p etc.)!
- **Interface em CLI 💻**: Utilize a linha de comando para inserir o link do vídeo e escolher o caminho do download.

<br />

## 📋 Pré-requisitos e Instalação

### Pré-requisitos

- [**Python 3.12+**](https://www.python.org/) 🐍: Versão mínima recomendada para compatibilidade com as dependências do projeto.
- [**YT-DLP**](https://github.com/yt-dlp/yt-dlp) 🎬: Principal dependência do projeto; encontra-se listada no arquivo [`requirements.txt`](requirements.txt).
- [**FFMPEG**](https://www.ffmpeg.org/) ⌛: Responsável pelo pós-processamento do vídeo baixado - deve ser instalada globalmente.

### Instalação

1. **Clone o repositório**:

    ```Bash
    git clone https://github.com/germanocastanho/video-downloader.git
    ```

2. **Navegue até o diretório**:

    ```Bash
    cd video-downloader
    ```

3. **(Opcional) Crie um VENV**:

    - **Criação do VENV**:

      ```bash
      python -m venv .venv
      ```

    - **Ativação do VENV**:

      ```bash
      source .venv/bin/activate
      ```

4. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Instale o ffmpeg**:

    ```Bash
    sudo apt update
    sudo apt install ffmpeg
    ```

6. **Execute o downloader**:

    ```bash
    python main.py
    ```

<br />

## 📌 Exemplos de Uso

O script solicita ao usuário a URL do vídeo desejado e o diretório onde o arquivo será armazenado. Após receber essas informações, ele processa o download, garantindo que ele seja salvo no local indicado. O arquivo é nomeado aleatoriamente para fim de evitar conflitos, simplificando o gerenciamento dos vídeos baixados e evitando a necessidade de nomeação manual. Veja um exemplo de uso:

1. **Execute o script**:

    ```bash
    python main.py
    ```

2. **Insira a URL do vídeo**:

    ```bash
    Digite a URL do vídeo: <URL>
    ```

3. **Insira o PATH do download**:

    ```bash
    Digite o PATH do download: <PATH>
    ```

<br />

## ⚠️ IMPORTANTE!

> *O '**YT-DLP**' é uma biblioteca de comportamento muitas vezes instável, de maneira que o código pode não funcionar corretamente em todos os momentos. Dessa forma, em havendo problemas, considere abrir um issue no [repositório oficial](https://github.com/yt-dlp/yt-dlp/issues) do projeto. Certamente, a comunidade de desenvolvedores estará pronta para lhe ajudar! ✨*

<br />

## 🤝 Contribuições

Contribuições são sempre bem-vindas! Se deseja colaborar, siga boas práticas de programação e sugira melhorias. Faça um fork do repositório e implemente suas alterações. Envie um pull request com uma descrição clara do que foi feito. Caso encontre problemas ou tenha ideias, abra uma [issue](https://github.com/germanocastanho/video-downloader/issues). Juntos, podemos tornar o Downloader ainda mais incrível! 🚀

<br />

## 📜 Licença GPL-3.0

Distribuído sob a [Licença Pública Geral GNU v3.0 (GPL-3.0)](https://www.gnu.org/licenses/gpl-3.0.html), garantindo liberdade de uso, modificação e redistribuição do software, desde que os mesmos direitos sejam preservados em quaisquer versões derivadas. Ao utilizar ou contribuir com o projeto, você apoia a filosofia de software livre e a promoção de um ambiente colaborativo e aberto para inovação! 🔬

<br />

## ✉️ Créditos e Contato

- **Créditos**: Copyleft 🄯, Germano Castanho, 2025
- **E-mail**: [germanocastanho@proton.me](mailto:germanocastanho@proton.me)
- **Problemas?** Abra uma [issue](https://github.com/germanocastanho/video-downloader/issues) no repositório oficial.

<br />

**Cada linha, um manifesto pela liberdade!** ✊🏴
