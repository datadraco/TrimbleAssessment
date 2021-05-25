# Trimble Data Science Assessment

This repository was completed as an assigned exercise for an internship application at Trimble Inc.

---

## Question 1A

Admittedly I do not have any experience with SQL so I was unable to answer this question, but I am currently looking into ways of learning the language such as coding academy.

---

## Question 2

Through the use of the `describe()` function we can see that there are 10000 observations, a mean of roughly 23, a standard deviation of roughly 3, and we can also see that the quantile values are 11.2, 21, 23, 25, and 33.2 respectively. Through the Central Limit Theorem this distribution can be described as normal, and we would be able to further evaluate the distribution of the data in a histogram plot (my seaborn package was not operating for some reason at the time of writing this). 50% of the data lies between 21 and 25, so the mass majority of the statistics are densely populated around the mean and there are balanced outliers on both ends of the spectrum, which is reflected by the nearly identical values of the median (23.02) and the mean (23.03). Further statistical analysis could be done through the use of z-scores and normal approximations.

---

## Question 3

In the event that I needed to impute null values in a massive file, I feel like that the strategy would be a bit contextual to the actual data itself but I know that I would not remove the values. I would either replace them with a test statistic such as the mean or median (depending on the distribution/characteristics of the data) or ideally I would somehow write a program to predict what values would replace the nulls through a model of some sort.

---

## Question 4

If I was asked to complete the previously discussed task every week, then I would definitely attempt to create the model that I proposed at the end of my previous answer as that model could hopefully be slightly adjusted and adapted to any given data set depending on the features and where the null values are located. That tactic would most likely be more efficient and produce better results than force feeding sample statistics into each null value of any given data set.

---

## Question 5

Last quarter for a data science course I read a book titled _Data Feminism_ by Catherine D'Ignazio and Lauren F. Klein and I thoroughly enjoyed their perspective and take on data science as a practice, so I would definitely consider those two individuals as some of my favorites.

I also became aware of Freeman Dyson when he passed away a little over a year ago, and through some brief online research and light reading I've come to really enjoy his perspective and philosophy on math and the universe as a whole. 
