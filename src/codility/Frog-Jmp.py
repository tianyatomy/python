__author__="tomy"
__date__ ="$2013-12-19 21:14:40$"
def solution(X, Y, D):
    # write your code in Python 2.6
    per = (Y-X)%D
    if per == 0:
        result = (Y-X)/D
    else:
        result = (Y-X)/D+1
    print result
    return result

solution(10, 85, 30);
solution(10, 70, 30);
solution(1000000000, 1000000000, 1000000000);
solution(0, 1000000000, 500000000);
solution(0, 1000000000, 499999999);