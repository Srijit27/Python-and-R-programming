create<-function(vtype,vlen){
  val<-vector(vtype,vlen)
  for(i in 1:vlen){
    x<-readline(prompt=paste("Enter the value",i,":"))
    if(vtype=="numeric"){
      val[i]<-as.numeric(x)
    }
    else if(vtype=="complex"){
      val[i]<-as.complex(x)
    }
    else if(vtype=="character"){
      val[i]<-as.character(x)
    }
    else if(vtype=="logical"){
      val[i]<-as.logical(x)
    }
  }
  return(val)
}
n<-create("numeric",6)
c<-create("complex",6)
ch<-create("character",6)
l<-create("logical",6)
cat("Numeric vector is:",n,"\n")
cat("Complex vector is:",c,"\n")
cat("Character vector is:",ch,"\n")
cat("Logical vector is:",l,"\n")