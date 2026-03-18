import pyautogui # importa la libreria pyautogui, previamente hay que instalarla con pip
import time


TARGET_IMAGE = "imagen.png" #imagen que quieres detectar (tiene que estar en la misma carpeta hay una de ejemplo)


DELAY = 0.9 # delay entre cada coincidencia

print("Bot iniciado, CTRL + C para detenerlo.")

while True:
    try:
        # busca la imagen e la pantalla (SI NO ESTÁ EN LA PANTALLA NO LA BUSCA!)
        location = pyautogui.locateCenterOnScreen(TARGET_IMAGE, confidence=0.85)
        # la funcion locate hace que busca en toda la pantalla y confidence es el % de coincidencia

        # si la imagen aparece, hace clic por coordenadas en la pantalla
        if location is not None:
            print(f"Coincidencia encontrada en {location}. Haciendo clic...")
            pyautogui.click(location.x, location.y)

        # delay antes de volver a buscar una coincidencia
        time.sleep(DELAY)

    except KeyboardInterrupt:
        print("Bot detenido manualmente.")
        break

        # permite hacer el CTRL + C para pararlo
    except Exception as e:
        print("Error:", e)
        time.sleep(1)
