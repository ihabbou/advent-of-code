package main

import (
	"fmt"
	"strconv"
	"strings"
)

func Day2_1() {
	input := `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green`

	for _, game := range strings.Split(input, "\n") {
		gameid, _ := strconv.Atoi(strings.Replace(strings.Split(game, ":")[0], "Game ", "", -1))
		fmt.Println((gameid))

		sets := strings.Split(strings.Split(game, ": ")[1], "; ")
		for _, pull := range sets {

			fmt.Println(strings.Split(pull, ", "))
		}

	}
}

func main() {
	Day2_1()
}
