def is_balanced(expression: str) -> bool:
    stack = []
    mapping = {'(': ')', '[': ']', '{': '}'}
    for char in expression:
        if char in mapping:
            stack.append(mapping[char])
        elif char in {')', ']', '}'}:
            if not stack or stack.pop() != char:
                return False
    return not stack