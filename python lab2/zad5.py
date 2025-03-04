def transposition_cipher(text: str, key: int) -> str:
    if key <= 0 or key > len(text):
        return text
    chars = list(text)
    for i in range(key - 1, len(chars), key):
        if i + 1 < len(chars):
            chars[i], chars[i+1] = chars[i+1], chars[i]
    return ''.join(chars)