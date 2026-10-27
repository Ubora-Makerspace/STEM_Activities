numbers = [9, 23, 3, 4, 5, 45, 76, 47, -56, 0, 19, 1]
sum = 0
min = 20000
max = -20000
med = 0
for num in numbers:
    sum = sum + num
    if num < min:
        min = num
    if num > max:
        max = num
        
sort_numbers = numbers

for i in range(len(sort_numbers)):
    for j in range(len(sort_numbers)-1):
        if sort_numbers[j] > sort_numbers[j + 1]:
            sort_numbers[j],sort_numbers[j + 1] = sort_numbers[j + 1], sort_numbers[j]

print("Sorted numbers:", sort_numbers)           

#Median
if len(sort_numbers) % 2 == 1:
    med = sort_numbers[(len(sort_numbers)//2)]
else:
    med1 = sort_numbers[(len(sort_numbers)//2)]
    med2 = sort_numbers[(len(sort_numbers)//2) - 1] 
    med = int((med1 + med2)/2)
    
print("Sum:", sum)
print("Min:", min)
print("Max:", max)
if len(sort_numbers) % 2 == 0:
    print(f"Median is the sum of the two middle values: {med1} & {med2} divided by 2 = {med}")
else:
    print(f"Median: {med}")