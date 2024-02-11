# import modules
from simpleWiresAction import *
from buttonAction import *
from simonSaysAction import *
from complicatedWiresAction import *
from wireSequencesAction import *
from passwordsAction import *

# Simple Wire tests

second = "second"
last = "last"
lastBlue = "last blue"
lastRed = "last red"
first = "first"
fourth = "fourth"
third = "third"

def test_simpleWires31():
    assert simpleWiresAction(["blue", "white", "black"], 2) == second

def test_simpleWires32():
    assert simpleWiresAction(["blue", "red", "white"], 5) == last

def test_simpleWires33():
    assert simpleWiresAction(["blue", "red", "blue"], 4) == lastBlue

def test_simpleWires34():
    assert simpleWiresAction(["red", "white", "black"], 1) == last

def test_simpleWires41():
    assert simpleWiresAction(["red", "white", "black", "red"], 1) == lastRed

def test_simpleWires42():
    assert simpleWiresAction(["yellow", "white", "black", "yellow"], 1) == first

def test_simpleWires43():
    assert simpleWiresAction(["red", "white", "black", "blue"], 2) == first

def test_simpleWires44():
    assert simpleWiresAction(["yellow", "yellow", "blue", "blue"], 1) == last

def test_simpleWires45():
    assert simpleWiresAction(["white", "white", "white", "white"], 2) == second

def test_simpleWires51():
    assert simpleWiresAction(["red", "white", "black", "blue", "black"], 1) == fourth

def test_simpleWires52():
    assert simpleWiresAction(["red", "white", "black", "yellow", "yellow"], 1) == first

def test_simpleWires53():
    assert simpleWiresAction(["blue", "white", "blue", "yellow", "yellow"], 1) == second

def test_simpleWires54():
    assert simpleWiresAction(["black", "white", "blue", "yellow", "yellow"], 2) == first

def test_simpleWires61():
    assert simpleWiresAction(["black", "white", "blue", "red", "red", "white"], 1) == third

def test_simpleWires62():
    assert simpleWiresAction(["yellow", "white", "blue", "red", "red", "white"], 1) == fourth

def test_simpleWires63():
    assert simpleWiresAction(["black", "white", "blue", "yellow", "yellow", "white"], 1) == last
    
def test_simpleWires64():
    assert simpleWiresAction(["black", "white", "blue", "red", "red", "red"], 2) == fourth



# Button tests

press = "press"
hold = "hold"

def test_button1():
    assert buttonAction("blue", "abort", 2, True, True) == hold

def test_button2():
    assert buttonAction("blue", "detonate", 2, True, True) == press

def test_button3():
    assert buttonAction("white", "abort", 2, True, True) == hold

def test_button4():
    assert buttonAction("red", "hold", 3, False, True) == press

def test_button5():
    assert buttonAction("yellow", "hold", 1, False, False) == hold

def test_button6():
    assert buttonAction("red", "hold", 1, False, False) == press

def test_button7():
    assert buttonAction("green", "detonate", 0, False, True) == hold

# Held Button tests
one = 1
four = 4
five = 5

def test_button8():
    assert heldButton("blue") == four

def test_button9():
    assert heldButton("white") == one

def test_button10():
    assert heldButton("yellow") == five

def test_button11():
    assert heldButton("red") == one


# Simon Says tests

simonList = ["red", "blue", "green", "yellow", "yellow"]

def test_simonSays_v0():
    assert simonSaysAction(simonList, 0, True) == ["blue", "red", "yellow", "green", "green"]

def test_simonSays_v1():
    assert simonSaysAction(simonList, 1, True) == ["yellow", "green", "blue", "red", "red"]

def test_simonSays_v2():
    assert simonSaysAction(simonList, 2, True) == ["green", "red", "yellow", "blue", "blue"]

def test_simonSays_nv0():
    assert simonSaysAction(simonList, 0, False) == ["blue", "yellow", "green", "red", "red"]

def test_simonSays_nv1():
    assert simonSaysAction(simonList, 1, False) == ["red", "blue", "yellow", "green", "green"]

def test_simonSays_nv2():
    assert simonSaysAction(simonList, 2, False) == ["yellow", "green", "blue", "red", "red"]


