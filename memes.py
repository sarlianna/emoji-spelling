#!/bin/python3
import argparse

SPACE_DEFAULT = ":blank:"
FILLED_DEFAULT = ":kappa:"
FILLED2_DEFAULT = ":pagchomp:"
FILLED3_DEFAULT = ":pagchomp:"
FILLED4_DEFAULT = ":kappa:"
DEFAULT_VALUES = [SPACE_DEFAULT, FILLED_DEFAULT, FILLED2_DEFAULT, FILLED3_DEFAULT, FILLED4_DEFAULT]
HEIGHT = 5

LETTER_BITMAPS_5 = {
    "a": [[0, 1, 0, 0],
          [1, 0, 1, 0],
          [1, 1, 1, 0],
          [1, 0, 1, 0],
          [1, 0, 1, 0]],
    "b": [[1, 1, 1, 0, 0],
          [1, 0, 0, 1, 0],
          [1, 1, 1, 0, 0],
          [1, 0, 0, 1, 0],
          [1, 1, 1, 0, 0]],
    "c": [[0, 1, 1, 1, 0],
          [1, 0, 0, 0, 0],
          [1, 0, 0, 0, 0],
          [1, 0, 0, 0, 0],
          [0, 1, 1, 1, 0]],
    "d": [[1, 1, 0, 0],
          [1, 0, 1, 0],
          [1, 0, 1, 0],
          [1, 0, 1, 0],
          [1, 1, 0, 0]],
    "e": [[1, 1, 1, 0],
          [1, 0, 0, 0],
          [1, 1, 1, 0],
          [1, 0, 0, 0],
          [1, 1, 1, 0]],
    "f": [[0, 1, 1, 1, 0],
          [1, 0, 0, 0, 0],
          [1, 1, 1, 1, 0],
          [1, 0, 0, 0, 0],
          [1, 0, 0, 0, 0]],
    "g": [[0, 1, 1, 1, 0],
          [1, 0, 0, 0, 0],
          [1, 0, 1, 1, 0],
          [1, 0, 0, 1, 0],
          [0, 1, 1, 1, 0]],
    "h": [[1, 0, 0, 1, 0],
          [1, 0, 0, 1, 0],
          [1, 1, 1, 1, 0],
          [1, 0, 0, 1, 0],
          [1, 0, 0, 1, 0]],
    "i": [[1, 1, 1, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [1, 1, 1, 0]],
    "j": [[0, 1, 1, 1, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0],
          [1, 0, 1, 0, 0],
          [1, 1, 1, 0, 0]],
    "k": [[1, 0, 0, 1, 0],
          [1, 0, 1, 0, 0],
          [1, 1, 0, 0, 0],
          [1, 0, 1, 0, 0],
          [1, 0, 0, 1, 0]],
    "l": [[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 1, 1, 0]],
    "m": [[1, 0, 0, 0, 1, 0],
          [1, 1, 0, 1, 1, 0],
          [1, 0, 1, 0, 1, 0],
          [1, 0, 1, 0, 1, 0],
          [1, 0, 0, 0, 1, 0]],
    "n": [[1, 0, 0, 1, 0],
          [1, 1, 0, 1, 0],
          [1, 1, 1, 1, 0],
          [1, 0, 1, 1, 0],
          [1, 0, 0, 1, 0]],
    "o": [[0, 1, 1, 0, 0],
          [1, 0, 0, 1, 0],
          [1, 0, 0, 1, 0],
          [1, 0, 0, 1, 0],
          [0, 1, 1, 0, 0]],
    "p": [[0, 1, 1, 0, 0],
          [1, 0, 0, 1, 0],
          [1, 1, 1, 0, 0],
          [1, 0, 0, 0, 0],
          [1, 0, 0, 0, 0]],
    "q": [[0, 1, 1, 0, 0],
          [1, 0, 0, 1, 0],
          [1, 0, 0, 1, 0],
          [1, 0, 1, 0, 0],
          [0, 1, 0, 1, 0]],
    "r": [[1, 1, 1, 0, 0],
          [1, 0, 0, 1, 0],
          [1, 1, 1, 0, 0],
          [1, 1, 0, 0, 0],
          [1, 0, 1, 0, 0]],
    "s": [[0, 1, 1, 0],
          [1, 0, 0, 0],
          [1, 1, 1, 0],
          [0, 0, 1, 0],
          [1, 1, 0, 0]],
    "t": [[1, 1, 1, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0]],
    "u": [[1, 0, 0, 1, 0],
          [1, 0, 0, 1, 0],
          [1, 0, 0, 1, 0],
          [1, 0, 0, 1, 0],
          [1, 1, 1, 1, 0]],
    "v": [[1, 0, 0, 0, 1, 0],
          [1, 0, 0, 0, 1, 0],
          [0, 1, 0, 1, 0, 0],
          [0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0]],
    "w": [[1, 0, 0, 0, 1, 0],
          [1, 0, 1, 0, 1, 0],
          [1, 0, 1, 0, 1, 0],
          [0, 1, 1, 1, 0, 0],
          [0, 1, 0, 1, 0, 0]],
    "x": [[1, 0, 1, 0],
          [1, 0, 1, 0],
          [0, 1, 0, 0],
          [1, 0, 1, 0],
          [1, 0, 1, 0]],
    "y": [[1, 0, 1, 0],
          [1, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0]],
    "z": [[1, 1, 1, 1, 0],
          [0, 0, 0, 1, 0],
          [0, 0, 1, 0, 0],
          [0, 1, 0, 0, 0],
          [1, 1, 1, 1, 0]],
    ".": [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 0, 0]],
    ",": [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 0, 0],
          [1, 1, 0, 0]],
    "!": [[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]],
    "?": [[1, 1, 1, 0],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 0, 0]],
    " ": [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]],
    "4": [[0, 0, 1, 0],
          [0, 1, 1, 0],
          [1, 0, 1, 0],
          [1, 1, 1, 0],
          [0, 0, 1, 0]],
    "2": [[0, 1, 1, 0, 0],
          [1, 0, 0, 1, 0],
          [0, 0, 1, 1, 0],
          [0, 1, 0, 0, 0],
          [1, 1, 1, 1, 0]],
    "0": [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 0],
          [1, 1, 0, 1, 0],
          [1, 0, 0, 1, 0],
          [0, 1, 1, 0, 0]]
}

