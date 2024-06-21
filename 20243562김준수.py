import random

n = int(input("한 행에 출력할 구구단의 개수를 입력하세요: "))
if n < 1:
    print("한 행에 출력할 구구단의 개수가 1보다 작아서 실행이 불가능합니다.")
else:
    st_dan = int(input("<2단부터 시작: 1 | 입력한 단부터 시작: 2 | 2~10사이의 랜덤단으로 시작: 3> =>"))
    if st_dan == 1:
        start = 2
    elif st_dan ==2:
        start = int(input("몇단부터 시작할까요?"))
    elif st_dan ==3:
        start = random.randint(2,10) #2부터 10까지

    
end = int(input("최대 출력할 단 수를 입력하세요: "))
print("------------------"*n)
    
for row in range(start, end + 1, n):
    print(" => %d단 부터 %d단까지 출력" % (row, min(row + n - 1, end)))
    for i in range(1, 10):
        print("|\t",end="")
        for j in range(row, min(row + n, end + 1)):
            print("%d * %d = %d\t" % (j, i, j*i), end="")
        print("|",end="")
        print("")
    print("------------------"*n)