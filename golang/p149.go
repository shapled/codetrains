package main

type LineKey struct {
	Point [2]int  // 点
	K [3]int  // 三元组表示斜率，(正负1/-1, 约后的分子, 约后的分母), 斜率无穷时为 (1, 1, 0), 斜率为0时(1, 0, 1)
}

type LineData struct {
	positions []int
	total int
}

type Line *LineData

func GCD(m, n int) int {  // 最大公约数
	if m == n {
		return m
	}
	if m < n {
		m, n = n, m
	}
	if n == 1 {
		return 1
	}
	return GCD(m-n, n)
}

func CalculateK(point1, point2 [2]int) [3]int {
	m := point2[1] - point1[1]
	n := point2[0] - point1[0]
	if m == 0 {
		return [3]int{1, 0, 1}
	}
	if n == 0 {
		return [3]int{1, 1, 0}
	}
	f := 1
	if m < 0 {
		m = -m
		f *= -1
	}
	if n < 0 {
		n = -n
		f *= -1
	}
	v := GCD(m, n)
	return [3]int{f, m/v, n/v}
}

func InitMark(n int) [][]bool {
	mark := [][]bool{}
	for i := 0; i < n; i++ {
		mark = append(mark, []bool{})
		for j := 0; j < n; j++ {
			e := false
			if i == j {
				e = true
			}
			mark[i] = append(mark[i], e)
		}
	}
	return mark
}

func PointCount(points [][]int) (map[[2]int]int, [][2]int) {
	m := map[[2]int]int{}
	for _, p := range points {
		point := [2]int{p[0], p[1]}
		cnt, ok := m[point]
		if !ok {
			cnt = 0
		}
		m[point] = cnt + 1
	}
	keys := [][2]int{}
	for p, _ := range m {
		keys = append(keys, p)
	}
	return m, keys
}

func maxPoints(points [][]int) int {
	if len(points) == 0 {
		return 0
	}
	counter, keys := PointCount(points)
	if len(counter) == 1 {
		for _, cnt := range counter {
			return cnt
		}
	}
	lines := map[LineKey]Line{}  // (点, 斜率) -> 点集，点集可以看作是线
	mark := InitMark(len(counter))  // i 与 j 是否已经计算斜率
	for i, p1 := range keys {
		for j, p2 := range keys {
			if !mark[i][j] {
				k := CalculateK(p1, p2)
				key1 := LineKey{[2]int{p1[0], p1[1]}, k}
				key2 := LineKey{[2]int{p2[0], p2[1]}, k}
				line, ok := lines[key2]
				if ok {  // point2 有相关斜率的数据，指向同一条 line
					lines[key1] = line
					line.positions = append(line.positions, i)
					line.total += counter[p1]
					for _, l := range line.positions {
						mark[i][l] = true
						mark[l][i] = true
					}
				} else {  // 构建 line，并都指向它
					line = &LineData{[]int{i, j}, counter[p1] + counter[p2]}
					lines[key1] = line
					lines[key2] = line
					mark[i][j] = true
					mark[j][i] = true
				}
			}
		}
	}
	maxPoints := 0
	for _, line := range lines {
		if line.total > maxPoints {
			maxPoints = line.total
		}
	}
	return maxPoints
}

func main() {
	assertEqual(maxPoints([][]int{}), 0)
	assertEqual(maxPoints([][]int{{1, 1}, {1, 1}}), 2)
	assertEqual(maxPoints([][]int{{1, 1}, {1, 1}, {1, 1}, {1, 2}}), 4)
	assertEqual(maxPoints([][]int{{1, 1}, {1, 1}, {1, 1}, {1, 2}, {1, 3}, {1, 3}, {2, 3}}), 6)
	assertEqual(maxPoints([][]int{{1, 1}, {1, 2}}), 2)
	assertEqual(maxPoints([][]int{{1, 1}, {2, 1}}), 2)
	assertEqual(maxPoints([][]int{{1, 1}, {2, 2}}), 2)
	assertEqual(maxPoints([][]int{{1, 1}, {2, 2}, {3, 3}}), 3)
	assertEqual(maxPoints([][]int{{1, 1}, {3, 2}, {5, 3}, {4, 1}, {2, 3}, {1, 4}}), 4)
}
