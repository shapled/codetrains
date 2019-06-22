package main

type TrieTree struct {
	Value string
	Children map[rune]*TrieTree
	Fail *TrieTree
}

func NewTrieTree(words []string) *TrieTree{
	root := &TrieTree{}
	for _, word := range words {
		current := root
		for _, ch := range word {
			_, ok := current.Children[ch]
			if !ok {
				current.Children[ch] = &TrieTree{}
			}
			current = current.Children[ch]
		}
		current.Value = word
	}
	return root
}

func NewACAutomation(root *TrieTree) {

}

func wordBreak(s string, wordDict []string) []string {

}

func main() {
	assertStringSliceEqual(
		wordBreak("catsanddog", []string{"cat", "cats", "and", "sand", "dog"}),
		[]string{"cats and dog", "cat sand dog"},
	)
	assertStringSliceEqual(
		wordBreak("pineapplepenapple", []string{"apple", "pen", "applepen", "pine", "pineapple"}),
		[]string{"pine apple pen apple", "pineapple pen apple", "pine applepen apple"},
	)
}
