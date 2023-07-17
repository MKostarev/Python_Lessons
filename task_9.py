#поиск слов с числами через списковые включения
#ввод: sfd4 $sdf sdf44 sdf5 !sfs #qwe
#результат: sfd4 sdf44 sdf5

string = "sfd4 $sdf sdf44 sdf5 !sfs #qwe"
string = " ".join(string.split()) #работает и без этого
b = string.split(" ")

words = [str(i) for i in b if i.isalnum() == True]

words = " ".join(words)
print(words)