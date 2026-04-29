#Make a algorithm to check distance formula

#Start
#Get input as (x₁, y₁) and (x₂, y₂)
#apply the formula to calculate distance
#print the results
#End

def distance_formula (x1, y1, x2, y2):

    pointA = (x1, y1)
    print(f"\nA({pointA[0]:g}, {pointA[1]:g})")

    pointB = (x2, y2)
    print(f"\nB({pointB[0]:g}, {pointB[1]:g})")

    distance = ((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5)
    print(f"\nThe distance between point A and point B is {distance} \n")

    
if __name__ == "__main__":
    distance_formula(
        x1=float(input("Enter x₁\t:\t")), 
        y1=float(input("Enter y₁\t:\t")), 
        x2=float(input("Enter x₂\t:\t")), 
        y2=float(input("Enter y₂\t:\t"))
        )