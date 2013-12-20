__author__="tomy"
__date__ ="$2013-12-19 21:14:40$"

def solution(A):
    # write your code in Python 2.6
    innersum=0
    sum_value=sum(A)
    mid_value=sum_value/2
    for index in range(len(A)):
        pre_sum = innersum + A[index]
        if pre_sum > mid_value:
            break
        else:
            innersum = pre_sum
    result = abs(sum_value - 2*innersum)
    return result

print solution([3,1,2,4,3])#1
#print solution([1,2,3,4,5])
#print solution([1,2,3,4,5,6,7,8,9,10])
#print solution([-1,2,3,-4])
#print solution([-1000,1000])#2000
#print solution(range(100000))
#print solution([])