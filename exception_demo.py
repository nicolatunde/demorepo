# numb1 = int(input("enter number:"))
# numb2 = int(input("enter number"))
# result = numb1 / numb2
# print(result)


# class NegativeNumberError(Exception):
#     def __init__(self, message="number is negative"):
#         super().__init__(message)
        
# def check_positive(number):
#     if number < 0:
#         raise NegativeNumberError
    
# try:
#    check_positive((-5))
# except NegativeNumberError as e:
#     print("number error ",e)


# Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.



def safe_divide(a,b):
    try: 
        a = float(a)
        b = float(b)
        print(a / b)
    except ZeroDivisionError as e:
        print("divisor cant be zero",e)
    except TypeError as e:
        print("unsupported type",e)
    except ValueError as e:
        print("number are not intergers",e)
    except Exception as e:
        print(e)


safe_divide(2,2)
