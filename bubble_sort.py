from random import randint
def main():
    number_list = [randint(0, 10) for _ in range(10)]
    for i in range(len(number_list)-1):
        flag:bool =True
        for j in range(len(number_list)-i-1):
            if number_list[j] > number_list[j+1]:
                flag = False
                number_list[j],number_list[j+1] = number_list[j+1],number_list[j]
        if flag:
            break
    print(number_list)

for i in range(10):
    main()

