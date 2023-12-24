package main

import (
	"fmt"
	"strconv"
	"strings"
)

func Day1_2() {

	digi := []string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}

	input := `two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen`
	// inputf, err := os.ReadFile("input1.txt")
	// if err != nil {
	// 	panic(err)
	// }
	// input = string(inputf)

	var numbers []int = []int{}
	var sumn int = 0

	for _, line := range strings.Split(input, "\n") {
		var left, right byte = 'n', 'n'

		// for i, char := range line {
		for i := 0; i < len(line); i++ {

			// if line[i] >= 48 && line[i] <= 57 {
			if left == 'n' && (line[i] >= '0' && line[i] <= '9') {
				left = line[i]
			}
			if right == 'n' && (line[len(line)-i-1] >= '0' && line[len(line)-i-1] <= '9') {
				right = line[len(line)-i-1]
			}
			if left != 'n' && right != 'n' {
				break
			}
		}

		num, err := strconv.Atoi(string(left) + string(right))
		if err != nil {
			num = 0
		}
		numbers = append(numbers, num)
		sumn += num

	}
	// fmt.Println(numbers)

	// sum := func(numbers []int) int {
	// 	var sum int = 0
	// 	for _, num := range numbers {
	// 		sum += num
	// 	}
	// 	return sum
	// }
	fmt.Println(sumn)

}
