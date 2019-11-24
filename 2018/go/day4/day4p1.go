// package day4 contains the solutions to the Day 4 challenge
// of the 2018 Advent of Code challenge.
package day4

import (
	"../utils"
	"fmt"
	"strings"
	"time"
	"sort"
	"strconv"
)

type Log struct {
	logString string
	date time.Time
	guardNumber int
	isStart bool
	isAsleep bool
}



type Guard struct {
	guardNumber int
	minsAsleep float64
	sectionsAsleep [][]time.Time
}

var logs []Log
var guards  = make(map[int]*Guard)

func Day4Part1() {
	input := utils.GetInputFileAsString("day4input.txt")
	logStrings := strings.Split(input, "\n")
	for _, ls := range logStrings {
		logs = append(logs, makeLogFromString(ls))
	}
	sort.Slice(logs[:], func(i, j int) bool {
		return logs[i].date.Before(logs[j].date)
	})

	var currentGuardNumber int
	var currentGuard Guard
	var asleepLogStart time.Time
	for _, log := range logs {
		if log.guardNumber > 0 {
			currentGuardNumber = log.guardNumber
			//fmt.Println(currentGuardNumber)
			if _, ok := guards[currentGuardNumber]; !ok {
				currentGuard := new(Guard)
				currentGuard.guardNumber = currentGuardNumber
				guards[currentGuard.guardNumber] = currentGuard
			} else {
				currentGuard = *guards[currentGuardNumber]
			}
			
		} else {
			if log.isAsleep {
				asleepLogStart = log.date
			} else if log.date.Sub(asleepLogStart).Minutes() <= 90 {
				//section := []time.Time {asleepLogStart, log.date}
				//currentGuard.sectionsAsleep = append(currentGuard.sectionsAsleep, section)
				currentGuard.minsAsleep += log.date.Sub(asleepLogStart).Minutes()
				fmt.Println(currentGuard)
				guards[currentGuard.guardNumber] = &currentGuard
			}
		}
	}

	var sleepiestGuard = *new(Guard)
	for _, guard := range guards {
		fmt.Println(*guard)
		if sleepiestGuard.guardNumber == 0 || sleepiestGuard.minsAsleep < guard.minsAsleep {
			sleepiestGuard = *guard
		}
	}
	fmt.Println(sleepiestGuard.minsAsleep)
}

func makeLogFromString(ls string) Log {
	var newLog Log
	newLog.logString = ls

	date := ls[1:17]
	date += ":00Z"
	date = strings.Replace(date, " ", "T", -1)
	t, err := time.Parse(time.RFC3339, date)
	if err != nil {
		panic(err)
	}
	newLog.date = t
	str := ls[19:]
	sections := strings.Split(str, " ")
	if sections[0] == "Guard" {
		newLog.guardNumber, _ = strconv.Atoi(sections[1][1:])
		newLog.isStart = sections[2] == "begins"
	} else if sections[0] == "wakes" {
		newLog.isAsleep = true
	}
	return newLog
}
