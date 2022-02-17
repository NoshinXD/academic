import time
import os
#-----------------------Constants------------------------------
word_length = 4
num_of_bits = int(input ("Enter number of bits in key : "))
num_of_round = int(num_of_bits/32) + 6
num_of_chars = int(num_of_bits/8)
num_of_ws = int(num_of_chars / word_length) 

#---------------------------------------------------------------------------------------------
###----------bitvector_demo.py start-----------------
# -*- coding: utf-8 -*-
"""BitVector Demo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18MOtTMOl78t08PSpHkEQBQ7rmFk9Z8l6

Install The BitVector Library
"""
#pip install BitVector


"""Tables"""

from BitVector import *
Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]

b = BitVector(hexstring="4E")
int_val = b.intValue()
s = Sbox[int_val]
s = BitVector(intVal=s, size=8)
#print(s.get_bitvector_in_hex())

AES_modulus = BitVector(bitstring='100011011')

bv1 = BitVector(hexstring="02")
bv2 = BitVector(hexstring="63")
bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
#print(bv3)
###----------bitvector_demo.py end-----------------
#---------------------------------------------------------------------------------------------
###----------sbox_or_invSbox.py start-----------------
def generate_Sbox():
    SboxList = []
    for i in range(256):
        SboxList.append(0)

    n = 8
    for i in range(256):
        if i == 0:
            SboxList[0] = 99
        else:
            t = BitVector(intVal=i, size=n)
            b = t.gf_MI(AES_modulus, n)
            const = BitVector(hexstring="63")
            s = const ^ b ^ (b << 1) ^ (b << 1) ^ (b << 1) ^ (b << 1)
            #SboxList[i] = format(int(s), "x")
            SboxList[i] = int(s)

    return SboxList

def generate_InvSbox():
    InvSboxList = []
    for i in range(256):
        InvSboxList.append(0)

    n = 8
    for i in range(256):
        s = BitVector(intVal=i, size=n)
        const = BitVector(hexstring="5")
        b = const ^ (s << 1) ^ (s << 2) ^ (s << 3)
        if int(b) == 0:
            #InvSboxList[i] = format(int(0), "x")
            InvSboxList[i] = 0
        else:
            t = b.gf_MI(AES_modulus, n)
            #InvSboxList[i] = format(int(t), "x")
            InvSboxList[i] = int(t)

    return InvSboxList

###----------sbox_or_invSbox.py end-----------------
#---------------------------------------------------------------------------------------------
###----------rounKey.py start-----------------
def leftCircularShiftbyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def leftCircularShift(arr, d, n):
    for i in range(d):
        leftCircularShiftbyOne(arr, n)

def byteSubstitution(list, n):
    for i in range(n):
        b = BitVector(hexstring=list[i])
        int_val = b.intValue()
        s = Sbox[int_val]
        s = BitVector(intVal=s, size=8)
        list[i] = s.get_bitvector_in_hex()

def byteSubstitution_2(list, n):
    sboxList = generate_Sbox()
    for i in range(n):
        b = BitVector(hexstring=list[i])
        int_val = b.intValue()
        s = sboxList[int_val]
        s = BitVector(intVal=s, size=8)
        list[i] = s.get_bitvector_in_hex()

def addRoundConstant(list, list0, constList0):
    list[0] = format(int(list0, 16) ^ int(constList0, 16), "x")

def XOR(list1, list2, n):
    lst = []
    for i in range(n):
        lst.append(format(int(list1[i], 16) ^ int(list2[i], 16), "x"))

    return lst


def g(w_list, constList):
    #print("left shift:")
    w_list_len = len(w_list)
    leftCircularShift(w_list, 1, w_list_len)

    #print("Byte substitution:")
    byteSubstitution(w_list, w_list_len)

    #print("Adding round constant:")
    addRoundConstant(w_list, w_list[0], constList[0])

    return w_list


def generate_one_key(roundKeyList, imm_prev_roundKey, cur, constList, word_length, num_of_chars):
    w = []
    w0 = []
    w3 = []
    #making w[0]
    for i in range(word_length):
        w0.append(imm_prev_roundKey[i])
    
    #makingw[3]
    idx = num_of_chars - word_length
    for i in range(word_length):
        w3.append(imm_prev_roundKey[idx])
        idx = idx + 1
    
    #making w4
    w3 = g(w3, constList)
    w4 = XOR(w0, w3, word_length)

    for i in range(word_length):
        roundKeyList[cur].append(w4[i])

    num_of_itr = int(num_of_chars / word_length) - 1

    for itr in range(num_of_itr):
        wi = [] # wi = w[i-4] xor w[i-1]
        wi_4 = [] # w[i-4]

        k = 4 * (itr + 1)
        for i in range(word_length):
            wi_4.append(imm_prev_roundKey[k])
            k = k + 1
        wi = XOR(wi_4, w4, word_length)
        
        w4 = wi
        for i in range(word_length):
            roundKeyList[cur].append(w4[i])
    

