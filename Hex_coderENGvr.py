from PIL import Image
import numpy as np
import random

dict_utf8 = {'!':33, '"':34, '#':35, '$':36, '%':37, '&':38, "'":39, '(':40, ')':41, '*':42, '+':43, ',':44, '-':45,
             '.':46, '/':47, '0':48, '1':49, '2':50, '3':51, '4':52, '5':53, '6':54, '7':55, '8':56, '9':57, ':':58,
             ';':59, '<':60, '=':61, '>':62, '?':63, '@':64, 'A':65, 'B':66, 'C':67, 'D':68, 'E':69, 'F':70, 'G':71,
             'H':72, 'I':73, 'J':74, 'K':75, 'L':76, 'M':77, 'N':78, 'O':79, 'P':80, 'Q':81, 'R':82, 'S':83, 'T':84,
             'U':85, 'V':86, 'W':87, 'X':88, 'Y':89, 'Z':90, '[':91, "'\'":92, ']':93, '^':94, '_':95, '`':96, 'a':97,
             'b':98, 'c':99, 'd':100, 'e':101, 'f':102, 'g':103, 'h':104, 'i':105, 'j':106, 'k':107, 'l':108, 'm':109, 'n':110,
             'o':111, 'p':112, 'q':113, 'r':114, 's':115, 't':116, 'u':117, 'v':118, 'w':119, 'x':120, 'y':121, 'z':122, '{':123,
             '|':124, '}':125, '~':126}
##===========================================================================
'''PIXELATION'''
##===========================================================================
def PIXELATION(file_name):
  line_word, line_bytes = [], []
  file = open(file_name, 'r', encoding="utf-8")
  while (byte := file.read(1)): ##read file.txt
    line_word.append(byte)
  file.close
  for i in range(len(line_word)):
      for word, w_num in dict_utf8.items():
          if line_word[i] == word:
              line_bytes.append(w_num)
  key, line_bytes1 = random.randrange(194, 255), []
  for i in line_bytes:
    if i < key:
      line_bytes1.append(key - i)
    elif i == key:
      line_bytes1.append(random.randrange(1, 32))
  lenf = len(line_bytes1)
  line_lenght = []
  if len(line_bytes1) % 3 != 0:
    while len(line_bytes1) % 3 != 0:
      line_bytes1.append(random.randrange(1, 255))
  leght_s = len(line_bytes1)
  while lenf > 0:
    line_lenght.append(((lenf % 256), 0, 0))
    lenf = lenf // 256
  line_lenght.append((key, 0, random.randrange(1, 255)))
  for k in range(0, (leght_s - len(line_lenght))):
    line_lenght.append((0, random.randrange(1, 255), random.randrange(1, 255)))  
  list_all, stroka = [], []
  for i in range(0, leght_s):
    tiple = (line_bytes1[i], random.randrange(1, 255), random.randrange(1, 255))
    stroka.append(tiple)
  list_all.append(stroka)
  list_all.append(line_lenght)
  array = np.array(list_all, dtype=np.uint8)
  new_image = Image.fromarray(array)
  return new_image.save('new' + str(random.randrange(1, 10000000)) + '.png') 
##===========================================================================
'''UNPIXELATION'''
##===========================================================================
def UNPIXELATION(file_name):
  im = Image.open(file_name, 'r') 
  lenght, width = im.size 
  pixel_values = list(im.getdata()) 
  im.close()
  massive, massive_lenghttrue = [], []
  for l_pixel in range(0, lenght * width): 
      if (pixel_values[l_pixel][2] != 0) & (pixel_values[l_pixel][1] != 0) & (pixel_values[l_pixel][0] != 0):
          massive.append(pixel_values[l_pixel][0]) 
      elif (pixel_values[l_pixel][2] == 0) & (pixel_values[l_pixel][1] == 0):
          massive_lenghttrue.append(pixel_values[l_pixel][0])
      elif (pixel_values[l_pixel][0] != 0) & (pixel_values[l_pixel][1] == 0):
          key = pixel_values[l_pixel][0]
  init, massive_ky = 0, []
  for l_lenght in range(0, len(massive_lenghttrue)): 
      init += massive_lenghttrue[l_lenght] * (256 ** l_lenght) 
  for leng in range(init):
      if massive[leng] < 33:
          massive_ky.append(key)
      elif massive[leng] > key:
          massive_ky.append(massive[leng] + key)
      elif massive[leng] < key:
          massive_ky.append(key - massive[leng])  
  file_out = open('result' + str(random.randrange(1, 10000000)) + '.txt', 'w')
  for i in range(init):
      for word, w_num in dict_utf8.items():
          if w_num == massive_ky[i]:
              file_out.write(word)
  file_out.close()  
##===========================================================================
print('                      _        _                                            ')
print('                     | |      | |                                           ')
print('  _ __ ___   __ _  __| | ___  | |__  _   _   _ __ ___   ___  _ __ ___ _ __  ')
print(" | '_ ` _ \ / _` |/ _` |/ _ \ | '_ \| | | | | '_ ` _ \ / _ \| '__/ _ \ '_ \ ")
print(' | | | | | | (_| | (_| |  __/ | |_) | |_| | | | | | | | (_) | | |  __/ | | |')
print(' |_| |_| |_|\__,_|\__,_|\___| |_.__/ \__, | |_| |_| |_|\___/|_|  \___|_| |_|')
print('                                      __/ |                                 ')
print('                                     |___/                                  ')
print('--|{HEX CODER V2}|--')
print('choose the type of script')
print('1 -- encode txt')
print('2 -- decode png')
print('|{--------------------------------------------WARNING:this script works with eng and special characters!!!-----------------------------------------------------------------------}|')
print('|if you have any problems or questions, then write here (Herman Garsky#2574). When publishing a question / problem, describe in detail with attaching screenshots. good using :-) |')
while True:
  choose = int(input('num type: '))
  if choose == 1:
    print('copy the path and file name. the script only reads the txt file!!!!')
    ff = input()
    print(PIXELATION(ff))
  elif choose == 2:
    print('take the encoded apg with dimension (n * 2). You need to paste below the full address with her name')
    ff = input()
    print(UNPIXELATION(ff))
