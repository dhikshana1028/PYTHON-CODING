from googletrans import Translator
x=Translator()
text1=input("enter any sentence : ")
text2=input("enter target language : ")
res=x.translate(text1,dest=text2)
print("the original :",text1)
print("Translated sentence :",res)