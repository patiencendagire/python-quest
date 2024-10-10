#Using a function,calculate a program that calculates the volume of a cylinder
height=int(input("Enter the height of the cylinder:"))
radius=int(input("enter the radius of a cyliner:"))
volume =22/7*radius**2*height
print(f'The volume of a cylinder of radius {radius} and height {height} is {volume:.2f}')