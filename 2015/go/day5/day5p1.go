// package day5 contains the solutions to the Day 5 challenge
// of the 2015 Advent of Code challenge.
package day5

import (
	"../utils"
	"fmt"
	"strings"
)

var vowels = []rune{'a', 'e', 'i', 'o', 'u'}
var badStrings = []string{"ab", "cd", "pq", "xy"}

func Day5Part1() {
	niceStrings := 0
	var input = utils.GetInputFileAsString("day5input.txt")
	var lines = strings.Split(input, "\n")
	for _, line := range lines {
		hasDouble, hasBadString := false, false
		vowelsCount := 0
		var currentChar, lastChar rune
		for _, char := range line {
			currentChar = char
			if lastChar != 0 {
				if lastChar == currentChar {
					hasDouble = true
				}
				charPair := string(lastChar) + string(currentChar)
				for _, bs := range badStrings {
					if bs == charPair {
						hasBadString = true
						break
					}
				}
			}
			if hasBadString {
				break
			}
			for _, vowel := range vowels {
				if char == vowel {
					vowelsCount += 1
				}
			}
			lastChar = currentChar
		}
		if hasDouble && vowelsCount >= 3 && !hasBadString {
			niceStrings++
		}
	}
	fmt.Println(niceStrings)
}
