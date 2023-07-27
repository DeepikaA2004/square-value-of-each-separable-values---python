if __name__ == '__main__':
    n = int(input())
    i=0
list=[]
while i < n:
    list.append(i)
    i=i+1
for x in list:
    print(x**2)