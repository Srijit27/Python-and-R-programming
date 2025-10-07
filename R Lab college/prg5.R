a=as.numeric(readline("Enter the co-eddicient of x^2:"))
b=as.numeric(readline("Enter the co-efficient of x:"))
c=as.numeric(readline("Enter the constant:"))
det=b**2-(4*a*c)
if(det==0){
  cat("Roots are real and equal\n")
  cat("Root 1:",-b/2*a,"\n")
  cat("Root 2:",-b/2*a)
}else if(det>0){
  cat("Roots are real and distinct\n")
  cat("Root 1:",(-b/(2*a))+sqrt(det)/(2*a),"\n")
  cat("Root 2:",(-b/(2*a))-sqrt(det)/(2*a))
}else{
  cat("Roots are complex conjugates of each other\n")
  cat("Root 1:",(-b/(2*a)),"+",(sqrt(det*(-1))/(2*a)),"i","\n")
  cat("Root 2:",(-b/(2*a)),"-",(sqrt(det*(-1))/(2*a)),"i")
}