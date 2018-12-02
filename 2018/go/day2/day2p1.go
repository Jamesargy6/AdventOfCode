// package day2 contains the solutions to the Day 2 challenge
// of the 2018 Advent of Code challenge.
package day2

import (
	"../utils"
	"fmt"
	"strings"
)

func Day2Part1() {
	input := utils.GetInputFileAsString("day2input.txt")
	lines := strings.Split(input, "\n")
	doubles := make(map[string]bool)
	triples := make(map[string]bool)
	for _, line := range lines {
		charCount := make(map[rune]int)
		// count the number of appearances for each character
		for _, char := range line {
			charCount[char] += 1
		}
		for _, count := range charCount {
			// record whether some character appeared exactly twice
			if count == 2 {
				doubles[line] = true
			}
			// record whether some character appeared exactly three times
			if count == 3 {
				triples[line] = true
			}
		}

	}
	// multiply our counts together
	fmt.Println(len(doubles) * len(triples))
}
