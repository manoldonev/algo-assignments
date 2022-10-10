from heapq import heapify, heappop


def schedule_by_difference(jobs):
    """Schedule jobs by maximizing weight - length difference;
    break ties by scheduling job with higher weight first"""
    # negate difference weight-length and weight to comply with tiebreak rule (max heap)
    diff_list = [(l - w, -w, l) for w, l in jobs]
    heapify(diff_list)
    while diff_list:
        _, minus_w, l = heappop(diff_list)
        yield -minus_w, l


def schedule_by_ratio(jobs):
    """Schedule jobs by maximizing weight / length ratio;
    break ties arbitrarily"""
    # negate ratio weight/length (max heap)
    diff_list = [(-w / l, w, l) for w, l in jobs]
    heapify(diff_list)
    while diff_list:
        _, w, l = heappop(diff_list)
        yield w, l
