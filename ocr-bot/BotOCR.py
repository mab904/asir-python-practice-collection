import pyautogui # Hay que instalar las librerías previamente y el Tesseract
import pytesseract
import time

# ruta al ejecutable de Tesseract (CAMBIA esto si el ejecutable est en otra carpeta)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# coordenadas de la zona a capturar (x, y, ancho, alto) (en un punto concreto 500 300 hace un caja con 400 de ancho y 200 de alto)
CAPTURE_REGION = (500, 300, 400, 200)

DELAY = 5.0

print("Bot OCR iniciado.")

while True:
    try:
        # captura una región de la pantalla
        screenshot = pyautogui.screenshot(region=(500, 300, 400, 200))

        # convierte la imagen a texto
        text = pytesseract.image_to_string(screenshot, lang="eng")
        print("Texto detectado: ", text.strip())

        # si encuentra la palabra OK, hace click (no donde esta OK sino en una coordenada en específico) (esto lo hago como una prueba para ver si el texto en verdad es detectado)
        if "OK" in text.upper():
            print("Texto detectado. Haciendo click...")
            pyautogui.click(600, 400)  # coordenadas donde hace click

        time.sleep(DELAY)

    except KeyboardInterrupt:
        print("Bot detenido manualmente.")
        break

