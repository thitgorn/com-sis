add:
  push rbp
  mov rbp, rsp
  mov QWORD WORD[rbp-24], rdi
  mov DWORD WORD[rbp-28], esi
  mov DWORD WORD[rbp-4], 0
  mov DWORD WORD[rbp-8], 0
.L3:
  mov eax, DWORD WORD[rbp-8]
  cmp eax, DWORD WORD[rbp-28]
  jge .L2
  mov eax, DWORD WORD[rbp-8]
  cdqe
  lea rdx, [0+rax*4]
  mov rax, QWORD WORD[rbp-24]
  add rax, rdx
  mov eax, DWORD WORD[rax]
  add DWORD WORD[rbp-4], eax
  add DWORD WORD[rbp-8], 1
  jmp .L3
.L2:
  mov eax, DWORD WORD[rbp-4]
  pop rbp
  ret

