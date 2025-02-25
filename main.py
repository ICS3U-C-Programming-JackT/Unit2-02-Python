#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: February 25, 2025
# This code determines the circumference and area of a circle based on user input


import constants

def main():
    radius = float(input("Enter your radius here (cm): "))

    circumference = radius * constants.TAU

    print("The circumference of your circle is " + circumference + "cm!")

if __name__ == "__main__":
    main()
