#!/usr/bin/python
#
#

import os.path
from sets import Set
import sys


class Mastery():
    """
    """

    def __init__(self):
        """
        """
        pass

    def check(self, tokenList):
        """
        """
        tokenSet = Set(tokenList)

        if self.advanced.intersection(tokenSet):
            return 3
        if self.intermediate.intersection(tokenSet):
            return 2
        if self.basic.intersection(tokenSet):
            return 1
        else:
            return 0


class Abstraction(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set([""]) # FIXME
        self.intermediate = Set(["->","=>"]) 
        self.advanced = Set(["class","extends","super","@"]) 


class Parallelism(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set([])  # FIXME
        self.intermediate = Set([])  # FIXME
        self.advanced = Set([])  # FIXME


class Logic(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set(["if","true","yes","on","false","no","off"])
        self.intermediate = Set(["else","switch","when","unless"])
        self.advanced = Set(["and", "or", "not", "==","is","isnt"])


class Synchronization(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set(["pause"])
        self.intermediate = Set(["stop","recv","send"])
        self.advanced = Set(["await","sync","defer"])


class Flow(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set(["for","while","tick"])
        self.intermediate = Set(["forever"])
        self.advanced = Set(["break","continue","return",
							"throw","try","catch","finally"])  


class Interactivity(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set(["pressed"])
        self.intermediate = Set(["read","readnum","readstr","click",
								"keydown","keyup","keypress","dblclick",
								"button","mousemove","mouseup","mousedown",
								"listen","menu"])
        self.advanced = Set(["Audio","play","tone","silence","Webcam"])


class Data_representation(Mastery):
    """
    """

    def __init__(self):
        """
        """
		
		#Texto, movimiento, esconder, pintar.
        self.basic = Set(['print','say','write','type','typebox','speed',
						'turnto','moveto','hsl','label','slide','remove',
                     	'movexy','hide','show','wear','grow','home','mark',
					  	'jump','jumpto','jumpxy','twist','img','mirror',
						'pen','dot','box','fill','table','arrow','Piano',
						'bk','cg','cs','ct','fd','ht','rt','lt','st',
						'scale','fadeOut','fadeIn'])


        self.intermediate = Set(["new","delete","copy"]) #nueva variable
        self.advanced = Set(["[","]","in"])  # crear listas #tambien usado para bucles for.  # FIXME


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python coffee-mastery.py filename.coffee")

    coffeefile = sys.argv[1]

    if not os.path.exists(coffeefile):
        print "Error: filename does not exist"
        sys.exit("Usage: python coffee-mastery.py filename.coffee")

    with open(coffeefile) as filed:
        code = filed.read()

    tokenList = code.replace('[', '').replace(']', '').split()

    print tokenList
    print "Abstraction:", Abstraction().check(tokenList)
    print "Parallelism:", Parallelism().check(tokenList)
    print "Logic:", Logic().check(tokenList)
    print "Synchronization:", Synchronization().check(tokenList)
    print "Flow:", Flow().check(tokenList)
    print "Interactivity:", Interactivity().check(tokenList)
    print "Data representation:", Data_representation().check(tokenList)
