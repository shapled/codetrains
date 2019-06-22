package main

func IsPalindrome(s string) bool {
	i := 0
	j := len(s) - 1
	for i < j {
		if s[i] != s[j] {
			return false
		}
		i++
		j--
	}
	return true
}

func MinInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func minCut(s string) int {
	if len(s) == 0 {
		return 0
	}
	var cuts []int
	for j, ch := range s {
		if cuts == nil {
			cuts = []int{0}
		} else {
			cuts = append(cuts, cuts[j-1] + 1)
			for i := 0; i < j; i++ {
				if int(s[i]) == int(ch) && IsPalindrome(s[i:j+1]) {
					solution := 0
					if i != 0 {
						solution = cuts[i-1] + 1
					}
					cuts[j] = MinInt(cuts[j], solution)
				}
			}
		}
	}
	return cuts[len(s)-1]
}

func main() {
	assertEqual(minCut("aab"), 1)
	assertEqual(minCut(""), 0)
	assertEqual(minCut("baab"), 0)
	assertEqual(minCut("abaab"), 1)
	assertEqual(minCut("abaabbacac"), 2)
}