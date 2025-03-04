def prime_selector(numbers: list[int]) -> list[int]:
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    return [num for num in numbers if is_prime(num)]