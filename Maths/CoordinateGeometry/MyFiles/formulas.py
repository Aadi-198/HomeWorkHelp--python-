#Import required libraries
import shutil

# import required files
import distance_formula
import midpoint_formula
import section_formula

size = shutil.get_terminal_size()
seps = "-" * size.columns #DRY stands for dont repeat yourself so, instead of separators in every file, I am using it in the final version

def formula():

        is_calculating = True
        while is_calculating == True:
                print(seps)
                action = input("Which formula do you want to use? \n[D]istance formula, [M]idpoint formula, [S]ection formula. \nTo stop click [enter]. \n").strip().lower()
                if not action:
                        is_calculating = False
                elif action == "d":
                        print(seps)
                        distance_formula.distance_formula(
                                x1=float(input("Enter x₁\t:\t")), 
                                y1=float(input("Enter y₁\t:\t")),
                                x2=float(input("Enter x₂\t:\t")),
                                y2=float(input("Enter y₂\t:\t"))
                                )
                elif action == "m":
                        print(seps)
                        midpoint_formula.midpoint_formula(
                                x1=float(input("Enter x₁\t:\t")), 
                                y1=float(input("Enter y₁\t:\t")),
                                x2=float(input("Enter x₂\t:\t")),
                                y2=float(input("Enter y₂\t:\t"))
                                )       
                elif action == "s":
                        print(seps)
                        section_formula.section_formula(
                                x1=float(input("Enter x₁\t:\t")), 
                                y1=float(input("Enter y₁\t:\t")),
                                x2=float(input("Enter x₂\t:\t")),
                                y2=float(input("Enter y₂\t:\t")),
                                m1=float(input("Enter m₁\t:\t")),
                                m2=float(input("Enter m₂\t:\t"))
                                )
                else:
                        print(seps)
                        print("An error occured")
formula()