# Используем официальный Python-образ
FROM python:3.9-slim

# Устанавливаем зависимости для OpenCV
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && apt-get clean

# Устанавливаем OpenCV и другие зависимости
RUN pip install --no-cache-dir opencv-python-headless

# Копируем скрипт в контейнер
COPY detect_faces.py /app/detect_faces.py
COPY images /app/images

# Задаем рабочую директорию
WORKDIR /app

# Выполняем скрипт при запуске контейнера
CMD ["python", "detect_faces.py"]
