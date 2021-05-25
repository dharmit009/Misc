# Hello World...
# Go Documentation.....

This probably must the highest rated feature of any language. GO has inbuilt documentation which you can use anytime you want just run the following: 

`godoc -http :8000`

# How to test ????

To test we seperate domain code from the outside world. 

So basically domains are main part of the program through which we interact.

> fmt.Println() --> this is a side-effect. 

The string which is passed through the function is the "domain" code.

# Importing go modules for testing

To run tests we need to initialize the directory with go mods as we will be running testing library. and we do that by 

> go mod init <name>  

# Importing go packaged for testing

To import testing library you need to add the following line: 

> import "testing"

# Variables 

to declare variables we use a different notation 

varName := value

## How to write test functions ? 

The go programming language works in a very unique way. we can write test functions but there are some rules to declare such test functions. 

Let us see what they are: 
* The test code should be in its own file. 
* The test function should have the word `xxx*_test.go`. 
* The test function should have only one argument `t *testing.T`
	* I don't the reason for that but my best guess would be it will allow to handle all the error through one pointer meaning less code and less gibberish code. 
* To use testing functionalities, you need to import the testing lib.

functions can be decalared and called as a variable. functions 

here is a sample syntax for functions: 

```
func add(n1,n2 int) int {
				return n1+n2
}
```

We can even declare subset functions using Go here is how : 

```
func TestHello(){

t.run("hello", func(arg){

//block of code.
								}
				)
t.run("test", func(arg){

//block of code.

								}
				)
}

```


# if loops. 

if loops are almost same just no parenthesis i.e ();
i.e if got != want {
fmt.Print("hello, world");

}


# Methods
Errorf is a method which simply prints the error when the test is failed. 
***Note:*** The 'f' in the Errorf stands for format which allows us to use placeholder while printing the strings. 

%q wraps the data in "". 

Here are some more of them: 
%d --> prints decimal. 
%b --> prints binary. 
%o --> prints octal. 
%x --> prints hexadecimal. 
%t --> true or false. 

%s --> string values. 
%f --> floating numbers & Precision stuff (.3f) works too. 


---
---
---

# Hello, You. 

## What is TDD cycle ? and how to refactor ? 

* T - Test
* D - Driven 
* D - Development 

In TDD we keep testing your code before writing the actual code this makes sure that whatever we write is not only tested but also works. As the software is not only working but is also backed by tests. 

# refactoring 

Refactoring means just to remove duplicate lines of code and redefining them in one or the other form. 

Here is a test function example: 

``` 
func TestHello(t *testing.T) {

    t.Run("saying hello to people", func(t *testing.T) {
        got := Hello("Chris")
        want := "Hello, Chris"

        if got != want {
            t.Errorf("got %q want %q", got, want)
        }
    })

    t.Run("say 'Hello, World' when an empty string is supplied", func(t *testing.T) {
        got := Hello("")
        want := "Hello, World"

        if got != want {
            t.Errorf("got %q want %q", got, want)
        }
    })

}

```

The refactored version: 

```
TestHello(t *testing.T) {

    assertCorrectMessage := func(t testing.TB, got, want string) {
        t.Helper()
        if got != want {
            t.Errorf("got %q want %q", got, want)
        }
    }

    t.Run("saying hello to people", func(t *testing.T) {
        got := Hello("Chris")
        want := "Hello, Chris"
        assertCorrectMessage(t, got, want)
    })

    t.Run("empty string defaults to 'World'", func(t *testing.T) {
        got := Hello("")
        want := "Hello, World"
        assertCorrectMessage(t, got, want)
    })

}


```

so what did we actually do in the above code we just refactored the program by adding a common function. and in the common function we added `helper()` method which helps us to show that which function actually generated the error and at which line. 


# access modifiers of golang. 
The function name starts with a lowercase letter. In Go public functions start with a capital letter and private ones start with a lowercase. We don't want the internals of our algorithm to be exposed to the world, so we made this function private.

i.e
1. Public functions --> Starts with capital letters.
1. Private functions --> Starts with lowercase letters.



