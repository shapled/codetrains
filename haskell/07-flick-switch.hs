module FlickSwitch (flickSwitch) where

flickSwitch :: [String] -> [Bool]
flickSwitch [] = []
flickSwitch xs = f xs True
  where f [] _ = []
        f ("flick":ys) b = (not b) : f ys (not b)
        f (_:ys) b = b : f ys b
