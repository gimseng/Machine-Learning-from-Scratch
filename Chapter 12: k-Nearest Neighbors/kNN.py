from collections import Counter

def raw_majority_vote(labels):
    voters=Counter(labels)
    winner, _ = voters.most_common(1)[0]
    return winner


print(raw_majority_vote([2, 3,  1, 1, 3, 2,
                         3, 3, 5, 6, 8, 4, 8, 4]))
