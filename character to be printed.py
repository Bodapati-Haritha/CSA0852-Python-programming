char = input("Enter the Character to be printed: ")
max_num = int(input("Max Number of times to be printed: "))

for i in range(1, max_num+1):
    print(char * i)
