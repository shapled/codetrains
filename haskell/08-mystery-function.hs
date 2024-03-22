module MysteryFunction (mystery,mysteryInv,nameOfMystery) where

mystery :: Int -> Int
mystery 0 = 0
mystery 1 = 1
mystery x = 
  let n = floor $ logBase 2 $ fromIntegral x
  in (2 ^ n) + (mystery ((2 ^ (n + 1)) - x - 1))

mysteryInv :: Int -> Int
mysteryInv 0 = 0
mysteryInv 1 = 1
mysteryInv x =
  let n = floor $ logBase 2 $ fromIntegral x
  in (2 ^ (n + 1)) - 1 - mysteryInv (x - (2 ^ n))

nameOfMystery :: String
nameOfMystery = "Gray code"
