;; add.asm

; make the add function visible to the linker

global add


; prototype: int __cdecl add(int a, int b)

; desc: adds two integers and returns the result


global add


add:


push rbp

mov rbp, rsp

mov rax, rdi ; first argument

mov rbx, rsi ; 2nd argument

add rax, rbx

mov rsp,rbp

pop rbp

ret
