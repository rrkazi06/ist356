# when you write code: write the program
    # arguments are inputs into the function, return is the output

# numbers = [ 2, 3, 5, 10] # input

# # process
#     total = sum(numbers) #sum function will add up all int
#     count = len(numbers) #len means it will count how many inputs there are in the list
#     avg = total / count # 5.0 (the formula for average)

# # output
# print(average(numbers))

# 2) re-write the program into a function
def average(numbers: list[float]) -> float: # basically you're telling it to expect what it's gonna receive
# def average(numbers): 
    total = sum(numbers) #sum function will add up all int
    count = len(numbers) #len means it will count how many inputs there are in the list
    avg = total / count # 5.0 (the formula for average)
    return avg 

# re-write the entire thing
numbers = [ 5, 6 ]
grades = [ 100, 100, 100, 99, 94, 98, 45, 62, 86, 89]
avg_grade = average(grades) # call the average function with grades list
print(f"Average of {grades} is {avg_grade}")

def test_avg():
    numbers [ 1,1,1,1 ]
    expect = 1
    actual = average(numbers)
    assert expect == actual

test_avg()






