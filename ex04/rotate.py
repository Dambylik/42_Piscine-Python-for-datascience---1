from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def rotate(image: np.ndarray) -> np.ndarray:
    """
    Transposes the image by swapping rows and columns (reversing dimensions).
    """
    height = image.shape[0]
    width = image.shape[1]
    transposed_image = np.zeros((width, height), dtype=image.dtype)

    for i in range(height):
        for j in range(width):
            transposed_image[j, i] = image[i, j, 0]

    print(f"New shape after transpose: {transposed_image.shape}")
    print(transposed_image)
    plt.imshow(transposed_image, cmap='gray')
    plt.show()

    return transposed_image


def zoom(image: np.ndarray) -> np.ndarray:
    """
    Crops a 400x400 region from the input image and converts it to grayscale.
    """
    start_x = 440
    start_y = 91
    crop = image[start_y:start_y+400, start_x:start_x+400]
    gray = 0.299*crop[:, :, 0] + 0.587 * crop[:, :, 1] + 0.114 * crop[:, :, 2]
    gray = gray.astype(np.uint8)
    gray = np.expand_dims(gray, axis=2)
    print(f"The shape of image is: {gray.shape}")
    print(gray)
    return gray


def main():
    "main function"
    try:
        img = ft_load("animal.jpeg")
        rotate(zoom(img))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    "main run"
    main()
