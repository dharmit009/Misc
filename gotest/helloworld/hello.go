package main

import "fmt"

//Globalvars
const englishHelloPrefix = "Hello, "

func Hello(name string) string {
	if name == "" {
		name = "world"
	}
	return englishHelloPrefix + name

}

func main() {

	fmt.Println(Hello("world"))
	fmt.Println(Hello(""))

}
