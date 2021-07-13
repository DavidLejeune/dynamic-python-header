#!/usr/bin/env python
import os
import os.path, time
import console
from colorama import init
init()
from colorama import Fore, Back, Style

# FUNCTIONS ------------------------------------------------------------------------------------------

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def printHeader():
    print(" DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD        ") 
    print(" D:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::DDD     ")
    print(" D::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::DD   ")
    print(" DDD:::::DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD:::::D  ")
    print("   D:::::D                                                             D:::::D ")
    print("   D:::::D     Program : " + str_program_name  + "D:::::D")
    print("   D:::::D     " + str_underline + "D:::::D")
    print("   D:::::D                                                              D:::::D")
    print("   D:::::D      Author : " + str_author_name + "D:::::D")
    print("   D:::::D                                                              D:::::D")
    print("   D:::::D        Date :   [created] %s           D:::::D" % time.ctime(os.path.getctime(__file__)))
    print("   D:::::D                 [updated] %s           D:::::D" % time.ctime(os.path.getmtime(__file__)))
    print("   D:::::D                                                              D:::::D")
    print("   D:::::D     Description : " + str_descr1 + "D:::::D")
    if (len(descr2) > 1) : 
        print("   D:::::D                   " + str_descr2 + "D:::::D")
    if (len(descr3) > 1) : 
        print("   D:::::D                   " + str_descr3 + "D:::::D")
    if (len(descr4) > 1) : 
        print("   D:::::D                   " + str_descr4 + "D:::::D")
    if (len(descr5) > 1) : 
        print("   D:::::D                   " + str_descr5 + "D:::::D")
    print("   D:::::D                                                              D:::::D s")
    print("   D:::::D                                                              D:::::D ")
    print("   D:::::D                                                             D:::::D  ")
    print(" DDD:::::DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD:::::D   ")
    print(" D::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::DD    ")
    print(" D:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::DDD      ")
    print(" DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD         ")
    print("")

