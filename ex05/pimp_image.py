from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of an RGB image
    by replacing each value v with 255 - v.
    """
    print("Inverts the color of the image received")
    inverted_array = np.zeros_like(array)

    for i in range(array.shape[0]):  # rows (height)
        for j in range(array.shape[1]):  # columns (width)
            for k in range(array.shape[2]):  # channels (R, G, B)
                inverted_array[i, j, k] = 255 - array[i, j, k]

    plt.imshow(inverted_array)
    plt.show()
    return inverted_array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keep the red channel values as they are.
    Turn off the green and blue channels ([R, 0, 0]).
    """
    print("Intense red color of the image received")
    red_intensity = np.zeros_like(array)

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            red_intensity[i, j, 0] = array[i, j, 0]
            red_intensity[i, j, 1] = 0
            red_intensity[i, j, 2] = 0

    plt.imshow(red_intensity)
    plt.show()
    return red_intensity


def ft_green(array) -> np.ndarray:
    """
    Keep the green channel values as they are.
    Turn off the green and blue channels ([0, G, 0]).
    """
    print("Intense green color of the image received")
    green_intensity = np.zeros_like(array)

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            green_intensity[i, j, 0] = 0
            green_intensity[i, j, 1] = array[i, j, 0]
            green_intensity[i, j, 2] = 0

    plt.imshow(green_intensity)
    plt.show()
    return green_intensity


def ft_blue(array) -> np.ndarray:
    """
    Keep the blue channel values as they are.
    Turn off the green and blue channels ([0, 0, B]).
    """
    print("Intense blue color of the image received")
    blue_intensity = np.zeros_like(array)

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            blue_intensity[i, j, 0] = 0
            blue_intensity[i, j, 1] = 0
            blue_intensity[i, j, 2] = array[i, j, 0]

    plt.imshow(blue_intensity)
    plt.show()
    return blue_intensity


def ft_grey(array) -> np.ndarray:
    """
    Converts an RGB image to greyscale by averaging R, G, B values
    and replicating the average across all channels.
    """
    grey_array = np.zeros_like(array)

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            red_value = array[i, j, 0]
            grey_value = red_value // 3
            for k in range(array.shape[2]):
                grey_array[i, j, k] = grey_value

    plt.imshow(grey_array)
    plt.show()
    return grey_array


def main():
    "main function"
    try:
        img = ft_load("landscape.jpg")
        # print(img)
        # ft_invert(img)
        # ft_red(img)
        # ft_green(img)
        # ft_blue(img)
        ft_grey(img)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    "main run"
    main()
