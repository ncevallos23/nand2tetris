@256
D=A
@SP
M=D
@returnaddy0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0; JMP
(returnaddy0)
(Main.fibonacci)
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@SP
M=M-D
A=M
D=M
@SP
M=M+1
A=M
D=D-M
@TRUE0
D;JLT
@SP
A=M
M=0
A=A-1
M=0
@FINAL0
0; JEQ
(TRUE0)
@SP
A=M-1
M=-1
A=A+1
M=0
(FINAL0)
@SP
M=M-1
A=M
D=M
M=0
@IF_TRUE
D;JNE
@IF_FALSE
0;JMP
(IF_TRUE)
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@13
M=D
@5
D=D-A
A=D
D=M
@14
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@13
D=M
@1
A=D-A
D=M
@THAT
M=D
@13
D=M
@2
A=D-A
D=M
@THIS
M=D
@13
D=M
@3
A=D-A
D=M
@ARG
M=D
@13
D=M
@4
A=D-A
D=M
@LCL
M=D
@14
A=M
0;JMP
(IF_FALSE)
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@SP
M=M-D
A=M
D=M
@SP
M=M+1
A=M
D=D-M
@SP
A=M-1
M=D
@SP
A=M
M=0
@returnaddy1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0; JMP
(returnaddy1)
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@SP
M=M-D
A=M
D=M
@SP
M=M+1
A=M
D=D-M
@SP
A=M-1
M=D
@SP
A=M
M=0
@returnaddy2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0; JMP
(returnaddy2)
@2
D=A
@SP
M=M-D
A=M
D=M
@SP
M=M+1
A=M
D=D+M
@SP
A=M-1
M=D
@SP
A=M
M=0
@LCL
D=M
@13
M=D
@5
D=D-A
A=D
D=M
@14
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@13
D=M
@1
A=D-A
D=M
@THAT
M=D
@13
D=M
@2
A=D-A
D=M
@THIS
M=D
@13
D=M
@3
A=D-A
D=M
@ARG
M=D
@13
D=M
@4
A=D-A
D=M
@LCL
M=D
@14
A=M
0;JMP
(Sys.init)
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
@returnaddy3
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0; JMP
(returnaddy3)
(WHILE)
@WHILE
0;JMP
