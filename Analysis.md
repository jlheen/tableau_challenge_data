# Analysis Overview
There were four questions I set out to answer, as follows:

*Question 1*
Create a static map comparing the bike stations to see how the stations compare as starting points versus end destination stations.

*Question 2*
How do trips vary by customers (defined as a 24-hour or 3-day pass user) versus subscribers (defined by an annual subscription user)?
Note that this data was compiled using April 2019 to April 2020 data. 

*Question 3*
What are the peak *days* the bikes are used in those summer and winter months? 
This was not by the day of the week but rather the calendar day.

*Question 4* 
What are the peak *hours* in the summer and winter months?
Note that I defined these months as June, July, and August of 2017, 2018, & 2019 for the summer and January, February, and March of those same years for the winter (I believed that using a prime holiday month like December might skew the data if there were extraordinary bike trips for holiday visitors or shopping trips).


# Findings

*Question 1*
According to the Tableau maps themselves and a comparison bar chart, there were few significantly different stations when it came to starting versus ending stations. There were definitely stations that appeared to be in zip codes that had higher traffic overall for both. If I were to do further analysis, I would create a more formal hypothesis and set a threshold for what would be considered statistically signficant. If I were to continue with the data I had, however, I believe I would continue marketing heavily in those stations where there is already high traffic and do some further analysis on the bike ids that were used in those parts of town to make sure the wear and tear was not too significant. Otherwise, we could start cycling out (cycle, yeah?) the bikes that are in more high traffic areas with the lower traffic stations to ensure that we are mainting reliable bikes.

*Question 2*
The amount of trips taken by customers and subscribers are highest in the summer months, which I would not say I was surprised by - you can't beat the weather here in New York City in June! What I was not expecting was to see such long trips taken by our customers during the winter. Rides appear to be longer in the winter months, even by annual subscribers. By and large, however, subscribers seem to stay on the bikes for as short of a time as they can and keep their trips quick. If I were to do further analysis, I would see what our revenues are compared between these two groups overall. It would seem that we are thriving in both markets, but I would want to know how we can continue to keep both types of customers happy and investigate if there are certain incentives we are missing for either group. 

*Question 3*
Although I am a morning person, I would not have expected there to be such a high amount of riders so early in the morning! I was reminded by a colleague that these are prime night-life hours. There is another peak at around 8 PM, as well, especially in August. What I was especially surprised by is that this was for both summer and winter! If I were to do further analysis, I would mine the data further and try to compress out some of the existing outliers to get a more exact picture of median ride times, rather than overall averages. If I were to advise our staff with what we see here, I would definitely press for good staffing during the night hours -- we want our riders to stay safe! 

*Question 4* 
The days of the month did not yield any significant findings just by looking at the line charts. I would like to use some calendar data and identify what days of the week these days fell on. It was good to get a glimpse of how much time our riders spent on the bike, but I would like to see this mapped out more by how this peaked and dipped depending on where it fell in the week.

# Thank You!
Thank you for your time! I hope you like looking at, clicking on, and zooming over this Tableau Viz set. Please let me know what further questions YOU would like answered from the data I've collected -- and what you'd still like to see me collect and investigate!!



# Here is some further background on this data set. 

# Background

![Citi-Bikes](Images/citi-bike-station-bikes.jpg)

Congratulations on your new job! As the new lead analyst for the [New York Citi Bike](https://en.wikipedia.org/wiki/Citi_Bike) Program, you are now responsible for overseeing the largest bike sharing program in the United States. In your new role, you will be expected to generate regular reports for city officials looking to publicize and improve the city program.

Since 2013, the Citi Bike Program has implemented a robust infrastructure for collecting data on the program's utilization. Through the team's efforts, each month bike data is collected, organized, and made public on the [Citi Bike Data](https://www.citibikenyc.com/system-data) webpage.

However, while the data has been regularly updated, the team has yet to implement a dashboard or sophisticated reporting process. City officials have a number of questions on the program, so your first task on the job is to build a set of data reports to provide the answers.