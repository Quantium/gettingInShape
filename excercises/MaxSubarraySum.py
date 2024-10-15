#Maximum Subarray Sum (Window Pattern)
#Given an array of integers, find the maximum sum of a subarray with the lenght k.

def maxSubArray(arr, k):
    return None #Max sum of subarray given k

#Test cases
errors = False
try:
    assert maxSubArray([2, 3, 4, 1, 5], 2) == 9
except AssertionError:
    print("Test case failed: [2, 3, 4, 1, 5], 2")
    errors=True

try:
    assert maxSubArray([2, 1, 5, 1, 3, 2], 3) == 10
except AssertionError:
    print("Test case failed: [2, 1, 5, 1, 3, 2], 3")
    errors=True

try:
    assert maxSubArray([8,3,1,9,12,6,22], 2) == 34
except AssertionError:
    print("Test case failed: [8,3,1,9,12,6,22], 2")
    errors=True

try:
    assert maxSubArray([8,3,1,9,12,6,22], 2) == 34
except AssertionError:
    print("Test case failed: [8,3,1,9,12,6,22], 2")
    errors=True

try:
    assert maxSubArray([8,3,1,9,12,6,22], 3) == 43
except AssertionError:
    print("Test case failed: [8,3,1,9,12,6,22], 3")
    errors=True

if not errors:
    print("All test cases passed!")