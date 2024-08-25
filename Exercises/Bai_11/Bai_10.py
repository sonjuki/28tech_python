'''
Khi bạn chia dư 1 số cho số nguyên N thì số dư của phép chia đó sẽ là các số từ 0 tới N - 1. 
Ví dụ khi bạn chia cho 5 thì phép chia có số dư có thể là 0, 1, 2, 3, 4. Bài toán này yêu cầu các bạn nhập 2 số a và b sau đó tìm phép dư khi chia a cho b.

Input Format
Dòng duy nhất chứa 2 số nguyên a, b, giữa a và b chứa 5 dấu cách

Constraints
1<=a,b<=10^6;

Output Format
In ra số dư khi chia a cho b

Sample Input 0
806     605

Sample Output 0
201
'''

a, b = map(int, input().split())
print(a % b)
