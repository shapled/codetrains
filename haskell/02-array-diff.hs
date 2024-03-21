module Difference where

difference :: Eq a => [a] -> [a] -> [a]
difference a [] = a
difference a (x:xs) = difference (filter (\e -> e /= x) a) xs