def generate_keys(roundKeyList, word_length, num_of_chars):
    #print("printing from generate keys:")
    constList = ['01', '00', '00', '00']
    for i in range(len(roundKeyList)-1):
        generate_one_key(roundKeyList, roundKeyList[i], i+1, constList, word_length, num_of_chars)
        bv1 = BitVector(hexstring=constList[0])
        bv2 = BitVector(hexstring="02")
        bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
        constList[0] = format(int(bv3), "x")


###----------rounKey.py end-----------------
#---------------------------------------------------------------------------------------------
###----------matrix.py start-----------------
def getTranspose(temp_matrix, num_of_ws, wordinCol):
    if wordinCol == 1:
        rows, cols = (4, num_of_ws) 
    else:
        rows, cols = (num_of_ws, 4)
    matrix = []
    idx = 0
    for i in range(rows): 
        col = [] 
        for j in range(cols): 
            col.append(0)
            idx = idx + 1 
        matrix.append(col) 

    for i in range(len(temp_matrix)):
        for j in range(len(temp_matrix[0])):
            matrix[j][i] = temp_matrix[i][j]
 
    return matrix

def getMatrix(list, num_of_ws):
    rows, cols = (4, num_of_ws) 
    temp_matrix = [] 
    idx = 0
    for i in range(cols): 
        col = [] 
        for j in range(rows): 
            col.append(list[idx])
            idx = idx + 1 
        temp_matrix.append(col) 
    wordinCol = 1
    matrix = getTranspose(temp_matrix, num_of_ws, wordinCol)
 
    return matrix

def getList(temp_matrix, num_of_ws):
    
    wordinCol = 0
    matrix = getTranspose(temp_matrix, num_of_ws, wordinCol)

    lst = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            lst.append(matrix[i][j])
    return lst

def matrix_mult(A, B, num_of_ws):
    rows, cols = (4, num_of_ws) 
    result = []
    idx = 0
    for i in range(rows): 
        col = [] 
        for j in range(cols): 
            col.append(BitVector(hexstring = "00"))
            idx = idx + 1 
        result.append(col) 

    rows, cols = (4, num_of_ws) 
    mat_mul = []
    idx = 0
    for i in range(rows): 
        col = [] 
        for j in range(cols): 
            col.append(0)
            idx = idx + 1 
        mat_mul.append(col) 

    for i in range(len(A)): 
        for j in range(len(B[0])): 
            for k in range(len(B)): 
                bv1 = A[i][k]
                bv2 = BitVector(hexstring = B[k][j])
                temp = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
                result[i][j] = result[i][j] ^ temp
                int_val = result[i][j].intValue()
                hex_val = format(int_val, "x")
                mat_mul[i][j] = hex_val
    
    return mat_mul
    
###----------matrix.py end-----------------
#---------------------------------------------------------------------------------------------
###----------encryption_round.py start-----------------

def get_encryption_round(roundList, next_roundKey, lastRound, round_idx, n, word_length, num_of_ws):
    stateList = []
    for i in range(n):
        stateList.append(roundList[round_idx][i])
    #print("substitution bytes:")
    byteSubstitution(stateList, n)
    #print(stateList)  #page-5
    newStateMatrix = getMatrix(stateList, num_of_ws)
    #print("shift row:")
    for i in range(word_length):
        tempList = newStateMatrix[i]
        leftCircularShift(tempList, i, word_length)
        newStateMatrix[i] = tempList
    
    #print(newStateMatrix) #page-6
    
    if round_idx != lastRound:
        #print("mix column:")
        cur_stateMatrix = matrix_mult(Mixer, newStateMatrix, num_of_ws) 
        #print(cur_stateMatrix) #page-7
        cur_stateList = getList(cur_stateMatrix, num_of_ws)
    else:
        cur_stateList = getList(newStateMatrix, num_of_ws)

    #print("add round key:")
    l_len = len(cur_stateList)
    newList = XOR(cur_stateList, next_roundKey, l_len)
    for i in range(n):
        roundList[round_idx + 1].append(newList[i])
    
    return newList


def encryption(roundList, roundKeyList, hex_text_list, hex_key, word_length, num_of_ws):
    newStateList = []
    
    #add roundkey, round 0
    s_list_len = len(hex_text_list)
    newStateList = XOR(hex_text_list, hex_key, s_list_len)
    
    for i in range(s_list_len):
        roundList[0].append(newStateList[i])

    #round 1-10
    lastRound = len(roundList) - 2
    for i in range(len(roundList)-1):
        newList = get_encryption_round(roundList, roundKeyList[i+1], lastRound, i, s_list_len, word_length, num_of_ws)


