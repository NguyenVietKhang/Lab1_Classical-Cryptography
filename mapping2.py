def rep(text, mapping):
    return ''.join([mapping.get(char, char) for char in text])

mapping = {
    'O': 'T',
    'L': 'H',
    'E': 'E',
    'I': 'A',
    'A': 'N',
    'C': 'D',
    'N': 'O',
    'S': 'S',
    'T': 'I',
    'Y': 'F',
}

cipher_text = ""

dt = rep(cipher_text, mapping)

print(dt)
