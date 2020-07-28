# Tests for question 1
from partA import is_palindrome

assert (is_palindrome("a12 21A"))
assert (is_palindrome(""))
assert (is_palindrome(" "))
assert (is_palindrome(" a "))
assert (is_palindrome("vv"))
assert (is_palindrome("  "))

assert (not is_palindrome("a12 21b"))
assert (not is_palindrome("abb a"))
assert (not is_palindrome("ab"))
assert (not is_palindrome("abb abb"))
assert (not is_palindrome(" a"))

