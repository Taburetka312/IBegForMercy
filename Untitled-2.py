

def times():
    first_action = True
    time_action=input("Сколько действий сделать?")
    time_actions = int(time_action)
    while time_actions>0:
        print("Введите номер действия: 1) Сложение 2) Вычитание 3) Умножение 4) Деление 5) Возведение в степень")
        act = input()
        if first_action==True:
            first_number = float(input("Введите первое число: "))
            second_number = float(input("Введите второе число:"))
        else:
            second_number = float(input("Введите число: "))
        action = int(act)
        if action==1:
            first_number = first_number+second_number           
            print(f"Ответ: {first_number}")
            first_action = False
        elif action==2:
            first_number = first_number-second_number
            print(f"Ответ: {first_number}")
            first_action = False
        elif action==3:
            first_number = first_number*second_number
            print(f"Ответ: {first_number}")
            first_action = False
        elif action==4:
            if second_number==0:
                print("Деление на 0 невозможно")
                time_actions+=1
            else:
                first_number = first_number/second_number
                print(f"Ответ: {first_number}")
                first_action = False
        elif action==5:
            first_number = first_number**second_number
            print(f"Ответ: {first_number}")
            first_action = False
        time_actions-=1
    
    

    




times()

