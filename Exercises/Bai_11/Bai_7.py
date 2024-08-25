'''
Cho nguyên dương N, bạn hãy sử dụng phép chia dư để lấy ra chữ số cuối cùng và 2 chữ số cuối cùng của N. 
Gợi ý : Để lấy chữ số cuối cùng của N bạn chỉ cần lấy N chia dư cho 10. Ví dụ N = 1234 % 10 = 4. 
Tương tự để lấy 2 chữ số cuối cùng của N bạn chỉ cần lấy N chia dư cho 100. Ví dụ N = 1234 % 100 = 34. ....

Lưu ý chọn kiểu dữ liệu của N cho phù hợp

int main(){
    //Khai báo biến nguyên n
    //Nhập n từ bàn phím
    //In ra n % 10
    //In ra n % 100
}

Input Format
1 dòng duy nhất chứa số nguyên dương N

Constraints
100<=N<=10^18

Output Format
Dòng 1 in ra chữ số cuối cùng; Dòng 2 in ra 2 chữ số cuối cùng, nếu 2 chữ số cuối cùng của N có số 0 ở đầu thì bạn bỏ đi số 0 đó và chỉ in ra số cuối cùng.

Sample Input 0
1005

Sample Output 0
5
5
'''

n = int(input())

tmp = n % 10
print(tmp)
n = n//10

tmp = (n % 10)*10 + tmp

print(tmp)