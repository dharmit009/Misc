# Arrays:

## What are arrays ? 

> Arrays are collection of a particular data set. The main advantage of arrays is that you can refer to any value stored in it using the same variable and we achieve that by indexing the element. 

First let us see how to declare a array:
`arrayVarName := [size] dataType {data to be stored}`

Here are some samples: 
`numbers := [5] int {1,2,3,4,5}`

N^th array: 
`numbers := [...] int {1,2,3,4,5}`

This is how we pass array as an argument in Golang: 

```
func Sum(numbers [5] int) {

}

```

## What are slices ? 

They are nothing arrays without limitation of size rest everything is just same as array. 

> Syntax: 
`numbers := [] int {1,2,3,4,5}`

Can you spot the difference ?
> if not just see the size box its empty. 

## What are variadic functions ? 

Variadic functions can be called with any number of trailing arguments. 
For Example: `fmt.Println("")` is a common variadic function as the input can be anything inside the quotes. 

For Example: 
``` 
package main

import "fmt"

func sum(nums ...int) {
    fmt.Print(nums, " ")
    total := 0
    for _, num := range nums {
        total += num
    }
    fmt.Println(total)
}

func main() {

    sum(1, 2)
    sum(1, 2, 3)

    nums := []int{1, 2, 3, 4}
    sum(nums...)
}
``` 
