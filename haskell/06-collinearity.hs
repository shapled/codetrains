module Collinearity (collinearity) where

collinearity :: (Int,Int) -> (Int,Int) -> Bool
collinearity (x1,y1) (x2,y2) = x1 * y2 == x2 * y1
