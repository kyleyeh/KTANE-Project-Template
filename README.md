Write code to help solve six "Keep Talking and Nobody Explodes" modules!  Point values and descriptions are below.  In order to receive full credit for this assignment, you must earn 30 points.  (Extra credit is possible for earning more than 30 points!)

Each module that you write code for should have two key components:
1. A dialog file/function that read in information from the user, pass it into the action file/function(s), and display the result to the user.
2. An action file/function that takes in the necessary information, uses the module logic to determine what should be done in each scenario, and returns that information to the dialog file/function.

(For example, for the Simple Wires module, you will have a simpleWiresDialog.py file containing a simpleWiresDialog function and a simpleWiresAction.py file containing a simpleWiresAction function.  Note that these files can (and sometimes will need to) contain multiple functions.  Pay close attention to the specifications below!)

----------------------------------------------------------------

***Module Action Specifications***

*Note that when colors are used, they are one of the following:*

*red, blue, black, white, yellow, green*

----------------------------------------------------------------

**Simple Wires (4 points)**
'''
simpleWiresAction
    Given a list of wire colors and the last digit of the serial number, use selection statements and return a description of which wire to cut.  Return one of the following descriptions:
        "second", "last", "last blue", "last red", "first", "fourth", "third"

    Arguments: wireList (list of wire colors - see possibilities above), num (last digit of serial number)
    Return: description of which wire to cut
'''

----------------------------------------------------------------

**Button (6 points)**
'''
heldButton
    Given a color (see possibilities above), return which digit is needed in the countdown timer (1, 4, or 5)

    Arguments: color (what color the lit strip turned)
    Return: 1, 4, or 5
'''


'''
buttonAction
    Given a button color (see possibilities above), word, the number of batteries, and booleans indicating if there are lit CAR and/or FRK indicators, return either "press" or "hold"

    Arguments: color (button color), word (button word), numBatteries (number of batteries), car (if there is a lit CAR indicator (T/F)), frk (if there is a lit FRK indicator (T/F))
    Return: "press" or "hold"
'''

----------------------------------------------------------------

**Simon Says (8 points)**
'''
simonSaysAction
    Given a list of flashing colors, the number of strikes, and whether or not the bomb's serial number has a vowel, return a list containing the sequence of colors (in lowercase) that should be pressed 

    Arguments: colors (the list of reds, greens, blues, and yellows), numStrikes (the current number of strikes), hasVowel (T/F indicating if the serial number contains a vowel)
    Return: a list containing the sequence of colors (in lowercase) that should be pressed
'''

----------------------------------------------------------------

**Complicated Wires (10 points)**
'''
serialCheck
    Given the last digit of the bomb's serial number, return True if the wire should be cut

    Arguments: num (last digit of the bomb's serial number)
    Return: True (cut!) or False (don't cut!)
'''


'''
parallelCheck
    Given whether or not the bomb has a parallel port, return True if the wire should be cut

    Arguments: hasParallel (T/F)
    Return: True (cut!) or False (don't cut!)
'''


'''
batteryCheck
    Given the number of batteries on the bomb, return True if the wire should be cut

    Arguments: numBatteries (number of batteries)
    Return: True (cut!) or False (don't cut!)
'''


'''
complicatedWiresAction
    Given a wire description, the last digit of the serial number, whether or not the bomb has a parallel port, 
    and the number of batteries on the bomb, return whether you should cut the wire or not (T/F)

    Wire descriptions will consist of four attributes: red, blue, star, and light.
      "rbsl" indicates that all of these attributes are present.
      "rl" indicates that the wire has some red and is connected to a light.
      "bsl" indicates that the wire has some blue and is connected to a star and a light.
      "" indicates a wire that has none of these attributes.

    Note that descriptions should always be in that order: red-blue-star-light.

    Arguments: color (wire description, see above), lastDigit (of serial number), hasParallel (T/F), numBatteries (number of batteries)
    Return: True (cut!) or False (don't cut!)
'''

----------------------------------------------------------------

**Passwords (10 points)**

'''
passwordsAction
    Given the letters in each of the five dials, return (in caps) what word should be entered in this module

    Arguments: dial1, dial2, dial3, dial4, dial5 (each is a list containing the letters on the respective dial)
    Return: the word (in caps!) that should be entered to solve the module
'''

----------------------------------------------------------------

**Wire Sequences (12 points)**

'''
wireSequencesAction
    Given the color of the current wire and a list containing the sequence of letters that wires of the current color
    have been connected to, return whether or not to cut the current wire

    Arguments: color (the color of the current wire, see list above), currentColorList (a list containing the sequence of letters that wires of the current color have been connected to)
    Return: T/F (indicating whether or not the user should cut the wire)
'''

----------------------------------------------------------------
