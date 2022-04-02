numbers=[0]+list(map(int,input().split()))

remember=numbers[:]

def check(arr):
    if arr[1]==arr[2]==arr[3]==arr[4]:
        if arr[5]==arr[6]==arr[7]==arr[8]:
            if arr[9]==arr[10]==arr[11]==arr[12]:
                if arr[13]==arr[14]==arr[15]==arr[16]:
                    if arr[17]==arr[18]==arr[19]==arr[20]:
                        if arr[21]==arr[22]==arr[23]==arr[24]:
                            return True

    return False

# front
numbers[3],numbers[4],numbers[17],numbers[19],numbers[10],numbers[9],numbers[16],numbers[14]=numbers[17],numbers[19],numbers[10],numbers[9],numbers[16],numbers[14],numbers[3],numbers[4]
if check(numbers):
    print(1)
    exit(0)
numbers=remember[:]

numbers[17],numbers[19],numbers[10],numbers[9],numbers[16],numbers[14],numbers[3],numbers[4]=numbers[3],numbers[4],numbers[17],numbers[19],numbers[10],numbers[9],numbers[16],numbers[14]
if check(numbers):
    print(1)
    exit(0)
numbers=remember[:]

# back
numbers[1],numbers[2],numbers[18],numbers[20],numbers[12],numbers[11],numbers[15],numbers[13]=numbers[18],numbers[20],numbers[12],numbers[11],numbers[15],numbers[13],numbers[1],numbers[2]
if check(numbers):
    print(1)
    exit(0)
numbers=remember[:]

numbers[18],numbers[20],numbers[12],numbers[11],numbers[15],numbers[13],numbers[1],numbers[2]=numbers[1],numbers[2],numbers[18],numbers[20],numbers[12],numbers[11],numbers[15],numbers[13]
if check(numbers):
    print(1)
    exit(0)
numbers=remember[:]

# right
numbers[2],numbers[4],numbers[6],numbers[8],numbers[10],numbers[12],numbers[23],numbers[21]=numbers[6],numbers[8],numbers[10],numbers[12],numbers[23],numbers[21],numbers[2],numbers[4]
if check(numbers):
    print(1)
    exit(0)
numbers=remember[:]

numbers[6],numbers[8],numbers[10],numbers[12],numbers[23],numbers[21],numbers[2],numbers[4]=numbers[2],numbers[4],numbers[6],numbers[8],numbers[10],numbers[12],numbers[23],numbers[21]
if check(numbers):
    print(1)
    exit(0)
numbers=remember[:]

# left
numbers[1],numbers[3],numbers[5],numbers[7],numbers[9],numbers[11],numbers[24],numbers[22]=numbers[5],numbers[7],numbers[9],numbers[11],numbers[24],numbers[22],numbers[1],numbers[3]
if check(numbers):
    print(1)
    exit(0)
numbers=remember[:]

numbers[5],numbers[7],numbers[9],numbers[11],numbers[24],numbers[22],numbers[1],numbers[3]=numbers[1],numbers[3],numbers[5],numbers[7],numbers[9],numbers[11],numbers[24],numbers[22]
if check(numbers):
    print(1)
    exit(0)
numbers=remember[:]

# top
numbers[13],numbers[14],numbers[5],numbers[6],numbers[17],numbers[18],numbers[21],numbers[22]=numbers[5],numbers[6],numbers[17],numbers[18],numbers[21],numbers[22],numbers[13],numbers[14]
if check(numbers):
    print(1)
    exit(0)
numbers=remember[:]

numbers[5],numbers[6],numbers[17],numbers[18],numbers[21],numbers[22],numbers[13],numbers[14]=numbers[13],numbers[14],numbers[5],numbers[6],numbers[17],numbers[18],numbers[21],numbers[22]
if check(numbers):
    print(1)
    exit(0)
numbers=remember[:]

# bottom
numbers[15],numbers[16],numbers[7],numbers[8],numbers[19],numbers[20],numbers[23],numbers[24]=numbers[7],numbers[8],numbers[19],numbers[20],numbers[23],numbers[24],numbers[15],numbers[16]
if check(numbers):
    print(1)
    exit(0)
numbers=remember[:]

numbers[7],numbers[8],numbers[19],numbers[20],numbers[23],numbers[24],numbers[15],numbers[16]=numbers[15],numbers[16],numbers[7],numbers[8],numbers[19],numbers[20],numbers[23],numbers[24]
if check(numbers):
    print(1)
    exit(0)
numbers=remember[:]

print(0)