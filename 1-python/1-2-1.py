# PASSWORD = "secret"
# # putting it in capitals creates a constant, it won't change, but the parameters around it might
# success = False # not capital bc not constant
# for attempt in range(5):
#     your_password = input("Enter Password:")

#     if your_password == PASSWORD:
#         print("Access Granted")
#         success = True # you record the success of the password so that you can reference it later at the bottom
#         # exit(0) # the 0 means good exit, the 1 means bad exit
#         break # you should put it here because the code has found what it's looking for, otherwise it will keep going
#     else:
#         print("Access Denied")
#         # exit(1) # exit allows you to flag issues

#     print(f"Attempt {attempt + 1} of 5") # this goes here because you want this displayed in each iteration that the code runs, so it will display each time (5)

# if not success:
#     print("You are locked out")
# else:
#     print("Welcome!")


    # You can also do:
PASSWORD = "secret"
MAX_ATTEMPTS = 5
success = False 
for attempt in range(MAX_ATTEMPTS):
    your_password = input("Enter Password:")

    if your_password == PASSWORD:
        print("Access Granted")
        success = True 
        break 
    else:
        print("Access Denied")

    print(f"Attempt {attempt + 1} of {MAX_ATTEMPTS}") # this goes here because you want this di

if not success:
    print("You are locked out")
else:
    print("Welcome!")

# in general, you're gonna be using definite loops more than indefinite bc they're not very useful in a data pipeline, more for a video game or something
