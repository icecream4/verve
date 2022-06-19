import argparse


def twoSum(nums, target=2020):
    """
    Return the multiply of two numbers of input list which sum is equal to 'target'.
    Return list of solutions, if in input list more then one pair of numbers which sum is equal to 'target'.
    
    Algorithm complexity is 0(n), where n - is input list length.
    Used one for loop to memorize what number is visited, 
    for each number cheack if number2 = 'target' - number visited, 
    if yes return multiply of number and number2.
    """
    results = []
    visited = set()
    for i in range(len(nums)):
        if (target - nums[i]) in visited:
            results.append(nums[i] * (target - nums[i]))

        visited.add(nums[i])
    
    return results


def threeSum(nums, target=2020):
    """
    Return the multiply of three numbers of input list which sum is equal to 'target'.
    Return list of solutions, if in input list more then one triplet of numbers which sum is equal to 'target'.
    
    Algorithm complexity is 0(n*n), where n - is input list length.
    In this algorithm used twoSum algorithm approach, 
    where in for loop for each number a twoSum function is called 
    with parameters list with numbers after number and target is 'taget' - number.
    """
    results = []
    for i in range(len(nums)-2):
        result = twoSum(nums[i+1:], target-nums[i])
        if len(result) > 0:
            for j in range(len(result)):
                results.append(nums[i] * result[j])
    
    return results


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--dataset', default="dataset", type=str,
        help='Input dataset filename'
    )

    args = parser.parse_args()

    with open(args.dataset, "r") as f:
        numbers = [int(i) for i in f.readlines()]

    print("Part One answer:", twoSum(numbers))
    print("Part Two answer:", threeSum(numbers))
