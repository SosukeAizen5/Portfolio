```{r}
# 2014 American Community Survey Dataset Assignment
# DSC 520
# Week 3
# Statistics for Data Science Assignment Week 3
# David Berberena
# 12/17/2023

# Assignment Start

"I. List the name of each field and what you believe the data type and intent is
of the data included in each field (Example: Id - Data Type: varchar 
(contains text and numbers) Intent: unique identifier for each row)"

## 1. Id - Data Type: character (chr) Intent: unique identifier for each row 
## using a consistent number of both letters and numbers

## 2. Id2 - Data Type: double (dbl) Intent: unique identifier for each row using
## only numbers

## 3. Geography - Data Type: chr Intent: states the individual city and state of
## each data point 

## 4. PopGroupID - Data Type: dbl Intent: show that all data points are measured
## on the same scale for credibility

## 5. 'POPGROUP.display-label' - Data Type: chr Intent: identify the scale on
## which all data points are measured

## 6. RacesReported - Data Type: dbl Intent: displays results of the scale being
## measured (the total population of each city/state pair within the dataset)

## 7. HSDegree - Data Type: dbl Intent: shows the percentage of people within
## the total population of each data point who attained a high school diploma

## 8. BachDegree - Data Type: dbl Intent: shows the percentage of people within
## the total population of each data point who went on to attain a bachelor's 
## degree

"II. Run the following functions and provide the results: str(); nrow(); ncol()"

str(week_3_dataset)

## spc_tbl_ [136 × 8] (S3: spec_tbl_df/tbl_df/tbl/data.frame)
## $ Id                    : chr [1:136] "0500000US01073" "0500000US04013" "0500000US04019" "0500000US06001" ...
## $ Id2                   : num [1:136] 1073 4013 4019 6001 6013 ...
## $ Geography             : chr [1:136] "Jefferson County, Alabama" "Maricopa County, Arizona" "Pima County, Arizona" "Alameda County, California" ...
## $ PopGroupID            : num [1:136] 1 1 1 1 1 1 1 1 1 1 ...
## $ POPGROUP.display-label: chr [1:136] "Total population" "Total population" "Total population" "Total population" ...
## $ RacesReported         : num [1:136] 660793 4087191 1004516 1610921 1111339 ...
## $ HSDegree              : num [1:136] 89.1 86.8 88 86.9 88.8 73.6 74.5 77.5 84.6 80.6 ...
## $ BachDegree            : num [1:136] 30.5 30.2 30.8 42.8 39.7 19.7 15.4 30.3 38 20.7 ...
## - attr(*, "spec")=
##   .. cols(
##     ..   Id = col_character(),
##     ..   Id2 = col_double(),
##     ..   Geography = col_character(),
##     ..   PopGroupID = col_double(),
##     ..   `POPGROUP.display-label` = col_character(),
##     ..   RacesReported = col_double(),
##     ..   HSDegree = col_double(),
##     ..   BachDegree = col_double()
##     .. )
## - attr(*, "problems")=<externalptr> 

nrow(week_3_dataset)

## [1] 136

ncol(week_3_dataset)

## [1] 8

"III. Create a Histogram of the HSDegree variable using the ggplot2 package.
1. Set a bin size for the Histogram that you think best visuals the data 
(the bin size will determine how many bars display and how wide they are)
2. Include a Title and appropriate X/Y axis labels on your Histogram Plot."

library(ggplot2)

ggplot(week_3_dataset, aes(x = HSDegree)) +
geom_histogram(binwidth = 2, fill = "green", color = "black") +
labs(title = "Histogram of High School Degree Percentages", 
x = "Percentage of Total Population to Attain a High School Degree", 
y = "Number of Counties")

"IV. Answer the following questions based on the Histogram produced:"

"1. Based on what you see in this histogram, is the data distribution unimodal?"

## Yes, there is one singular peak in the histogram

"2. Is it approximately symmetrical?"

## The histogram can be interpreted both ways: yes it can be considered
## approximately symmetrical if symmetry is judged based on the location of the 
## mode, and no it could be considered not symmetrical if symmetry is judged 
## from the middle of the entire histogram as many data points lie towards the
## right of the histogram

"3. Is it approximately bell-shaped?"

## Yes

"4. Is it approximately normal?"

## No 

"5. If not normal, is the distribution skewed? If so, in which direction?"

## The data distribution is negatively skewed, meaning that the skew appears on
## the left-hand side of the histogram

"6. Include a normal curve to the Histogram that you plotted."

histogram_part_2_week_3 <- readPNG("HSDegree_HistNorm.png")
grid::grid.raster(histogram_part_2_week_3)

"7. Explain whether a normal distribution can accurately be used as a model 
for this data."

## A normal distribution cannot be used as a model for this data as the curve 
## shown does not display the data in such a way that is easily discernible or
## even telltale of a normal distribution

"V. Create a Probability Plot of the HSDegree variable."

## Not certain whether the phrase "probability plot" refers to a probability 
## density plot or a q-q plot, so I will include both for this question

## Probability Density Plot

ggplot(week_3_dataset, aes(x = HSDegree)) + geom_density(fill = "green", 
color = "black") + labs(title = "Probability Density of High School Degree 
Percentages", x = "Percentage of Total Population to Attain a High School 
Degree", y = "Probability of Counties")

## Q-Q Plot

ggplot(week_3_dataset, aes(sample = HSDegree)) +
geom_qq()

"VI. Answer the following questions based on the Probability Plot:"

"1. Based on what you see in this probability plot, is the distribution 
approximately normal? Explain how you know."

## For the probability density plot, the distribution is not normal. This is 
## true because the data points are bunched up on one side of the plot with 
## uneven looking tails

## For the q-q plot, the distribution is indeed normal. This is because the data
## points derived from both quantiles form a relatively straight line

"2. If not normal, is the distribution skewed? If so, in which direction? 
Explain how you know."

## For the probability density plot, the data distribution is negatively skewed,
## meaning that the skew appears on the left-hand side of the density plot. This
## results in the plot having very few data points at the left of the plot and 
## almost all of the data points being on the right side of the plot, including
## the unimodal peak with a steep decline in the curve beyond the mode

## For the q-q plot, the distribution is normal, therefore the data isn't skewed

"VII. Now that you have looked at this data visually for normality, you will now
quantify normality with numbers using the stat.desc() function. 
Include a screen capture of the results produced."

library(pastecs)

stat.desc(week_3_dataset)

"VIII. In several sentences provide an explanation of the result produced for 
skew, kurtosis, and z-scores. In addition, explain how a change in the sample 
size may change your explanation?"

## An explanation as to why the data was negatively skewed in such a way could
## be that the the United States' federal school system is compulsory, leading 
## most all students to achieve a high school diploma barring unusual events. 
## Looking at the histogram, the data points do not begin until a county has 
## had around 60% of their population attain a high school diploma. This 
## phenomenon also explains the fat tails of the distribution, which spell out a
## leptokurtic distribution. The large tail present in this plotted data allowed
## the viewer to see that even 60% of a county's population achieving a high 
## school diploma is an outlier. In regards to z-scores, the data may look 
## skewed currently, yet z-score transformation places this dataset as more 
## normally distributed when computed to a +3/-3 set of data points. 

## Should a change in the sample size occur, I do not believe the skewness or 
## kurtosis would regulate to show any major difference due to the nature of the
## dataset and what it means for county schools and citizens. With regards to 
## z-scores, more data points would simply make the transformed dataset appear
## to be even more normally distributed since the skewness and kurtosis would 
## not dramatically change even given a mass influx of new data points.