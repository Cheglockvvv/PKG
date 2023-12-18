import cv2
import numpy as np
import matplotlib.pyplot as plt

# Загрузка изображения
image_path = "test.png"
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Создание графика с 4x4 подграфиками
fig, axes = plt.subplots(3, 4, figsize=(9, 9))

# Оригинальное изображение
axes[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0, 0].set_title('Исходник')
axes[0, 0].axis("off")
axes[2, 3].axis("off")


# Функция построения гистограммы изображения
def MakeHistogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_normalized = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX)
    hist_image = np.zeros((256, 256), dtype=np.uint8)
    for i in range(256):
        cv2.line(hist_image, (i, 255), (i, 255 - int(hist_normalized[i][0])), 255)
    return hist_image


# Построение изначальной гистограммы
constant = 50
axes[0, 1].imshow(MakeHistogram(image))
axes[0, 1].set_title('Гистограмма')
axes[0, 1].axis("off")

# Построение эквализированного для RGB компонент изображения
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
r, g, b = cv2.split(image)
r_equalized = cv2.equalizeHist(r)
g_equalized = cv2.equalizeHist(g)
b_equalized = cv2.equalizeHist(b)
rgb_equalized_image = cv2.merge([r_equalized, g_equalized, b_equalized])
axes[0, 2].imshow(rgb_equalized_image)
axes[0, 2].set_title('по RGB')
axes[0, 2].axis("off")

# Построение гистограммы эквализации по RGB
axes[0, 3].imshow(MakeHistogram(rgb_equalized_image))
axes[0, 3].set_title('по RGB')
axes[0, 3].axis("off")


# Эквализация по каналу яркости HSV
def HSVEqualizedImage(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv_image)
    v_equalized = cv2.equalizeHist(v)
    hsv_equalized_image = cv2.merge([h, s, v_equalized])
    rgb_hsv_equalized_image = cv2.cvtColor(hsv_equalized_image, cv2.COLOR_HSV2RGB)
    return rgb_hsv_equalized_image


# Построение эквализированного изображения по HSV
axes[1, 0].imshow(HSVEqualizedImage(image), cmap='gray')
axes[1, 0].set_title('по HSV')
axes[1, 0].axis("off")

# Построение гистограммы эквализации по HSV
axes[1, 1].imshow(MakeHistogram(HSVEqualizedImage(image)))
axes[1, 1].set_title('по HSV')
axes[1, 1].axis("off")


# Применение линейного контрастирования к изображению
def LinearContrast1(image):
    min_value = np.min(image)
    max_value = np.max(image)
    output_image = np.clip((255 / (max_value - min_value)) * (image - min_value), 0, 255).astype(np.uint8)
    return output_image


# Линейное контрастирование
axes[1, 2].imshow(LinearContrast1(image))
axes[1, 2].set_title('Лин. контрастирование')
axes[1, 2].axis("off")


axes[1, 3].imshow(MakeHistogram(LinearContrast1(image)))
axes[1, 3].set_title('Лин. контрастирование')
axes[1, 3].axis("off")


# Функция однородного усредняющего фильтра
def blurFilter1(image):
    kernel_size = (11, 11)
    blurred_image = cv2.blur(image, kernel_size)
    return blurred_image


# Функция неоднородного усредняющего фильтра
def blurFilter2(image):
    kernel_size = 15
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)
    for i in range(kernel_size):
        for j in range(kernel_size):
            kernel[i, j] = 1 / ((i - kernel_size // 2) ** 2 + (j - kernel_size // 2) ** 2 + 1)
    kernel /= np.sum(kernel)
    filtered_image = cv2.filter2D(image, 0, kernel)
    return filtered_image


image_path = "test4.png"
image = cv2.imread(image_path, cv2.COLOR_BGR2GRAY)

# Отображение результатов

axes[2, 0].imshow(image, cmap='gray')
axes[2, 0].set_title("Исходник")
axes[2, 0].axis("off")

axes[2, 1].imshow(blurFilter1(image), cmap='gray')
axes[2, 1].set_title("Однородный")
axes[2, 1].axis("off")

axes[2, 2].imshow(blurFilter2(image), cmap='gray')
axes[2, 2].set_title("Неоднородный")
axes[2, 2].axis("off")

kernel_size = (19, 19)
axes[2, 3].imshow(cv2.GaussianBlur(image, kernel_size, 0), cmap='gray')
axes[2, 3].set_title("Фильтр Гаусса")
axes[2, 3].axis("off")

# Отображение результатов
plt.tight_layout()
plt.show()
