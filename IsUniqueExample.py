# TODO: create a new Repo named CrackingTheCodingInterview and there
# you'll push all the challenges you solve of this book.

# Is Unique: Implement an algorithm to determine if a string has all unique
# characters. What if you cannot use additional data structures?

#  Test cases:
# abcde
# aaabbb
# aabcd
# edwwft
# q!@#$$

def Count(s, letter): # runtime: len(s), space: O(1)
  sum = 0
  for j in range(len(s)):
    if s[j] == letter:
      sum += 1
  return sum

def HasAllUniques(s): # runtime: len(s^2), space: O(1)
  # go through all the elements of s, in every element of s check how many times
  # that element appears in s, if any of those elements is greater than 1, return
  # False
  for i in range(len(s)):
    if Count(s, s[i]) > 1:
      return False
  return True

def main():
  tests = [
    {
      "s": "abcde",
      "expected": True
    },
    {
      "s": "aaabbb",
      "expected": False
    }
    # TODO: finish this tests
    # "aabcd",
    # "edwwft",
    # "q!@#$$",
    # "",
    # "1"
  ]

  succeed = True
  for test in tests:
    out = HasAllUniques(test["s"])
    if test["expected"] != out:
      print("You messed it up!")
      succeed = False

  if succeed:
    print("Good job!")
  else:
    print("Keep trying.")


