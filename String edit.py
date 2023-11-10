String = input()
String=String.lower()
for i in range(0,len(String)):
    if String[i] == "a" or String[i] == "e"  or String[i] == "i" or String[i] == "o" or String[i] == "u":
        String = String[:i]+"."+String[i+1:]
String = String.replace(".","")
Str_final =""
for j in range (0,len(String)):
    Str_final = "." + String[j]+ Str_final
print (Str_final)