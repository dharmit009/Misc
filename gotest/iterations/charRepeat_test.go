package iteration

import (
	"fmt"
	"strings"
	"testing"
)

func TestHelloWorld(t *testing.T) {
	got := Repeat("a", 5)
	want := "aaaaa"
	if got != want {
		t.Errorf("got %s and wanted %s", got, want)
	}
}

func BenchmarkRepeat(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Repeat("a", 7)
	} //for
}

func ExampleRepeat() {
	repString := Repeat("a", 8)
	fmt.Println(repString)
	// Output: aaaaaaaa
}

func ExampleRepeater() {
	repString := strings.Repeat("a", 8)
	fmt.Println(repString)
	// Output: aaaaaaaa
}
