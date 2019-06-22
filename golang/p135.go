package main

type Layer struct {
	Start int  // 开始位置的下标
	Count int  // 可以抬升的次数，小于0可以无限使用，用尽 layer 会和上一个合并
}

func candy(ratings []int) int {
	if len(ratings) == 0 {
		return 0
	}
	sum := 0
	cost := 0
	var layers []*Layer
	for i, rating := range ratings {
		if i == 0 {
			sum += 1
			cost = 1
			layers = []*Layer{&Layer{0, -1}}
			continue
		}
		last := ratings[i-1]
		if rating == last {
			cost = 1
			sum += cost
			layers = append(layers, &Layer{i, -1})
		} else if rating > last {
			cost += 1
			sum += cost
			layers = append(layers, &Layer{i, -1})
		} else {
			if cost == 1 {
				lastLayer := layers[len(layers)-1]
				cost = 1
				sum += i - lastLayer.Start + cost
				if lastLayer.Count > 0 {
					lastLayer.Count -= 1
					if lastLayer.Count == 0 {
						layers = append(layers[:len(layers)-1])
					}
				}
			} else {
				if cost > 2 {
					layers = append(layers, &Layer{i, cost-2})
				}
				cost = 1
				sum += cost
			}
		}
	}
	return sum
}

func main() {
	assertEqual(candy([]int{}), 0)
	assertEqual(candy([]int{1}), 1)
	assertEqual(candy([]int{1, 0, 2}), 5)
	assertEqual(candy([]int{1, 2, 2}), 4)
	assertEqual(candy([]int{1, 2, 2}), 4)
	assertEqual(candy([]int{2, 3, 4, 3, 2, 1}), 13)
}