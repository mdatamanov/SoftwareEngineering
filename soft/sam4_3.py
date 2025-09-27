str = input('Введите строку: ').lower()
print('Длина предложения: ', len(str))
print('Предложение в нижнем регистре: ',str.lower())
print('Количество гласных: ',
      str.count('a')+
      str.count('e')+
      str.count('i')+
      str.count('o')+
      str.count('u'))
str = str.replace('ugly','beauty')
print('Предложение начинается на "The": ',str.startswith('the'))
print("Предложение заканчивается на 'end': ",str.endswith('end'))
print('Предложение после изменений: ',str)