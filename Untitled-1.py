def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return [tuple(interval) for interval in merged]

if __name__ == "__main__":
    k = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(k)]
    result = merge_intervals(intervals)
    print(result)
    "'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'"

