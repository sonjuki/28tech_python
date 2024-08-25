'''
Nhập n là một số nguyên không quá 100. In ra các hình tương ứng, mỗi hình cách nhau một dòng trống.

Input Format
Số nguyên dương N

Constraints
1≤n≤100

Output Format
In ra hình số theo mẫu

Sample Input 0
5

Sample Output 0
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25 

1 2 3 4 5 
2 3 4 5 6 
3 4 5 6 7 
4 5 6 7 8 
5 6 7 8 9 

~~~~1
~~~22
~~333
~4444
55555

1 
2 6 
3 7 10 
4 8 11 13 
5 9 12 14 15 
'''

n = int(input())
dem = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(dem, end = ' ')
        dem += 1
    print()
print()

for i in range(1, n + 1):
    ktao = i
    for j in range(1, n + 1):
        print(ktao, end = ' ')
        ktao += 1
    print()
print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= n - i:
            print('~', end = '')
        else:
            print(i, end = '')
    print()
print()

for i in range(1, n + 1):
    ktao = i
    kc = n -1 
    for j in range(i):
        print(ktao, end = ' ')
        ktao += kc
        kc -=1
    print()
print()