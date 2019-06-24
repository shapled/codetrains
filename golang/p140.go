package main

import (
	"strings"
)

type TrieTree struct {
	Value string
	Children map[rune]*TrieTree
	Fail *TrieTree
}

type Matched struct {
	start int
	end int
	word string
}

func NewTrieTree(words []string) *TrieTree{
	root := &TrieTree{"", map[rune]*TrieTree{}, nil}
	for _, word := range words {
		current := root
		for _, ch := range word {
			_, ok := current.Children[ch]
			if !ok {
				current.Children[ch] = &TrieTree{"", map[rune]*TrieTree{}, nil}
			}
			current = current.Children[ch]
		}
		current.Value = word
	}
	return root
}

func NewACAutomation(root *TrieTree) *TrieTree {
	queue := []*TrieTree{}
	for _, child := range root.Children {
		child.Fail = root
		queue = append(queue, child)
	}
	for len(queue) != 0 {
		first := queue[0]
		queue = queue[1:]
		for ch, child := range first.Children {
			queue = append(queue, child)
			fail := first.Fail
			for {
				if fail == nil {
					child.Fail = root
					break
				}
				to, ok := fail.Children[ch]
				if ok {
					child.Fail = to
					break
				}
				fail = fail.Fail
			}
		}
	}
	return root
}

func Distinct(words []string) []string {
	set := map[string]int{}
	for _, word := range words {
		set[word] = 1
	}
	ret := []string{}
	for word := range set {
		ret = append(ret, word)
	}
	return ret
}

func MultiMatch(s string, words []string) []*Matched {
	ac := NewACAutomation(NewTrieTree(words))
	matched := []*Matched{}
	current := ac
	for i:=0; i<len(s); {
		ch := s[i]
		child, ok := current.Children[rune(ch)]
		if ok {
			current = child
			if current.Value != "" {
				matched = append(matched, &Matched{i+1-len(current.Value), i+1, current.Value})
			}
			next := current.Fail
			for next != nil {
				if next.Value != "" {
					matched = append(matched, &Matched{i+1-len(next.Value), i+1, next.Value})
				}
				next = next.Fail
			}
			i++
		} else {
			current = current.Fail
			if current == nil {
				current = ac
				i++
			}
		}
	}
	return matched
}

/*
 * 从位置 from 到位置 to 的方法，少于 100 种就缓存
 */
func DFSPositionMap2(positionMap map[int][]string, from int, to int, cache map[[2]int][][]string, limit int) [][]string {
	r, ok := cache[[2]int{from, to}]
	if ok {
		return r
	}
	ret := [][]string{}
	for _, word := range positionMap[from] {
		if from + len(word) > to {
			continue
		}
		if from + len(word) == to {
			ret = append(ret, []string{word})
			continue
		}
		for _, solution := range DFSPositionMap2(positionMap, from+len(word), to, cache, limit) {
			ret = append(ret, append([]string{word}, solution...))
		}
	}
	if len(ret) <= limit {
		cache[[2]int{from, to}] = ret
	}
	return ret
}

func wordBreak(s string, wordDict []string) []string {  // s is non-empty
	matched := MultiMatch(s, Distinct(wordDict))
	positionMap := map[int][]string{}
	for _, m := range matched {
		l, ok := positionMap[m.start]
		if !ok {
			l = []string{}
		}
		l = append(l, m.word)
		positionMap[m.start] = l
	}

	ret := []string{}
	for _, solution := range DFSPositionMap2(positionMap, 0, len(s), map[[2]int][][]string{}, 100) {
		ret = append(ret, strings.Join(solution, " "))
	}
	return ret
}

func main() {
	// error
	assertStringSliceSetEqual(
		wordBreak("a", []string{"a"}),
		[]string{"a"},
	)
	wordBreak(
		"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
		[]string{"a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"},
	)
	assertStringSliceSetEqual(
		wordBreak("aaaaaaa", []string{"aaaa", "aa", "a"}),
		[]string{"a a a a a a a","aa a a a a a","a aa a a a a","a a aa a a a","aa aa a a a","aaaa a a a","a a a aa a a","aa a aa a a","a aa aa a a","a aaaa a a","a a a a aa a","aa a a aa a","a aa a aa a","a a aa aa a","aa aa aa a","aaaa aa a","a a aaaa a","aa aaaa a","a a a a a aa","aa a a a aa","a aa a a aa","a a aa a aa","aa aa a aa","aaaa a aa","a a a aa aa","aa a aa aa","a aa aa aa","a aaaa aa","a a a aaaa","aa a aaaa","a aa aaaa"},
	)

	assertStringSliceSetEqual(wordBreak("abc", []string{"a", "c"}), []string{})
	assertStringSliceSetEqual(
		wordBreak("catsanddog", []string{"cat", "cats", "and", "sand", "dog"}),
		[]string{"cats and dog", "cat sand dog"},
	)
	assertStringSliceSetEqual(
		wordBreak("pineapplepenapple", []string{"apple", "pen", "applepen", "pine", "pineapple"}),
		[]string{"pine apple pen apple", "pineapple pen apple", "pine applepen apple"},
	)
}
