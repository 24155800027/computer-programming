#Find all pairs of numbers in a list that add up to a target sum.

def find_pairs(lst, target_sum):
    pairs = []
    seen = set()
    for num in lst:
        diff = target_sum - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
    return pairs
