def get_num_input():
    num = 0
    while (True):
        num_input = input()
        try:
            num = float(num_input)
        except ValueError:
            print("Not a Number")
            continue
        return num

def calculator():
    history = []
    while (True):
        op = input("(+, -, *, /) 연산자, history, 혹은 q를 통해 프로그램 종료 : ")
        if op == "history":
            print(history)
            continue
        if op == "q":
            break
        if op not in ["+", "-", "*", "/"]:
            print("Not a Valid Operator")
            continue
        num1 = get_num_input()
        num2 = get_num_input()
        while (num2 == 0 and op == "/"):
            print("Can't divide by ZERO")
            num2 = get_num_input()
        res = 0
        match op:
            case "+":
                res = num1 + num2
            case "-":
                res = num1 - num2
            case "*":
                res = num1 * num2
            case "/":
                res = num1 / num2
        print(res)
        history.append(res)

if __name__ == "__main__":
    calculator()