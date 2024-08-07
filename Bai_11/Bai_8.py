'''
Trong ngôn ngữ lập trình như C, C++, Java khi bạn sử dụng 2 số nguyên để chia cho nhau thì kết quả của phép chia đó chỉ dữ lại phần nguyên cho dù bạn có để kết quả ở số thực như float
hay double. Ví dụ a = 10, b = 3 thì phép chia a / b sẽ có kết quả là 3 thay vì 3.3333, 
để lấy được phần thập phân khi chia 2 số nguyên cho nhau bạn cần thực hiện ép kiểu a hoặc b, 
hoặc cả 2 và b sang dạng số thực trước khi chia. Ví dụ float c = (float) a / b thì khi đó c = 3.3333

Gợi ý : Bạn nên sử dụng số double khi chia thập phân để kết quả có độ chính xác tốt hơn

Input Format
1 dòng duy nhất chứa lần lượt 2 số nguyên b và a;

Constraints
1<=a,b<=1000;

Output Format
Dòng 1 in ra thương của a / b khi sử dụng phép chia nguyên; Dòng 2 in ra thương của a / b khi sử dụng phép chia lấy phần thập phân với độ chính xác 2 số sau dấu phẩy.

Sample Input 0
30 70

Sample Output 0
2
2.33

Sample Input 1
39 259

Sample Output 1
6
6.64
'''

b, a = map(int, input().split())
print(a // b)
print('%.2f' %(a / b))