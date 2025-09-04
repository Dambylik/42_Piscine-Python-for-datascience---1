import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a list and returns a truncated NumPy array.
    Prints the shape of the original and sliced arrays.
    """
    if not isinstance(family, list):
        raise TypeError("Argument should be a list")
    if len(family) == 0:
        raise ValueError("List should not be empty")

    for row in family:
        if not isinstance(row, list):
            raise TypeError("family must be a list of lists")

    first_row_length = len(family[0])
    for row in family:
        if len(row) != first_row_length:
            raise ValueError("All rows must have the same size")

    new_array = np.array(family)
    print(f"My shape is : {new_array.shape}")
    truncated_array = new_array[start:end]
    print(f"My new shape is : {truncated_array.shape}")
    return truncated_array.tolist()


def main():
    "main function"
    pass


if __name__ == "__main__":
    "main run"
    main()
