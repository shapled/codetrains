module MultiplesOf3And5 where

solution :: Integer -> Integer
solution number = (s number 3) + (s number 5) - (s number 15)
  where s n v = v * ((n - 1) `div` v) * (1 + (n - 1) `div` v) `div` 2
