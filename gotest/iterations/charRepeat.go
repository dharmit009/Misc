package iteration

func Repeat(c string, rnum int) string {
	var repeated string
	for i := 0; i < rnum; i++ {
		repeated += c
	}
	return repeated
}
