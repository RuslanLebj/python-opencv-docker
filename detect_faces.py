import cv2

def detect_faces(image_path):
    # Загружаем классификатор для распознавания лиц
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Загружаем изображение
    image = cv2.imread(image_path)
    if image is None:
        print("Изображение не найдено")
        return

    # Конвертируем изображение в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Выполняем распознавание лиц
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Выводим количество найденных лиц
    print(f"Найдено {len(faces)} лиц(о/а).")

if __name__ == "__main__":
    # Путь к изображению
    image_path = "images/sample.jpg"
    detect_faces(image_path)
