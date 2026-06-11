print("hello world")

# Positional argument - in order by commas
print(round(3.14159, 2))
# Keyword argument - by references
print(round(number=3.14159, ndigits=2))
 # print(help(round))

def average(values, rounded=False):
        """
        Function: average
        
        Description:
            Find the mean in a sequence of values and round to 2 decimal places if 'rounded' is True
        
        Args:
            values (list): A list of numeric values
            rounded (boolean): True/False for if result to be rounded

        Returns:
            rounded_average (float): The mean of values
        """
        if rounded == True:
                average_value = sum(values) / len(values)
                rounded_average = round(average_value, 2)
                return rounded_average
        else:  
            average_value = sum(values) / len(values)
            return average_value
        
preperation_times = [19.23, 15.67, 48.57, 23.45, 12.06, 34.56, 45.67]

# below function call uses keyword arguments
print(average(values=preperation_times, rounded=True))
# below is how to get docstring for a function
print(average.__doc__)
# Update a function's docstring
average.__doc__ = "Calculate the mean of values in a data structure, rounding to 2 digits"

# Allow any number of keyword arguments 'kwargs'
def average2(**kwargs):
       # Function code remains the same
        average_value = sum(kwargs.values()) / len(kwargs.values())
        rounded_average = round(average_value, 2)
        return rounded_average

# Calling an average with six kwargs - list
print(average2(a=15, b=29, c=4, d=13, e=11, f=8))

# Calling average with one kwarg - dictionary
print(average2(**{"a":15, "b":29, "c":4, "d":13, "e":11, "f":8}))

# Calling average with three kwargs - dictionary
print(average2(**{"a":15, "b":29}, **{"c":4, "d":13}, **{"e":11, "f":8}))

### Lambda Functions ###

## Single variable Lambda functions ##

# Get the average with Lambda
(lambda x: sum(x) / len(x))([3, 6, 9])

# Get & Print the average with Lambda
print((lambda x: sum(x) / len(x))([3, 6, 9]))

# Store Lambda function as variable
average_lam = lambda x: sum(x) / len(x)

## Multiple variable Lambda functions ##

# Call the average_lam function/variable
print(average_lam([3, 6, 9]))

# Store Lambda function with two arguments
power_lam = lambda x, y: x**y

# Raise 2 to the power of 3 - call power_lam function/variable
print(power_lam(2, 3))

## Lambda functions with iterables ##

    # map() applies a function to ALL elements in an iterable

names = ["john", "sally", "leah"]
# Apply a Lambda function inside map()
capitalize = map(lambda x: x.capitalize(), names)
# Convert to a list
print(list(capitalize))
