// package day4 contains the solutions to the Day 4 challenge
// of the 2015 Advent of Code challenge.
package day4

import (
	"crypto/md5"
	"strconv"
	"fmt"
	"encoding/hex"
)

func Day4Part1() {
	var input = "iwrupvqb"
	index := 1
	for true {
		data := []byte(input + strconv.Itoa(index))
		output := md5.Sum(data)
		outputString := hex.EncodeToString(output[:3])
		if string(outputString[:5]) == "00000" {
			fmt.Println(index)
			return
		}
		index++
	}
	
}
