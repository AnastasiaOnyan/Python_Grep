import sys
import argparse
from typing import Literal

matched_at_least_once = False

def find_pattern_indices(the_line: str, the_pattern: str) -> list[tuple[int, int]]:
    indices = []
    j = len(the_pattern)
    if (len(the_line) == 0 and len(the_pattern) == 0) or len(the_pattern) == 0:
        return [(0, -1)]
    elif (len(the_line) == 0 and len(the_pattern) != 0) or len(the_line) < len(the_pattern):
        return []
    elif j == 1:
        for i in range(0, len(the_line)):
            if the_line[i] == the_pattern:
                indices.append((i, i + 1))
        return indices
    else:
        for i in range(0, len(the_line)):
            if j == len(the_line) + 1:
                return indices
            elif the_line[i:j] == the_pattern:
                indices.append((i,j))
            j += 1


def highlighter_func(list_of_indices: list[tuple[int, int]], the_line: str) -> str:
    highlighted = ''
    if list_of_indices == []:
        return the_line
    elif list_of_indices == [(0, -1)]:
        return the_line
    for k, index in enumerate(list_of_indices):
        i = index[0]
        j = index[1]
        if k == 0:
            if i != 0:
                highlighted += the_line[:i]
        else:
            highlighted += the_line[j_previous:i]
        highlighted += '\033[01;31m\033[K' + the_line[i:j] + '\033[m\033[K' 
        j_previous = j
    highlighted += the_line[j:]
    return highlighted


def color_lines_filter(the_line: str, the_pattern: str, color: Literal["always", "never", "auto"]):
    global matched_at_least_once
    idx = find_pattern_indices(the_line, the_pattern)
    # if idx == []:
    #     return
    if idx != []:
        if color == "auto":
            if sys.stdout.isatty():
                print(highlighter_func(idx, the_line), end="")
            else:
                print(the_line, end="")
        elif color == "always":
            print(highlighter_func(idx, the_line), end="")
        elif color == "never":
            print(the_line, end="")
    

def reverse_line(the_line: str, the_pattern: str, color: Literal["always", "never", "auto"], invert_match: bool):
    if args.invert_match:
        if the_pattern not in the_line:
            print(the_line, end="")
    else:
        color_lines_filter(the_line, the_pattern, color)

        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern")
    parser.add_argument("filename", default=None, nargs="?")
    parser.add_argument("--color", default="auto", choices=["always", "never", "auto"])
    parser.add_argument("-v", "--invert-match", action="store_true")
    args = parser.parse_args()
    pattern = args.pattern
    color = args.color
    invert_match = args.invert_match
    

    if args.filename != None:
        with open(args.filename) as f:
            for line in f:
                reverse_line(line, pattern, color, invert_match)
    else:
        for line in sys.stdin:
            reverse_line(line, pattern, color, invert_match)
                    
#sys.exit(1)


