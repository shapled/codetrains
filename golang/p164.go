package main

import (
	"math"
)

func maximumGap(nums []int) int {
	if len(nums) < 2 {
		return 0
	}
	minValue := math.MaxInt32
	maxValue := 0
	for _, num := range nums {
		if num < minValue {
			minValue = num
		}
		if num > maxValue {
			maxValue = num
		}
	}
	// 桶排序
	buckets := make([]uint32, maxValue / 32 + 1)
	for _, num := range nums {
		num -= minValue
		buckets[num/32] |= 1 << (uint)(num % 32)
	}
	// 查询连续 0 的个数
	currentLength := 1
	maxLength := 0
	isFirst := true
	for _, num := range buckets {
		remain := 32
		for num != 0 {
			if num % 2 == 1 {
				if isFirst {
					isFirst = false
					currentLength = 1
					maxLength = 0
				} else {
					if currentLength > maxLength {
						maxLength = currentLength
					}
					currentLength = 1
				}
			} else {
				currentLength += 1
			}
			num >>= 1
			remain -= 1
		}
		currentLength += remain
	}
	return maxLength
}

func main() {
	// error
	assertEqual(maximumGap([]int{1, 1, 1, 1, 1, 5, 5, 5, 5, 5}), 4)

	assertEqual(maximumGap([]int{3, 6, 9, 1}), 3)
	assertEqual(maximumGap([]int{}), 0)
	assertEqual(maximumGap([]int{3}), 0)
	assertEqual(maximumGap([]int{3, 3}), 0)
	assertEqual(maximumGap([]int{7, 3, 189, 22, 10, 201}), 167)
	assertEqual(maximumGap([]int{798, 134, 555, math.MaxInt32, 0, 0, 0}), math.MaxInt32-798)
}