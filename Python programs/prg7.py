secs=(int)(input("Enter the no of seconds:"))
hours=secs//3600
mins=(secs%3600)//60
secs=(secs%3600)%60
print("Conversion:",hours,"hours",mins,"mins",secs,"secs")