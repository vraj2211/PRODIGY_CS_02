define the encryption and decryption functions:

Encryption: We'll shift pixel values and swap pixel positions.
Decryption: We'll reverse the process of encryption


Explanation


Encryption:

We first convert the image to a NumPy array for easier manipulation.
Each pixel value is shifted by a key (default is 42).
We swap adjacent pixels in a simple pattern (e.g., swap every pair of pixels in even positions).
Decryption:

The process is reversed by swapping the pixels back to their original positions.
The pixel values are then shifted back by subtracting the key
