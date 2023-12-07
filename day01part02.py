def calculate_calibration_sum(file_path):

    with open(file_path, 'r') as file:

        lines = file.readlines()
    calibration_sum = sum(concatenate_digits(line) for line in lines)
    print(calibration_sum)

    return calibration_sum


def replace_digits(string):
    digits = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
              'eight': '8', 'nine': '9', 'zerone': '01', 'oneight': '18', 'twone': '21', 'threeight': '38',
              'fiveight': '58', 'sevenine': '79', 'eightwo': '82', 'eighthree': '83', 'nineight': '98'}

    keys = sorted(digits.keys(), key=len, reverse=True)

    for i in range(len(string)):

        for key in keys:

            if string[i:i + len(key)] == key:
                string = string[:i] + digits[key] + string[i + len(key):]

                break

    return string


def concatenate_digits(string):

    replaced = replace_digits(string)

    first_digit = next((c for c in replaced if c.isdigit()), None)

    last_digit = next((c for c in reversed(replaced) if c.isdigit()), None)

    if first_digit is None or last_digit is None:
        return "Invalid input. The string should contain at least one digit."

    result = int(str(first_digit) + str(last_digit))
    # print(string,replaced,result)

    return result


# Example usage:

datos = "codenumbers.txt"

calibration_sum = calculate_calibration_sum(datos)

print("The sum of the calibration values is:", calibration_sum)