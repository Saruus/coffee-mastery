#!/usr/bin/python
#
#

import os.path
from sets import Set
import sys
import re
import ast
from collections import Counter



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
        dicc = {}

        if self.basic.intersection(tokenSet) or self.intermediate.intersection(tokenSet) or self.advanced.intersection(tokenSet):
            dicc['1'] = self.basic.intersection(tokenSet)
            dicc['2'] = self.intermediate.intersection(tokenSet)
            dicc['3'] = self.advanced.intersection(tokenSet)
            for element in dicc:
                if dicc[element] == Set([]):
                    dicc[element] = 'false'
                else:
                    value = str(dicc[element])
                    value = value[value.find("(")+1:value.find(")")]
                    value = ast.literal_eval(value)
                    dicc[element] = value

            return dicc
        else:
            return "false"

    def checkinglevel(self, tokenList):
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


class Move(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set(["fd","rt","lt","bk"])
        self.intermediate = Set(["speed","home","pause","slide"])
        self.advanced = Set(["turnto","moveto","movexy","jumpto","jumpxy","getxy","direction","distance"])

class Art(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set(["pen","dot","box","fill","grow","scale","twist","mirror","clip","drawon"])
        self.intermediate = Set(["wear","img","show","hide","ht","st","remove","cs","pu","pd","cg","ct"])
        self.advanced = Set(["canvas","rgba","rgb","hsl","hsla","fadeIn","fadeOut"])

    #    self.exist = Set(["Webcam","copy"])


class Text(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set(["write","type","typebox","label"])
        self.intermediate = Set(["menu","typeline"])
        self.advanced = Set(["read","readnum","readstr","debug"])


class Sound(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set(["play","tone"])
        self.intermediate = Set(["Audio","Piano"])
        self.advanced = Set(["stop","silence"])

class Control(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set(["if","in","switch","when","default"])
        self.intermediate = Set(["for","while","else","button","unless","loop","forever"])
        self.advanced = Set(["keyup","keypress","dblclick","keydown","mousedown",
                        "mouseup","mousemove","click","await","defer","lastmousemove"])

        self.exist = Set(["tick","break","continue","stop","then"])

       
class Operators(Mastery):
    """
    """

    def __init__(self):
        """
        """
        self.basic = Set([">","<","+","-","*","/",'=',"+=","==",'<=','=>',
                        'sin','cos','sqrt','tan','acos','atan','asin',"ln","exp",
                        "abs","max","min"])
        self.intermediate = Set(["is",'isnt',"and","or","not","true","false","random",
                        "round","ceil","floor","typeof"])
        self.advanced = Set(["->","return","do","NaN"])

        self.exist = Set(["match","pow","null","Infinity"])


def removeComments(string):
    rgx = re.compile('#{\w*}\s*')
    string = rgx.sub('',string)
    string = re.sub(re.compile("#.*?\n" ) ,"",string) # remove all occurance singleline comments (#COMMENT\n ) from string
    return string

def removeText(string):
    string = re.sub(re.compile("'.*?'" ), '', string) # remove all occurance singleline text ('TEXT'\n ) from string
    string = re.sub(re.compile('".*?"' ), '', string)
    return string

def removeParentheses(string):
    string = re.sub(re.compile(r'\('),"", string)
    string = re.sub(re.compile(r'\)'),"", string)
    string = re.sub(re.compile(r'\[.+?\]\s*'), "[]\n", string)
    string = re.sub(re.compile(r'\{.+?\}\s*'), "{}\n", string)
    return string

def removeNumbers(string):
    string = re.sub(re.compile("\d+"), "", string)
    string = re.sub(re.compile(r'\,'),' ', string)
    string = re.sub(re.compile(r'\.'),' ',string)
    
    return string

def duplicates(string):
    duplic = dict(Counter(string))
    duplic = { k:v for k, v in duplic.items() if v != 1 }
    return duplic

def niveles(tokenList):
    diccLevels = {}
    diccLevels['Move'] = Move().checkinglevel(tokenList)
    diccLevels['Art'] = Art().checkinglevel(tokenList)
    diccLevels['Text'] = Text().checkinglevel(tokenList)
    diccLevels['Sound'] =  Sound().checkinglevel(tokenList)
    diccLevels['Control'] = Control().checkinglevel(tokenList)
    diccLevels['Operators'] = Operators().checkinglevel(tokenList)
    return diccLevels


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python coffee-mastery.py filename.coffee")

    coffeefile = sys.argv[1]

    if not os.path.exists(coffeefile):
        print "Error: filename does not exist"
        sys.exit("Usage: python coffee-mastery.py filename.coffee")

    with open(coffeefile) as filed:
        code = filed.read() # la variable code contiene lo que hay escrito en el programa pencilcode. if, for, while...
        code = removeComments(code)
        code = removeText(code)
        code = removeParentheses(code)
        code = removeNumbers(code)


    print "CODE \n", code

    tokenList = code.replace('[', '').replace(']', '').split() #se mete lo que tiene el programa entre [] y comillas.
    duplicated = duplicates(tokenList)
    levels = niveles(tokenList)

    print tokenList
    print "Move:", Move().check(tokenList)
    print "Art:", Art().check(tokenList)
    print "Text:", Text().check(tokenList)
    print "Sound:", Sound().check(tokenList)
    print "Control:", Control().check(tokenList)
    print "Operators:", Operators().check(tokenList)
    print "Duplicados:", duplicated
    print "Levels:", levels