###----------encryption_round.py end-----------------
#---------------------------------------------------------------------------------------------
###----------decription_round.py start-----------------
def rightCircularShiftbyOne(arr, n):
    temp = arr[n-1]
    for i in range(n-1, -1, -1):
        arr[i] = arr[i-1]
    arr[0] = temp

def rightCircularShift(arr, d, n):
    for i in range(d):
        rightCircularShiftbyOne(arr, n)

def inverseByteSubstitution(list, n):
    for i in range(n):
        b = BitVector(hexstring=list[i])
        int_val = b.intValue()
        s = InvSbox[int_val]
        s = BitVector(intVal=s, size=8)
        list[i] = s.get_bitvector_in_hex()

def inverseByteSubstitution_2(list, n):
    invSboxList = generate_InvSbox()
    for i in range(n):
        b = BitVector(hexstring=list[i])
        int_val = b.intValue()
        s = invSboxList[int_val]
        s = BitVector(intVal=s, size=8)
        list[i] = s.get_bitvector_in_hex()

def get_decryption_round(decryptRoundList, roundKey, lastRound, round_idx, n, word_length, num_of_ws):
    decryptStateList = []
    for i in range(n):
        decryptStateList.append(decryptRoundList[round_idx][i])

    decryptStateMatrix = getMatrix(decryptStateList, num_of_ws)

    #print("inverse shift row:")
    for i in range(word_length):
        tempList = decryptStateMatrix[i]
        rightCircularShift(tempList, i, word_length)
        decryptStateMatrix[i] = tempList

    decypytStateList_sub = getList(decryptStateMatrix, num_of_ws) 
    #print("inverse sub bytes:")
    inverseByteSubstitution(decypytStateList_sub, n)

    #print("add round key:")
    newDecryptStateList = XOR(decypytStateList_sub, roundKey, n)

    if round_idx != lastRound:
        #print("inverse mix column:")
        decryptMatrix_mix = getMatrix(newDecryptStateList, num_of_ws)
        decrypt_cur_stateMatrix = matrix_mult(InvMixer, decryptMatrix_mix, num_of_ws) 
        f_list = getList(decrypt_cur_stateMatrix, num_of_ws)
    else:
        f_list = newDecryptStateList

    for i in range(n):
        decryptRoundList[round_idx + 1].append(f_list[i])


def get_decryption(decryptRoundList, encryptedText, roundKeyList, num_of_round, word_length, num_of_ws):
    s_list_len = len(encryptedText)
    #add round key, round 0
    decryptStateList = XOR(encryptedText, roundKeyList[num_of_round], s_list_len)

    for i in range(s_list_len):
        decryptRoundList[0].append(decryptStateList[i])
    
    #round 1-10
    lastRound = len(decryptRoundList) - 2
    for i in range(len(decryptRoundList)-1):
        req_key_idx = len(decryptRoundList) - 2 -i
        get_decryption_round(decryptRoundList, roundKeyList[req_key_idx], lastRound, i, s_list_len, word_length, num_of_ws)


###----------decription_round.py end-----------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

#reading files
def byte_target2(filename):
    with open(filename, "rb") as f:
        tlist = []
        byte = f.read(1)
        if byte:
            tlist.append(byte)
        while byte:
            byte = f.read(1)
            if byte:
                tlist.append(byte)
    f.close()
    return tlist

key = input ("Enter key : ") 
#key = "Thats my Kung Fu"

print("1. Plaintext     2. File ")

option = int(input("Please Enter: "))

if option == 1:
    plainText = input ("Enter Plaintext : ")
    #plainText = "Implement CBC (Cipher Blocker Chaining) mode for your AES algorithm. \nIf you have reached this far, we highly appreciate your interest in cryptography though we are out of bonus marks. \nPat yourself on the back"
else:
    filename = input("Enter Filename : ")
    #filename = "sample.pdf"
    input_filename, file_extension = os.path.splitext(filename)
    plainText = byte_target2(filename)

#fixing key_length
length = len(key)
if length < num_of_chars:
    req = num_of_chars - length
    for i in range(req):
        key = key + '\0'
elif length > num_of_chars:
    key = key[:num_of_chars]

#fixing text length
text_length = len(plainText)
original_file_len = len(plainText)
if text_length % num_of_chars != 0:
    multiplier = int(text_length / num_of_chars) + 1
    req = multiplier * num_of_chars - text_length
    
    if option == 1:
        for i in range(req):
            plainText = plainText + ' '
    else:
        for i in range(req):
            my_str = ' '
            my_str_as_bytes = str.encode(my_str)
            plainText.append(my_str_as_bytes)


hex_key = []
hex_text_list = []

