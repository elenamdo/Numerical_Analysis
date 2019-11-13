#!/usr/bin/python

#Compute the absolute error and relative error in approximations of p by p∗
#p* is an approximation of p

#Function to make sure input is correct and convert to float or int
def IntegerOrNot (x):
    try:
        if "." in x:
            val = float(x)
        else:
            val = int(x)
    except ValueError:
        print("Please enter a valid number.")
    return val

#ask for input and check
p_star = input("Enter the approximation: ");
p_star = IntegerOrNot(p_star);

p = input("Enter the exact value: ");
p = IntegerOrNot(p);

#absolute error calculation
absolute_error= abs(p-p_star);
print("The absolute error is " + str(absolute_error));

#relative error calculation
relative_error = (abs(p-p_star))/abs(p);
print("The relative error is " + str(relative_error));
