close_data = [23750,23750,23800,23550,23750,23950,
        24300,24050,23550,23650]

average_5 = 0
average_10 = 0
index = 0

for item in close_data :
    if index < 5 :
        average_5 = average_5 + item
    if index < 10 :
        average_10 = average_10 + item
    index = index + 1

average_5 = average_5 / 5
average_10 = average_10 / 10

if close_data[0] > average_5 :
    print("5일선 위에있습니다.")
else :
    print("5일선 아래있습니다.")

if close_data[0] > average_10 :
    print("10일선 위에있습니다.")
else :
    print("10일선 아래있습니다.")
