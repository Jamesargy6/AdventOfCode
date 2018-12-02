// package day2 contains the solutions to the Day 2 challenge
// of the 2018 Advent of Code challenge.
package day2

import (
	"../utils"
	"fmt"
	"strings"
)

func Day2Part2() {
	input := utils.GetInputFileAsString("day2input.txt")
	lines := strings.Split(input, "\n")
	// compare each line against one another
	for _, line := range lines {
		for _, line2 := range lines {
			diff := 0
			index := 0
			// compare each character against one another
			for idx1, char1 := range line {
				for idx2, char2 := range line2 {
					// count the positional differences between the strings
					if idx1 == idx2 && char1 != char2 {
						diff++
						index = idx1
					}
				}
			}
			// if there wast only one difference, print the common letters between the strings
			if diff == 1 {
				fmt.Println(line[:index] + line[index+1:])
				return
			}
		}

	}
}
