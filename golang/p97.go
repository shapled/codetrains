package main

type Pair struct {
	_1 int
	_2 int
}

func Counter(s string) map[rune]int {
	m := map[rune]int{}
	for _, ch := range s {
		cnt, ok := m[ch]
		if ok {
			m[ch] = cnt + 1
		} else {
			m[ch] = 1
		}
	}
	return m
}

func MapEqual(c1, c2 map[rune]int) bool {
	if len(c1) != len(c2) {
		return false
	}
	for key := range c1 {
		_, ok := c2[key]
		if !ok || c1[key] != c2[key] {
			return false
		}
	}
	return true
}

func isInterleave(s1 string, s2 string, s3 string) bool {
	if len(s3) != len(s1) + len(s2) {
		return false
	}
	if !MapEqual(Counter(s1 + s2), Counter(s3)) {
		return false
	}
	mark := map[Pair]int{Pair{-1, -1}: 1}
	for i:=0; i<len(s3); i++{
		mark2 := map[Pair]int{}
		for pair := range mark {
			if len(s1) > pair._1 + 1 && s3[i] == s1[pair._1 + 1] {
				mark2[Pair{pair._1 + 1, pair._2}] = 1
			}
			if len(s2) > pair._2 + 1 && s3[i] == s2[pair._2 + 1] {
				mark2[Pair{pair._1, pair._2 + 1}] = 1
			}
		}
		mark = mark2
		if len(mark) == 0 {
			return false
		}
	}
	return true
}

func main() {
	// error
	assertEqual(isInterleave("cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc", "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb", "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb"), true)

	assertEqual(isInterleave("", "", ""), true)
	assertEqual(isInterleave("a", "", "a"), true)
	assertEqual(isInterleave("a", "", "b"), false)
	assertEqual(isInterleave("aabcc", "dbbca", "aadbbcbcac"), true)
	assertEqual(isInterleave("aabcc", "dbbca", "aadbbbaccc"), false)
}
