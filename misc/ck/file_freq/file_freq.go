package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
	"time"

	"github.com/pkg/errors"
)

const (
	_fileName       = "file.log"
	_colNumLoglevel = 1
	_colNumTS       = 0
	_tsLayout       = "2006-01-02T15:04:05"
	// _tsLayout = time.RFC3339Nano
)

type LogCounter struct {
	lines    []string
	tsColumn int
	tsLayout string
}

func NewLogCounter(fname string, tsColumn int, tsLayout string) (*LogCounter, error) {
	fbytes, err := ioutil.ReadFile(fname)
	if err != nil {
		return nil, errors.Wrap(err, "initializing LogCounter")
	}
	lines := strings.Split(string(fbytes), "\n")
	lines = lines[:len(lines)-1] // trim the last empty line

	return &LogCounter{
		lines:    lines,
		tsColumn: tsColumn,
		tsLayout: tsLayout,
	}, nil
}

func (c *LogCounter) CountFreqTotal(countColumn int) map[string]int {
	count := make(map[string]int)

	for _, line := range c.lines {
		columns := strings.Split(line, " ")
		var columnValue string
		if len(columns) >= countColumn+1 {
			columnValue = columns[countColumn]
			count[columnValue] += 1
		}
	}

	return count
}

func (c *LogCounter) CountFreqTimeInterval(countColumn int, startTS, endTS time.Time) map[string]int {
	var err error
	count := make(map[string]int)

	lineStart, err := c.getLineStart(startTS, endTS)
	if err != nil {
		return count
	}

	for i := lineStart; i < len(c.lines); i++ {
		columns := strings.Split(c.lines[i], " ")
		lineTS, err := c.getLineTS(c.lines[i])
		if err != nil {
			return count
		}
		if lineTS.After(endTS) {
			// we reached the end of the interval
			break
		}

		var columnValue string
		if len(columns) >= countColumn+1 {
			columnValue = columns[countColumn]
			count[columnValue] += 1
			// fmt.Printf("%v count %v for %v\n", i, columnValue, lineTS) // FIXME: DEBUG
		}
	}

	return count
}

func (c *LogCounter) getLineStart(startTS, endTS time.Time) (int, error) {
	var err error

	// bin search
	lineFound := -1
	lineL := 0
	lineR := len(c.lines) - 1
	var lineMid int
	var lineMidTS time.Time
	for lineR-lineL > 1 {
		lineMid = (lineL + lineR) / 2
		lineMidTS, err = c.getLineTS(c.lines[lineMid])
		if err != nil {
			return -1, err
		}

		if lineMidTS.After(startTS) {
			lineR = lineMid
		} else {
			lineL = lineMid
		}
	}
	lineLTS, _ := c.getLineTS(c.lines[lineL])
	lineRTS, _ := c.getLineTS(c.lines[lineR])
	// found startTS or at least startTS < closestTS < endTS
	if lineLTS == startTS || (lineLTS.After(startTS) && !lineLTS.After(endTS)) {
		lineFound = lineL
	} else if lineRTS == startTS || (lineRTS.After(startTS) && !lineRTS.After(endTS)) {
		lineFound = lineR
	} else {
		// not found
		return -1, errors.New("not found")
	}

	// find the 1st TS=startTS in the log
	lineStart := lineFound
	lineFoundTS, _ := c.getLineTS(c.lines[lineFound])
	for i := lineFound; i >= 0; i-- {
		lineTS, _ := c.getLineTS(c.lines[i])
		if lineTS != lineFoundTS {
			lineStart = i + 1
			break
		}
	}

	return lineStart, nil
}

func (c *LogCounter) getLineTS(line string) (time.Time, error) {
	columns := strings.Split(line, " ")
	if c.tsColumn > len(c.lines)-1 {
		return time.Time{}, errors.New("wrong TS column number")
	}
	strTS := columns[c.tsColumn]
	ts, err := time.Parse(c.tsLayout, strTS)

	return ts, err
}

func printCount(c map[string]int) {
	for k, v := range c {
		fmt.Printf("Count: %v: %v\n", k, v)
	}
}

// func getFile(name string) io.ReadCloser {
// 	f, err := os.Open(name)
// 	if err != nil {
// 		fmt.Println(err)
// 		os.Exit(1)
// 	}

// 	return f
// }

// // countFreq_lineByLine reads file line by line
// func countFreq_lineByLine(f io.ReadCloser) map[string]int {
// 	defer f.Close()

// 	count := make(map[string]int)

// 	s := bufio.NewScanner(f)
// 	for s.Scan() {
// 		columns := strings.Split(s.Text(), " ")
// 		var loglevel string
// 		if len(columns) >= 2 {
// 			loglevel = columns[1]
// 			count[loglevel] += 1
// 		}
// 	}
// 	err := s.Err()
// 	if err != nil {
// 		fmt.Println(err)
// 		os.Exit(1)
// 	}

