# Descripción
Este proyecto es un bot que utiliza OCR (Reconocimiento Óptico de Caracteres) usando [Tesseract](https://github.com/tesseract-ocr/tesseract) para leer texto directamente desde una zona específica de la pantalla.
Si detecta una palabra concreta (en este caso, “OK”), realiza un clic automático en una coordenada determinada (Esto no tiene ninguna utilidad en específico solo era un comprobante para ejecutar una acción al detectar la palabra).

Es útil para automatizar tareas donde el texto en pantalla cambia dinámicamente y personalmente quería ver el funcionamiento en acción.

## Tecnologías utilizadas
- PyAutoGUI — captura pantalla y controla el ratón.
- Pytesseract — puente entre Python y Tesseract OCR.
- Tesseract OCR — motor que interpreta texto dentro de imágenes.
- time — controla pausas entre iteraciones.

# Description
This project is a bot that uses OCR (Optical Character Recognition) through [Tesseract](https://github.com/tesseract-ocr/tesseract) to read text directly from a specific area of the screen. 
If it detects a specific word (“OK”), it performs an automatic click at a specific coordinates (This action has no particular practical purpose; it simply serves as a test to confirm that the detected text triggers an automated response).

The bot is useful for automating tasks where on‑screen text changes dynamically and I personally wanted to see how it works in action.

## Technologies Used
- PyAutoGUI — captures the screen and controls the mouse.
- Pytesseract — acts as a bridge between Python and Tesseract OCR.
- Tesseract OCR —  the engine that interprets text inside images.
- time — delays between iterations.
