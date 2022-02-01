numbers_list=list(range(1,10001))
numbers_original=numbers_list

def d(number):
    if number<10:
        return 2*number
    elif number<100:
        return number+int(str(number)[0])+int(str(number)[1])
    elif number<1000:
        return number+int(str(number)[0])+int(str(number)[1])+int(str(number)[2])
    elif number<10000:
        return number+int(str(number)[0])+int(str(number)[1])+int(str(number)[2])+int(str(number)[3])

ds=list(map(d,numbers_list))
ds.remove(None)
ds=list(set(ds))

for num in ds:
    if num<=10000:
        numbers_original.remove(num)

for i in range(len(numbers_original)):
    print(numbers_original[i])