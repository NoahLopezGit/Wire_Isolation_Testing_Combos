import math

def verify_all_isolated_n(n, check_isolation):
    """
    Verify all pins 1..n are mutually isolated using the fewest calls.
    Uses ceil(log2(n)) disjoint bipartitions; early-exits on failure.

    check_isolation(A, B) must return True iff all cross-pairs AxB are isolated.
    """
    if n <= 1:
        return True

    pins = list(range(1, n + 1))
    k = math.ceil(math.log2(n))  # minimal number of calls

    test_lists = []

    for i in range(k):
        # Split by bit i of (index), to guarantee every pair is separated at least once
        A, B = [], []
        for idx, p in enumerate(pins):           # idx = 0..n-1
            if (idx >> i) & 1 == 0:
                A.append(p)
            else:
                B.append(p)

        test_lists.append((A, B))

        # Sanity: A and B are disjoint and cover all pins
        # Sizes differ by at most 1 (roughly n//2 and n - n//2)
        if not check_isolation(A, B):
            return False, test_lists  # found a violation

    return True, test_lists  # all cuts passed → every pair was separated at least once


def check_isolation(A, B):
    return True


if __name__ == "__main__":
    pins = 10000

    result, test_lists = verify_all_isolated_n(pins, check_isolation)
    print((len(test_lists)))