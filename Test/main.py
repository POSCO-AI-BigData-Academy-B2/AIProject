def solution(n, k):
    if (n//10>0):
        service = n//10
    else:
        service = 0
    total = (12000*n)+(2000*(k-service))
    answer = 0
    return answer