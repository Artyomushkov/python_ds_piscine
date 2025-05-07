import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    This function takes a list of heights and weights
    and returns array of BMIs.
    The BMI is calculated using the formula: weight / (height * height)
    """
    # Convert height and weight lists to NumPy arrays
    height_array = np.array(height)
    weight_array = np.array(weight)

    # Check if the lengths of the arrays are equal
    if height_array.shape != weight_array.shape:
        print("The length of height and weight lists must be equal.")
        return

    # Calculate BMI using NumPy's element-wise operations
    try:
        bmi = weight_array / (height_array ** 2)
    except ZeroDivisionError:
        print("Height cannot be zero.")
        return
    except TypeError:
        print("Height and weight must be numbers.")
        return

    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    This function takes a list of BMIs and a limit
    and returns a list of booleans.
    Each boolean indicates whether the corresponding BMI is above the limit.
    """
    # Check if the limit is a number
    if not isinstance(limit, int):
        print("Limit must be int.")
        return

    bmi_array = np.array(bmi)
    # Apply the limit using NumPy's element-wise comparison
    res = bmi_array > limit
    return res.tolist()
