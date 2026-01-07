## Well, it’s time for you to test your logic skills, since this will be required both in day-to-day work and in selection processes. Try to solve the challenge below:

## You are given a list of integers in ascending order. The list is a string and represents the page numbers of a book. Write a function called last_page that returns the last page from the string. If there is any number out of order, you must return the last number that is still in order. See the 3 examples below with 3 different inputs for the program and what it should return:

## Input: '12345'

## Expected output: 5

## Input: '12345678910111213'

## Expected output: 13 

## Input: '1235678'

## Expected output: 3

## Notice that if the program receives '12345', since all page numbers are in order, you simply return the last one. In the case of '12345678910111213', the last page is 13. Here, you have an additional complication related to multi-digit numbers, so it is not enough to simply return the last character of the string — you need to think about this issue.

## Finally, we have an example where the page number sequence starts correctly but becomes incorrect starting from the 4th element. Therefore, in this last case, the program returns the 3rd element. Can you think of a solution?



def last_page(s):
    """
    Given a string of concatenated page numbers starting at 1,
    return the last page that is still in correct ascending order.
    """
    current = 1
    i = 1

    while i < len(s):
        expected = current + 1
        expected_str = str(expected)

        if s[i:i + len(expected_str)] == expected_str:
            i += len(expected_str)
            current = expected
        else:
            break

    return current

# Example usage:
print(last_page("12345"))                 # 5
print(last_page("12345678910111213"))     # 13
print(last_page("1235678"))               # 3


            
