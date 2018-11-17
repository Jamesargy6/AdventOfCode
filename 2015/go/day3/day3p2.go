// package day3 contains the solutions to the Day 3 challenge
// of the 2015 Advent of Code challenge.
package day3

import (
	"../utils"
	"fmt"
)

func Day3Part2() {
	var input = utils.GetInputFileAsString("day3input.txt")
	visitedCoords := make(map[Coord]bool)
	var coordPointers = []Coord{{0, 0}, {0, 0}}
	visitedCoords[Coord{0, 0}] = true
	for index, direction := range input {
		currentCoord := coordPointers[index%2]
		if direction == '^' {
			currentCoord.y++
		} else if direction == 'v' {
			currentCoord.y--
		} else if direction == '>' {
			currentCoord.x++
		} else if direction == '<' {
			currentCoord.x--
		}
		visitedCoords[currentCoord] = true
		coordPointers[index%2] = currentCoord
	}
	fmt.Println(len(visitedCoords))
}
