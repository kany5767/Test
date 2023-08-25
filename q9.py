def reverse_words(sentence):
    words = sentence.split()  # แยกประโยคเป็นคำๆ
    reversed_words = [word[::-1] for word in words]  # สร้างคำที่ถูกเปลี่ยนลำดับตัวอักษรแล้ว
    reversed_sentence = ' '.join(reversed_words)  # รวมคำเป็นประโยคใหม่
    return reversed_sentence

def main():
    input_sentence = input("กรุณาใส่คำหรือประโยค: ")
    reversed_result = reverse_words(input_sentence)
    print("ผลลัพธ์หลังจาก revert คำ:", reversed_result) 

if __name__ == "__main__":
    main()
