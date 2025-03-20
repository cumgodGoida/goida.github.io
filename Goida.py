import requests
import pygame
import android.media
import android.content

def main():
    url = "https://www.myinstants.com/media/sounds/zhestokie-stony.mp3"
    filepath = "/storage/emulated/0/Download/porn2.mp3"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        with open(filepath, "wb") as f:
            f.write(response.content)

        pygame.mixer.init()

        while True:
            try:
                pygame.mixer.music.load(filepath)
                pygame.mixer.music.play()

                audio_manager = android.app.Application.getContext().getSystemService(android.content.Context.AUDIO_SERVICE)
                max_volume = audio_manager.getStreamMaxVolume(android.media.AudioManager.STREAM_MUSIC)
                audio_manager.setStreamVolume(android.media.AudioManager.STREAM_MUSIC, max_volume, android.media.AudioManager.FLAG_SHOW_UI)

                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)  # Keep the loop running while music plays

            except pygame.error as e:
                print(f"Pygame error: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
    except IOError as e:
        print(f"File I/O error: {e}")

if __name__ == "__main__":
    main()
