total_seconds = int(input("ใส่จำนวนวินาทีที่ต้องการทราบ: "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

time_format = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
print("เวลาที่ได้:", time_format)
