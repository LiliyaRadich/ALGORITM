word = input('введите слово на русском или английском языке: ').upper()
print(word)
english = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JZ', 10:'QZ'}
print(sum([k for i in word for k, v in english.items() if i in v]))