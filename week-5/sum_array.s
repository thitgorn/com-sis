	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 13
	.globl	_add
	.p2align	4, 0x90
_add:                                   ## @add
	.cfi_startproc
## BB#0:
	pushq	%rbp
Lcfi0:
	.cfi_def_cfa_offset 16
Lcfi1:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Lcfi2:
	.cfi_def_cfa_register %rbp
	movq	%rdi, -8(%rbp)
	movl	%esi, -12(%rbp)
	movl	$0, -16(%rbp)
	movl	$0, -20(%rbp)
LBB0_1:                                 ## =>This Inner Loop Header: Depth=1
	movl	-20(%rbp), %eax
	cmpl	-12(%rbp), %eax
	jge	LBB0_4
## BB#2:                                ##   in Loop: Header=BB0_1 Depth=1
	movq	-8(%rbp), %rax
	movslq	-20(%rbp), %rcx
	movl	(%rax,%rcx,4), %edx
	addl	-16(%rbp), %edx
	movl	%edx, -16(%rbp)
## BB#3:                                ##   in Loop: Header=BB0_1 Depth=1
	movl	-20(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -20(%rbp)
	jmp	LBB0_1
LBB0_4:
	movl	-16(%rbp), %eax
	popq	%rbp
	retq
	.cfi_endproc


.subsections_via_symbols
