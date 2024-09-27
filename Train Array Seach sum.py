number_list = []
print("Enter '0' for calculate")

# ลูปป้อนตัวเลข
while True:
    number = int(input("Enter number : "))
    # ใส่ 0 เพื่อหยุดรับตัวเลข
    if number == 0:
        break

    number_list.append(number)

print("List of numbers:", number_list)
# ผลบวกที่ต้องการ
target_number = int(input("Enter desired sum : "))


# ฟังก์ชันหาคู่ของตัวเลข ตามที่ผลบวกต้องการ แบ่งเป็นเซ็ต
def find_sum(num, sum):
    search = set()

    # ลูปตรวจสอบใน number_list
    for i in num:
        cal_sum = target_number - i

        if cal_sum in search:
            return (i, cal_sum)

        search.add(i)
    return None


result = find_sum(number_list, target_number)

if result:
    print(f"True becase {result[0]} + {result[1]} = {target_number}")
else:
    print(f"Not found that sum to the desired")
