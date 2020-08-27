"""
Project 7: Lis
solves the longest increasing subsequence problem
Sources: https://stackoverflow.com/questions/3992697/longest-increasing-subsequence?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
"""
def verify_subseq(seq, subseq):
    """
    iterates through the subseq and checks to see if
    it exists in the actual seq.
    """
    # initializes counter
    sublen = len(subseq)
    seqlen = len(seq)
    if sublen > seqlen:
        return False
    i = 0
    j = 0
    d1 = sublen
    d2 = seqlen
    while i < sublen and j < seqlen:
        # iterate through subsequence
        while subseq[i] != seq[j]:
            j += 1
            d2 -= 1
            if d1 > d2:
                return False
        i += 1
        j += 1
        d1 -= 1
        d2 -= 1
        if d1 > d2:
            return False
    return True

def verify_increasing(seq):
    """
    iterate through the sequence check to see if
    previous element is less than current.
    """
    initial = 0
    # initializes counter
    result = True
    # initializes result
    for i in range(1, len(seq)):
        # iterate through subsequence
        current = i
        if seq[initial] >= seq[current]:
            # checks if the previous item is less than current
            result = False
            return result
            # returns result if not less than
        else:
            initial = current
    # returns result
    return result

def find_lis(seq):
    """
    Finds the longest increasing subsequence of
    the given sequence.
    """
    if not seq:
    # if the seq doesn't exist
        return seq
    length = 1
    # marks the length of longest incresing subsequence
    m = [None] * len(seq)
    # list that points to smallest val
    p = [None] * len(seq)
    # list with previous val
    m[0] = 0
    # Looping over the sequence starting from the second element
    for i in range(1, len(seq)):
        # Binary search
        lower = 0
        upper = length
        if seq[m[upper-1]] < seq[i]:
        # look at the upper bound value
            j = upper
        else:
            # binary search loop
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[m[mid-1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid
            j = lower #set the default value to 0
        p[i] = m[j-1]
        if j == length or seq[i] < seq[m[j]]:
            m[j] = i
            length = max(length, j+1)
    result = []
    pos = m[length-1]
    for _ in range(length):
        result.append(seq[pos])
        pos = p[pos]
    result.reverse()
    return result # reverse the list
