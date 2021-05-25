# Iterations in Golang 

This is a very unique topic espeacially in Golang. You will be surpised for sure ....\ Golang has only one loop that is for loop which apparently is good thing soon we will understand how. 

So points to remember: 
 * While loops dont exist.
 * Do while does not exist.
 * until keyword does not exist. 

## Benchmarking. 

> Benchmarking is a process in which the function runs multiple times and measures it's performanance. The b in `t testing.B` stands for benchmarking.

`testing.B` gives us acess to `b.N`. This number is automatically decided by the framework and will determine what will be the good value for the benchmarking test. 

go test -bench=. for Linux/macOS
go test -bench="." for Windows. 

