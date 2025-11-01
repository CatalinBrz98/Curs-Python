from datetime import datetime
import random


def timer_decorator(f):
    def wrapper_with_timer(*args, **kwargs):
        now = datetime.now()
        rezultat = f(*args, **kwargs)
        print(f'Rularea a durat {datetime.now() - now}.')
        return rezultat

    return wrapper_with_timer

@timer_decorator
def normal_search(x, nums):
    for i, y in enumerate(nums):
        if y == x:
            return i
    return None

@timer_decorator
def binary_search(x, nums):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return None

@timer_decorator
def random_distinct_numbers_list(nums):
    return_list = []
    for num in nums:
        if num not in return_list:
            return_list.append(num)
    return return_list

@timer_decorator
def random_distinct_numbers_set(nums):
    return_set = set()
    for num in nums:
        if num not in return_set:
            return_set.add(num)
    return return_set



if __name__ == '__main__':
    # print(normal_search(-1, list(range(100000000))))
    # print(binary_search(-1, list(range(1000000000))))
    nums = [random.randint(1, 100000) for _ in range(100000)]
    print(random_distinct_numbers_list(nums))
    print(random_distinct_numbers_set(nums))