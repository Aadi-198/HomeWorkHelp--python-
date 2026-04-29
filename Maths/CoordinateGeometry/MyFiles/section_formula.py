def section_formula (x1, y1, x2, y2, m1, m2):

    pointA = (x1, y1)
    print(f"\nA({pointA[0]:g}, {pointA[1]:g})")

    pointB = (x2, y2)
    print(f"\nB({pointB[0]:g}, {pointB[1]:g})")

    ratio = f"m1 : m2"
    print(f"Ratio - {ratio}")

    section = ((((m1 * x2) + (m2 * x1)) / (m1 + m2)), (((m1 * y2) + (m2 * y1)) / (m1 + m2)))
    print(f"\nThe section between point A and point B is point C{section} \n")

    
if __name__ == "__main__":
    section_formula(
        x1=float(input("Enter x₁\t:\t")),
        y1=float(input("Enter y₁\t:\t")),
        x2=float(input("Enter x₂\t:\t")),
        y2=float(input("Enter y₂\t:\t")),
        m1=float(input("Enter m₁\t:\t")),
        m2=float(input("Enter m₂\t:\t"))
        )