library(survival)
kaplan <- read.csv("C:/Project/statiqueProject/Results/R3/new/phpunit/Results_Commits.csv", col.names=c("Time","Died","Group"), row.names=NULL)

km<-survfit(Surv(kaplan$Time, kaplan$Died) ~ as.factor(kaplan$Group))


quantile(km, c(0.25, 0.5, 0.75))$quantile



plot(km, col =c(1,2,3,4,5,6,7,8),xlab="#Commits ", ylab="Probabilité de survivabilité par commit ")

# Add a legend
legend("topright", 
       legend = c("HMC", "ECL","EML","EPL","HNPC", "HC","ECB","EDOI"), 
       col = c(1,2,3,4,5,6,7,8,"grey"),
       lty=1,
       text.col = "black", 
       cex = 1, 
       inset = c(0.01, 0.01))    

