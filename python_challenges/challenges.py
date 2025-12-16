## CHALLENGE 1: You need a function that will receive an array of integers, nums, of length n, ranging from 0 to n, with one missing number. Write a function called missing_number that returns the missing number in the array.

## Input:

## nums = [1,2,3,4,5,6,8] 

## missing_number(nums)

## Output: 

## 7​

def missing_number(nums):
    n = len(nums)  # numbers should go from 0 to n
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