# Complicated Helper tests

def test_complicatedWires_serial_odd():
    assert serialCheck(1) == False

def test_complicatedWires_serial_even():
    assert serialCheck(8) == True

def test_complicatedWires_parallel_true():
    assert parallelCheck(True) == True

def test_complicatedWires_parallel_false():
    assert parallelCheck(False) == False

def test_complicatedWires_batteries_true():
    assert batteryCheck(2) == True

def test_complicatedWires_batteries_true():
    assert batteryCheck(1) == False

# Complicated tests

lastDigit = 6
hasParallel = False
numBatteries = 1

def test_complicatedWires_0000():
    assert complicatedWiresAction("", lastDigit, hasParallel, numBatteries) == True

def test_complicatedWires_1000():
    assert complicatedWiresAction("r", lastDigit, hasParallel, numBatteries) == serialCheck(lastDigit)

def test_complicatedWires_0100():
    assert complicatedWiresAction("b", lastDigit, hasParallel, numBatteries) == serialCheck(lastDigit)

def test_complicatedWires_0010():
    assert complicatedWiresAction("s", lastDigit, hasParallel, numBatteries) == True

def test_complicatedWires_0001():
    assert complicatedWiresAction("l", lastDigit, hasParallel, numBatteries) == False

def test_complicatedWires_1100():
    assert complicatedWiresAction("rb", lastDigit, hasParallel, numBatteries) == serialCheck(lastDigit)

def test_complicatedWires_1010():
    assert complicatedWiresAction("rs", lastDigit, hasParallel, numBatteries) == True

def test_complicatedWires_1001():
    assert complicatedWiresAction("rl", lastDigit, hasParallel, numBatteries) == batteryCheck(numBatteries)

def test_complicatedWires_0110():
    assert complicatedWiresAction("bs", lastDigit, hasParallel, numBatteries) == False

def test_complicatedWires_0101():
    assert complicatedWiresAction("bl", lastDigit, hasParallel, numBatteries) == parallelCheck(hasParallel)

def test_complicatedWires_0011():
    assert complicatedWiresAction("sl", lastDigit, hasParallel, numBatteries) == batteryCheck(numBatteries)

def test_complicatedWires_1110():
    assert complicatedWiresAction("rbs", lastDigit, hasParallel, numBatteries) == parallelCheck(hasParallel)

def test_complicatedWires_1101():
    assert complicatedWiresAction("rbl", lastDigit, hasParallel, numBatteries) == serialCheck(lastDigit)

def test_complicatedWires_1011():
    assert complicatedWiresAction("rsl", lastDigit, hasParallel, numBatteries) == batteryCheck(numBatteries)

def test_complicatedWires_0111():
    assert complicatedWiresAction("bsl", lastDigit, hasParallel, numBatteries) == parallelCheck(hasParallel)

def test_complicatedWires_1111():
    assert complicatedWiresAction("rbsl", lastDigit, hasParallel, numBatteries) == False


# Wire Sequences tests

def test_wireSequences_r1c():
    assert wireSequencesAction("red", ["c"]) == True

def test_wireSequences_r2a():
    assert wireSequencesAction("red", ["c", "a"]) == False

def test_wireSequences_r3b():
    assert wireSequencesAction("red", ["c", "a", "b"]) == False

def test_wireSequences_r4b():
    assert wireSequencesAction("red", ["c", "a", "b", "b"]) == False

def test_wireSequences_r5c():
    assert wireSequencesAction("red", ["c", "a", "b", "b", "c"]) == False

def test_wireSequences_r6a():
    assert wireSequencesAction("red", ["c", "a", "b", "b", "c", "a"]) == True

def test_wireSequences_r7c():
    assert wireSequencesAction("red", ["c", "a", "b", "b", "c", "a", "c"]) == True 

def test_wireSequences_r8b():
    assert wireSequencesAction("red", ["c", "a", "b", "b", "c", "a", "c", "b"]) == True

def test_wireSequences_r9a():
    assert wireSequencesAction("red", ["c", "a", "b", "b", "c", "a", "c", "b", "a"]) == False 

def test_wireSequences_u1c():
    assert wireSequencesAction("blue", ["c"]) == False 

