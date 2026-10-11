# Backend - Visión Artificial (NOM-051 Detector)

Este directorio está reservado para la implementación del backend de visión artificial para la detección de sellos de advertencia en productos comerciales en México (NOM-051).

## Tecnologías sugeridas para esta etapa:
- **Python 3.10+**
- **FastAPI** (para API REST y WebSockets en tiempo real)
- **OpenCV** (para preprocesamiento y extracción de regiones de interés - ROI)
- **YOLOv8 / YOLOv11** o detector basado en contornos/OCR (Tesseract / EasyOCR) para clasificación de los 5 sellos principales y las 2 leyendas precautorias:
  1. EXCESO CALORÍAS
  2. EXCESO AZÚCARES
  3. EXCESO GRASAS SATURADAS
  4. EXCESO GRASAS TRANS
  5. EXCESO SODIO
  - CONTIENE EDULCORANTES - NO RECOMENDABLE EN NIÑOS
  - CONTIENE CAFEÍNA - EVITAR EN NIÑOS

## Integración con Frontend:
El frontend enviará capturas de cámara o archivos de imagen hacia el endpoint `/api/v1/detect` y recibirá las coordenadas normalizadas (`bounding_boxes`), etiquetas detectadas y nivel de confianza.

