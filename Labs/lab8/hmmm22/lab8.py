"""
Author: Kobe Dawes
Pledge: I pledge that I have abidided by the stevens hoor system. Kobe Dawes
CS 115
"""

# Demo of hmmm, the Harvey Mudd miniature machine
# D.Naumann 2015, rev Oct 2018

# When this file is loaded, it runs the program assigned
# to variable RunThis. Debug mode is controlled by 
# variable Mode. Read all the comments before trying it out.
# Remember to press F5 to run, after making changes.  

import sys
import importlib
# Also requires hmmmAssembler.py and hmmmSimulator.py to
# be available in the same directory as this file.


# Example1 is an example program that
#   1) asks the user for two inputs
#   2) computes the product of the inputs
#   3) prints out the result (with write)
#   4) stops

Example1 = """
00 read r1          # get # from user to r1
01 read r2          # ditto, for r2
02 mul r3 r1 r2     # assign r3 = r1 * r2
03 write r3         # print what's in r3
04 halt             # stop.
"""


# Example2 is an example program that
#   1) asks the user for an input
#   2) counts up from that input
#   3) keeps going and going...

Example2 = """
00 read r1          # get # from user to r1
01 write r1         # print the value of r1
02 addn r1 1        # add 1 to r1
03 jumpn 01         # jump to line 01
04 halt             # never halts! [use ctrl-c]
"""

# AbsVal is a program that asks the user for
# an input and then prints its absolute value.

AbsVal = """
00 read r1
01 jltz r1 4     # if r1 < 0 go to line 4
02 write r1      # print the absolute value
03 halt
04 setn r2 -1
05 mul r1 r1 r2  # assign r1 = r1 * -1 
06 jumpn 2       # go to line 2  
"""

# StoreLoad is an example program that
#   1) asks the user for an input
#   2) stores the value in a memory location
#   3) increments it and stores in another location
#   4) loads from that location and writes that value
# Try changing 11 to the address of an instruction!

StoreLoad = """
00 read r1         
01 storen r1 11   # put the value into mem[11]
02 addn r1 1       
03 setn r2 13 
04 storer r1 r2   # put incremented value into mem[13]
05 loadn r1 13
06 write r1       # write what was loaded
07 halt
"""

Triangle1 = """
00 read  r1          # get base
01 read  r2          # get height
02 mul   r1 r1 r2    # b times h into r1
03 setn  r2 2
04 div   r1 r1 r2    # divide by 2
05 write r1
06 halt
"""

Triangle2 = """
00 read  r1          # get base
01 read  r2          # get height
02 mul   r1 r1 r2    # b times h into r1
03 setn  r2 2
04 div   r1 r1 r2    # divide by 2
05 write r1
06 jumpn 0
"""

Triangle3 = """
00 read  r1          # get base
01 jeqzn r1 9
02 read  r2          # get height
03 jeqzn r2 9
04 mul   r1 r1 r2    # b times h into r1
05 setn  r2 2
06 div   r1 r1 r2    # divide by 2
07 write r1
08 jumpn 0
09 halt
"""

Factorial = """
# Input: n 
# Assume: n >= 0
# Output: n!
#

# register usage: r1 for the input, r13 for the output

0       read    r1         # Get n
1       setn    r13 1      # initialize r13
2       jeqzn   r1 6       # done if r1 is 0
3       mul     r13 r13 r1 # change r13 = r13 * r1
4       addn    r1 -1      # change r1 = r1 - 1
5       jumpn   2          # repeat
6       write   r13
7       halt
"""

Fib = """
0       read    r1          #get n
1       setn    r2 -2       #setting r2 as -2
2       add     r3 r1 r2    # adds registers r1 and r2 and places it in r3
3       jltzn   r3 16        # jumps to halt if less than 0
4       setn    r4 1        #sets r4 to 1. a =k-1
5       setn    r5 1        #sets r5 to 1. b =k-2
6       setn    r6 2        #sets r6 to 2. keeps track of count
7       add     r7 r4 r5    #adds r4 and r5 and places it in r7. C
8       addn    r6 1        #increments the tracker by 1
9       copy    r5 r4       #sets b = a
10      copy    r4 r7       #sets a = c
11      sub     r8 r6 r1    # subtracting n from tracker
12      jgtzn   r8 14       # if k is greater than 0
13      jump    7
14      write   r7          # prints c
15      halt
16      setn    r8 1
17      write   r8
18      halt    

"""



# Set this variable to whichever program you want to execute
# when this file is loaded.
RunThis = Triangle3

# Choose whether to use debug mode; uncomment one of the following lines.
Mode = ['-n'] # not debug mode, 
#Mode = ['-d'] # debug mode
#Mode = []     # prompt for whether to enter debug mode


# When you press F5 in IDLE, the following code will
# load the assembler and simulator, then run them.
# You can interrupt with Ctrl-C; then re-start Python.

if __name__ == "__main__" : 
    import hmmmAssembler ; importlib.reload(hmmmAssembler)
    import hmmmSimulator ; importlib.reload(hmmmSimulator)
    hmmmAssembler.main(RunThis) # assemble input into machine code file out.b
    hmmmSimulator.main(Mode)    # run the machine code in out.b




