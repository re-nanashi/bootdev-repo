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
