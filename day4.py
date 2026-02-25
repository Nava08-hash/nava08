def remove_duplicates(nums):
    if not nums:
        return []
    result = [nums[0]]
    for x in nums[1:]:
        if x != result[-1]:
            result.append(x)
    return result


# Test cases
if __name__ == "__main__":
    # Test 1
    test1 = [1, 1, 2, 2, 2, 3, 4, 4, 5]
    print(f"Input: {test1}")
    print(f"Output: {remove_duplicates(test1)}")
    
    # Test 2
    test2 = [1, 1, 1, 1]
    print(f"\nInput: {test2}")
    print(f"Output: {remove_duplicates(test2)}")
    
    # Test 3
    test3 = []
    print(f"\nInput: {test3}")
    print(f"Output: {remove_duplicates(test3)}")


# Sign of the Product of an Array
def array_sign(nums):
    """Return sign of product: 1 (positive), -1 (negative), 0 (zero)."""
    negative_count = 0
    
    for num in nums:
        if num == 0:
            return 0
        if num < 0:
            negative_count += 1
    
    return -1 if negative_count % 2 == 1 else 1


# Test sign function
print("\n--- Sign of Product ---")
test_sign1 = [-1, -2, -3, -4, 3, 2, 1]
print(f"Array: {test_sign1}")
print(f"Sign: {array_sign(test_sign1)}")

test_sign2 = [-1, 0, -2]
print(f"\nArray: {test_sign2}")
print(f"Sign: {array_sign(test_sign2)}")

test_sign3 = [1, 2, 3, 4]
print(f"\nArray: {test_sign3}")
print(f"Sign: {array_sign(test_sign3)}")


# Intersection of Two Arrays (LeetCode 349)
def intersection(nums1, nums2):
    """
    Return an array of their intersection.
    Each element in the result must be unique and you may return the result in any order.
    """
    return list(set(nums1) & set(nums2))


# Intersection of Two Arrays II (LeetCode 350)
def intersect(nums1, nums2):
    """
    Return an array of their intersection where each element can appear multiple times.
    Each element in the result must appear as many times as it shows in both arrays.
    """
    from collections import Counter
    count = Counter(nums1)
    result = []
    for num in nums2:
        if count[num] > 0:
            result.append(num)
            count[num] -= 1
    return result


# Test intersection function (LeetCode 349)
print("\n--- Intersection of Two Arrays (LeetCode 349) ---")
nums1_test1 = [1, 2, 2, 1]
nums2_test1 = [2, 2]
print(f"Input: nums1 = {nums1_test1}, nums2 = {nums2_test1}")
print(f"Output: {intersection(nums1_test1, nums2_test1)}")

nums1_test2 = [4, 9, 5]
nums2_test2 = [9, 4, 9, 8, 4]
print(f"\nInput: nums1 = {nums1_test2}, nums2 = {nums2_test2}")
print(f"Output: {intersection(nums1_test2, nums2_test2)}")

# Test intersect function (LeetCode 350)
print("\n--- Intersection of Two Arrays II (LeetCode 350) ---")
nums1_test3 = [1, 2, 2, 1]
nums2_test3 = [2, 2]
print(f"Input: nums1 = {nums1_test3}, nums2 = {nums2_test3}")
print(f"Output: {intersect(nums1_test3, nums2_test3)}")

nums1_test4 = [4, 9, 5]
nums2_test4 = [9, 4, 9, 8, 4]
print(f"\nInput: nums1 = {nums1_test4}, nums2 = {nums2_test4}")
print(f"Output: {intersect(nums1_test4, nums2_test4)}")
