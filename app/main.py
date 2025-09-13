import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern == "\d": # Return True if numeric
        return any(char.isnumeric() for char in input_line)
    elif pattern == "\w": # Return True if alphanumeric or _
        return any((char.isalnum() or char == "_") for char in input_line)
    elif (pattern[0] == "[" and pattern[-1] == "]"): 
        if pattern[1] == "^": # Return False if character inside brackets matches
            for char in pattern[2:-1]:
                if char not in input_line:
                    return True
        else: # Return True if character inside brackets matches
            return any(char in pattern[1:-1] for char in input_line)
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()
    print("Logs from your program will appear here!", file=sys.stderr)

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
