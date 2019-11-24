import sys
from typing import List


def generate_new_recipes(elf_indexes: List[int], recipe_scores: List[int]):
    new_recipe_score = sum(recipe_scores[ei] for ei in elf_indexes)
    recipe_tens = new_recipe_score // 10
    recipe_ones = new_recipe_score % 10
    if recipe_tens > 0:
        recipe_scores.append(recipe_tens)
    recipe_scores.append(recipe_ones)


if __name__ == '__main__':
    part = int(sys.argv[2])
    recipe_scores = [3, 7]
    elf_indexes = [0, 1]

    if part == 1:
        input = int(sys.argv[1])
        required_length = input + 10
        while len(recipe_scores) < required_length:
            generate_new_recipes(elf_indexes, recipe_scores)
            elf_indexes = [(ei+recipe_scores[ei]+1) % len(recipe_scores) for ei in elf_indexes]

        print(''.join([str(score) for score in recipe_scores[input:required_length]]))

    if part == 2:
        input = sys.argv[1]
        while [int(x) for x in input] not in [recipe_scores[-len(input)-x:-x] for x in range(2)]:
            generate_new_recipes(elf_indexes, recipe_scores)
            elf_indexes = [(ei + recipe_scores[ei] + 1) % len(recipe_scores) for ei in elf_indexes]
        print(len(recipe_scores)-len(sys.argv[1])-1)

