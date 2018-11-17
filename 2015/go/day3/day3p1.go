// package day3 contains the solutions to the Day 3 challenge
// of the 2015 Advent of Code challenge.
package day3

import (
	"../utils"
	"fmt"
)

type Coord struct {
	x int
	y int
}

func Day3Part1() {
	var input = utils.GetInputFileAsString("day3input.txt")
	visitedCoords := make(map[Coord]bool)
	x, y := 0, 0
	visitedCoords[Coord{x, y}] = true
	for _, direction := range input {
		if direction == '^' {
			y++
		} else if direction == 'v' {
			y--
		} else if direction == '>' {
			x++
		} else if direction == '<' {
			x--
		}
		visitedCoords[Coord{x, y}] = true
	}
	fmt.Println(len(visitedCoords))
}
