def round_numbers(numbers: list[int], threshold: int) -> list[int]:
    rounded = []
    for num in numbers:
        if num < threshold:
            rounded_num = (num // 10) * 10
        else:
            rounded_num = ((num + 9) // 10) * 10
        rounded.append(rounded_num)
    return rounded