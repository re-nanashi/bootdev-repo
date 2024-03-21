def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return False


def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping == True:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i], nums[i - 1] = nums[i - 1], nums[1]
                swapping = True
        end -= 1
    return nums


def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    first_half = merge_sort(nums[:mid])
    second_half = merge_sort(nums[mid:])
    return merge(first_half, second_half)


def merge(first, second):
    sorted = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            sorted.append(first[i])
            i += 1
        else:
            sorted.append(second[j])
            j += 1
    while i < len(first):
        sorted.append(first[i])
        i += 1
    while j < len(second):
        sorted.append(second[j])
        j += 1
    return sorted


def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums


def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i


def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quick_sort(nums, low, p - 1)
        quick_sort(nums, p + 1, high)
