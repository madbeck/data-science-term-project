# data-science-term-project
read details at: https://medium.com/fighting-for-food-security/blog-post-3-c5e8f747e0d1

## Vision
Our project aims to explore the intersection between food access, health, and economic disparity in Los Angeles county. As the following two graphs show, there is a clear link between household income and obesity. Using these graphs as a starting point, we explore how food plays into this equation.


Median household income in LA County (left). Body mass index in LA County (right).

Our goal is to better understand the extent to which access to healthy food plays a role in income and health in LA. Existing studies argue that food access is a crucial determinant for neighborhood health, evidenced by high rates of obesity and diabetes in areas with minimal healthy food access.We decided to focus on Los Angeles because it has the highest number of fast food restaurants per capita in the United States, and despite mass produce production in surrounding areas is considered a “food dessert” for low income communities, meaning they lack access to healthy and nutritious options.

We hypothesized that supermarket and fast food access for a given neighborhood are inversely related (i.e., the more supermarkets, the less fast food restaurants) and that the number of supermarkets is directly correlated to income. We believe that this should explain above average rates of obesity in low income neighborhoods that lack access to healthy food options. 

## Data Collection
SimplyAnalytics: To construct our dataset on health and wealth in LA, we initially gathered data from different websites, joining them with zip code as the primary key. However, we later discovered the website SimplyAnalytics.com, which allowed us to generate a CSV file with all of our desired fields: employment, income, obesity and diabetes data, grouped by zip code.

Google Maps API: As SimplyAnalytics.com did not offer data on fast food restaurants and supermarkets at specific geographical locations, we generated a second dataset using the Google Maps Places API. For this, we scraped coordinates approximating the centers of each of the zip codes in Los Angeles county to retrieve the numbers of supermarkets and fast food restaurants within a 1km and 3km radius. A table with this data and a table with the data above comprised our SQL Database.

Challenges with Data Collection: Data collection served as the most challenging aspect of this project. We found it hard to find a consistent concept of “neighborhoods,” as different datasets were grouped by different location indicators (i.e geoIDs, census tracts, county districts, and zip codes). We ultimately chose to represent neighborhoods by zip codes, since this was the most manageable and consistent metric. To determine “centers” of each zip code, we scraped latitude and longitudes from a website that correspond to zip code centers. We recognize, however, that this may have resulted in overlapping information between zip codes and/or data that is not representative of all communities living in one zip code.

##Visualizations/Algorithms:
Visualizing our data on food access (generated from the Google Maps API) was initially challenging. SimplyAnalytics (where we found our health and economic data for LA), provides a nice way to visualize their data on maps of LA, but we were unable to use the site to plot our own data as zip code densities. Instead, we used ArcGIS, a mapping software that gives you more flexibility to do this. This allowed us to look at where in LA we see the highest numbers of fast food restaurants and supermarkets. An initial analysis of this “density-map” of LA showed that the center of LA had both higher numbers of supermarkets and fast food restaurants. Keep in mind from the graphs above, the areas in the center of the county tend to have lower incomes and higher rates of obesity.

In addition to visualizing supermarket and fast food density, we used a KMeans clustering algorithm and a Logistic Regression algorithm to determine the significance of our food access data. KMeans was used to cluster the data on unemployment, income, obesity, and diabetes, as well as all of the food access data. Using ArcGIS to visualize these clusters, we saw the following:


Regression was used to test how well income predicted the number of fast food restaurants vs. supermarkets. We found that in general, as income increased the overall number of establishments (both fast food chains and supermarkets) decreased. This may be a factor of land in wealthier neighborhoods being both more expensive and more spread out.



We also used a linear regression to examine how well the number of fast food restaurants and supermarkets predicted health. We found that while the number of fast food restaurants within 3km of a neighborhood seemed to be an strong indicator of health, the number of supermarkets within the same radius was a not statistically significant indicator of health.


##Main Takeaways
Overall, we found that the number of fast food restaurants directly relates to both income and obesity, while unemployment, diabetes, and number of supermarkets require further study. In other words, more fast food restaurants in lower income neighborhoods often mean higher rates of obesity. 

What is most unexpected is the finding that the prevalence of supermarkets is not a meaningful indicator of either income or health. We found a high number of supermarkets in low income areas which implies that simply having access to supermarkets does not lead to a healthier lifestyle. There may be many other factors at play, such as prices, food preference, and convenience.

##Moving Forward
Though we found a high number of supermarkets in low income neighborhoods, we don’t have a concept of who frequents them and how much money they spend and need to better understand this to truly and effectively combat obesity. We know there is a strong relationship between income and obesity so, as we move forward, it will be important to look more into the details of both supermarkets and fast food restaurants to examine what’s actually being bought and what the revenue generated by each looks like. Are people frequenting supermarkets as often as fast food chains? If so, what are they actually buying? Healthy produce or equally unhealthy packaged foods? It’s possible that supermarkets are visited less often than fast food restaurants (due to price points or convenience). It’s also possible that the loose term “supermarket” includes corner stores that lack healthy options. The Google Maps API didn’t have a very strict definition of what a supermarket is and several studies show that many of the “bodegas” in LA tend to only keep packaged and unhealthy foods because that’s what sells best. Those studies found that produce, if kept in stock at all, tended to be in the back and of questionable quality. If either of these are the case, then we’d have a better starting point for understanding how to combat obesity. Clearly putting establishments there isn’t enough to provide access to healthy foods, other barriers are in place that are keeping low income communities from accessing nutritious options.


