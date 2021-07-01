package main

import "testing"

func TestSum(t *testing.T) {
	t.Run("fixed size addition", func(t *testing.T) {
		numbers := []int{1, 2, 3, 4, 5}
		got := Sum(numbers)
		want := 15

		if got != want {
			t.Errorf("Number passed: %v\nSum: %d\nwanted:%d", numbers, got, want)
		}

	}) //t.run 1

	t.Run("slices are not fixed sizes.", func(t *testing.T) {
		numbers := []int{1, 2, 3}
		got := Sum(numbers)
		want := 6

		if got != want {
			t.Errorf("Number passed: %v\nSum: %d\nwanted:%d", numbers, got, want)
		}
	})

} // testing func

func TestSumAll(t *testing.T) {
	got := SumAll([]int{1, 2}, []int{0, 9})
	want := []int{3, 9}

	if got != want {
		t.Errorf("got %v and wanted %v", got, want)
	}
}
