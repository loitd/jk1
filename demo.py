import heapq
import math
import itertools, collections

a1 = [23,-4,5,6,-76,0,8,-9,10,11,12,-1]
# a1 = [-1,-2,-3,-4,-5]
a1 = [1,5,3]
s1 = set([1,2,4,7,9])
s2 = set([1,3,5,7,9])
s1 = "quetzalcoatl"
s2 = "tezcatlipoca"
a7 = [6,7,8,9]

def f1(n):
    """Số cách phân tích n thành tổng các số nguyên dương <= n"""
    pass

def f2(a):
    """Quy hoạch động cho bài toán tìm độ dài lớn nhất dãy con không giảm
    Thuật toán có thời gian O(n^2) và không gian O(n)"""
    n = len(a)
    l = [1]*n #Khởi tạo mảng lưu trữ bộ đếm tăng theo công thức L[1] = 1
    for i in range(n):
        for j in range(i):
            if a[i] >= a[j]: #nếu giá trị đang kiểm tra a[i] >= giá trị của phần tử trước nó a[j]
                l[i] = max(1, l[j]+1) # theo công thức Li = max (1, Lj + 1)
    return l #chỉ cần tính max(l) là ra giá trị
    # breakpoint()
    
def f3(a):
    '''Tìm đoạn con có tổng lớn nhất trong mảng a1,a2,...,an
    1. Gọi dp(p) là đoạn con có tổng lớn nhất với 0<=p<=n
    2. Chia nhỏ bài toán:
    - dp(0) = a(0)
    - dp(1) = max(dp(0), dp(0)+a[1])
    - dp(2) = max(dp(1), dp(1)+a[2])'''
    n = len(a)
    maxsum = 0 #giữ giá trị max thực sự
    s = 0 #giữ giá trị tổng tiềm năng của các phần tử, không cho phép < 0, nếu < 0 thì reset = 0 => bỏ đoạn phía trước
    for i in range(n):
        # s += a[i]
        s = max(0, s+a[i]) #reset nếu < 0
        maxsum = max(s, maxsum) #chỉ chấp nhận max nếu lớn hơn
    return maxsum 

def f4(x,n):
    '''Viết hàm f tính theo công thức đệ quy'''
    if n <= 0: return 1
    return f4(x,n-1) + x**n/math.factorial(n)

def f5(a,s):
    '''Bài toán tìm đồng xu:
    Cho a là n đồng xu nặng lần lượt a[1], a[2], ... 
    Tìm số lượng đồng xu nhỏ nhất để tổng khối lượng là S
    Phương pháp quy hoạch động: 
    1. Gọi dp(P) với P<S là bài toán tìm số đồng xu nhỏ nhất để khối lượng là P
    2. chia nhỏ thành các bài toán con bắt đầu từ dp(0) và tiếp tục với các bài toán con lớn hơn. Yêu cầu của quy hoạch động là bài toán sau phải sử dụng và yêu cầu bài toán trước phải giải được.
    Giả sử có các đồng xu có khối lượng là 1,2,4,6,8...
    dp(0) = 0                                       -> l[0] = 0
    dp(1) = dp(0)+1                                 -> l[1] = 1
    dp(2) = min(dp(1)+1, dp(2)) -> min(2,1) = 1     -> l[2] = 1
    3. Mảng lưu trữ giá trị tính toán của các bài toán con. Thường là 1 mảng.
    Ở đây sẽ là 1 mảng có độ dài S+1 (do có xuất hiện 0 và S)
    4. Yêu cầu thực hiện vòng lặp là phải thực hiện sao cho ta sẽ giải bài toán con trước từ nhỏ đến lớn lý do là do các bài toán lớn đều cần kết quả tính toán từ bài toán nhỏ.'''
    l = [0]*(s+1) #mảng lưu giữ kết quả của các bài toán con
    for p in range(1,s+1):
        # chạy toàn bảng l
        l[p] = min(l[p-x] for x in a if x<=p) + 1 #"fake đệ quy" với tất cả các giá trị đã tính trước đó
    print(l) #[0, 1, 2, 1, 2, 1, 2, 3, 2, 3, 2, 3]
    return l

def f6(s1, s2):
    '''Tìm độ dài xâu con chung nhỏ nhất giữa chúng. Ví dụ với 2 xâu "quetzalcoatl" và "tezcatlipoca" thì xâu con chung dài nhất sẽ là "ezaloa" với độ dài 6
    1. Gọi dp[i,j] là độ dài xâu chung lớn nhất của i phần tử ở s1 và j phần tử s2 -> bài toán lớn sẽ được giải nếu lấy từ dp[0,0] và tăng dần độ dài.
    2. Bắt đầu giải các bài toán con, các trường hợp ngoại lệ giải riêng, còn lại theo công thức.
    - dp(0,j) = dp(i,0) = 0
    - nếu ký tự cuối cùng ở xâu 1 không có mặt trong xâu chung con dài nhất => có thể bỏ mà không ảnh hường kết quả => dp(i,j) = dp(i-1,j)
    - tương tự với ký tự cuối ở xâu 2, dp(i,j) = dp(i,j-1)
    - cuối cùng, nếu ký tự cuối cùng của cả x1 và x2 đều có mặt trong xâu dài nhất => dp(i,j) = dp(i-1,j-1) + 1
    3. Ta sẽ lưu trữ dp của các bài toán con trong mảng 2 chiều.
    4. Tương tự yêu cầu thực hiện vòng lặp cho bài toán từ nhỏ đến lớn.'''
    n1 = len(s1)
    n2 = len(s2)
    l = [[0]*(n2+1)]*(n1+1)
    for i,x1 in enumerate(s1,1):
        for j,x2 in enumerate(s2,1):
            if x1==x2:
                l[i][j] = l[i-1][j-1]+1
            else:
                l[i][j] = max(l[i][j-1], l[i-1][j])
    print(l[-1][-1])
    return l

def f7(a):
    '''Cho 4 số 6,7,8,9. Tìm 2 số có 2 chữ số sao cho tích của chúng là lơn nhất, các chữ số chỉ được xuất hiện môt  lần. Ex: 67*89'''
    pems = itertools.permutations(a,2)
    for pem in pems: print(pem)
    pass

def f8():
    gen = (for a[i] in range(n,-1,-1))
    
    [a[i]-]

if __name__ == "__main__":
    # top3 = heapq.nsmallest(3, a1)
    # print(f2(a1))
    # print(f3(a1))
    # print(f4(4,5))
    # print(f5(a1,11))
    # s = s1.intersection(s2)
    # print(s)
    # f6(s1, s2)
    f7(a7)
    # breakpoint()