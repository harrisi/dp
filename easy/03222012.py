#!/usr/local/bin/python

if __name__ == '__main__':
  s = raw_input('palindrome?> ')
  print(s == s[::-1])
