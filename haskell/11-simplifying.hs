module Simplifying (simplify) where

import Data.Maybe (maybeToList, fromMaybe)
import Data.Char (isDigit)
import Data.List ((\\), nub, groupBy)

type Symbol = String
type Row = [Double]
type Matrix = [Row]
data Token = Number Int
           | Symbol Symbol
           | Equal
           | Plus
           | Sub
           | ParenLeft
           | ParenRight
           deriving (Show, Eq)
data Buffer = Empty
            | BNumber String
            | BSymbol String
            deriving (Show, Eq)

tokenizer :: String -> [Token]
tokenizer expr = parseTokens expr Empty []
  where flushBuffer :: Buffer -> Maybe Token
        flushBuffer buff = case buff of
          Empty -> Nothing
          BNumber number -> Just $ Number (read $ reverse number)
          BSymbol symbol -> Just $ Symbol $ reverse symbol
        parseTokens :: String -> Buffer -> [Token] -> [Token]
        parseTokens "" buff previous = previous ++ maybeToList (flushBuffer buff)
        parseTokens (ch:expr) buff previous
          | ch == '+' = append Plus
          | ch == '-' = append Sub
          | ch == '(' = append ParenLeft
          | ch == ')' = append ParenRight
          | ch == '=' = append Equal
          | isDigit ch = case buff of
              BNumber number -> parseTokens expr (BNumber (ch:number)) previous
              _ -> parseTokens expr (BNumber [ch]) (previous ++ maybeToList (flushBuffer buff))
          | ch == ' ' = parseTokens expr Empty $ previous ++ maybeToList (flushBuffer buff)
          | otherwise = case buff of
              BSymbol symbol -> parseTokens expr (BSymbol (ch:symbol)) previous
              _ -> parseTokens expr (BSymbol [ch]) (previous ++ maybeToList (flushBuffer buff))
          where append token = parseTokens expr Empty $ previous ++ maybeToList (flushBuffer buff) ++ [token]

eval :: [Token] -> [(Symbol, Int)]
eval tokens = mergeSymbols $ evalTokens tokens [] []
  where evalTokens :: [Token] -> [Int] -> [(Symbol, Int)] -> [(Symbol, Int)]
        evalTokens [] _ previous = previous
        evalTokens (Sub:Sub:tokens) times previous = evalTokens tokens times previous
        evalTokens (Sub:Number number:tokens) times previous = evalTokens (Number (-number):tokens) times previous
        evalTokens (Number number:Symbol symbol:tokens) times previous = evalTokens tokens times $ (symbol, number * product times):previous
        evalTokens (Number number:ParenLeft:tokens) times previous = evalTokens tokens (number:times) previous
        evalTokens (Number number:tokens) times previous = evalTokens tokens (number:times) previous
        evalTokens (Symbol symbol:tokens) times previous = evalTokens tokens times $ (symbol, product times):previous
        evalTokens (Equal:tokens) times previous = evalTokens (Sub:tokens) times previous
        evalTokens (Plus:tokens) times previous = evalTokens tokens times previous
        evalTokens (Sub:tokens) times previous = evalTokens (Number (-1):tokens) times previous
        evalTokens (ParenLeft:tokens) times previous = evalTokens tokens (1:times) previous
        evalTokens (ParenRight:tokens) times previous = evalTokens tokens (tail times) previous

        mergeSymbols :: [(Symbol, Int)] -> [(Symbol, Int)]
        mergeSymbols formula = map (\group -> ((fst . head) group, sum $ map snd group)) $ groupBy (\(a, _) (b, _) -> a == b) formula

-- https://luckytoilet.wordpress.com/2010/02/21/solving-systems-of-linear-equations-in-haskell/
gaussianReduce :: Matrix -> Matrix
gaussianReduce matrix = fixlastrow $ foldl reduceRow matrix [0..length matrix-1]
  where swap xs a b
          | a > b = swap xs b a
          | a == b = xs
          | a < b = let
          (p1,p2) = splitAt a xs
          (p3,p4) = splitAt (b-a-1) (tail p2)
          in p1 ++ [xs!!b] ++ p3 ++ [xs!!a] ++ tail p4

        reduceRow matrix1 r = let
          firstnonzero = head $ filter (\x -> matrix1 !! x !! r /= 0) [r..length matrix1-1]
          matrix2 = swap matrix1 r firstnonzero
          row = matrix2 !! r
          row1 = map (\x -> x / (row !! r)) row
          subrow nr = let k = nr!!r in zipWith (\a b -> k*a - b) row1 nr
          nextrows = map subrow $ drop (r+1) matrix2
          in take r matrix2 ++ [row1] ++ nextrows

        fixlastrow matrix' = let
          a = init matrix'; row = last matrix'; z = last row; nz = last (init row)
          in a ++ [init (init row) ++ [1, z / nz]]

substitute :: Matrix -> Row
substitute matrix = foldr next [last (last matrix)] (init matrix) where
  next row found = let
    subpart = init $ drop (length matrix - length found) row
    solution = last row - sum (zipWith (*) found subpart)
    in solution : found

simplify :: [String] -> String -> String
simplify formulaStrings formula = do
  let formulas = map (eval . tokenizer) formulaStrings
      symbols = nub $ map fst $ concat formulas
      baseSymbols = map (fst . head) formulas
      targetSymbol = head $ symbols \\ baseSymbols
      matrix = makeMatrix formulas baseSymbols targetSymbol
      solved = substitute $ gaussianReduce matrix
      v = calc ((eval . tokenizer) formula) $ zip (baseSymbols ++ [targetSymbol]) (solved ++ [1.0])
      (a, b) = properFraction v
  (if b == 0 then show a else show v) ++ targetSymbol

makeMatrix :: [[(Symbol, Int)]] -> [Symbol] -> Symbol -> Matrix
makeMatrix formulas symbols symbol = map (\x -> makeVector x symbols symbol) formulas

makeVector :: [(Symbol, Int)] -> [Symbol] -> Symbol -> Row
makeVector list symbols symbol = map (fromIntegral . (\x -> fromMaybe 0 $ lookup x list)) symbols
                              ++ [-1.0 * fromIntegral (fromMaybe 0 $ lookup symbol list)]
calc :: [(Symbol, Int)] -> [(Symbol, Double)] -> Double
calc list1 list2 = sum [ y * fromIntegral x | (str1, num1) <- list1, (str2, num2) <- list2, str1 == str2, let x = num1, let y = num2]
