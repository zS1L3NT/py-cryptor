# Cryptor
Cryptor is a simple custom Python text encryptor and decryptor that works offline with no database conection

## External Installs
No external installs with [pip](https://pip.pypa.io/en/stable/)

## Usage
`encrypt()` and  `decrypt()` are functions that take in only 1 parameter which is the text you want to encrypt or decrypt

## How it works
### Example Input:<br>
a x 1 x b x 2 x c<br>
### Stage 1 (Swap Letters): ax->xa or bg->gb leaving last single letter out<br>
a x 1 x b x 2 x c<br>
x a x 1 x b x 2 c<br>
### Stage 3 (Salt k onwards): start with salting k then l then m,n,o,p......<br>
x a x 1 x b x 2 c<br>
k x l a m x n 1 o x p b q x r 2 s c <br>
### Stage 4 (Alternate letter): +1 -1 -1 +1<br>
k x l a m x n 1 o x p b q x r 2 s c <br>
l w k b n w m 2 p w o c r w q 3 t b <br>
### Stage 5 (Reverse):<br>
l w k b n w m 2 p w o c r w q 3 t b <br>
b t 3 q w r c o w p 2 m w n b k w l <br>
### Stage 6 (Alternate Case Change): every 2 characters will be changed to uppercase<br>
b t 3 q w r c o w p 2 m w n b k w l <br>
b T 3 Q w R c O w P 2 M w N b K w L <br>
### Stage 7 (Alternate letter): +3 -6 -3 +2<br>
b T 3 Q w R c O w P 2 M w N b K w L <br>
e N 0 S z L z Q z J 9 O z H y M z F <br>
### Stage 8 (Every Salt every digit with a decimal of π ): (Max 100 chars because of 100 digits of π)<br>
e N 0 S z L z Q z J 9 O z H y M z F <br>
e 1 N 4 0 1 S 5 z 9 L 2 z 6 Q 5 z 3 J 5 9 8 O 9 z 7 H 9 y 3 M 2 z 3 F 8 <br>
Done:<br>
e 1 N 4 0 1 S 5 z 9 L 2 z 6 Q 5 z 3 J 5 9 8 O 9 z 7 H 9 y 3 M 2 z 3 F 8 <br>

## Contributing
Pull requests are welcomed. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
