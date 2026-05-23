package main

import (
	"fmt"

	"github.com/cagox/pensnexus/internal/crypto"
)

func main() {
	fmt.Println("Hello, World!")
	fmt.Println(crypto.HashPassword("password"))
}
