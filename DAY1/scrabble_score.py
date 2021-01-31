# Create a dictionary of letters along with their corresponding point values
points={"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":2,"K":5,"L":1,"M":3,
          "N":1,"O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,"V":4,"W":4,"X":8,"Y":4,"Z":10}
# Prompt the user for a word
word =input("Enter a word:")
word=word.upper()
score: int=0
for letter in word:
    score = score + points[letter]
print(word,"is worth",score,"points")
