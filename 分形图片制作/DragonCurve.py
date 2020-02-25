import turtle as t

def dragon(level=4, size=200, zig=t.right, zag=t.left):
    if level <= 0:
        t.forward(size)
        return
    else:
        size /= 1.41421
        zig(45)
        dragon(level-1, size, t.right, t.left)
        zag(90)
        dragon(level - 1, size, t.left, t.right)
        zig(45)

if __name__ == '__main__':
    t.speed(10)
    t.hideturtle()
    dragon(8)
    t.exitonclick()
