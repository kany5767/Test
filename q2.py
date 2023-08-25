def check_similarity(s1, s2):
    if len(s1) != len(s2):
        return False

    count = [0] * 26  # จำนวนของตัวอักษร a-z

    for char in s1:
        count[ord(char) - ord('a')] += 1

    for char in s2:
        count[ord(char) - ord('a')] -= 1

    return all(value == 0 for value in count)

def main():
    s1 = input("กรุณาใส่สตริงที่หนึ่ง: ").lower()
    s2 = input("กรุณาใส่สตริงที่สอง: ").lower()

    if check_similarity(s1, s2):
        print("ผลลัพธ์: true")
    else:
        print("ผลลัพธ์: false")

if __name__ == "__main__":
    main()
