#!/usr/bin/env python3

# Implementation of route cipher from Impractical Python Projects

ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
cipherlist = list(ciphertext.split())
COLS = 4
ROWS = 5
key = "-1 2 -3 4" #neg number means up column and positive means down column
translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS

key_int = [int(element) for element in key.split()]

#creating a loop for populating translation matrix

for k in key_int:
    if k < 0:
       col_list = cipherlist[start:stop]
    elif k > 0:
        col_list = list((reversed(cipherlist[start:stop])))
    translation_matrix[abs(k) - 1] = col_list
    start += ROWS
    stop += ROWS

print(f'\n cipher text: {ciphertext} \n')
print(f'\n translation matrix: {translation_matrix} \n')
print(f'\n key length: {len(key_int)}')

# looping through the list to pop off the last item from each list so that the decoded cipher can be created

for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + ' '
print(f'\n plain text: {plaintext}\n')
