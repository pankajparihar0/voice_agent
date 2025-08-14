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

