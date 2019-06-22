package main

func numDistinct(s string, t string) int {
	if s == t || t == "" {
		return 1
	}
	if len(s) < len(t) {
		return 0
	}
	mark := map[int]int{-1: 1}
	for _, ch := range s {
		mark2 := map[int]int{}
		for pos := range mark {
			if len(t) > pos + 1 && int(t[pos+1]) == int(ch) {
				cnt, ok := mark[pos+1]
				if !ok {
					cnt = 0
				}
				mark2[pos+1] = cnt + mark[pos]
			}
		}
		// update mark
		for key := range mark2 {
			mark[key] = mark2[key]
		}
	}
	cnt, ok := mark[len(t)-1]
	if !ok {
		cnt = 0
	}
	return cnt
}

func main() {
	assertEqual(numDistinct("ba", "bag"), 0)
	assertEqual(numDistinct("bag", "bag"), 1)
	assertEqual(numDistinct("", ""), 1)
	assertEqual(numDistinct("babgbag", ""), 1)
	assertEqual(numDistinct("rabbbit", "rabbit"), 3)
	assertEqual(numDistinct("babgbag", "bag"), 5)
	assertEqual(numDistinct("babgbag", "balala"), 0)
}