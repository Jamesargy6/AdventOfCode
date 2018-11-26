// package day5 contains the solutions to the Day 5 challenge
// of the 2015 Advent of Code challenge.
package day5

import (
	"../utils"
	"fmt"
	"strings"
)

func Day5Part2() {
	niceStrings := 0
	var input = utils.GetInputFileAsString("day5input.txt")
	var lines = strings.Split(input, "\n")
	for _, line := range lines {
		var pairs []string
		var currentChar, lastChar rune
		// initialize pair array
		for _, char := range line {
			currentChar = char
			if lastChar != 0 {
				charPair := string(lastChar) + string(currentChar)
				pairs = append(pairs, charPair)
			}
			lastChar = currentChar
		}

		hasMatchingPairs, hasSandwich := false, false
		for i, p1 := range pairs {
			for j, p2 := range pairs {
				if i != j {
					if i != j+1 && i != j-1 {
						if p1 == p2 {
							hasMatchingPairs = true
						}
					} else if i == j-1 {
						if p1[0] == p2[1] {
							hasSandwich = true
						}
					}
				}
			}
		}
		if hasMatchingPairs && hasSandwich {
			niceStrings += 1
		}
	}
	fmt.Println(niceStrings)
}