def test_wireSequences_u2a():
    assert wireSequencesAction("blue", ["c", "a"]) == True 

def test_wireSequences_u3b():
    assert wireSequencesAction("blue", ["c", "a", "b"]) == True 

def test_wireSequences_u4b():
    assert wireSequencesAction("blue", ["c", "a", "b", "b"]) == False 

def test_wireSequences_u5c():
    assert wireSequencesAction("blue", ["c", "a", "b", "b", "c"]) == False 

def test_wireSequences_u6a():
    assert wireSequencesAction("blue", ["c", "a", "b", "b", "c", "a"]) == False 

def test_wireSequences_u7c():
    assert wireSequencesAction("blue", ["c", "a", "b", "b", "c", "a", "c"]) == True 

def test_wireSequences_u8b():
    assert wireSequencesAction("blue", ["c", "a", "b", "b", "c", "a", "c", "b"]) == False 

def test_wireSequences_u9a():
    assert wireSequencesAction("blue", ["c", "a", "b", "b", "c", "a", "c", "b", "a"]) == True 

def test_wireSequences_a1c():
    assert wireSequencesAction("black", ["c"]) == True 

def test_wireSequences_a2a():
    assert wireSequencesAction("black", ["c", "a"]) == True 

def test_wireSequences_a3b():
    assert wireSequencesAction("black", ["c", "a", "b"]) == True 

def test_wireSequences_a4b():
    assert wireSequencesAction("black", ["c", "a", "b", "b"]) == False 

def test_wireSequences_a5c():
    assert wireSequencesAction("black", ["c", "a", "b", "b", "c"]) == False 

def test_wireSequences_a6a():
    assert wireSequencesAction("black", ["c", "a", "b", "b", "c", "a"]) == False 

def test_wireSequences_a7c():
    assert wireSequencesAction("black", ["c", "a", "b", "b", "c", "a", "c"]) == False 

def test_wireSequences_a8b():
    assert wireSequencesAction("black", ["c", "a", "b", "b", "c", "a", "c", "b"]) == False 

def test_wireSequences_a9a():
    assert wireSequencesAction("black", ["c", "a", "b", "b", "c", "a", "c", "b", "a"]) == False 


# Passwords tests

def test_passwords1():
    assert passwordsAction(["K", "T", "Y", "U", "W", "M"], ["W", "O", "L", "Z", "I", "M"], ["M", "Q", "K", "L", "O", "U"], ["O", "Z", "L", "I", "R", "T"], ["D", "Z", "L", "I", "R", "T"]) == "WOULD" 

def test_passwords2():
    assert passwordsAction(["W", "U", "K", "J", "C", "G"], ["R", "U", "E", "P", "B", "C"], ["Z", "Y", "I", "L", "O", "W"], ["O", "Z", "L", "I", "R", "T"], ["E", "Z", "L", "I", "R", "T"]) == "WRITE" 

def test_passwords3():
    assert passwordsAction(["Z", "M", "S", "N", "L", "Q"], ["N", "Z", "V", "E", "O", "Q"], ["Q", "V", "E", "P", "Z", "I"], ["O", "E", "L", "I", "R", "T"], ["O", "Z", "L", "I", "R", "T"]) == "NEVER"

def test_passwords4():
    assert passwordsAction(["Y", "V", "F", "O", "A", "I"], ["K", "U", "G", "I", "R", "C"], ["A", "M", "O", "Q", "J", "F"], ["O", "Z", "L", "I", "R", "T"], ["N", "Z", "L", "I", "R", "T"]) == "AGAIN"

def test_passwords5():
    assert passwordsAction(["R", "C", "H", "G", "T", "D"], ["T", "D", "J", "O", "P", "R"], ["M", "O", "P", "U", "W", "D"], ["J", "S", "N", "I", "M", "T"], ["E", "Z", "L", "I", "R", "T"]) == "HOUSE"

def test_passwords6():
    assert passwordsAction(["X", "Y", "S", "A", "M", "Q"], ["L", "A", "U", "T", "R", "Q"], ["J", "C", "S", "I", "N", "O"], ["O", "Z", "L", "I", "R", "T"], ["O", "Z", "L", "I", "R", "T"]) == "STILL"
