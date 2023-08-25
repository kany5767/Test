def format_range(start, end):
    if start == end:
        return str(start)
    return f"{start} - {end}"

def main():
    array = [1, 4, 6, 9, 10, 14, 16, 17]
    formatted_result = []

    i = 0
    while i < len(array):
        start = array[i]
        end = start

        while i + 1 < len(array) and array[i + 1] == end + 1:
            end = array[i + 1]
            i += 1

        formatted_result.append(format_range(start, end))
        i += 1

    result = ", ".join(formatted_result)
    print("ผลลัพธ์ที่ได้:")
    print(result)

if __name__ == "__main__":
    main()
