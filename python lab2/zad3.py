def longest_increasing_subsequence(sequence: list[int]) -> int:
    if not sequence:
        return 0
    max_len = current_len = 1
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1
    return max_len