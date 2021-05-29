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
