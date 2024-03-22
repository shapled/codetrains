module MovingZeros (moveZeros) where

moveZeros :: [Int] -> [Int]
moveZeros [] = []
moveZeros (0:xs) = moveZeros xs ++ [0]
moveZeros (x:xs) = x : moveZeros xs
