import random as rm

words = ["Apple", "Banana", "Umbrela", "Smartphon"]

word= rm.choice(words).upper()

das = "-"*len(word)

print(das)
chance = 7

while chance != 0:
    letter = input("Enter Your Words ").upper()

    if letter in word:
        for index in  range(len(word)):
            if word[index] == letter:
                das = das[:index]+word[index]+das[index+1:]
                print(das)
        if das == word:
         print("Congratulation You Win")
         break
    else:
      chance-=1
      print("Wrong Word\nyou have only ",chance, "chances")
else:
    print("Game Over\nyour Chances is ",chance,"\n",word)