TO_MASK_5_5 = [[1, 2, 1, 2, 1],
               [3, 4, 3, 4, 3],
               [1, 2, 1, 2, 1],
               [3, 4, 3, 4, 3],
               [1, 2, 1, 2, 1]]
MASK_BASE = TO_MASK_5_5


def apply_binary_mask(source, mask):
    """both source and mask are expected to be a list, not a 2d array.
    example transformation:
        source = [1, 2, 3, 4, 5]
        mask = [0, 1, 0, 1, 0]
        result: [0, 2, 0, 4, 0]"""
    result = []
    for i, bit in enumerate(mask):
        result_bit = bit if bit == 0 else source[i]
        result.append(result_bit)
    return result


def main(string, bitmap, mask=False, emoji=None):
    if emoji is None:
        emoji = DEFAULT_VALUES
    if None in emoji:
        for i, e in enumerate(emoji):
            if e is None:
                emoji[i] = DEFAULT_VALUES[i]

    if len(emoji) > 5:
        emoji = emoji[:5]
    value_map = dict(enumerate(emoji))

    bit_result = [[] for _ in range(HEIGHT)]
    string = string.lower()
    for char in string:
        if char in bitmap:
            for i in range(HEIGHT):
                if mask:
                    bit_result[i] += apply_binary_mask(MASK_BASE[i], bitmap[char][i])
                else:
                    bit_result[i] += bitmap[char][i]
    def convert_to_str(row):
        result = [value_map[value] for value in row]
        result = "".join(result)
        return result
    bit_result = list(map(convert_to_str, bit_result))
    result = "\n".join(bit_result)
    print(result)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="memes.py")
    parser.add_argument("text", help="text to write out")
    parser.add_argument("--multipart", action="store_true")
    parser.add_argument("--space", help="text value to put for a blank 'pixel'", default=None)
    parser.add_argument("-f", "--filled", help="text to put for a filled 'pixel'", default=None)
    parser.add_argument("-f2", "--filled2", help="a second text value to put for a filled 'pixel'", default=None)
    parser.add_argument("-f3", "--filled3", help="a third text value to put for a filled 'pixel'", default=None)
    parser.add_argument("-f4", "--filled4", help="a fourth text value to put for a filled 'pixel'", default=None)
    parser.add_argument("--mp-pattern", default="[[1, 2, 1, 2, 1], [3, 4, 3, 4, 3], [1, 2, 1, 2, 1], [3, 4, 3, 4, 3], [1, 2, 1, 2, 1]]",
                            help="""Multipart value pattern that bitmasks mask over.  Can contain 0-4, where 0 corresponds to --space, and 1-4 to -f through -f4. 
                            Is expected to be a list of lists that is large enough for all bitmaps to cover.""")
    parser.add_argument("--bitmap", help="ignored.")
    args = parser.parse_args()
    values = [args.space, args.filled, args.filled2, args.filled3, args.filled4]
    main(args.text, LETTER_BITMAPS_5, args.multipart, values)
