import numpy as np
import bitarray as ba

#Задание 1
H = np.array([[1, 1, 1, 0, 1, 0, 0],
             [1, 1, 0, 1, 0, 1, 0],
             [1, 0, 1, 1, 0, 0, 1]])

G = np.array([[1, 0, 0, 0, 1, 1, 1],
              [0, 1, 0, 0, 1, 1, 0],
              [0, 0, 1, 0, 1, 0, 1],
              [0, 0, 0, 1, 0, 1, 1]])

a = np.array([1, 0, 1, 0])

c = np.dot(a, G)%2

print("№ 1\nvector c = ",  c)

# Задание 2
c_t = np.transpose(c)
b = np.dot(H, c_t)%2
print("№ 2\nno error vector b = ", b)

e = ([0, 0, 0, 0, 1, 0, 0])
c1 = (c+e)%2
c1_t = np.transpose(c1)
b1 = np.dot(H, c1_t)%2
print("error vector b1 = ", b1)

# Задание 3
f = open("f3.txt", "rb")
a3 = ba.bitarray()
a3.fromfile(f)
print("№3\nread sequence = ", a3)

#Задание 4
print("№4\nread sequence = ", a3)
cr = []
for i in range(len(a3)//4):
    a_pos = np.array([a3[i*4], a3[(i*4)+1], a3[(i*4)+2], a3[(i*4)+3]])
    a_2pos = np.dot(a_pos, G)%2
    cr.extend(a_2pos)
bit = ba.bitarray()
bit.extend(cr)
with open("res4.txt", "wb") as f_enc:
    bit.tofile(f_enc)

#Задание 5
bit2 = ba.bitarray()
with open("res4.txt", "rb") as f_enc:
    bit2.fromfile(f_enc)
print("№5\nread encoded sequence = ", bit2)
cr2 = ba.bitarray()
for i in range(len(bit2)//7):
    cr2.extend([bit2[i*7], bit2[(i*7)+1], bit2[(i*7)+2], bit2[(i*7)+3]])
with open("res5.txt", "wb") as f_enc:
    cr2.tofile(f_enc)
bit3 = ba.bitarray()
with open("res5.txt", "rb") as f_enc:
    bit3.fromfile(f_enc)
print("read decoded sequence = ", bit3)
print("sequence from №4  = ", a3)

#Задание 6
bit4 = ba.bitarray()
with open("f3.zip", "rb") as f_enc:
    bit4.fromfile(f_enc)
print("№6\nread sequence = ", bit4)
bit4[4] = not bit4[4]
with open("res6.zip", "wb") as f_enc:
    bit4.tofile(f_enc)
print("changed (wrong) sequence = ", bit4)

#Задание 7
bit5 = ba.bitarray()
with open("res4.txt", "rb") as f_enc:
    bit5.fromfile(f_enc)
print("№7\nread encoded sequence = ", bit5)
bit5[5] = not bit5[5]
with open ("res7_er.txt", "wb") as f_enc:
    bit5.tofile(f_enc)
bit6 = ba.bitarray()
with open("res7_er.txt", "rb") as f_enc:
    bit6.fromfile(f_enc)
print("read error sequence = ", bit6)

Ht = np.transpose(H)
cr7 = ba.bitarray()
cr8 = ba.bitarray()
for i in range(len(bit6)//7):
    cr7 = [bit6[i*7], bit6[(i*7)+1], bit6[(i*7)+2], bit6[(i*7)+3], bit6[(i*7)+4], bit6[(i*7)+5], bit6[(i*7)+6]]
    b_n = np.dot(H, cr7)%2
    for j in range (0, len(cr7)//7):
        if (np.array_equal(b_n, Ht[j])):
            cr7[j+1] = not cr7[j+1]
    cr8.extend(cr7)
cr9 = ba.bitarray()
for i in range(len(cr8)//7):
    cr9.extend([cr8[i*7], cr8[(i*7)+1],cr8[(i*7)+2], cr8[(i*7)+3]])
with open("res7_cor.txt", "wb") as f_enc:
    cr9.tofile(f_enc)
bit7 = ba.bitarray()
with open("res7_cor.txt", "rb") as f_enc:
    bit7.fromfile(f_enc)
print("correct sequence = ", bit7)
print("sequence from №4 = ", a3)