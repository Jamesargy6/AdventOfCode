// package day6 contains the solutions to the Day 6 challenge
// of the 2015 Advent of Code challenge.
package day6

import (
	"../utils"
	"fmt"
	"strconv"
	"strings"
)

func Day6Part2() {

	var grid = make([][]int, 1000)
	for i := range grid {
		grid[i] = make([]int, 1000)
	}

	var input = utils.GetInputFileAsString("day6input.txt")
	var lines = strings.Split(input, "\n")
	for _, line := range lines {
		//EXAMPLE turn on 489,959 through 759,964
		tokens := strings.Split(line, " ")
		isToggle := tokens[0] == "toggle"
		var point1Tokens, point2Tokens []string
		if isToggle {
			point1Tokens = strings.Split(tokens[1], ",")
			point2Tokens = strings.Split(tokens[3], ",")
		} else {
			point1Tokens = strings.Split(tokens[2], ",")
			point2Tokens = strings.Split(tokens[4], ",")
		}
		var coord1 []int
		c1x, err := strconv.Atoi(point1Tokens[0])
		c1y, err := strconv.Atoi(point1Tokens[1])
		if err != nil {
			panic(err)
		}
		coord1 = append(coord1, c1x)
		coord1 = append(coord1, c1y)

		var coord2 []int
		c2x, err := strconv.Atoi(point2Tokens[0])
		c2y, err := strconv.Atoi(point2Tokens[1])
		if err != nil {
			panic(err)
		}
		coord2 = append(coord2, c2x)
		coord2 = append(coord2, c2y)

		xMin := coord1[0]
		xMax := coord2[0]

		yMin := coord1[1]
		yMax := coord2[1]

		for i := xMin; i <= xMax; i++ {
			for j := yMin; j <= yMax; j++ {
				if isToggle {
					grid[i][j] += 2
				} else {
					turnOn := tokens[1] == "on"
					if turnOn {
						grid[i][j] += 1
					} else {
						grid[i][j] -= 1
						if grid[i][j] < 0 {
							grid[i][j] = 0
						}
					}
				}
			}
		}
	}

	brightness := 0
	for _, row := range grid {
		for _, b := range row {
			brightness += b
		}
	}
	fmt.Println(brightness)

}
