// package day6 contains the solutions to the Day 6 challenge
// of the 2018 Advent of Code challenge.
package day6

import (
	"../utils"
	"fmt"
	"strings"
	"strconv"
)

type Coord struct {
	id rune
	closestTo rune
	X int
	Y int
	mDistance int
}

var grid [][]Coord
var nodes []Coord
var closestToNodeMap map[rune][]Coord

func Day6Part1() {
	input := utils.GetInputFileAsString("day6input.txt")
	// parse the input into a list of coords
	coordStrings := strings.Split(input, "\n")
	for _, cs := range coordStrings {
		strs := strings.Split(cs, ", ")
		x, _ := strconv.Atoi(strs[0])
		y, _ := strconv.Atoi(strs[1])
		coord := Coord {
			X : x,
			Y : y,
		}
		nodes = append(nodes, coord)
	}
	fmt.Println(nodes)


}
