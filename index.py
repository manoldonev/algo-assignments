#!/usr/bin/python

from collections import defaultdict
from week1.schedule import schedule_by_difference, schedule_by_ratio


def main():
    jobs = []
    with open("tests/week1_jobs.txt") as handle:
        handle.readline()  # skip first line specifying number of jobs
        for line in handle:
            weight, length = line.split()
            jobs.append((int(weight), int(length)))

    completion_time = 0
    weighted_completion_times_sum = 0
    schedule = schedule_by_ratio(jobs)
    for weight, length in schedule:
        completion_time += length
        weighted_completion_times_sum += weight * completion_time

    return weighted_completion_times_sum


if __name__ == '__main__':
    print(main())
