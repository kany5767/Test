def sort_numbers():
    numbers = []
    for i in range(10):
        number = int(input(f"ใส่ตัวเลขที่ {i+1}: "))
        numbers.append(number)
    
    numbers.sort()
    
    print("จำนวนที่เรียงลำดับจากน้อยไปมาก:", numbers)

sort_numbers()