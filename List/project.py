number_of_days = input("How many days temprature: ")

temprature_record_by_days = list()

for i in range(0,int(number_of_days)):
    value = input("Day"+str(i)+"'s high temp: ")
    value = int(value)
    temprature_record_by_days.append(value)

avg = sum(temprature_record_by_days) / len(temprature_record_by_days)
print("Average: ",avg)

count = 0

for i in temprature_record_by_days:
    if i > avg:
        count += 1

print(str(count)+" day(s) above average" )

        