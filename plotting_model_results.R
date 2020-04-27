library(tidyverse)
library(ggplot2)

# Read in all datasets
new_mt_data = read.csv("model_test_data/new_mt_data.csv")
new_mtr_data = read.csv("model_test_data/new_mtr_data.csv")

org_mt_data = read.csv("model_test_data/org_mt_data.csv")
org_mtr_data = read.csv("model_test_data/org_mtr_data.csv")

plot_solve_acc <- function(omt, omtr, nmt, nmtr){
    
  par(mfrow = c(2,2)) # Create 2x2 grid of plots
  
  barplot( omt$solve_prop ~ omt$rotations, col = "steelblue", xlab = "Number of Rotations", ylab = "Proportion Solved", main = "oboorg1.model on model_test")
  
  barplot(omtr$solve_prop ~ omtr$rotations, col = "springgreen", xlab = "Number of Rotations", ylab = "Proportion Solved", main = "oboorg1.model on model_test_random")

  barplot(nmt$solve_prop ~ nmt$rotations, col = "plum", xlab = "Number of Rotations", ylab = "Proportion Solved", main = "obonew1.model on model_test")
  
  barplot(nmtr$solve_prop ~ nmtr$rotations, col = "navy", xlab = "Number of Rotations", ylab = "Proportion Solved", main = "obonew1.model on model_test_random")
  
}

psa_together <- function(omt, omtr, nmt, nmtr){
  tog = table(omt$solve_prop, omtr$solve_prop, nmt$solve_prop, nmtr$solve_prop)
  
  barplot(tog, main = "Accuracies of ML models", xlab = "Number of Rotations", ylab = "Proportion Solved", beside = TRUE, col = c("green", "red", "navy", "purple"))
  
}

psa_together(omt = org_mt_data, omtr = org_mtr_data, nmt = new_mt_data, nmtr = new_mtr_data) 

plot_solve_acc(omt = org_mt_data, omtr = org_mtr_data, nmt = new_mt_data, nmtr = new_mtr_data)

