
def give_bmi(height: list[int | float],
             weight: list[int | float]
             ) -> list[int | float]:
    """
    Compute BMI values from height and weight lists.
    Formula: BMI = weight / (height^2)
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be the same length")

    for h in height:
        if not isinstance(h, (int, float)):
            raise TypeError("Height must only be int or float")

    for w in weight:
        if not isinstance(w, (int, float)):
            raise TypeError("Weight must only be int or float")

    bmi_list = []
    for i in range(len(height)):
        h = height[i]
        w = weight[i]
        bmi_index = w / (h ** 2)
        bmi_list.append(bmi_index)
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Return a list of booleans where True means BMI > limit.
    """
    return [value > limit for value in bmi]


def main():
    "main function"
    pass


if __name__ == "__main__":
    "main run"
    main()
