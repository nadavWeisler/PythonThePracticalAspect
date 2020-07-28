# Tests for question 2
from partA import EvenNumber, MultiplesOfSix

num = EvenNumber(4)
assert (num.value == 4)
assert (num.add_number(0))
assert (num.value == 4)
assert (num.add_number(4))
assert (num.value == 8)
assert (not num.add_number(3))
assert (num.value == 8)
assert (not num.add_number(92))
assert (num.value == 8)
assert (not num.add_number(1))
assert (num.value == 8)
assert (not num.add_number(331))
assert (num.value == 8)
assert (not num.add_number(1692))
assert (num.value == 8)

try:
    num = EvenNumber(3)
except ValueError as e:
    print(e)
try:
    num = EvenNumber(99)
except ValueError as e:
    print(e)
try:
    num = EvenNumber(100)
except ValueError as e:
    print(e)
try:
    num = EvenNumber(102)
except ValueError as e:
    print(e)

num2 = MultiplesOfSix(12)
assert (num2.value == 12)
assert (num2.add_number(6))
assert (num2.value == 18)
assert (num2.add_number(0))
assert (num2.value == 18)
assert (num2.add_number(36))
assert (num2.value == 54)

assert (not num2.add_number(4))
assert (num2.value == 54)
assert (not num2.add_number(54))
assert (num2.value == 54)
assert (not num2.add_number(1))
assert (num2.value == 54)


try:
    num2 = MultiplesOfSix(13)
except ValueError as e:
    print(e)
try:
    num2 = MultiplesOfSix(1)
except ValueError as e:
    print(e)
try:
    num2 = MultiplesOfSix(0)
except ValueError as e:
    print(e)
try:
    num2 = MultiplesOfSix(108)
except ValueError as e:
    print(e)
try:
    num2 = MultiplesOfSix(102)
except ValueError as e:
    print(e)
