-- Convert string to camel case

module CamelCase (toCamelCase) where

import Data.Char (toUpper)

merge :: String -> Bool -> String
merge [] _ = []
merge (x:xs) start
  | x == '_'  = merge xs True
  | x == '-'  = merge xs True
  | otherwise = (if start then toUpper x else x) : merge xs False

toCamelCase :: String -> String
toCamelCase str = merge str False
