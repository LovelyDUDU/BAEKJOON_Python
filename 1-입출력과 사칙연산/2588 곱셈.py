# 123, 456
x = input()
y = input()
a = int(x)*int(y[2])
b = int(x)*int(y[1])
c = int(x)*int(y[0])
z = a + b*10 + c*100
print(a)
print(b)
print(c)
print(z)

# inp1 = int(input())
# inp2 = int(input())

# out1 = inp1*((inp2%100)%10)
# out2 = inp1*((inp2%100)//10)
# out3 = inp1*(inp2//10)
# res = inp1*inp2

# print(out1,out2,out3, res, sep= '\n')

# sep 파라미터는 print함수에서 출력할 값이 여러개일때
# 각 값의 사이사이에 삽입할 문자를 지정할 수 있는 파라미터다.