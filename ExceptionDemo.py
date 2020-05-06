"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    try:
        print(4/0)
    except ZeroDivisionError:
        print("\nYou tried to divide by zero dummy! The program will now self destruct.\n")
        exit
    except:
        print("We don't know what happened there. Too bad.")
        exit
    

main()    