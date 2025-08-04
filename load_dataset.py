import pandas as pd
from calculator import add, subtract, multiply, divide

# Load the CSV dataset
df = pd.read_csv("data/sample_dataset.csv")

# Loop through each row and apply calculator functions
for index, row in df.iterrows():
    op = row["operation"]
    a, b = row["num1"], row["num2"]

    if op == "add":
        result = add(a, b)
    elif op == "subtract":
        result = subtract(a, b)
    elif op == "multiply":
        result = multiply(a, b)
    elif op == "divide":
        result = divide(a, b)
        if result is None:
            result = "Error: Division by zero"
    else:
        result = "Unsupported operation"

    print(f"{index+1}. {op}({a}, {b}) = {result}")
