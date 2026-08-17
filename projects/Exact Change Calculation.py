def exact_change(user_total):
    num_dollars = user_total // 100
    user_total = user_total % 100
    num_quarters = user_total // 25
    user_total = user_total % 25
    num_dimes = user_total // 10
    user_total = user_total % 10
    num_nickels = user_total // 5
    num_pennies = user_total % 5
    return (num_dollars, num_quarters, num_dimes, num_nickels, num_pennies)

def main():
    user_input = int(0)
    if user_input <= 0:
        print("no change")
    else:
        num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(user_input)
        if num_dollars == 1:
            print(str(num_dollars) + " dollar")
        elif num_dollars > 1:
            print(str(num_dollars) + " dollars")
        if num_quarters == 1:
            print(str(num_quarters) + " quarter")
        elif num_quarters > 1:
            print(str(num_quarters) + " quarters")
        if num_dimes == 1:
            print(str(num_dimes) + " dime")
        elif num_dimes > 1:
            print(str(num_dimes) + " dimes")
        if num_nickels == 1:
            print(str(num_nickels) + " nickel")
        elif num_nickels > 1:
            print(str(num_nickels) + " nickels")
        if num_pennies == 1:
            print(str(num_pennies) + " penny")
        elif num_pennies > 1:
            print(str(num_pennies) + " pennies")

if __name__ == '__main__':
    main()
