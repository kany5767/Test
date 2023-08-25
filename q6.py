def sort_numbers_descending(numbers):
    numbers.sort(reverse=True)
    return numbers

def main():
    numbers = []
    for i in range(10):
        number = int(input(f"ใส่เลขที่ต้องการ {i+1}: "))
        numbers.append(number)
    
    sorted_numbers = sort_numbers_descending(numbers)
    print("เรียงลำดับจากมากไปน้อย:", sorted_numbers) 

if __name__ == "__main__":
    main()
