import itertools

def unique_permutations(elements: list) -> list[list]:
    seen = set()
    permutations = []
    for perm in itertools.permutations(elements):
        if perm not in seen:
            seen.add(perm)
            permutations.append(list(perm))
    return permutations