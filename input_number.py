result = None
operand = None
operator = None
operator_list = ["-","+","*","/","="]
num_list = []
wait_for_number = True
while True:
    if wait_for_number == True:
        try:
            operand = int(input("operand (number): "))
            num = operand
            num_list.append(num)
            print("num_list", num_list)
            wait_for_number = False
        except ValueError:
            print("input number, try again")
            wait_for_number = True
            
    if len(num_list) == 3:
        a = num_list.pop()
        symbol = num_list.pop()
        b = num_list.pop()
        if symbol == "+":
            result = b+a
            num_list.clear()
            num_list.append(result)
        if symbol == "-":
            result = b-a
            num_list.clear()
            num_list.append(result)
        if symbol == "*":
            result = b*a
            num_list.clear()
            num_list.append(result)
        if symbol == "/":
            result = b/a
            num_list.clear()
            num_list.append(result)
            
    if wait_for_number == False:
        operator = (input("operator: "))
        if operator in operator_list:
            num_list.append(operator)
            print("num_list", num_list)
            wait_for_number = True
            if operator == "=":
                print("result", result)
                break
        else:
            print("input correct operator")
            wait_for_number = False
                    
        
  #2, 3, -, 1, +, 10, *, 2, = 22
