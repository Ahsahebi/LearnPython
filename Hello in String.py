Hello = input()
if "h" in Hello:
    h = Hello.find("h")
    Hello = Hello[h:]
else : 
    print("NO")
if "e" in Hello:
    e = Hello.find("e")
    Hello = Hello[e:]
else : 
    print("NO")    
if "l" in Hello:
    l = Hello.find("l")
    Hello = Hello[l:]
else : 
    print("NO")    
if "l" in Hello:
    L = Hello.find("l")
    Hello = Hello[L:]
else : 
    print("NO")    
if "o" in Hello:
    o = Hello.find("o")
    print ("YES")
else : 
    print("NO")    
