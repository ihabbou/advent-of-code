// dynamically runs a file based on input number
// files are in the format of day{number}.go
package main

func main21() {
	Day1_1()
}

// func main1() {

// 	// get the day number from the command line
// 	day := os.Args[1]

// 	// use reflection to call the function with the name "Day" + day
// 	funcName := "Day" + day
// 	funcValue := reflect.ValueOf(run)
// 	funcType := funcValue.Type()
// 	funcArgTypes := funcType.In()
// 	funcArgs := make([]reflect.Value, len(funcArgTypes))
// 	for i, argType := range funcArgTypes {
// 		funcArgs[i] = reflect.New(argType).Elem()
// 	}
// 	funcValue.Call(nil)

// 	// convert the day number to an int
// 	// dayInt, _ := strconv.Atoi(day)

// 	// get the current directory
// 	dir, _ := os.Getwd()
// 	// get the path to the file
// 	path := filepath.Join(dir, "day"+day+".go")
// 	// check if the file exists
// 	if _, err := os.Stat(path); os.IsNotExist(err) {
// 		fmt.Println("File does not exist")
// 		return
// 	}
// 	// run the file
// 	runFile(path)
// }
// func runFile(path string) {
// 	// read the file
// 	data, err := ioutil.ReadFile(path)
// 	if err != nil {
// 		log.Fatal(err)
// 	}
// 	// split the file into lines
// 	lines := strings.Split(string(data), "\n")
// 	// run the file
// 	run(lines)
// }
// func run(lines []string) {
// 	// get the current directory
// 	dir, _ := os.Getwd()
// 	// get the path to the file
// 	path := filepath.Join(dir, "day"+strconv.Itoa(time.Now().Day())+".go")
// 	// check if the file exists
// 	if _, err := os.Stat(path); os.IsNotExist(err) {
// 		fmt.Println("File does not exist")
// 		return
// 	}
// 	// run the file
// 	runFile(path)
// }
