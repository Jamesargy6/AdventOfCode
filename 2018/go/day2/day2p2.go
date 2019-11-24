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
			diffIndex := 0
			// compare each character against one another
			for idx, _ := range line {
				// count the positional differences between the strings
				if line[idx] != line2[idx] {
					diff++
					diffIndex = idx
				}
			}
			// if there was only one difference, print the common letters between the strings
			if diff == 1 {
				fmt.Println(line[:diffIndex] + line[diffIndex+1:])
				return
			}
		}

	}
}
