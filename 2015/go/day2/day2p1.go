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

func Day2Part1() {
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
		sides := []int{l * w, l * h, w * h}
		smallestSide := math.MaxUint32
		for _, side := range sides {
			if side < smallestSide {
				smallestSide = side
			}
		}
		total += (2 * ((l * w) + (l * h) + (w * h))) + smallestSide
	}
	fmt.Println(total)

}
