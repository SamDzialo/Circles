"""
file: Circles.py
author: Sam Dzialo
Email: sad8333@rit.edu
language: python3.7
description: Circles Turtle
"""
import turtle as tt


def circle(r):
    """draws a circle around the spot that it starts at
    r(int): current radius of circle
    Precondition:
    Starts in the center facing east
    r >= 0,turtle pen is up"""
    tt.up()
    tt.forward(r)
    tt.down()
    tt.left(90)
    tt.circle(r)
    tt.right(90)
    tt.up()
    tt.forward(-r)
    """Preconditions:
    *Ends in the center facing east
    turtle pen is up"""


def rec_circle(rad, dep):
    """The rec_circle function recursively draws circles
    in the top corners of the past circle
    rad(int): the current radius of the circle
    dep(int): the current level of the recursion
    Precondition:
    turtle is in the center facing east
    turtle pen is up
    rad >= 0, dep >=0"""
    if dep == 0:
        pass
    elif dep == 1:
        circle(rad)
    else:
        tt.up()
        circle(rad)
        tt.forward(rad)
        tt.left(90)
        tt.forward(rad/2)
        tt.right(90)
        rec_circle(rad/2, dep-1)
        tt.left(90)
        tt.forward(-rad/2)
        tt.right(90)
        tt.forward(-rad)
        tt.left(180)
        tt.forward(rad)
        tt.right(90)
        tt.forward(rad/2)
        tt.right(90)
        rec_circle(rad/2, dep-1)
        tt.left(90)
        tt.forward(-rad/2)
        tt.left(90)
        tt.forward(-rad)
        tt.left(180)
    """Precondition:
    circles were drawn for the current depth,
    turtle is facing east, turtle pen is up"""


def main():
    """obtains the variable from the user
    and then sends the variable to the rec_circle function"""
    tt.speed(0)
    rad = int(input("Enter the circle radius: "))
    dep = int(input("Enter the amount of levels: "))
    rec_circle(rad, dep)
    tt.done()
    """After rec_circle is done turtle ends here with tt.done"""


main()
