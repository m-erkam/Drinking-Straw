
glass_size = int(input())
straw_pos = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

# Calculating number of glass according to inputs
number_of_glass = None
n = ((glass_size * 2) + 1) - straw_pos
n1 = n / 2 + 1
n2 = n % 2
if n2 == 1:
    number_of_glass = n1 + 0.5
if n2 == 0:
    number_of_glass = n1


# I define a blank function to use when I need blanks
def blank(b):
    if b <= 0:
        return

    blank(b-1)
    print(" ", end="")
    return


# I define a star function to fill the glass
def star(s):
    if s == 0:
        return
    else:
        print("*", end="")
        star(s - 1)
        print("*", end="")
    return


# Printing straws with blanks according to straw_pos input
def straw(st):
    if st == 0:
        return
    blank(straw_pos - st)
    print("o")
    straw(st - 1)
    return


# Outer glass function is to print the part of the glass that contains water
def outer_glass(t):
    if t == 0:
        return
    blank(glass_size - t)
    print("\\", end="")
    star(t)
    print("/")
    outer_glass(t - 1)
    return


# Bottom glass function is to print "||" according to glass size input
def bottom_of_the_glass(k):
    if k == 0:
        return

    if k == glass_size:
        blank(glass_size)
        print("--")
    blank(glass_size)
    print("||")
    bottom_of_the_glass(k - 1)
    return


# Middle of the glass function is to print the part of the glass that is formed after the water level decreases
def middle_of_the_glass(m, g):
    if m <= 0:
        return
    middle_of_the_glass(m - 1, g)
    blank(m-1)
    print("\\", end="")
    blank(straw_pos-1)
    print("o", end="")
    blank(g*2 - straw_pos - (m-1)*2)
    print("/", end="")
    print()
    return


# Lastly, I define print glass function to print all glasses with different shapes by combining all functions
def print_glass(g, no, m1=0):
    if no == 0:
        return

    straw(straw_pos)
    middle_of_the_glass(m1, glass_size)
    outer_glass(g)
    bottom_of_the_glass(glass_size)
    return print_glass(g-1, no-1, m1+1)


print_glass(glass_size, number_of_glass)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

