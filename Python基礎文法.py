# python 資料型態
# 數值型態：int 整數, float 浮點數, bool 布林值
# 字串型態：str 字串, chr 字元
# 容器型態：list 列表, dict 字典, tuple 元組

int = 1
float = 3.14
bool = True

str = 'Apple'
chr = 'A'

list = ["a", "b", "c"]
dict = {'Name': 'David', 'Age': 22}
tuple = 10, 20, 30

# if 文法示範

a = eval(input("a = "))
b = eval(input("b = "))

if a > b:
    print("a > b")
elif a == b:
    print("a = b")
else:
    print("a < b")

# while 文法示範

result = 0
i = 1
n = 10

while i <= n:
    print("i = ", i)
    result += i
    i += 1

print("result = ", result)

# for 文法示範

for i in range(3):
    for j in range(3):
        print("i = {:d}\tj = {:d}".format(i, j))
