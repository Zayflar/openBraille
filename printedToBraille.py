braille_chars = [
    # Letters
    ('a', [[1,0],[0,0],[0,0]]),
    ('b', [[1,0],[1,0],[0,0]]),
    ('c', [[1,1],[0,0],[0,0]]),
    ('d', [[1,1],[0,1],[0,0]]),
    ('e', [[1,0],[0,1],[0,0]]),
    ('f', [[1,1],[1,0],[0,0]]),
    ('g', [[1,1],[1,1],[0,0]]),
    ('h', [[1,0],[1,1],[0,0]]),
    ('i', [[0,1],[1,0],[0,0]]),
    ('j', [[0,1],[1,1],[0,0]]),
    ('k', [[1,0],[0,0],[1,0]]),
    ('l', [[1,0],[1,0],[1,0]]),
    ('m', [[1,1],[0,0],[1,0]]),
    ('n', [[1,1],[0,1],[1,0]]),
    ('o', [[1,0],[0,1],[1,0]]),
    ('p', [[1,1],[1,0],[1,0]]),
    ('q', [[1,1],[1,1],[1,0]]),
    ('r', [[1,0],[1,1],[1,0]]),
    ('s', [[0,1],[1,0],[1,0]]),
    ('t', [[0,1],[1,1],[1,0]]),
    ('u', [[1,0],[0,0],[1,1]]),
    ('v', [[1,0],[1,0],[1,1]]),
    ('w', [[0,1],[1,1],[0,1]]),
    ('x', [[1,1],[0,0],[1,1]]),
    ('y', [[1,1],[0,1],[1,1]]),
    ('z', [[1,0],[0,1],[1,1]]),

    # Numbers (represented as letters a-j with number prefix in braille, here just mapping)
    ('1', [[1,0],[0,0],[0,0]]),
    ('2', [[1,0],[1,0],[0,0]]),
    ('3', [[1,1],[0,0],[0,0]]),
    ('4', [[1,1],[0,1],[0,0]]),
    ('5', [[1,0],[0,1],[0,0]]),
    ('6', [[1,1],[1,0],[0,0]]),
    ('7', [[1,1],[1,1],[0,0]]),
    ('8', [[1,0],[1,1],[0,0]]),
    ('9', [[0,1],[1,0],[0,0]]),
    ('0', [[0,1],[1,1],[0,0]]),

    # Basic punctuation
    (',', [[0,1],[0,0],[0,0]]),
    (';', [[0,1],[1,0],[0,0]]),
    (':', [[0,1],[0,1],[0,0]]),
    ('.', [[0,1],[1,1],[0,0]]),
    ('!', [[0,1],[1,1],[0,1]]),
    ('?', [[0,1],[1,0],[0,1]]),
    ("'", [[0,0],[1,0],[0,0]]),
    ('-', [[0,0],[1,0],[1,0]]),
    ('/', [[0,1],[0,0],[1,0]])
]


def print_braille(text, max_chars_per_line=15):
    text = text.lower()

    for i in range(0, len(text), max_chars_per_line):
        segment = text[i:i+max_chars_per_line]
        print(segment)

        line1, line2, line3 = '', '', ''

        for ch in segment:
            matrix = next((m for c, m in braille_chars if c == ch), [[0,0],[0,0],[0,0]])
            line1 += ''.join('·' if dot else ' ' for dot in matrix[0]) + '|'
            line2 += ''.join('·' if dot else ' ' for dot in matrix[1]) + '|'
            line3 += ''.join('·' if dot else ' ' for dot in matrix[2]) + '|'

        print(line1)
        print(line2)
        print(line3)
        print() 



print_braille("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")