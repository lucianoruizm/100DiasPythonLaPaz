import itertools

string = "P1y2t3h4o5n6!7"
selector = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
print("".join(itertools.compress(string, selector)))