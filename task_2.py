import turtle

def pythagoras_tree(turtle_obj, length, depth):
    if depth > 0:
        turtle_obj.forward(length * depth)
        turtle_obj.left(45)
        pythagoras_tree(turtle_obj, length, depth - 1)
        turtle_obj.right(90)
        pythagoras_tree(turtle_obj, length, depth - 1)
        turtle_obj.left(45)
        turtle_obj.backward(length * depth)

def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.backward(200)
    t.pendown()
    return t

def main():
    recursion_depth = int(input("Введіть рівент рекурсії: "))
    branch_size = 10

    screen = turtle.Screen()
    screen.bgcolor("white")

    turtle_obj = setup_turtle()
    pythagoras_tree(turtle_obj, branch_size, recursion_depth)
    
    screen.mainloop()

if __name__ == "__main__":
    main()
