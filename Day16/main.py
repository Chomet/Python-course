import turtle

# Documentation: https://docs.python.org/3/library/turtle.html
logo = turtle.Turtle()
print(logo)
logo.shape("turtle")
logo.color("orange")
logo.fd(100)
window = turtle.Screen()
window.exitonclick()
print(window.canvheight, window.canvwidth)

# Python packages: https://pypi.org/
# Installing packages:
# File -> Settings -> name_of_project -> Python Interpreter -> click on + sign -> find package -> Install

import prettytable
table = prettytable.PrettyTable()
table.add_column("Name", ["Marko", "Antonio", "Sandro"])
table.add_column("Age", [10, 20, 30])
table.align = "l"
print(table)