for c in key:
    hex_key.append(format(ord(c), "x"))

for c in plainText:
    hex_text_list.append(format(ord(c), "x"))

list_of_text = []
list_of_text_len = int(len(hex_text_list) / num_of_chars) 

#creating blocks of hex_text
text_block_list = []
for i in range(list_of_text_len):
    text_block_list.append([])

k = 0
for i in range(list_of_text_len):
    for j in range(num_of_chars):
        text_block_list[i].append(hex_text_list[k])
        k = k + 1

#creating blocks of ciphertext
ciphertext_block_list = []
for i in range(list_of_text_len):
    ciphertext_block_list.append([])

#creatng blocks of decrypted text
decrypted_block_list = []
for i in range(list_of_text_len):
    decrypted_block_list.append([])

key_schedule_start_time = time.time()

#making list_of_keys
roundKeyList = []
keyList_idx = 0
for i in range(num_of_round + 1):
    roundKeyList.append([])

size_of_keyList = len(roundKeyList)
for i in range(num_of_chars):
    roundKeyList[0].append(hex_key[i])

generate_keys(roundKeyList, word_length, num_of_chars)

print("KeyList:")
for i in range(num_of_round + 1):
    keyLst = roundKeyList[i]
    print(*keyLst)
print()

key_schedule_end_time = time.time()
key_schedule_time = key_schedule_end_time - key_schedule_start_time

#making list of ciphers
for i in range(list_of_text_len):
    if option == 2: 
        print("round " + str(i))
    encryption_roundList = []
    for j in range(num_of_round + 1):
        encryption_roundList.append([])
    encryption(encryption_roundList, roundKeyList, text_block_list[i], hex_key, word_length, num_of_ws)
    ciphertext = encryption_roundList[num_of_round]
    for j in range(num_of_chars):
        ciphertext_block_list[i].append(ciphertext[j])

encryption_end_time = time.time()
encryption_time = encryption_end_time - key_schedule_end_time

#making list of decipheredtexts
for i in range(list_of_text_len):
    if option == 2: 
        print("round " + str(i))
    decryption_roundList = []
    for j in range(num_of_round + 1):
        decryption_roundList.append([])
    get_decryption(decryption_roundList, ciphertext_block_list[i], roundKeyList, num_of_round, word_length, num_of_ws)
    decrypted_text = decryption_roundList[num_of_round]
    for j in range(num_of_chars):
        decrypted_block_list[i].append(decrypted_text[j])


if option == 1:
    originalText = ""
    for i in range(list_of_text_len):
        for j in range(num_of_chars):
            a = decrypted_block_list[i][j]
            a = int(a, 16)
            if a <= 15:
                a = format(a, '02x')
                bytes_object = bytes.fromhex(a)
            else:
                bytes_object = bytes.fromhex(decrypted_block_list[i][j])
            #bytes_object = bytes.fromhex(decrypted_block_list[i][j])
            ascii_string = bytes_object.decode("ASCII")
            originalText = originalText + ascii_string
else:
    originalText = []
    for i in range(list_of_text_len):
        print("round " + str(i))
        for j in range(num_of_chars):
            a = decrypted_block_list[i][j]
            a = int(a, 16)
            if a <= 15:
                a = format(a, '02x')
                bytes_object = bytes.fromhex(a)
            else:
                bytes_object = bytes.fromhex(decrypted_block_list[i][j])
            originalText.append(bytes_object)


if option == 1:
    print("original text:")
    print(originalText)
    print()
else:
    #print("original text:")
    #print(originalText)
    print()
    output_filename = "output_" + input_filename + file_extension
    f2 = open(output_filename, 'wb')
    for i in range(original_file_len):
        f2.write(originalText[i])

    f2.close()

decryption_end_time = time.time()
decryption_time = decryption_end_time - encryption_end_time

print("key_scheduling: %s seconds" % (key_schedule_time))
print("encryption_time: %s seconds" % (encryption_time))
print("decryption_time: %s seconds" % (decryption_time))
print()

def printMatrix(lst):
    rows, cols = (16, 16) 
    mySbox = []
    idx = 0
    for i in range(rows): 
        col = [] 
        for j in range(cols): 
            col.append(0)
            idx = idx + 1 
        mySbox.append(col) 

    k = 0
    for i in range(rows):
        for j in range(cols):
            mySbox[i][j] = format(lst[k], "x")
            k = k + 1

    for i in range(rows):
        print(mySbox[i])
        #pass
    print()

if_sbox = int(input("Enter 1 to show Sbox/invSbox "))
if if_sbox == 1:
    print("SBox:")
    mySboxList = generate_Sbox()
    printMatrix(mySboxList)

    print("invSBox:")
    myInvSboxList = generate_InvSbox()
    printMatrix(myInvSboxList)