// package day1 contains the solutions to the Day 1 challenge
// of the 2015 Advent of Code challenge.
package day1

import (
	"../utils"
	"fmt"
)

func Day1Part1() {
	var input = utils.GetInputFileAsString("day1input.txt")
	var floor = 0;
	for _, char := range input {
		if(char == '(') {
			floor += 1
		} else {
			floor -= 1
		}
	}
	fmt.Println(floor)
}
