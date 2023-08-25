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
    s1 = input("คำที่ 1: ").lower()
    s2 = input("คำที่ 2: ").lower()

    if check_similarity(s1, s2):
        print("ผลลัพธ์ที่ได้: true")
    else:
        print("ผลลัพธ์ที่ได้: false")

if __name__ == "__main__":
    main()
