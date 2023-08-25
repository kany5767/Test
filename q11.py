def sort_numbers():
    numbers = []
    for i in range(10):
        number = int(input(f"ใส่เลขที่ต้องการ {i+1}: "))
        numbers.append(number)
    
    numbers.sort()
    
    print("เรียงลำกับจากน้อยไปมาก:", numbers) 

sort_numbers()