def calculate_calibration_sum(file_path):

    with open(file_path, 'r') as file:

        lines = file.readlines()
    calibration_sum = sum(concatenate_digits(line) for line in lines)

    return calibration_sum


def concatenate_digits(string):
    first_digit = next((c for c in string if c.isdigit()), None)

    last_digit = next((c for c in reversed(string) if c.isdigit()), None)

    if first_digit is None or last_digit is None:
        return "Invalid input. The string should contain at least one digit."

    result = int(str(first_digit) + str(last_digit))

    return result


# Example usage:

datos = "codenumbers.txt"

calibration_sum = calculate_calibration_sum(datos)

print("The sum of the calibration values is:", calibration_sum)