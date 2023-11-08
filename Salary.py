Per_Hour = int(input("How much do you get paid per hour?"))
Hours = int (input("How many hours did you work?"))
def Salary (Per_Hour, Hours):
    if Hours > 220 :
       return "Saat kar bish az 220 nemitavanad bashad")
    else :
        Total_incom = Hours * Per_Hour
        return Total_incom
print ( Salary (Per_Hour, Hours))
