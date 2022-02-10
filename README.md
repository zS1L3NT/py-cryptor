# Cryptor

![License](https://img.shields.io/github/license/zS1L3NT/py-cryptor?style=for-the-badge) ![Languages](https://img.shields.io/github/languages/count/zS1L3NT/py-cryptor?style=for-the-badge) ![Top Language](https://img.shields.io/github/languages/top/zS1L3NT/py-cryptor?style=for-the-badge) ![Commit Activity](https://img.shields.io/github/commit-activity/y/zS1L3NT/py-cryptor?style=for-the-badge) ![Last commit](https://img.shields.io/github/last-commit/zS1L3NT/py-cryptor?style=for-the-badge)

Cryptor is a simple custom Python text encryptor and decryptor using my own encryption algorithm.

## Motivation

I was interested in how text encryptors work and tried to make my own, which clearly didn't go very well.

## Features

-   Simple Text Encryption and Decryption

## Usage

Run the command

```
$ python crypt.py
```

## How it works

### Example Input:

a x 1 x b x 2 x c

### Stage 1 (Swap Letters): ax->xa or bg->gb leaving last single letter out

a x 1 x b x 2 x c
x a x 1 x b x 2 c

### Stage 3 (Salt k onwards): start with salting k then l then m, n, o, p......

x a x 1 x b x 2 c
k x l a m x n 1 o x p b q x r 2 s c

### Stage 4 (Alternate letter): +1 -1 -1 +1

k x l a m x n 1 o x p b q x r 2 s c
l w k b n w m 2 p w o c r w q 3 t b

### Stage 5 (Reverse):

l w k b n w m 2 p w o c r w q 3 t b
b t 3 q w r c o w p 2 m w n b k w l

### Stage 6 (Alternate Case Change): every 2 characters will be changed to uppercase

b t 3 q w r c o w p 2 m w n b k w l
b T 3 Q w R c O w P 2 M w N b K w L

### Stage 7 (Alternate letter): +3 -6 -3 +2

b T 3 Q w R c O w P 2 M w N b K w L
e N 0 S z L z Q z J 9 O z H y M z F

### Stage 8 (Every Salt every digit with a decimal of π ): (Max 100 chars because of 100 digits of π)

e N 0 S z L z Q z J 9 O z H y M z F
e 1 N 4 0 1 S 5 z 9 L 2 z 6 Q 5 z 3 J 5 9 8 O 9 z 7 H 9 y 3 M 2 z 3 F 8

Done:
e 1 N 4 0 1 S 5 z 9 L 2 z 6 Q 5 z 3 J 5 9 8 O 9 z 7 H 9 y 3 M 2 z 3 F 8

## Built with

-   Python
