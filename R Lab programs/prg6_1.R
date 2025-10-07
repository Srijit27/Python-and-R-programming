a<-as.numeric(readline("Enter 1st no:"))
b<-as.numeric(readline("Enter 2nd no:"))
gcd<-function(a,b){
  while(b!=0){
    t=b
    b=a%%b
    a=t
  }
  return (a)
}
cat("GCD value is:",gcd(a,b))