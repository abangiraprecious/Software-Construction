def sum_of_events(nums):
    return sum(num for num in nums if num % 2 == 0)

def test_sum_of_events():
    # Test Case 1: Regular case with positive numbers
    nums1 = [2, 4, 6]
    assert sum_of_events(nums1) == 12

    # Test Case 2: Regular case with negative numbers
    nums2 = [-3, 5, -6, 8]
    assert sum_of_events(nums2) == 2

    # Test Case 3: Edge case with all odd numbers
    nums3 = [1, 3, 5]
    assert sum_of_events(nums3) == 0

    # Test Case 4: Edge case with all even numbers
    nums4 = [2, 4, 6]
    assert sum_of_events(nums4) == 12

    # Test Case 5: Edge case with empty list
    nums5 = []
    assert sum_of_events(nums5) == 0

    print("All test cases passed successfully!")

test_sum_of_events()