from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def zoom(image: np.ndarray) -> np.ndarray:
    """
    Crops a 400x400 region from the input image and converts it to grayscale.
    """
    start_x = 440
    start_y = 91
    crop = image[start_y:start_y+400, start_x:start_x+400]
    gray = 0.299*crop[:, :, 0] + 0.587 * crop[:, :, 1] + 0.114 * crop[:, :, 2]
    gray = gray.astype(np.uint8)  # Convert to integers

    gray = np.expand_dims(gray, axis=2)

    print(f"New shape after slicing: {gray.shape}")
    print(gray)
    plt.imshow(gray, cmap="gray")
    return gray


def main():
    "main function"
    try:
        img = ft_load("animal.jpeg")
        print(img)
        zoom(img)
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    "main run"
    main()
