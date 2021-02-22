"""Division Beads
By Al Sweigart al@inventwithpython.com

A small Python CLI app of the "divison beads" math education tool."""

__version__ = '0.1.2'

import sys, re

UP_DOWN_CHAR         = chr(9474)
LEFT_RIGHT_CHAR      = chr(9472)
DOWN_RIGHT_CHAR      = chr(9484)
DOWN_LEFT_CHAR       = chr(9488)
UP_RIGHT_CHAR        = chr(9492)
UP_LEFT_CHAR         = chr(9496)
UP_DOWN_RIGHT_CHAR   = chr(9500)
UP_DOWN_LEFT_CHAR    = chr(9508)
DOWN_LEFT_RIGHT_CHAR = chr(9516)
UP_LEFT_RIGHT_CHAR   = chr(9524)

BEAD_LEFT = 'O' + LEFT_RIGHT_CHAR
BEAD_RIGHT = LEFT_RIGHT_CHAR + 'O'


def getStrFromCanvas(canvas):
    # Determine the width and height of the canvas:
    width = 0
    height = 0
    for x, y in canvas.keys():
        if x > width:
            width = x
        if y > height:
            height = y

    assert width != 0
    assert height != 0

    # Create the multiline string from the canvas:
    s = []
    for y in range(height + 1):
        for x in range(width + 1):
            s.append(canvas.get((x, y), ' '))
        s.append('\n')

    return ''.join(s)


def getDivisionBeadsStr(dividend, divisor):
    assert dividend >= 1
    assert divisor >= 1
    canvas = {}
    quotient = dividend // divisor
    remainder = dividend % divisor

    # If divisor is 1, skip the divisor bar and just draw the label:
    if divisor == 1:
        canvas[(1, 0)] = '1'
    else:
        # Draw left side of divisor bar:
        canvas[(1, 0)] = UP_DOWN_RIGHT_CHAR

        # Draw label of the divisor bar:
        divisorLabelWithNumber = str(divisor).center((divisor - 1) * 2, LEFT_RIGHT_CHAR)
        for i, v in enumerate(divisorLabelWithNumber):
            canvas[(2 + i, 0)] = v

        # Draw right side of divisor bar:
        canvas[(1 + len(divisorLabelWithNumber), 0)] = UP_DOWN_LEFT_CHAR

    # Draw all of the full rows of beads:
    fullRowOfBeads = LEFT_RIGHT_CHAR.join(['O'] * (divisor))
    for row in range(quotient):
        for ix, v in enumerate(fullRowOfBeads):
            canvas[(1 + ix, row + 2)] = v

    # Draw the connectors on the right side:
    numOfRightConnectors = (quotient + (remainder != 0)) // 2
    for iy in range(numOfRightConnectors):
        canvas[(len(fullRowOfBeads) + 1, (iy * 2) + 2)] = DOWN_LEFT_CHAR
        canvas[(len(fullRowOfBeads) + 1, (iy * 2) + 3)] = UP_LEFT_CHAR

    # Draw the connectors on the left side:
    numOfLeftConnectors = (quotient + 1 + (remainder != 0)) // 2 - 1
    for iy in range(numOfLeftConnectors):
        canvas[(0, (iy * 2) + 3)] = DOWN_RIGHT_CHAR
        canvas[(0, (iy * 2) + 4)] = UP_RIGHT_CHAR

    # Draw the remainder row of beads:
    if remainder != 0:
        remainderRowOfBeads = LEFT_RIGHT_CHAR.join(['O'] * (remainder))
        if quotient % 2 == 0:
            if quotient == 0:
                remainderRowOfBeads = ' ' + remainderRowOfBeads
            else:
                remainderRowOfBeads = UP_RIGHT_CHAR + remainderRowOfBeads
        else:
            remainderRowOfBeads = remainderRowOfBeads.rjust(1 + len(fullRowOfBeads), ' ')

        for ix, v in enumerate(remainderRowOfBeads):
            canvas[(ix, 2 + quotient)] = v

    if 0 <= quotient <= 2:
        # Just draw quotient without the quotient bar:
        canvas[(3 + len(fullRowOfBeads), 2)] = str(quotient)
    else:
        # Draw the top of the quotient bar:
        canvas[(3 + len(fullRowOfBeads), 2)] = DOWN_LEFT_RIGHT_CHAR

        # Draw the middle of the quotient bar:
        for iy in range(3, 1 + quotient):
            if iy == ((quotient - 1) // 2) + 2:
                # Draw the quotient number label:
                for i, v in enumerate(str(quotient)):
                    canvas[(3 + len(fullRowOfBeads) + i, iy)] = v
            else:
                # Draw the vertical bar:
                canvas[3 + len(fullRowOfBeads), iy] = UP_DOWN_CHAR

        # Draw the bottom of the quotient bar:
        canvas[(3 + len(fullRowOfBeads), 1 + quotient)] = UP_LEFT_RIGHT_CHAR


    if remainder == 0 or remainder == 1:
        # Just draw remainder without the remainder bar:
        remainderBar = str(remainder)
    else:
        # Draw the remainder bar:
        remainderBar = UP_DOWN_RIGHT_CHAR + str(remainder).center(remainder * 2 - 3, LEFT_RIGHT_CHAR) + UP_DOWN_LEFT_CHAR

    # Put the remainder bar on the canvas:
    if quotient % 2 == 0:
        # Remainder bar is left justified:
        remainderBar = ' ' + remainderBar
    else:
        # Remainder bar is right justified:
        remainderBar = str(remainderBar).rjust(1 + len(fullRowOfBeads), ' ')
    for ix, v in enumerate(remainderBar):
        canvas[(ix, 4 + quotient)] = v

    return getStrFromCanvas(canvas)


def askUserForDivisionProblems():
    while True:
        print('Enter a division problem (example: 23 / 7) or QUIT.')
        response = input('> ').upper()
        if response.startswith('Q'):
            return

        mo = re.search(r'(\d+)\s*/\s*(\d+)', response)
        if mo is None:
            print('That is not valid input. Enter a number, a backslash, and another number.')
            continue

        dividend, divisor = mo.groups()
        dividend, divisor = int(dividend), int(divisor)
        print('\n%s / %s = %s r %s\n' % (dividend, divisor, dividend // divisor, dividend % divisor))
        print(getDivisionBeadsStr(dividend, divisor))

def interactiveMode():
    try:
        import keyboard, os
    except:
        sys.exit('Division beads interactive mode requires the keyboard module. Run pip install keyboard.')

    dividend = 1
    divisor = 1

    while True:
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

        print('\n%s / %s = %s r %s\n' % (dividend, divisor, dividend // divisor, dividend % divisor))
        print(getDivisionBeadsStr(dividend, divisor))

        print('Press WASD to change size, Q to quit.')
        key = keyboard.read_key().upper()  # read key down event
        if key == 'A' and divisor > 1:
            divisor -= 1
        elif key == 'D':
            divisor += 1
        elif key == 'W' and dividend > 1:
            dividend -= 1
        elif key =='S':
            dividend += 1
        elif key == 'Q':
            return

        keyboard.read_key()  # read key up event