import re


reaction_regex = r'([a-zA-Z])(?!\1)(?i:\1)'


def part_1(input_string):
    while True:
        input_length = len(input_string)
        input_string = re.sub(reaction_regex, r'', input_string)
        new_length = len(input_string)
        if input_length == new_length:
            break
    return input_length


def part_2(input_string):
    polymer_substring_lengths = []
    for polymer in range(ord('a'), ord('z')+1):
        stripped_polymer_string = re.sub(rf'(?i:{chr(polymer)})', r'', input_string)
        polymer_substring_lengths.append(part_1(stripped_polymer_string))
    return min(polymer_substring_lengths)


if __name__ == '__main__':
    input_string = open('./input.txt').read()
    print(part_1(input_string))
    print(part_2(input_string))

