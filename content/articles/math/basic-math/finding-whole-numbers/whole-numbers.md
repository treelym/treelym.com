Title: Finding Whole Numbers
Date: 2020-09-28 1:00
Category: math
Tags: basic-math, nim
Slug: finding-whole-numbers
Authors: treelym
Image: ../../../images/finding-whole-numbers.png
Thumbnail: ../../../images/finding-whole-numbers-thumbnail.png

Any number that is a positive integer is a **whole number**, including the number zero. Whole numbers can be expressed as a set like so:

`{0, 1, 2, 3, 4, 5, ...}`

When developing software, whole numbers can be useful in several cases, for example, if I want to validate a user's age, or tell someone how many hours they exercised in a given day (rounded). In both of these scenarios negative numbers wouldn't make sense, leaving only whole numbers to work with.

## Finding Whole Numbers using Nim
Nim has a built-in `Natural` type that can be used to easily determine whether a number is whole or natural.

```nim
const myNum1: Natural = 5 # Will compile
const myNum2: Natural = 0 # Will compile.
const myNum3: Natural = -1 # Won't compile - throws an error
```

However, just for fun, I want to write a simple procedure that determines a whole number with the assumption that I cannot know at compile time if a given number is of a `Natural` type. In order to do this, I can use the `int` type and a small amount of logic.

```nim
func isWhole(num: int): bool = num >= 0

when isMainModule:
  assert isWhole(5) == true
  assert isWhole(0) == true
  assert isWhole(-1) == false
```

The `isWhole` procedure takes one argument, an integer named `num` and returns `true` if it is greater than or equal to zero. Otherwise the procedure will return `false`. Dead simple!

But what happens if I try to pass it a float such as `10.0`?

```nim
func isWhole(num: int): bool = num >= 0

when isMainModule:
  assert isWhole(10.0) == true
```

If I run this I will get the following error: `Error: type mismatch: got <float64>`. Since `isWhole` expects `num` to be an `int`, I cannot currently pass a `float` to it. In order to support floats, I'll have to add a little more code. This is the solution I came up with.

```nim
import math


func isInt(num: float): bool = (floor num) == num

func isWhole(num: int): bool = num >= 0
func isWhole(num: float): bool = isInt(num) and num >= 0

when isMainModule:
  assert isWhole(10) == true
  assert isWhole(10.0) == true
  assert isWhole(0) == true
  assert isWhole(-1) == false
```

In this solution I've defined `isWhole` twice, overloading it so it can handle both `int` and `float` values. If `num` is a `float`, a new function `isInt` is called to make sure that the decimal portion of the number is zero (e.g. 5.0, 3.00000, etc.). This way, floating point numbers such as 10.0 will be accurately treated as whole numbers.

A natural (haha) next step to this problem is figuring out how to extract whole numbers out of a list or sequence.

```nim
import math


type Number = int | float

func isInt(num: float): bool = (floor num) == num

func isWhole(num: int): bool = num >= 0
func isWhole(num: float): bool = isInt(num) and num >= 0

func getWholeNums(nums: seq[Number]): seq[Number] =
  for num in nums:
    if isWhole(num):
      result.add(num)

when isMainModule:
  assert getWholeNums(@[-3, -2, -1, 0, 1, 2, 3]) == @[0, 1, 2, 3]
  assert getWholeNums(@[-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 3.1, 3.2]) == @[0.0, 1.0, 2.0, 3.0]
```

This works fine, but `getWholeNums` can be simplified.

```nim
import math
import sequtils


type Number = int | float

func isInt(num: float): bool = (floor num) == num

func isWhole(num: int): bool = num >= 0
func isWhole(num: float): bool = isInt(num) and num >= 0

func getWholeNums(nums: seq[Number]): seq[Number] = filter(nums, isWhole)

when isMainModule:
  assert getWholeNums(@[-3, -2, -1, 0, 1, 2, 3]) == @[0, 1, 2, 3]
  assert getWholeNums(@[-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 3.1, 3.2]) == @[0.0, 1.0, 2.0, 3.0]
```

By using the `filter` procedure I'm able to save a few lines of code. I would argue that this example is slightly easier to read than the previous one as well, even though it probably won't execute quite as fast (yet to be tested).

## In Summary
* A whole number is any positive integer including the number zero
* Finding whole numbers programatically is easy!
