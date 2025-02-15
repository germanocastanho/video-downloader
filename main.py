# Copyleft 🄯, Germano Castanho, 2025;
# Software livre licenciado sob a GPL-3.0;
# Cada linha, um manifesto pela liberdade!


import uuid

import yt_dlp


def download_video():
    video_url = input("Digite a URL do vídeo: ")
    video_path = input("Digite o PATH do download: ")

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": f"{video_path}/{uuid.uuid4()}.mp4",
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            },
            {
                "key": "FFmpegFixupM3u8",
            },
        ],
        "http_headers": {"Referer": video_url, "User-Agent": "Mozilla/5.0"},
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            print("Download concluído com sucesso!")

    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    download_video()
