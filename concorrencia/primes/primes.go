package main

import (
	"fmt"
	"math"
)

var primeFixture = []struct {
	number int64
	isPrime bool
}{
	{2, true},
	{142702110479723, true},
	{299593572317531, true},
	{3333333333333301, true},
	{3333333333333333, false},
	{3333335652092209, false},
	{4444444444444423, true},
	{4444444444444444, false},
	{4444444488888889, false},
	{5555553133149889, false},
	{5555555555555503, true},
	{5555555555555555, false},
	{6666666666666666, false},
	{6666666666666719, true},
	{6666667141414921, false},
	{7777777536340681, false},
	{7777777777777753, true},
	{7777777777777777, false},
	{9999999999999917, true},
	{9999999999999999, false},
}

func isPrime(n int64) bool {
	if n < 2 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 || n%3 == 0 {
		return false
	}

	limit := int64(math.Sqrt(float64(n)))
	for i := int64(5); i <= limit; i += 6 {
		if n%i == 0 || n%(i+2) == 0 {
			return false
		}
	}
	return true
}

func autoTest() {
	for _, test := range primeFixture {
		primeRes := isPrime(test.number)
		if primeRes == test.isPrime {
			fmt.Println(test.number, primeRes)
		}
	}
}

func main() {
	autoTest()
}