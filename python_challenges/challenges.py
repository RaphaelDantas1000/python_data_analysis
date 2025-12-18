## CHALLENGE 1:
## You need a function that will receive an array of integers, nums, of length n,
## ranging from 0 to n, with one missing number.
## Write a function called missing_number that returns the missing number.

## Input:
## nums = [1, 2, 3, 4, 5, 6, 8]
## missing_number(nums)

## Output:
## 7

def missing_number(nums):
    n = len(nums)  # numbers should go from 0 to n
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


## CHALLENGE 2:
## Create a function called largest_difference that takes a list of numbers
## as a parameter and returns the difference between the largest and smallest number.

## For simplicity, let's assume that no number is less than or greater than -100 and 100.

## Input:
## nums = [5, 10, 20, 15, 30]
## largest_difference(nums)

## Output:
## 25

def largest_difference(nums):
    return max(nums) - min(nums)


## CHALLENGE 3:
## From a dictionary containing the connection status of individuals,
## determine how many people have the status "online".

## Example dictionary:
## statuses = {
##     "Alice": "online",
##     "Bob": "offline",
##     "Eve": "online"
## }

## Develop a function called online_count.
## The function should accept a dictionary where:
## - keys are names (strings)
## - values are "online" or "offline"
## The function should return the number of people who are online.

def online_count(statuses):
    count = 0
    for status in statuses.values():
        if status == "online":
            count += 1
    return count
