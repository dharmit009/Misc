package main

import "fmt"

//Globalvars
const spanish = "Spanish"
const french = "French"
const englishHelloPrefix = "Hello, "
const spanishHolaPrefix = "Hola, "
const frenchBonjourPrefix = "Bonjour, "

func Hello(name string, lang string) string {

	if name == "" {
		name = "world"
	} // if

	//	if lang == spanish {
	//		return spanishHolaPrefix + name
	//
	//	} //if
	//
	//	if lang == french {
	//		return frenchBonjourPrefix + name
	//
	//	} //if
	//
	//	return englishHelloPrefix + name

	// converted the entire blokc to switch case.

	return greetingPrefix(lang) + name

}

func greetingPrefix(lang string) (prefix string) {

	switch lang {
	case french:
		prefix = frenchBonjourPrefix
	case spanish:
		prefix = spanishHolaPrefix
	default:
		prefix = englishHelloPrefix
	}
	return
}

func main() {

	fmt.Println(Hello("world", ""))
	fmt.Println(Hello("", ""))
	fmt.Println(Hello("El", "jordan"))
	fmt.Println(Hello("El", "Spanish"))
	fmt.Println(Hello("RWXrob", "French"))

}
