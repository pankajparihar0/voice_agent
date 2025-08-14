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
    vHISG0GeOYBBz3x4BBXt2BUnWgrYSmVAOBfm2Wa-Wum80idlyMj8N_O5iSGot1e15_6Mu7FVj5T3BlbkFJSR3GdalWNQMtdXTonytN-WKD26BLCb_fOCz4atq27pxPzitztf7iyDryXEENCndgK5GPX5ARUA

