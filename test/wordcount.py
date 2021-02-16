sentence = input("문장을 입력해주세요. ") 
new_sentence= sentence.split(' ')
print(new_sentence)

a ={}

for word in new_sentence : 
    if word in a : 
        a[word] += 1 
    else :
        a[word] = 1  

print("당신이 입력한 문장은 '%s' 이며, " % (sentence))
print("문장 안의 단어 수는 '%d'개 이다. " % (len(new_sentence)))

for num in a : 
    print ("'%s' : '%d' 번" % (num, a[num]))