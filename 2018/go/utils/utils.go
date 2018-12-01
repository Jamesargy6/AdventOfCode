// package utils holds a set of useful file i/o functions that will be useful 
// across most AdventOfCode solutions. 
package utils

import (
	"io/ioutil"
	"os"
	"path/filepath"
)

// GetInputFileAsString access the passed in file name in the /inputs directory
// and returns it as a string
func GetInputFileAsString(fileName string) string {
	wd,err := os.Getwd()
	if err != nil {
	    panic(err)
	}
	parent := filepath.Dir(wd)
	dat, err := ioutil.ReadFile(parent + "/go/inputs/" + fileName)
    check(err)
    return string(dat)
} 

// check is a helper function to quickly handle errors
func check(e error) {
    if e != nil {
        panic(e)
    }
}
