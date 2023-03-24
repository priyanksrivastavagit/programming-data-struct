def solution(A):
    # Implement your solution here

    max_sum = A[0]
    max_iter = A[0]

    for i in range(1,len(A)):
        #print('-'*88)
        #print(i)
        #print(A[i])
        #print(max_iter + A[i])
        
        max_iter = max(max_iter + A[i], A[i])
        max_sum = max(max_sum, max_iter)
        #print(max_iter)
    
    return max_sum
