
try:
    list = [10,0,20]
    result = list[0] / list[1]
    print(result)
    print('Done')
except ZeroDivisionError:
    print('Dividing by zeroo is not possible')

finally:
    print('Successful')

# --------
try:
    num1 = int(input("Enter first Number: "))
    num2 = int(input("Enter first Number: "))
    result = num1 / num2
    print(result)

except (ValueError, ZeroDivisionError):
    print('You have enterd incorrect input')

finally:
    print("Thank you")

# -------------------
def voter(age):
    if age<18:
        raise ValueError('Invalid voter')
    return 'You are allowed to vote'

try:
    print(voter(17))

except ValueError as error:
    print(error)
