package main

import "fmt"

func Adder(numb ...int) int {
	total := 0
	for _, i := range numb {
		fmt.Printf("Individual number which is getting added %d\n", i)
		total += i
		fmt.Printf("Total: %d\n", total)
	}
	return total
}

func main() {
	num := []int{1, 2, 3}
	fmt.Println(Adder(num...))

}
