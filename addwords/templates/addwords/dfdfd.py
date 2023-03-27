word = '10.124.56.220'.split('.')


#print(f'{int(word[0], 2)}.{int(word[1], 2)}.{int(word[2], 2)}.{int(word[3], 2)}')
print(f'{bin(int(word[0]))[2:]}.{bin(int(word[1]))[2:]}.{bin(int(word[2]))[2:]}.{bin(int(word[3]))[2:]}')