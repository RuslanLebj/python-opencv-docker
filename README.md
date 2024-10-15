# Обнаружение лиц с использованием OpenCV в Docker

Этот проект демонстрирует, как создать Docker-образ с использованием Python и OpenCV для обнаружения лиц на изображении. Проект включает конвейер GitHub Actions, который автоматически собирает и отправляет Docker-образ в DockerHub.

## Возможности
- Обнаружение лиц на заданном изображении с использованием OpenCV.
- Вывод количества обнаруженных лиц в терминал.
- Автоматическая сборка и публикация Docker-образа в DockerHub с помощью GitHub Actions.

## Требования
- Установленный Docker на локальной машине.
- Аккаунт DockerHub.
- (Опционально) Репозиторий GitHub с настроенным GitHub Actions.

## Использование

### Локальный запуск с Docker

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/<your-username>/python-opencv-docker.git
   cd python-opencv-docker
   ```
2. Соберите Docker-образ локально:
   ```bash
   docker build -t opencv-face-detection .
   ```
3. Запустите Docker-контейнер:
   ```bash
   docker run --rm opencv-face-detection
   ```

### Использование Docker-образа из DockerHub

1. Загрузите Docker-образ:
   ```bash
   docker pull <your-dockerhub-username>opencv-face-detection:latest
   ```
2. Запустите Docker-образ:
   ```bash
   docker run --rm <your-dockerhub-username>opencv-face-detection
   ```

### Настройка для другого изображения

Если вы хотите использовать другое изображение, замените sample.jpg в папке images/ на ваше собственное. После этого пересоберите Docker-образ и запустите контейнер, как описано выше.

## CI/CD с GitHub Actions

Проект использует GitHub Actions для автоматической сборки и публикации Docker-образа в DockerHub. Вот как это работает:

1. При каждом пуше в ветку `main`, GitHub Actions:
   - Собирает Docker-образ с использованием `Dockerfile`.
   - Публикует собранный образ в ваш репозиторий DockerHub.

### Настройка секретов в GitHub

Для автоматической аутентификации в DockerHub через GitHub Actions добавьте следующие секреты в ваш репозиторий:

- `DOCKER_USERNAME`: Ваш логин DockerHub.
- `DOCKER_PASSWORD`: Ваш пароль DockerHub или персональный токен доступа (если у вас включена двухфакторная аутентификация).

Эти секреты используются в файле `.github/workflows/docker-image.yml` для аутентификации и публикации образа в DockerHub.
