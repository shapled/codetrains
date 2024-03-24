import qualified Data.Set as Set

check :: [Int] -> Bool
check p3x3 = length (Set.fromList p3x3) == 9
          && sum p3x3 == 45
          
checkRow :: [[Int]] -> Int -> Bool
checkRow p9x9 i = check $ p9x9 i

checkColumn :: [[Int]] -> Int -> Bool
checkColumn p9x9 i = check $ map (\xs -> xs !! i) p9x9

checkBlock :: [[Int]] -> Int -> Int -> Bool
checkBlock p9x9 i j = check [
    (p9x9 !! $ i * 3) !! $ j * 3,
    (p9x9 !! $ i * 3) !! $ j * 3 + 1,
    (p9x9 !! $ i * 3) !! $ j * 3 + 2,
    (p9x9 !! $ i * 3 + 1) !! $ j * 3,
    (p9x9 !! $ i * 3 + 1) !! $ j * 3 + 1,
    (p9x9 !! $ i * 3 + 1) !! $ j * 3 + 2,
    (p9x9 !! $ i * 3 + 2) !! $ j * 3,
    (p9x9 !! $ i * 3 + 2) !! $ j * 3 + 1,
    (p9x9 !! $ i * 3 + 2) !! $ j * 3 + 2,
]

replace :: [a] -> Int -> a -> [a]
replace xs n x = (take xs n) ++ [x] ++ (drop xs $ n + 1)

fill :: [[Int]] -> (Int, Int) -> Int -> [[Int]]
fill p9x9 (row, col) v = replace p9x9 row $ replace (p9x9 !! row) col v

main = print $ check [1, 3, 2, 4, 6, 5, 9, 2, 1, 8]
