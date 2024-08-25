'''
Cho 4 số X, Y, Z, T là số nguyên được nhập từ bàn phím. Bạn hãy in ra 3 dòng, dòng 1 lần lượt 4 số Y,Z,X,T mỗi số cách nhau một dấu phẩy, 
dòng 2 in ra tổng 4 số, dòng 3 in ra giá trị của biểu thử X - Y + Z * T. (Chú ý giá trị của tích Z * T và giá trị của tổng 4 số có thể tràn kiểu dữ liệu int)

Gợi ý : Tổng 4 số có thể bị tràn nên cần ép kiểu long long tong = (long long) x + y + z + t; Khi tính X - Y + Z * T thì cần ép kiểu Z * T vì nó sẽ bị tràn.
Nếu không muốn ép kiểu thì bạn khai báo luôn 4 biến x, y, z, t là long long.

Input Format
1 dòng chứa 4 số X, Y, Z, T

Constraints

1<=X, Y, Z, T <= 10^9

Output Format
In ra theo yêu cầu đầu bài

Sample Input 0
93 9 93 98

Sample Output 0
9,93,93,98
293
9198

'''

x, y, z, t = map(int, input().split())
print(y, z, x, t , sep = ',')
print(x + y + z + t)
print(x - y + z *t)
