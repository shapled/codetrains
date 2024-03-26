module Fibonacci (fib) where

-- -- solution 1: timeout
-- fib :: Integer -> Integer
-- fib n | n < 0 && odd n  = fib (-n)
--       | n < 0 && even n = - fib (-n)
--       | otherwise       = getFirst (until finished next initial)
--         where initial = (0, 1, 0)
--               finished (_, _, counter) = counter >= n
--               next (a, b, counter) = (b, a + b, counter + 1)
--               getFirst (x, _, _) = x

-- -- solution 2: https://zhuanlan.zhihu.com/p/31958470
-- fib :: Integer -> Integer
-- fib n | n < 0 && odd n  = fib (-n)
--       | n < 0 && even n = - fib (-n)
--       | n == 0          = 0
--       | n == 1          = 1
--       | even n          = let a = fib (n `div` 2) in
--                           let b = fib (n `div` 2 - 1) in
--                           a * (a + 2 * b)
--       | otherwise       = let a = fib ((n + 1) `div` 2) in
--                           let b = fib ((n - 1) `div` 2) in
--                           a * a + b * b

-- -- solution 3: https://zhuanlan.zhihu.com/p/307435857
-- fib :: Integer -> Integer
-- fib n | n < 0 && odd n  = fib (-n)
--       | n < 0 && even n = - fib (-n)
--       | n == 0          = 0
--       | n == 1          = 1
--       | otherwise       = getResult (until finished next initial)
--         where initial = (((1, 0), (0, 1)), ((1, 1), (1, 0)), n - 2)
--               finished (_, _, power) = power == 0
--               next (res, base, power) = (if odd power then matrixMulti res base else res, matrixMulti base base, power `div` 2)
--               getResult (x, _, _) = getMPos x 0 0 + getMPos x 0 1
--               getMPos m i j = (if j == 0 then fst else snd) $ (if i == 0 then fst else snd) m
--               matrixMulti m1 m2 = ((getMPos m1 0 0 * getMPos m2 0 0 + getMPos m1 0 1 * getMPos m2 1 0,
--                                     getMPos m1 0 0 * getMPos m2 0 1 + getMPos m1 0 1 * getMPos m2 1 1),
--                                    (getMPos m1 1 0 * getMPos m2 0 0 + getMPos m1 1 1 * getMPos m2 1 0,
--                                     getMPos m1 1 0 * getMPos m2 0 1 + getMPos m1 1 1 * getMPos m2 1 1))

-- -- solution 3.1
-- fib :: Integer -> Integer
-- fib n
--   | n < 0 && odd n  = fib (-n)
--   | n < 0 && even n = - fib (-n)
--   | n == 0          = 0
--   | n == 1          = 1
--   | otherwise       = getResult (until finished next initial)
--   where
--     initial = (((1, 0), (0, 1)), ((1, 1), (1, 0)), n - 1)
--     finished (_, _, power) = power == 0
--     next (res, base, power) = (if odd power then matrixMulti res base else res, matrixMulti base base, power `div` 2)
--     getResult (x, _, _) = getMPos x 0 0
--     getMPos ((a, _), (_, _)) 0 0 = a
--     getMPos ((_, a), (_, _)) 0 1 = a
--     getMPos ((_, _), (a, _)) 1 0 = a
--     getMPos ((_, _), (_, a)) 1 1 = a
--     matrixMulti ((a, b), (c, d)) ((e, f), (g, h)) =
--       ((a * e + b * g, a * f + b * h),
--        (c * e + d * g, c * f + d * h))

-- solution 2.1
fib :: Integer -> Integer
fib n
  | n < 0 && odd n  = fib (-n)
  | n < 0 && even n = - fib (-n)
  | otherwise       = fst (calc n)
  where calc :: Integer -> (Integer, Integer)
        calc 0 = (0, 1)
        calc 1 = (1, 1)
        calc x = let (a, b) = calc $ x `div` 2 in
                 let p = a * (2 * b - a) in
                 let q = b * b + a * a in
                 if even x then (p, q) else (q, p + q)
