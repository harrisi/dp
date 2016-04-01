--{-# OPTIONS_GHC -Wall #-}
module Main where

import qualified Numeric as N (showIntAtBase)
import qualified Data.Char as DC (intToDigit)

main :: IO ()
main = do
  putStrLn "Enter a number:"
  n <- getLine
  putStrLn ("population count: " ++ (show $ popCount n))
  where
    popCount :: String -> Int
    popCount n = length .
                 filter (== '1') $
                 N.showIntAtBase 2 DC.intToDigit (read n) ""
