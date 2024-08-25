'''
Số hoàn hảo là số có tổng các ước thực sự (Không tính chính nó) bằng chính số đó. Cho một số nguyên dương n, kiểm tra xem n có phải là số hoàn hảo hay không.

Định lý Euclid - Euler :' Nếu p là số nguyên tố và 2^p - 1 cũng là số nguyên tố thì : 2^(p-1) * (2^p - 1) 
sẽ tạo thành 1 số hoàn hảo. Ví dụ p = 2, 2^2 - 1 = 3, 2 * 3 = 6 => HH Ví dụ p = 3, 2^3 - 1 = 7, 4 * 7 = 28 => HH

Input Format
Số nguyên dương N

Constraints
1≤N≤9*10^18

Output Format
In YES nếu N là số hoàn hảo, ngược lại in NO

Sample Input 0
28
Sample Output 0

YES
Explanation 0
28 có các ước thực sự là 1, 2, 4, 7, 14 có tổng bằng 28.
'''

from math import *

def nt(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    for i in range(2, isqrt(n) + 1):
        if nt(i) and nt(2**i - 1):
            if ((2 ** (i -1)) * (2**i - 1)) == n:
                return True
    return False

if __name__ == '__main__':
    n = int(input())
    if check(n):
        print('YES')
    else: 
        print('NO')