// 	return count
// }

func main() {
	// fmt.Println("\ncountFreq_entireFile()")
	// count := countFreq_entireFile()
	// printCount(count)

	counter, err := NewLogCounter(_fileName, _colNumTS, _tsLayout)
	if err != nil {
		os.Exit(1)
	}

	fmt.Println("\ntotal count")
	totalCount := counter.CountFreqTotal(_colNumLoglevel)
	printCount(totalCount)

	// L, R inside the log
	fmt.Println("\n..L.R.")
	startTS := time.Date(2022, 10, 16, 21, 22, 5, 0, time.UTC)
	endTS := time.Date(2022, 10, 16, 21, 22, 7, 0, time.UTC)
	fmt.Printf("ts interval count: %v ... %v\n", startTS, endTS)
	intervalCount := counter.CountFreqTimeInterval(_colNumLoglevel, startTS, endTS)
	printCount(intervalCount)

	fmt.Println("\n..L=R.")
	startTS = time.Date(2022, 10, 16, 21, 22, 5, 0, time.UTC)
	endTS = time.Date(2022, 10, 16, 21, 22, 5, 0, time.UTC)
	fmt.Printf("ts interval count: %v ... %v\n", startTS, endTS)
	intervalCount = counter.CountFreqTimeInterval(_colNumLoglevel, startTS, endTS)
	printCount(intervalCount)

	fmt.Println("\n..L.R. (not exactly)")
	startTS = time.Date(2022, 10, 16, 21, 22, 9, 0, time.UTC)
	endTS = time.Date(2022, 10, 16, 21, 22, 12, 0, time.UTC)
	fmt.Printf("ts interval count: %v ... %v\n", startTS, endTS)
	intervalCount = counter.CountFreqTimeInterval(_colNumLoglevel, startTS, endTS)
	printCount(intervalCount)

	fmt.Println("\n..L=R. (not exactly)")
	startTS = time.Date(2022, 10, 16, 21, 22, 9, 0, time.UTC)
	endTS = time.Date(2022, 10, 16, 21, 22, 9, 0, time.UTC)
	fmt.Printf("ts interval count: %v ... %v\n", startTS, endTS)
	intervalCount = counter.CountFreqTimeInterval(_colNumLoglevel, startTS, endTS)
	printCount(intervalCount)

	// L, R outside the log
	fmt.Println("\n...... LR")
	startTS = time.Date(2022, 10, 16, 21, 22, 59, 0, time.UTC)
	endTS = time.Date(2022, 10, 16, 21, 22, 60, 0, time.UTC)
	fmt.Printf("ts interval count: %v ... %v\n", startTS, endTS)
	intervalCount = counter.CountFreqTimeInterval(_colNumLoglevel, startTS, endTS)
	printCount(intervalCount)

	fmt.Println("\nLR  ......")
	startTS = time.Date(2022, 10, 16, 21, 22, 1, 0, time.UTC)
	endTS = time.Date(2022, 10, 16, 21, 22, 2, 0, time.UTC)
	fmt.Printf("ts interval count: %v ... %v\n", startTS, endTS)
	intervalCount = counter.CountFreqTimeInterval(_colNumLoglevel, startTS, endTS)
	printCount(intervalCount)

	fmt.Println("\nL  ......  R")
	startTS = time.Date(2022, 10, 16, 21, 22, 1, 0, time.UTC)
	endTS = time.Date(2022, 10, 16, 21, 22, 59, 0, time.UTC)
	fmt.Printf("ts interval count: %v ... %v\n", startTS, endTS)
	intervalCount = counter.CountFreqTimeInterval(_colNumLoglevel, startTS, endTS)
	printCount(intervalCount)

	// L, R inside/outside the log
	fmt.Println("\nL  ....R.")
	startTS = time.Date(2022, 10, 16, 21, 22, 1, 0, time.UTC)
	endTS = time.Date(2022, 10, 16, 21, 22, 7, 0, time.UTC)
	fmt.Printf("ts interval count: %v ... %v\n", startTS, endTS)
	intervalCount = counter.CountFreqTimeInterval(_colNumLoglevel, startTS, endTS)
	printCount(intervalCount)

	fmt.Println("\n..L...  R")
	startTS = time.Date(2022, 10, 16, 21, 22, 5, 0, time.UTC)
	endTS = time.Date(2022, 10, 16, 21, 22, 59, 0, time.UTC)
	fmt.Printf("ts interval count: %v ... %v\n", startTS, endTS)
	intervalCount = counter.CountFreqTimeInterval(_colNumLoglevel, startTS, endTS)
	printCount(intervalCount)
}
