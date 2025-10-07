n<-as.numeric(readline("Enter a number:"))
fact<-function(n){
  if(n==1){
    return(1)
  }else{
    return(n*fact(n-1))
  }
}
cat("Factorial is:",fact(n))