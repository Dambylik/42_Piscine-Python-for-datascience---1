from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def zoom(image: np.ndarray, y0: int, y1: int, x0:int, x1:int ) -> np.ndarray:
    crop = image[y0:y1, x0:x1, :]
    gray_image = 0.299 * crop[:, :, 0] + 0.587 * crop[:, :, 1] + 0.114 * crop[:, :, 2]
    
    print(f"New shape after slicing: {gray_image.shape}")
    print(gray_image)
    
    plt.imshow(gray_image, cmap="gray")
    plt.show()
    
    return gray_image


def main():
    "main function"
    img = ft_load("animal.jpeg")
    # print(img)
    # plt.imshow(img)
    # plt.show()
    original_height = img.shape[0]
    print("original height y = ", original_height)
    original_width = img.shape[1]
    print("original width x = ", original_width)
    
    zoom_height = 400
    zoom_width = 400
    image_center_y = original_height // 2
    print("image center y = ", image_center_y)
    image_center_x = original_width // 2
    print("image center x = ", image_center_x)
    
    y0 = image_center_y - (zoom_height // 1.5)
    print(f"y0 = {y0}")
    y1 = image_center_y + (zoom_height // 2)
    print(f"y1 = {y1}")
    x0 = image_center_x - (zoom_width // 2)
    print(f"x0 = {x0}")
    x1 = image_center_x + (zoom_width // 2)
    print(f"x1 = {x1}")
    
    # zoom(img, y0, y1, x0, x1) x, y 490 /479


if __name__ == "__main__":
    "main run"
    main()