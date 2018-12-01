package main

import (
	. "./day1"
	"errors"
	"os"
	"strconv"
)

// declare some error types
var WrongNumberOfArgs = errors.New("Wrong number of Arguments passed in. Correct Number of Arguments: 2")
var WrongTypeOfArgs = errors.New("Program arguments invalid. Expecting integer arguments")

// initialize the list of solution functions
// we will use this list to quickly reference and run the correct solution based on the parameters passed into main
var solutions = [][]func(){
	{Day1Part1, Day1Part2}}

// main is the entry point for running all AdventOfCode solutions. it expects two integer arguments to be bassed in,
// representing the "day" and "part" of the solution we'd like to run.
func main() {
	var day, part = parseArgs()
	solutions[day][part]()
}

// parseArgs accesses the arguments used to run the program, and translates them
// into the day/part parameters for choosing what solution to run.
func parseArgs() (int, int) {
	args := os.Args[1:]
	if len(args) != 2 {
		panic(WrongNumberOfArgs)
	}
	day, err := strconv.Atoi(args[0])
	day -= 1
	part, err := strconv.Atoi(args[1])
	part -= 1
	if err != nil {
		panic(WrongTypeOfArgs)
	}
	return day, part
}
