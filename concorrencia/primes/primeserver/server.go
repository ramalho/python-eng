package main

import (
	"encoding/json"
	"fmt"
	"math"
	"math/big"
	"net/http"
	"strconv"
)

type responseLPF struct {
	N   uint64 `json:"n"`
	LPF uint64 `json:"lpf"`
}

func main() {
	http.HandleFunc("/lpf", getLPF)
	http.ListenAndServe(":8000", nil)
}

func getLPF(w http.ResponseWriter, r *http.Request) {
	q := r.URL.Query().Get("n")
	if len(q) == 0 {
		w.WriteHeader(http.StatusBadRequest)
		w.Write([]byte("missing query value n=<number>"))
		return
	}

	n, err := strconv.ParseUint(q, 10, 64)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		w.Write([]byte(fmt.Sprintf("invalid query string n=%v", q)))
		return
	}
	jsonBytes, err := json.Marshal(responseLPF{n, LPF(n)})
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		w.Write([]byte("internal server error"))
		return
	}
	w.WriteHeader(http.StatusOK)
	w.Write(jsonBytes)
}

func LPF(n uint64) uint64 {
	switch {
	case n == 1:
		return 1
	case n%2 == 0:
		return 2
	case n%3 == 0:
		return 3
	}

	// n.ProbablyPrime(0) uses the Baillie-PSW primality test
	// https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test
	if n < math.MaxInt64 && big.NewInt(int64(n)).ProbablyPrime(0) {
		return n
	}
	limit := uint64(math.Sqrt(float64(n)))
	for i := uint64(5); i <= limit; i += 6 {
		if n%i == 0 {
			return i
		}
		j := i + 2
		if n%j == 0 {
			return j
		}
	}
	return n
}
