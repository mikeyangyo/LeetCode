from typing import List


def partition(arr: List[int], front: int, end: int) -> int:
    pivot_index = end
    pivot = arr[pivot_index]
    i = front - 1
    for j in range(front, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
    return i


def quick_sort(arr: List[int], front: int, end: int) -> List[int]:
    if front < end:
        pivot_index = partition(arr, front, end)
        quick_sort(arr, front, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]
        quick_sort(nums1, 0, len(nums1) - 1)


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    Solution().merge(nums1, 3, nums2, 3)
    assert (nums1 == [1, 2, 2, 3, 5, 6])
    nums1 = [1]
    nums2 = []
    Solution().merge(nums1, 1, nums2, 0)
    assert (nums1 == [1])
    print('all test cases pass')
