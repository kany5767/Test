def calculate_change(total_price, payment):
    available_denominations = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    
    change = payment - total_price
    change_details = {}

    for denomination in available_denominations:
        if change >= denomination:
            count = change // denomination
            change_details[denomination] = count
            change -= count * denomination

    return change_details

def main():
    total_price = int(input("จำนวนเงินที่ต้องชำระ: ")) 
    payment = int(input("จำนวนเงินที่ลูกค้าจ่าย: ")) 

    if payment >= total_price:
        change_details = calculate_change(total_price, payment)
        print("เงินทอน:") 
        for denomination, count in change_details.items():
            if denomination >= 20:
                print(f"{denomination} บาท: {count} ใบ")
            else:
                print(f"{denomination} บาท: {count} เหรียญ")
    else:
        print("เงินที่ลูกค้าจ่ายมาไม่พอค่ะ") 

if __name__ == "__main__":
    main()
