# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # Implement your solution here

    flag = True
    rot = 0
    no_match = True
    n = len(A)

    while flag and rot < n:
        for i in range(n):
            if A[i] == B[i]:
                rot += 1
                B = B[-1:] + B[:-1]
                break
            elif i == n - 1:
                flag = False
                
        if rot == n:
            no_match = False
        
    return -1 if not no_match else rot
