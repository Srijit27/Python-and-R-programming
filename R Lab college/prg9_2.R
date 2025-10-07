n<-as.numeric(readline("Enter the value of n:"))
fibo<-function(n){
  if(n==0){
    return(0)
  }else if(n==1){
    return(1)
  }else{
    return(fibo(n-1)+fibo(n-2))
  }
}
cat("Fibonacci series is:-\n")
for(i in 0:(n-1)){
  cat(fibo(i)," ")
}