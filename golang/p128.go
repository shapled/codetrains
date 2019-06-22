package main

func FindSmaller(pos int, nums []int, m map[int]int, counter []int) int {
	num := nums[pos]
	i, ok := m[num-1]
	cnt := 0
	if ok {
		cnt = counter[i]
		if cnt == -1 {
			cnt = FindSmaller(i, nums, m, counter)
		}
	}
	counter[pos] = cnt + 1
	return counter[pos]
}

func longestConsecutive(nums []int) int {
	m := map[int]int{}
	counter := []int{}  // 以当前数字结尾的最大连续序列的值
	for i, num := range nums {
		m[num] = i
		counter = append(counter, -1)
	}
	for i := range nums {
		if counter[i] == -1 {
			FindSmaller(i, nums, m, counter)
		}
	}
	maxV := 0
	for _, cnt := range counter {
		if cnt > maxV {
			maxV = cnt
		}
	}
	return maxV
}

func main() {
	assertEqual(longestConsecutive([]int{}), 0)
	assertEqual(longestConsecutive([]int{1, 3, 5, 100}), 1)
	assertEqual(longestConsecutive([]int{100, 4, 200, 1, 3, 2}), 4)
	assertEqual(longestConsecutive([]int{99, 98, 97, 96}), 4)
	assertEqual(longestConsecutive([]int{99, 98, 93, 96, 94, 92}), 3)
}