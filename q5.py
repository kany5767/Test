num = int(input("Input Number 1-4: "))

if 1 <= num <= 4:
    n = 1
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(n, end='')
            n = (n + 1) % 10
        print()
else:
    print("ตัวเลขไม่ถูกต้อง")