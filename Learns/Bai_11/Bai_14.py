'''
Cho 2 số a và b, nhiệm vụ của bạn là in ra số lượng số nguyên tính từ a đến b.

Input Format
Dòng duy nhất chứa 2 số nguyên a và b.

Constraints
1<=a<=b<=10^12

Output Format
In ra kết quả của bài toán

Sample Input 0

14 19
Sample Output 0

6
'''

x, y = map(int, input().split())
print(abs(y - x + 1))