import csv
# print("welcome to file handling")
# print("Enter the file name")

with open('/home/dev/Desktop/AI/AI-ML/data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[1], row[2])

# Basic operations on file
with open("/home/dev/Desktop/AI/AI-ML/data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    count = sum(1 for row in reader)
print(f"Total number of employees: {count}")

# Calculate average
with open("/home/dev/Desktop/AI/AI-ML/data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    total = sum(float(row[3]) for row in reader) # Generator expression used to calculate sum, to generate data efficently with the help of lazy evaluation.
print(f"Average salary: {total / count}")


# Writing to a file
with open("/home/dev/Desktop/AI/AI-ML/output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("How are you?\n")
    file.write("I am fine.\n")

# Appending to a file
with open("/home/dev/Desktop/AI/AI-ML/output.txt", "a") as file:
    file.write("This is the appended line.\n")