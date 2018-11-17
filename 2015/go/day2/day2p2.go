// package day2 contains the solutions to the Day 2 challenge
// of the 2015 Advent of Code challenge.
package day2

import (
	"../utils"
	"fmt"
	"strconv"
	"strings"
	"math"
)

func Day2Part2() {
	var input = utils.GetInputFileAsString("day2input.txt")
	var lines = strings.Split(input, "\n")
	var total = 0
	for _, equation := range lines {
		var dim = strings.Split(equation, "x")
		l, err := strconv.Atoi(dim[0])
		w, err := strconv.Atoi(dim[1])
		h, err := strconv.Atoi(dim[2])
		if err != nil {
			panic(err)
		}
		perims := []int{(2 * l) + (2 * w), (2 * l) + (2 * h), (2 * w) + (2 * h)}
		smallestPerim := math.MaxUint32
		for _, perim := range perims {
			if perim < smallestPerim {
				smallestPerim = perim
			}
		}
		total += smallestPerim + (l * w * h)
	}
	fmt.Println(total)

}
