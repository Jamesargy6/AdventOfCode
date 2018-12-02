// package day1 contains the solutions to the Day 1 challenge
// of the 2018 Advent of Code challenge.
package day1

import (
	"../utils"
	"fmt"
	"strconv"
	"strings"
)

func Day1Part2() {
	var result = 0
	visitedCoords := make(map[int]bool)
	var input = utils.GetInputFileAsString("day1input.txt")
	var freqChanges = strings.Split(input, "\n")
	for true {
		for _, fq := range freqChanges {
			var plusMinus = fq[0]
			var amtStr = fq[1:]
			amt, _ := strconv.Atoi(amtStr)
			if plusMinus == '+' {
				result += amt
			} else {
				result -= amt
			}
			if visitedCoords[result] == true {
				fmt.Println(result)
				return
			} else {
				visitedCoords[result] = true
			}
		}
	}
}
