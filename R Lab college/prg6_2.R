a<-as.numeric(readline("Enter 1st no:"))
b<-as.numeric(readline("Enter 2nd no:"))
gcd<-function(a,b){
  if(b==0){
    return(a)
  }else{
    return(gcd(b,a%%b))
  }
}
cat("GCD value is:",gcd(a,b))