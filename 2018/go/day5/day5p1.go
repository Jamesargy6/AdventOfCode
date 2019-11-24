// package day5 contains the solutions to the Day 5 challenge
// of the 2018 Advent of Code challenge.
package day5

import (
	"../utils"
	"fmt"
)

func Day5Part1() {
	input := utils.GetInputFileAsString("day5input.txt")
	iters := 0
	for {
		
		iters += 1
		for idx, _ := range input {
			if idx < len(input)-2 {
				char1 := input[idx]
				char2 := input[idx+1]

				if min(char1, char2) + 26 == max(char1, char2) {
					
					input = input[:idx] + input[idx+1:]
					fmt.Println(len(input))
				}
			}
		}
	}
	fmt.Println(len(input))
	fmt.Println(len(input))
	fmt.Println(len(input))
}

func min(a byte, b byte) byte {
	if a<b {
		return a
	} else {
		return b
	}
}

func max(a byte, b byte) byte {
	if a>b {
		return a
	} else {
		return b
	}
}
