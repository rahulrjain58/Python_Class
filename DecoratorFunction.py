# def decorator(func):
#     def wrapper():
#         print("Before calling a function.")
#         func()
#         print("After Calling a function.")
#     return wrapper
# @ decorator
# def Greet():
#     print("hello World")

def validate_name_and_contact(func):
    def wrapper(name,contact_number):
        if not name or not isinstance(name,str):
            return "name must be non empty string"
        if len(contact_number) != 10 or not contact_number.isdigit():
            return "contact number must be a 10 digit number."
        return func(name, contact_number)
    return wrapper
    
@ validate_name_and_contact
def register_user(name,contact_number):
    return f"user {name} with contact number {contact_number} has been successfully registered."

print(register_user("Alice","1234567897"))
print(register_user("Bob","1234567897"))
print(register_user("","123456"))
print(register_user("Hari","123abc7897"))
print(register_user("",""))