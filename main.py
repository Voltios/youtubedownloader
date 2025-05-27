import yt_dlp
import os

def descargar_playlist_mp4(url_playlist, carpeta_destino='videos_descargados'):
    """
    Descarga todos los videos de una playlist de YouTube en formato MP4.

    Args:
        url_playlist (str): La URL de la playlist de YouTube.
        carpeta_destino (str): La carpeta donde se guardarán los videos.
                               Por defecto es 'videos_descargados'.
    """
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
        print(f"Carpeta '{carpeta_destino}' creada.")

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(carpeta_destino, '%(title)s.%(ext)s'),
        'ignoreerrors': True,  # Continúa si hay errores en algún video
        'download_archive': os.path.join(carpeta_destino, 'descargados.txt'), # Evita descargar videos repetidos
        'noplaylist': False,  # Asegura que se procese como playlist
        'continue_dl': True, # Continúa descargas interrumpidas
        'verbose': True, # Muestra información detallada del proceso
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\nDescargando videos de la playlist: {url_playlist}")
            ydl.download([url_playlist])
        print(f"\n¡Descarga de la playlist completada en la carpeta: {carpeta_destino}!")
    except Exception as e:
        print(f"\nOcurrió un error durante la descarga: {e}")

if __name__ == "__main__":
    url_playlist = input("Por favor, introduce la URL de la playlist de YouTube: ")
    descargar_playlist_mp4(url_playlist)