import turtle
chessboard = turtle.Turtle()
chessboard.speed(15)
chessboard.shape("turtle")
a=0
chessboard.forward(50)
chessboard.right(90)
for u in range(4):

    for i in range(8):
        if(a==0):
            chessboard.fillcolor('white')
            chessboard.begin_fill()
            a=1
        else:
            chessboard.fillcolor('black')
            chessboard.begin_fill()
            a=0
        for i in range(5):
            chessboard.forward(50)
            chessboard.right(90)
        chessboard.left(90)
        chessboard.end_fill()
    chessboard.left(90)
    chessboard.forward(50)
    chessboard.left(90)
    for i in range(8):
        if (a == 0):
            chessboard.fillcolor('white')
            chessboard.begin_fill()
            a = 1
        else:
            chessboard.fillcolor('black')
            chessboard.begin_fill()
            a = 0
        for i in range(5):
            chessboard.forward(50)
            chessboard.left(90)
        chessboard.right(90)
        chessboard.end_fill()
    chessboard.right(90)
    chessboard.forward(50)
    chessboard.right(90)





















