import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a list and returns a truncated NumPy array.
    Prints the shape of the original and sliced arrays.
    """
    if len(family) <= 0:
        raise ValueError("List should have length > 0")
    if (type(family) is not list):
        raise TypeError("Argument should be a list")
    new_array = np.array(family)
    print(f"My shape is : {new_array.shape}")
    truncated_array = np.array(new_array[start:end])
    print(f"My new shape is : {truncated_array.shape}")
    return truncated_array


def main():
    "main function"
    pass


if __name__ == "__main__":
    "main run"
    main()
