// package day7 contains the solutions to the Day 7 challenge
// of the 2015 Advent of Code challenge.
package day7

import (
	"../utils"
	"encoding/binary"
	"strings"
)

var NOT, AND, OR, LSHIFT, RSHIFT = "NOT", "AND", "OR", "LSHIFT", "RSHIFT"

func Day7Part1() {
	var input = utils.GetInputFileAsString("day7input.txt")
	var lines = strings.Split(input, "\n")
	for _, line := range lines {
		var values map[string]int
		var tokens = strings.Split(line, " ")
		var t1, t2, t3 string
		if tokens[0] == NOT {
			t1 = tokens[1]
			t2 = tokens[3]
			initValue(values, t1)
			initValue(values, t2)

			values[t2] = Not(values[t1])
		} else if len(tokens) > 3{
			t1 = tokens[0]
			t2 = tokens[2]
			t3 = tokens[4]


		} else {
			value, err := strconv.Atoi(tokens[0])
			if err != nil {
				panic(err)
			}
			values[tokens[2]] = value
		}

	}
}

func initValue(values map[string]int, value string){
	if v, ok := values[value]; !ok {
	    values[v] = 0
	}
}

func toByteArray(value int) byte {
	var byte byte
    return binary.LittleEndian.PutUint32(byte, value)
}

func toInt(byte byte) int {
    return binary.LittleEndian.Uint32(byte)
}
func Not(byte byte) byte {
	var oredByte string
	for _, bit := range byte {
		oredByte = oredByte + !bit
	}

}
