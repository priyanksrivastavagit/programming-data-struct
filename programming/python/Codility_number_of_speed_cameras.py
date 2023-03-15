
def solution(S):

    # Initialize variables
    # List of rights cars with same size as S
    # List of left cars with same size as S
    # Count of right cars
    # Count of left cars
    right = [0] * len(S)
    left = [0] * len(S)
    right_cars = 0
    left_cars = 0

    for i in range(len(S)):

        if S[i] == '.':
            right[i] = right_cars
        elif S[i] == '>':
            right_cars = right_cars + 1


    for i in range(len(S) - 1, -1, -1):

        if S[i] == '.':
            left[i] = left_cars
        elif S[i] == '<':
            left_cars = left_cars + 1

    passes = 0

    for i in range(0, len(S)):
        passes = passes + left[i] + right[i]


    return passes

