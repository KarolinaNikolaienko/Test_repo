presult = None
operand = None
operator = None
wait_for_number = True

while True:
    while True:
        try:
            operand = input(">>>")
            int(operand)
        except ValueError:
            print(f"'{operand}' is not a number. Enter again")
        else:
            operand = int(operand)
            if not operator:
                result = operand
            else:
                if operator == '+':
                    result += operand
                elif operator == '-':
                    result -= operand
                elif operator == '*':
                    result *= operand
                elif operator == '/':
                    result /= operand
            break

    #break
    while True:
        operator = input(">>>")
        if operator not in ['+', '-', '*', '/', '=']:
            print(f"'{operator}' is not an operator (+ - * / =). Enter again")
        else:
            break
    
    if operator == '=':
        break

print(result)