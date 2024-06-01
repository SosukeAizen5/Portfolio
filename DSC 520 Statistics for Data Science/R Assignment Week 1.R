# Intro to R Assignment
# DSC 520
# Week 1
# Statistics for Data Science Assignment Week 1
# David Berberena
# 12/3/2023

# Assignment Start

"Create function to print the Task 4 scenario and questions along with the 
desired answers to those questions."

task_4 <- function() {
  
  print("Task 4: Say I own 857 CDs. My friend has written a computer program that uses a webcam to scan the shelves in my house where I keep my CDs and measure how many I have. His program says that I have 863 CDs. Define measurement error. What is the measurement error in my friend’s CD-counting device?")
    print("Measurement error is the discrepancy between what is known to be true concerning the value of an entity being measured and the true value of that entity actually being measured in real time.")
}
  
# task_4 function must be called for it to run
  
task_4()

# Create function to display the shape of a normal distribution
# This function will use the dnorm() built-in function for distributions
# seq() built-in function will define the parameters of the distributions
# plot() built-in function will be used to sketch the shape of the distributions

task_5_norm_dist <- function() {
  
  # length.out is a keyword that sets the total number of values present
  x <- seq(-3, 3, length.out = 100)
  # standardized values for mean and standard deviation to create the plot 
  y <- dnorm(x, mean = 0, sd = 1)
  
  # Create a plot of the normal distribution using x and y as parameters
  # type is included as a parameter so R knows to draw a line or "l"
  plot(x, y, type = "l")
}

task_5_norm_dist()


# Create function to print the Task 5 instructions and answers

task_5 <- function() {
  
  print("Task 5: Sketch the shape of a normal distribution, a positively skewed distribution and a negatively skewed distribution.")
  task_5_norm_dist()
}

task_5()
