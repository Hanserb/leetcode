def topKFrequent(nums, k):
    # Count will hold {value : freq}
    count = {}

    # Freq will hold a list of lists of size nums
    freq = [[] for i in range(len(nums) + 1)]

    # Count: { "1": 3, "2": 2, "3": 1}
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    # Index will represent what number and freq will hold how many were counted
    # Index:   0    1    2    3    4    5    6
    # Freq: [ [ ], [3], [2], [1], [ ], [ ], [ ]]
    for n, c in count.items():
        freq[c].append(n)

    # Res: [ 1, 2]
    res = []

    # Count from the back of the list and return the number most freq k times
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(topKFrequent(nums, k))