def printHeaderColor():
    print(Fore.LIGHTRED_EX + " DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD        ") 
    print(Fore.LIGHTRED_EX +" D" + Fore.LIGHTBLUE_EX + ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::" + Fore.LIGHTRED_EX + "DDD     ")
    print(Fore.LIGHTRED_EX +" D" + Fore.LIGHTBLUE_EX + "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::" + Fore.LIGHTRED_EX + "DD   ")
    print(Fore.LIGHTRED_EX +" DDD" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D  ")
    print(Fore.LIGHTRED_EX +"   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                                                             D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D ")
    print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D" + Fore.YELLOW + "     Program : " + str_program_name  + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D" + Fore.YELLOW + "     " + str_underline + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                                                              D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D      " + Fore.LIGHTGREEN_EX + "Author" + Fore.WHITE + " : " + Fore.LIGHTMAGENTA_EX  + str_author_name + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                                                              D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D      " + Fore.LIGHTGREEN_EX + "  Date" + Fore.WHITE + " :  " + Fore.CYAN +" [created] " + Fore.LIGHTMAGENTA_EX  + time.ctime(os.path.getctime(__file__)) + "           " + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D       " + Fore.CYAN + "          [updated] " + Fore.LIGHTMAGENTA_EX  + time.ctime(os.path.getmtime(__file__)) + "           " + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                                                              D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D     " + Fore.LIGHTGREEN_EX + "Description" + Fore.WHITE + " : " + Fore.LIGHTMAGENTA_EX  + str_descr1 + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    if (len(descr2) > 1) : 
        print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                   " + Fore.LIGHTMAGENTA_EX  + str_descr2 + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    if (len(descr3) > 1) : 
        print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                   " + Fore.LIGHTMAGENTA_EX  + str_descr3 + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    if (len(descr4) > 1) : 
        print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                   " + Fore.LIGHTMAGENTA_EX  + str_descr4 + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    if (len(descr5) > 1) : 
        print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                   " + Fore.LIGHTMAGENTA_EX  + str_descr5 + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                                                              D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D ")
    print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                                                              D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D ")
    print(Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                                                             D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D  ")
    print(Fore.LIGHTRED_EX + " DDD" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D   ")
    print(Fore.LIGHTRED_EX + " D" + Fore.LIGHTBLUE_EX + "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::" + Fore.LIGHTRED_EX + "DD    ")
    print(Fore.LIGHTRED_EX + " D" + Fore.LIGHTBLUE_EX + ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::" + Fore.LIGHTRED_EX + "DDD      ")
    print(Fore.LIGHTRED_EX + " DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD         ")
    print("")


def printHeaderCentered():
    str_padding= " " * int((term_columns - 80) / 2)
    print(str_padding + " DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD        " + str_padding) 
    print(str_padding + " D:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::DDD     " + str_padding)
    print(str_padding + " D::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::DD   " + str_padding)
    print(str_padding + " DDD:::::DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD:::::D  " + str_padding)
    print(str_padding + "   D:::::D                                                             D:::::D " + str_padding)
    print(str_padding + "   D:::::D     Program : " + str_program_name  + "D:::::D" + str_padding)
    print(str_padding + "   D:::::D     " + str_underline + "D:::::D" + str_padding)
    print(str_padding + "   D:::::D                                                              D:::::D" + str_padding)
    print(str_padding + "   D:::::D      Author : " + str_author_name + "D:::::D" + str_padding)
    print(str_padding + "   D:::::D                                                              D:::::D" + str_padding)
    print(str_padding + "   D:::::D        Date :   [created] " + time.ctime(os.path.getctime(__file__)) + "           D:::::D" + str_padding)
    print(str_padding + "   D:::::D                 [updated] " + time.ctime(os.path.getmtime(__file__)) + "           D:::::D" + str_padding)
    print(str_padding + "   D:::::D                                                              D:::::D" + str_padding)
    print(str_padding + "   D:::::D     Description : " + str_descr1 + "D:::::D" + str_padding)
    if (len(descr2) > 1) : 
        print(str_padding + "   D:::::D                   " + str_descr2 + "D:::::D" + str_padding)
    if (len(descr3) > 1) : 
        print(str_padding + "   D:::::D                   " + str_descr3 + "D:::::D" + str_padding)
    if (len(descr4) > 1) : 
        print(str_padding + "   D:::::D                   " + str_descr4 + "D:::::D" + str_padding)
    if (len(descr5) > 1) : 
        print(str_padding + "   D:::::D                   " + str_descr5 + "D:::::D" + str_padding)
    print(str_padding + "   D:::::D                                                              D:::::D " + str_padding)
    print(str_padding + "   D:::::D                                                              D:::::D " + str_padding)
    print(str_padding + "   D:::::D                                                             D:::::D  " + str_padding)
    print(str_padding + " DDD:::::DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD:::::D   " + str_padding)
    print(str_padding + " D::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::DD    " + str_padding)
    print(str_padding + " D:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::DDD      " + str_padding)
    print(str_padding + " DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD         " + str_padding)
    print("")


def printHeaderCenteredColor():
    str_padding= " " * int((term_columns - 80) / 2)
    print(str_padding + Fore.LIGHTRED_EX + " DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD        ") 
    print(str_padding + Fore.LIGHTRED_EX +" D" + Fore.LIGHTBLUE_EX + ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::" + Fore.LIGHTRED_EX + "DDD     ")
    print(str_padding + Fore.LIGHTRED_EX +" D" + Fore.LIGHTBLUE_EX + "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::" + Fore.LIGHTRED_EX + "DD   ")
    print(str_padding + Fore.LIGHTRED_EX +" DDD" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D  ")
    print(str_padding + Fore.LIGHTRED_EX +"   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                                                             D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D ")
    print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D" + Fore.YELLOW + "     Program : " + str_program_name  + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D" + Fore.YELLOW + "     " + str_underline + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                                                              D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D      " + Fore.LIGHTGREEN_EX + "Author" + Fore.WHITE + " : " + Fore.LIGHTMAGENTA_EX  + str_author_name + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                                                              D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D      " + Fore.LIGHTGREEN_EX + "  Date" + Fore.WHITE + " :  " + Fore.CYAN +" [created] " + Fore.LIGHTMAGENTA_EX  + time.ctime(os.path.getctime(__file__)) + "           " + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D       " + Fore.CYAN + "          [updated] " + Fore.LIGHTMAGENTA_EX  + time.ctime(os.path.getmtime(__file__)) + "           " + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                                                              D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D     " + Fore.LIGHTGREEN_EX + "Description" + Fore.WHITE + " : " + Fore.LIGHTMAGENTA_EX  + str_descr1 + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    if (len(descr2) > 1) : 
        print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                   " + Fore.LIGHTMAGENTA_EX  + str_descr2 + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    if (len(descr3) > 1) : 
        print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                   " + Fore.LIGHTMAGENTA_EX  + str_descr3 + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    if (len(descr4) > 1) : 
        print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                   " + Fore.LIGHTMAGENTA_EX  + str_descr4 + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    if (len(descr5) > 1) : 
        print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                   " + Fore.LIGHTMAGENTA_EX  + str_descr5 + Fore.LIGHTRED_EX + "D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D")
    print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                                                              D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D ")
    print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                                                              D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D ")
    print(str_padding + Fore.LIGHTRED_EX + "   D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D                                                             D" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D  ")
    print(str_padding + Fore.LIGHTRED_EX + " DDD" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD" + Fore.LIGHTBLUE_EX + ":::::" + Fore.LIGHTRED_EX + "D   ")
    print(str_padding + Fore.LIGHTRED_EX + " D" + Fore.LIGHTBLUE_EX + "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::" + Fore.LIGHTRED_EX + "DD    ")
    print(str_padding + Fore.LIGHTRED_EX + " D" + Fore.LIGHTBLUE_EX + ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::" + Fore.LIGHTRED_EX + "DDD      ")
    print(str_padding + Fore.LIGHTRED_EX + " DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD         ")
    print("")


# INITS -----------------------------------------------------------------------------------------------
(term_columns, term_rows) = os.get_terminal_size()


len_text=47
len_descr=43


#clearConsole()

program_name="dynamic-python-header"
author_name="David Lejeune"
# keep description line under following width (desc0 is an example) :
descr0="###########################################"
descr1="Python header that can be imported or"
descr2="used in other scripts."
descr3=""
descr4=""
descr5=""


str_program_name=program_name + (" " * (len_text - len(program_name)))
str_underline="----------" + ("-" * len(program_name)) + (" " * (len_text - len(program_name)))
str_author_name=author_name + (" " * (len_text - len(author_name)))
str_descr1=descr1 + (" " * (len_descr - len(descr1)))
str_descr2=descr2 + (" " * (len_descr - len(descr2)))
str_descr3=descr3 + (" " * (len_descr - len(descr3)))
str_descr4=descr4 + (" " * (len_descr - len(descr4)))
str_descr5=descr5 + (" " * (len_descr - len(descr5)))


# SCRIPT ----------------------------------------------------------------------------------------------


printHeader()

printHeaderCentered()



printHeaderColor()
printHeaderCenteredColor()
