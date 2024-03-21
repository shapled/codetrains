module Tribonacci where

tribonacci :: Num a => (a, a, a) -> Int -> [a]
tribonacci (a, b, c) n
  | n == 0    = []
  | n == 1    = [a]
  | n == 2    = [a, b]
  | otherwise = a : tribonacci (b, c, a + b + c) (n - 1)
