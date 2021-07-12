#!/usr/bin/env python
import os
import os.path, time



# FUNCTIONS ------------------------------------------------------------------------------------------

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')





# INIT ------------------------------------------------------------------------------------------------

len_text=47
len_descr=43

clearConsole()

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

def printHeader():
    print(" DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD   ") 
    print(" D:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::DDD  ")
    print(" D::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::DD ")
    print(" DDD:::::DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD:::::D")
    print("   D:::::D                                                             D:::::D")
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
    print("   D:::::D                                                              D:::::D")
    print("   D:::::D                                                              D:::::D")
    print("   D:::::D                                                             D:::::D")
    print(" DDD:::::DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD:::::D")
    print(" D::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::DD")
    print(" D:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::DDD   ")
    print(" DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD     ")


printHeader()





