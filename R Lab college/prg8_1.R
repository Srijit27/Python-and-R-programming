n<-as.numeric(readline("Enter a number:"))
fact<-function(n){
  f=1
  while(n!=1){
    f=f*n
    n=n-1
  }
  return(f)
}
cat("Factorial is:",fact(n))
