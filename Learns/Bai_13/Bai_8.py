'''
Nhập vào 2 số nguyên, in ra tổng, hiệu, tích, thương(lấy độ chính xác với 4 chữ số) của 2 số đó. 
Bài này có thể bị sai do 2 nguyên nhân : 1. Khi tính tích bị tràn số, 2. Độ chính xác của thương.

Input Format
2 số nguyên a, b trên 1 dòng.

Constraints
-10^8≤a,b≤10^8

Output Format
In ra tổng, hiệu, tích, thương trên từng dòng. Nếu trường hợp không thể tìm được thương của 2 số thì sẽ in ra "INVALID" 
cho dòng kết quả của thương.

Sample Input 0
7769 0
Sample Output 0

7769
7769
0
INVALID
Sample Input 1

9794 1282
Sample Output 1

11076
8512
12555908
7.6396
'''

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
if b == 0:
    print('INVALID')
else:
    print('%.4f' %(a / b))