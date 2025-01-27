class CustomException(Exception):
    pass


first_number: float = float(input("Please enter the first number: "))
second_number: float = float(input("Please enter the second number: "))

try:
    if second_number == 0:
        raise CustomException()
except CustomException:
    print("!#$@%%%#$%#$%#")



# result: float = 0
# my_dict = {"first_name": "Peyman", "last_name": "Barjoueian"}
# try:
#     result = first_number / second_number
#     full_name = my_dict["first_name"] + " " + my_dict["last_names"]
# except ZeroDivisionError:
#     print("Error is happened.... :(")
#     second_number = 1
#     result = first_number / second_number
# except KeyError as exc:
#     print(exc)
#     print("My Key error...")
# finally:
#     print("Finaly block...")
# print(result)
