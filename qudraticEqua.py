import math

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        # Two real and distinct solutions
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # One real solution (both roots are the same)
        root = -b / (2*a)
        return root
    else:
        # No real solutions (complex roots)
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# Example usage
a = 2
b = -5
c = 2


roots = solve_quadratic_equation(a, b, c)
print("Roots:", roots)
