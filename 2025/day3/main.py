def task1(input_f: str) -> int:
    joltage = 0
    for line in open(input_f):
        bank = [int(n) for n in line.strip()]
        first_digit = -1
        second_digit = -1

        for battery_idx in range(len(bank)):
            digit = bank[battery_idx]

            if battery_idx == len(bank) - 1 and second_digit == -1:
                second_digit = digit

            elif digit > first_digit:
                first_digit = digit
                second_digit = -1

            elif digit > second_digit:
                second_digit = digit

        joltage += first_digit * 10 + second_digit

    return joltage


def task2(input_f: str) -> int:
    joltage = 0
    for line in open(input_f):
        bank = [int(n) for n in line.strip()]
        bank_digits = [-1] * 12

        for battery_idx in range(len(bank)):
            digit = bank[battery_idx]
            dist_from_end = len(bank) - battery_idx

            if (
                dist_from_end < len(bank_digits)
                and bank_digits[len(bank_digits) - dist_from_end] == -1
            ):
                bank_digits[len(bank_digits) - dist_from_end] = digit

            else:
                for bank_idx in range(len(bank_digits)):
                    if (
                        digit > bank_digits[bank_idx]
                        and dist_from_end > len(bank_digits) - bank_idx - 1
                    ):
                        bank_digits[bank_idx] = digit
                        for next_idx in range(bank_idx + 1, len(bank_digits)):
                            bank_digits[next_idx] = -1

                        break

        joltage += int("".join([str(d) for d in bank_digits]))

    return joltage


if __name__ == "__main__":
    input_f = "input.txt"
    print("task 1: ", task1(input_f))
    print("task 2: ", task2(input_f))
