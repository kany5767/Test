total_seconds = int(input("กรุณาใส่จำนวนวินาที: "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

time_format = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
print("เวลา:", time_format)
