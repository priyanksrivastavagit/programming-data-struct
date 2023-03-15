def solution(A):
    # Implement your solution here

    num_0 = 0
    passes = 0

    for i in range(len(A)):
        if A[i] == 0:
            num_0 += 1
        elif A[i] == 1:
            passes += num_0


    return passes
