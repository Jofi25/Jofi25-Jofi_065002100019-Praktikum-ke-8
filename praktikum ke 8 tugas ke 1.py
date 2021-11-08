# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 14:26:41 2021

@author: jofi
"""

print('Menentukan Bilangan Prima')
bagi = 2


def prima(nilai) :
        print('Bilangan', nilai, 'Adalah Bilangan Prima')

def cek_prima(nilai) :
    print('Bilangan', nilai, 'Bukan Bilangan Prima')
    if nilai % 2 == 0 :
        genap = nilai / 2 
        print('2 Dikali', int(genap), '=', nilai)
    else :
        ganjil = nilai / 3
        print('3 Dikali', int(ganjil), '=', nilai)
    

nilai = int(input('Masukkan Nilai : '))
while nilai % bagi != 0 :
    bagi = bagi + 1
if bagi == nilai :
    prima(nilai)
else :
    cek_prima(nilai)
    
    
