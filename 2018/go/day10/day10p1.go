// package day10 contains the solutions to the Day 10 challenge
// of the 2018 Advent of Code challenge.
package day10

import (
	"../utils"
	"fmt"
	"strings"
	"strconv"
	"regexp"
	"time"
)

type Point struct {
	pos []int
	vel []int
}

var points []Point

var minGridX, maxGridX, minGridY, maxGridY = 0,0,0,0

func Day10Part1() {
	input := utils.GetInputFileAsString("day10input.txt")
	lines := strings.Split(input, "\n")
	for _, line := range lines {
		points = append(points, buildPoint(line))

	}
	
	for {
		fmt.Println("iter")
		printGrid()
		movePoints()
		time.Sleep(1000 * time.Millisecond)
	}
}

func buildPoint(line string) Point {
	var p Point
	re := regexp.MustCompile("([-]*[0-9]+)")
	parts := re.FindAllString(line, -1)
	x, _ := strconv.Atoi(parts[0])
	y, _ := strconv.Atoi(parts[1])
	if x < minGridX {
		minGridX = x
	}
	if x > maxGridX {
		maxGridX = x
	}
	if y < minGridY {
		minGridY = y
	}
	if y > maxGridY {
		maxGridY = y
	}
	p.pos = append(p.pos, x)
	p.pos = append(p.pos, y)
	velx, _ := strconv.Atoi(parts[2])
	vely, _ := strconv.Atoi(parts[3])
	p.vel = append(p.vel, velx)
	p.vel = append(p.vel, vely)
	return p
}

func printGrid() {
	gridLength := Abs(maxGridY) + Abs(minGridY)
	gridWidth := Abs(maxGridX) + Abs(minGridX)
	grid:= make([][]string, gridWidth+1)
	for i:=0;i<=gridWidth;i++ {
	    grid[i] = make([]string, gridLength+1)
	}
	for i := 0; i < gridWidth; i++ {
		for j := 0; j < gridLength; j++ {
			grid[i][j] = "-"
		}
	}
	for _, p := range points {
		fmt.Println(p.pos[0]+Abs(minGridX), p.pos[1]+Abs(minGridY))
		grid[p.pos[0]+Abs(minGridX)][p.pos[1]+Abs(minGridY)] = "#"
	}

	for _, row := range grid {
		for _, char := range row {
			fmt.Print(char)
		}
		fmt.Println("")
	}
}

func movePoints() {
	for _, p := range points {
		p.pos[0] += p.vel[0]
		p.pos[1] += p.vel[1]
	}
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}