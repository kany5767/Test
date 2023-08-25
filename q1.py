def find_pairs_with_sum(nums, target_sum):
    pairs = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target_sum:
                pairs.append((nums[i], nums[j]))

    return pairs

def main():
    array = [1, 2, 3, 4, 5]
    target_sum = int(input("Enter Number: "))

    pairs = find_pairs_with_sum(array, target_sum)

    if len(pairs) > 0:
        print("Result:")
        for pair in pairs:
            print(f"{pair[0]},{pair[1]}")
    else:
        print("Sum not found", target_sum)

if __name__ == "__main__":
    main()
