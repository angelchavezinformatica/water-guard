def splitlines(string: str, keepends=False):
    lines = []
    current_line = []

    i = 0
    while i < len(string):
        char = string[i]
        if char in ('\n', '\r'):
            if keepends:
                current_line.append(char)
                if char == '\r' and i + 1 < len(string) and string[i + 1] == '\n':
                    current_line.append('\n')
                    i += 1
            lines.append(''.join(current_line))
            current_line = []
        else:
            current_line.append(char)
        i += 1

    if current_line or (string and string[-1] in ('\n', '\r')):
        lines.append(''.join(current_line))

    return lines


def join_path(*args):
    return "/".join(arg.strip("/") for arg in args)
