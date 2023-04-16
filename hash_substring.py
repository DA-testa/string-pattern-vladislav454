B = 31
Q = 10**9 + 9 # to avoid overflow

def get_hash(s):
    hash_val = 0
    for i in range(len(s)):
        hash_val = (hash_val * B + ord(s[i])) % Q
    return hash_val

def read_input():
    input_type = input().rstrip()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        with open("tests/06") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()

    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    pattern_len = len(pattern)
    text_len = len(text)

    multiplier = 1
    for i in range(1, pattern_len):
        multiplier = (B * multiplier) % Q

    pattern_hash = get_hash(pattern)
    text_hash = get_hash(text[:pattern_len])

    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash and pattern == text[i:i+pattern_len]:
            occurrences.append(i)
        if i < text_len - pattern_len:
            text_hash = (B * (text_hash - ord(text[i]) * multiplier) + ord(text[i + pattern_len])) % Q

    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
