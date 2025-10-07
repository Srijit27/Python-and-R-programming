gcd<-function(a,b){
  if(b==0){
    return(a)
  }else{
    return(gcd(b,a%%b))
  }
}
gcdn<-function(l){
  n<-gcd(l[1],l[2])
  for(i in 2:length(l)){
    n<-gcd(n,l[i])
  }
  return(n)
}
l<-c(39,91,104,143)
cat("GCD value is:",gcdn(l))