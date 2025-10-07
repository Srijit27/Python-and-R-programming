age=as.numeric(readline("Enter the age:"))
if(age>=18 && age<=90){
  cat("Eligible to vote")
}else if(age<18){
  cat("Person can vote after",18-age," years")
}else{
  cat("Enter a valid age again..!!")
}