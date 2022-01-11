// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.


// Put your code here.




(MAIN)
@SCREEN
D=A
@0
M=D
@KBD
D=M
@LOOP_BLACK
D; JNE
@LOOP_WHITE
D; JEQ
@MAIN
0; JMP

(LOOP_WHITE)
@0
D=M
@8192
D=D-A
@SCREEN
D=D-A
@MAIN
D; JEQ
@0
A=M
M=0
@0
D=M+1
M=D
@LOOP_WHITE
0, JMP

(LOOP_BLACK)
@R0
D=M
@8192
D=D-A
@SCREEN
D=D-A
@MAIN
D; JEQ
@0
A=M
M=-1
@0
D=M+1
M=D
@LOOP_BLACK
0, JMP

