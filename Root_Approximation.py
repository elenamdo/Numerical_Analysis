#!/usr/bin/python
import math

#Calculates the roots of quadratic equation ax^2+ bx +y using approximation and formulas 1.1 and 1.2

#Computes the absolute error and relative error in approximations of p by p∗
#p* is an approximation of p

#Function to make sure input is correct and convert to float or int
def IntegerOrNot (x):
    try:
        if "." in x:
            val = float(x)
        else:
            val = int(x)
        return val
    except ValueError:
        print("Please enter a valid number.")
        exit()

#Digit approximation
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return float(math.floor(n*multiplier + 0.5) / multiplier)

def round_half_down(n, decimals=0):
    multiplier = 10 ** decimals
    return float(math.ceil(n*multiplier - 0.5) / multiplier)

def rounder (m, approximation_digit):
    if m < 0:
        m = round_half_down(m, approximation_digit);
    if m > 0:
        m = round_half_up(m, approximation_digit);
    return float(m);

#ask for a, b and c and digit approximation
coefficient_a = input("Enter coefficient a: ");
coefficient_a = IntegerOrNot(coefficient_a);


coefficient_b = input("Enter coefficient b: ");
coefficient_b = IntegerOrNot(coefficient_b);

coefficient_c = input("Enter coefficient c: ");
coefficient_c = IntegerOrNot(coefficient_c);

approximation_digit = input("Enter the decimal to which you would like to approximate: ");
approximation_digit = IntegerOrNot(approximation_digit);

x_1 = input("Enter the exact value of x_1: ");
x_1 = IntegerOrNot(x_1);

x_2 = input("Enter the exact value of x_2: ");
x_2 = IntegerOrNot(x_2);

#Formula 1
rounded_b = rounder(coefficient_b, approximation_digit)
b_squared = math.pow(rounded_b, 2)
rounded_b_squared = rounder(b_squared, approximation_digit)
rounded_a = rounder(coefficient_a, approximation_digit)
rounded_c = rounder(coefficient_c, approximation_digit)
four_a_c = 4*rounded_a*rounded_c
rounded_four_a_c = rounder(four_a_c, approximation_digit)
b_2_minus_4ac = rounded_b_squared - rounded_four_a_c
rounded_b_2_minus_4ac = rounder(b_2_minus_4ac, approximation_digit)
square_root = math.sqrt(rounded_b_2_minus_4ac)
rounded_square_root = rounder(square_root, approximation_digit)
top = -rounded_b + rounded_square_root
rounded_top = rounder(top, approximation_digit)
bottom = 2* rounded_a
rounded_bottom = rounder(bottom, approximation_digit)
whole = rounded_top/rounded_bottom
rounded_whole = rounder(whole, approximation_digit)

x_1_1 = rounded_whole

rounded_b = rounder(coefficient_b, approximation_digit)
b_squared = math.pow(rounded_b, 2)
rounded_b_squared = rounder(b_squared, approximation_digit)
rounded_a = rounder(coefficient_a, approximation_digit)
rounded_c = rounder(coefficient_c, approximation_digit)
four_a_c = 4*rounded_a*rounded_c
rounded_four_a_c = rounder(four_a_c, approximation_digit)
b_2_minus_4ac = rounded_b_squared + rounded_four_a_c
rounded_b_2_minus_4ac = rounder(b_2_minus_4ac, approximation_digit)
square_root = math.sqrt(rounded_b_2_minus_4ac)
rounded_square_root = rounder(square_root, approximation_digit)
top = -rounded_b + rounded_square_root
rounded_top = rounder(top, approximation_digit)
bottom = 2* rounded_a
rounded_bottom = rounder(bottom, approximation_digit)
whole = rounded_top/rounded_bottom
rounded_whole = rounder(whole, approximation_digit)

x_1_2 = rounded_whole

#absolute error calculation
absolute_error= abs(x_1-x_1_1);
print("The absolute error is for x_1 using Formula 1 is: " + str(absolute_error));

#relative error calculation
relative_error = (abs(x_1-x_1_1))/abs(x_1);
print("The relative error is for x_1 using Formula 1 is: " + str(relative_error));

#absolute error calculation
absolute_error= abs(x_2-x_2_1);
print("The absolute error is for x_1 using Formula 1 is: " + str(absolute_error));

#relative error calculation
relative_error = (abs(x_2-x_2_1))/abs(x_2);
print("The relative error is for x_1 using Formula 1 is: " + str(relative_error));
