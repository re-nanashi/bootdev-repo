import math


def find_minimum(nums):
    minimum = float("inf")
    for num in nums:
        num = min(num, minimum)
    return minimum


def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]


def average_followers(nums):
    if len(nums) == 0:
        return None
    return sum(num for num in nums) / len(nums)


def get_estimated_spread(audiences_followers):
    return average_followers(audiences_followers) * (len(audiences_followers) ** 1.2)


def get_follower_prediction(follower_count, influencer_type, num_months):
    if influencer_type == "fitness":
        return follower_count * (4 ** num_months)
    if influencer_type == "cosmetic":
        return follower_count * (3 ** num_months)
    return follower_count * (2 ** num_months)


def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log(num_followers, 2)


def factorial(num):
    memo = {}

    def helper(x):
        if x in memo:
            return memo[x]
        else:
            new_ans = 1 if x > 0 and x == 1 else x * factorial(x - 1)
            memo[x] = new_ans  # insert to memo
            return new_ans
    return helper(num)


def num_possible_orders(num_posts):
    return factorial(num_posts)


def decayed_followers(intl_followers, fraction_lost_daily, days):
    return intl_followers * (1 - fraction_lost_daily)**days


def log_scale(data, base):
    def helper(x):
        return math.log(x, base)
    newlist = map(helper, data)
    print(newlist)


def find_max(nums):
    max = float("-inf")
    for num in nums:
        if num > max:
            max = num
    return max


def does_name_exist(first_names, last_names, full_name):
    for first_name in first_names:
        for last_name in last_names:
            if f"{first_name} {last_name}" == full_name:
                return True
    return False


def get_avg_brand_followers(all_handles, brand_name):
    handles_that_contain_brand_name = 0
    totallen = 0

    for handles in all_handles:
        totallen += 1
        for handle in handles:
            if brand_name in handle:
                handles_that_contain_brand_name += 1
    return handles_that_contain_brand_name / totallen * 100


def count_names(list_of_lists, target_name):
    count = 0
    for list in list_of_lists:
        for names in list:
            if names == target_name:
                count += 1
    return count


def remove_duplicates(nums):
    count = {}
    for num in nums:
        if not num in count:
            count[num] = 1
        else:
            count[num] += 1
    return list(x for x in count)


def power_set(input_set):
    if len(input_set) == 0:
        return [[]]

    subsets = []
    first = input_set[0]
    remaining = input_set[1:]
    remaining_subsets = power_set(remaining)
    for subset in remaining_subsets:
        subsets.append([first] + subset)
        subsets.append(subset)
    return subsets


def exponential_growth(n, factor, days):
    exponential_growth_list = []
    for i in range(days+1):
        exponential_growth_list.append(n * (factor**i))
    return exponential_growth_list


def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1

    while time_left >= time_in_country:
        time_left -= time_in_country
        time_in_country *= factor
        count += 1

    return count


def tsp(cities, paths, dist):
    ppaths = permutations(cities)
    for path in ppaths:
        totdist = 0
        for i in range(1, len(path)):
            totdist += paths[path[i - 1]][path[i]]
        if totdist < dist:
            return True
    return False

    # don't touch below this line


def permutations(arr):
    retval = []
    retval = helper(retval, arr, len(arr))
    return retval


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()  # original array
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res

# we have 26 characters
# if the password is length 1:: we will need 26 times to guess
# if the password is lenght 2:: we will need 702; 26^2 + 26


def get_num_guesses(length):
    count = 0
    for i in range(1, length):
        count += 26**i
    return count

# PRIME FACTORS ALGORITHM
# Given a large number, return a list of all the prime factors.
#
# prime_factors(8) -> [2, 2, 2]
# prime_factors(10) -> [2, 5]
# prime_factors(24) -> [2, 2, 2, 3]

# Divide N by two as many times as you can do so evenly (no remainder). For each division, append a 2 to the list of prime factors
# At this point, N must be odd. Start a loop that iterates over all odd numbers from 3 to the square root of N inclusive. Use math.sqrt().
# For each number i, if N can be divided evenly by i, then divide N by i and append i to the list. Repeat this (nested loop) until i can't divide evenly into N, then move on to the next i
# If N is still greater than 2 after that loop, it must still be prime, so just append it to the list.
# Return the list of primes
# ASSIGNMENT
# Complete the prime_factors function according to the given algorithm. Notice how the algorithm gets much slower as the size of the input (in bits) grows.
#
# Note: The returned list should only contain ints, no floats.


def prime_factors(n):
    pfactors = []
    while n % 2:
        n /= 2
        pfactors.append(2)
    end = math.sqrt(n)
    for i in range(3, int(end) + 1):
        while n % i == 0:
            n /= i
            pfactors.append(i)
    if n > 2:
        pfactors.append(n)

    return pfactors
