n<-as.numeric(readline("Enter the value of n:"))
fibo<-function(n){
  a=0
  b=1
  cat(a," ")
  cat(b," ")
  for(i in 2:(n-1)){
    t=a+b
    cat(t," ")
    a=b
    b=t
  }
}
cat("Fibonacci series is:-\n")
fibo(n)