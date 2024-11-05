#Maximum Subarray Sum (Window Pattern)
#Given an array of integers, find the maximum sum of a subarray with the lenght k.

def maxSubArray(arr, k):
    maxSum = 0
    windowSum = 0
    windowStart = 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowEnd >= k - 1:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return maxSum #Max sum of subarray given k

#Test cases
errors = False

try:
    assert maxSubArray([2, 3, 2, 4, 1, 5], 2) == 6
except AssertionError:
    print("Test case failed: [2, 3, 2, 4, 1, 5], 2")
    errors=True

try:
    assert maxSubArray([2, 1, 5, 1, 3, 5, 2], 3) == 10
except AssertionError:
    print("Test case failed: [2, 1, 5, 1, 3, 5, 2], 3")
    errors=True

try:
    assert maxSubArray([8,6,1,9,12,1,6,22], 2) == 28
except AssertionError:
    print("Test case failed: [8,6,1,9,12,1,6,22], 2")
    errors=True

try:
    assert maxSubArray([8,3,1,9,12,6,22], 2) == 28
except AssertionError:
    print("Test case failed: [8,3,1,9,12,6,22], 2")
    errors=True

try:
    assert maxSubArray([8,3,1,9,12,6,22], 3) == 40
except AssertionError:
    print("Test case failed: [8,3,1,9,12,6,22] 3")
    errors=True

if not errors:
    print("All test cases passed!")