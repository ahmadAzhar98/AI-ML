# Infinite sequence
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# Using infinte sequence we can build a pallindrome detector
def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num

for i in infinite_sequence():
    pal = is_palindrome(i)
    if pal:
        print(pal)
        break            


# Building generator with generator expression
nums_squared_lc = [num**2 for num in range(5)]
print(nums_squared_lc)

# Data pipeline with generator
file_name = "/home/dev/Desktop/AI/AI-ML/techcrunch.csv"
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")