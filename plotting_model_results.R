library(tidyverse)
library(ggplot2)

# Read in all datasets
new_mt_data = read.csv("model_test_data/new_mt_data.csv")
new_mtr_data = read.csv("model_test_data/new_mtr_data.csv")

org_mt_data = read.csv("model_test_data/org_mt_data.csv")
org_mtr_data = read.csv("model_test_data/org_mtr_data.csv")

plot_solve_acc <- function(omt, omtr, nmt, nmtr){
    
  par(mfrow = c(2,2)) # Create 2x2 grid of plots
  
  plot( omt$solve_prop ~ omt$rotations, col = "steelblue", xlab = "Number of Rotations", ylab = "Proportion Solved", main = "oboorg1.model on model_test")
  
  plot(omtr$solve_prop ~ omtr$rotations, col = "springgreen", xlab = "Number of Rotations", ylab = "Proportion Solved", main = "oboorg1.model on model_test_random")

  plot(nmt$solve_prop ~ nmt$rotations, col = "plum", xlab = "Number of Rotations", ylab = "Proportion Solved", main = "obonew1.model on model_test")
  
  plot(nmtr$solve_prop ~ nmtr$rotations, col = "navy", xlab = "Number of Rotations", ylab = "Proportion Solved", main = "obonew1.model on model_test_random")
  
}

psa_together <- function(omt, omtr, nmt, nmtr){
    
  #par(mfrow = c(2,2)) # Create 2x2 grid of plots
    
  plot( omt$solve_prop ~ omt$rotations, type = 'l', col = "blue", xlab = "Number of Rotations", ylab = "Proportion Solved", main = "Models on Regular vs. Random Tester")
    
  lines(omtr$solve_prop, col = "darkgreen", xlab = "Number of Rotations", ylab = "Proportion Solved", main = "oboorg1.model on model_test_random")
    
  lines(nmt$solve_prop, col = "red", xlab = "Number of Rotations", ylab = "Proportion Solved", main = "obonew1.model on model_test")
    
  lines(nmtr$solve_prop, col = "pink", xlab = "Number of Rotations", ylab = "Proportion Solved", main = "obonew1.model on model_test_random")
  
  legend("topright", cex = 0.8, title = "Legend",legend = c("org regular", "org random", "new regular", "new random"), col = c("blue", "darkgreen", "red", "pink"), lty = c(1,1,1,1),ncol = 1)
}

psa_together(omt = org_mt_data, omtr = org_mtr_data, nmt = new_mt_data, nmtr = new_mtr_data) 

plot_solve_acc(omt = org_mt_data, omtr = org_mtr_data, nmt = new_mt_data, nmtr = new_mtr_data)

