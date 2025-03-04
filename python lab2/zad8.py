import re

def readability_score(text: str) -> float:
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        return 0.0
    total_words = 0
    total_syllables = 0
    for sentence in sentences:
        words = sentence.split()
        total_words += len(words)
        for word in words:
            syllables = sum(1 for c in word.lower() if c in 'aeiou')
            total_syllables += syllables if syllables > 0 else 1
    avg_words = total_words / len(sentences)
    avg_syllables = total_syllables / total_words if total_words else 0
    return avg_words + avg_syllables