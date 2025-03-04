from collections import defaultdict

def group_words_by_length(words: list[str]) -> dict[int, list[str]]:
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)