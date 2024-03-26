module Sudoku where

import qualified Data.List as List
import qualified Data.Set as Set
import Data.Function (on)
import Data.Maybe

type A9 = [Int]
data N9 = Row [[Int]] Int | Col [[Int]] Int | Block [[Int]] (Int, Int)
data CheckResult = Ok | Error | NoError deriving (Eq, Show)

toA9 :: N9 -> A9
toA9 (Row p9x9 i) = p9x9 !! i
toA9 (Col p9x9 i) = map (!! i) p9x9
toA9 (Block p9x9 (i, j)) = [(p9x9 !! (i * 3 + s)) !! (j * 3 + t) | s <- [0..2], t <- [0..2]]

a9RemainNumbers :: A9 -> [Int]
a9RemainNumbers a9 = Set.toList $ Set.difference (Set.fromList [1..9]) (Set.fromList a9)

checkA9 :: A9 -> CheckResult
checkA9 a9 = f a9 $ length $ filter (/= 0) a9
    where f a9 9 = if length (Set.fromList a9) == 9 then Ok else Error
          f a9 n = if length (Set.fromList a9) == n + 1 then NoError else Error

allN9 :: [[Int]] -> [N9]
allN9 p9x9 = [Row p9x9 i | i <- [0..8]]
          ++ [Col p9x9 i | i <- [0..8]]
          ++ [Block p9x9 (i, j) | i <- [0..2], j <- [0..2]]

check :: [[Int]] -> CheckResult
check p9x9 = f (map (checkA9 . toA9) $ allN9 p9x9)
    where f bs
            | all (== Ok) bs = Ok
            | Error `elem` bs = Error
            | otherwise = NoError

replace :: [a] -> Int -> a -> [a]
replace xs n x = take n xs ++ [x] ++ drop (n + 1) xs

fill :: [[Int]] -> (Int, Int) -> Int -> [[Int]]
fill p9x9 (row, col) v = replace p9x9 row $ replace (p9x9 !! row) col v

nextN9Position :: N9 -> Maybe ((Int, Int), [Int])
nextN9Position (Row p9x9 i) = List.elemIndex 0 (toA9 (Row p9x9 i))
                          >>= (\index -> Just ((i, index), a9RemainNumbers $ toA9 (Row p9x9 i)))
nextN9Position (Col p9x9 i) = List.elemIndex 0 (toA9 (Col p9x9 i))
                          >>= (\index -> Just ((index, i), a9RemainNumbers $ toA9 (Col p9x9 i)))
nextN9Position (Block p9x9 (i, j)) = List.elemIndex 0 (toA9 (Block p9x9 (i, j)))
                                 >>= (\index -> Just ((i * 3 + index `div` 3, j * 3 + index `mod` 3),
                                                      a9RemainNumbers $ toA9 (Block p9x9 (i, j))))

nextPosition :: [[Int]] -> Maybe ((Int, Int), [Int])
nextPosition p9x9 = let pvs = mapMaybe nextN9Position (allN9 p9x9) in
                    if null pvs then Nothing else Just $ List.minimumBy (compare `on` (length . snd)) pvs

sudoku :: [[Int]] -> [[Int]]
sudoku p9x9 = f p9x9 []
    where f p9x9 [] = case nextPosition p9x9 of
            Nothing -> p9x9
            Just v -> f p9x9 [v]
          f p9x9 ((pos, []):xs) = f (fill p9x9 pos 0) xs
          f p9x9 ((pos, y:ys):xs) =
            let n = fill p9x9 pos y
            in case check n of
                Ok -> n
                Error -> f p9x9 ((pos, ys):xs)
                NoError -> case nextPosition n of
                    Nothing -> n
                    Just v -> f n (v : ((pos, ys):xs))
