// package day1 contains the solutions to the Day 1 challenge
// of the 2018 Advent of Code challenge.
package day1

import (
	"../utils"
	"fmt"
	"strconv"
	"strings"
)

func Day1Part1() {
	var result = 0
	var input = utils.GetInputFileAsString("day1input.txt")
	var freqChanges = strings.Split(input, "\n")
	for _, fq := range freqChanges {
		var plusMinus = fq[0]
		var amtStr = fq[1:]
		amt, err := strconv.Atoi(amtStr)
		if err != nil {
			panic(err)
		}
		if plusMinus == '+' {
			result += amt
		} else {
			result -= amt
		}
	}

	fmt.Println(result)
}
