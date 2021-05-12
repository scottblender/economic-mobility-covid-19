# Economic Mobility During COVID-19
Project Summary: Using human-centered mobility to gain insights into local and national economic recovery. 

# Project Overview:
Over the past few months, Dr. Webber and I have been working on a CARAS project investigating economic recovery using human-centered mobility data. The project idea originated from research I did last summer, utilizing human-centered mobility data in tandem with land-use data to investigate which types of regions people traveled to most frequently during the initial period of the COVID-19 pandemic. Extending off of this study, Dr. Webber and I decided to explore the economic consequences and effects related to mobility since traditional economic indicators provide fallible insights when looking into local or county-level trends on a daily basis. Since the pandemic presented a rapid shock to the economy, observing economic trends on a daily frequency and localized aggregate helps to provide a more granular picture into trends and insights occurring not just nationally, but regionally as well. Since mobility has direct implications and relations to policy as well, this study provides a framework for future extensions into policy analysis and implications. 

# What I’ve Learned:
Due to preparation for presentations and the large coding component of this project, I have developed the following skills: 
1. How to scrape data with R
2. Public speaking and presentation skills
3. Python data analysis and exploration using pandas and matplotlib
4. kNN and Frisch-Waugh-Lovell 
5. How to conduct a literature review 
6. How to write for scientific and academic purposes 
7. Basic econometrics
8. Basic LaTeX and Markdown

# Project Accomplishments:
Since inception, I have presented our work to a few notable places including:
1. NSF Student Conference
2. University of Wisconsin-Madison Data Bazaar 
3. Temple Undergraduate Research Symposium

As we continue to work on our methods and report, the end goal is to produce a working paper reporting our findings and research. 

# Methodology:
For this project, Dr. Webber and I utilized a key theorem in econometrics, Frisch-Waugh-Lovell, to analyze trends and datasets. Frisch-Waugh-Lovell allowed us to compare residuals of our time-series variables and control for time, considering time-scales were implicative of influencing results. 

In order to compare pre-COVID mobility to present mobility, data from the US Social Mobility Index project (https://www.jmir.org/2020/12/e21499/) was used as data up to a year prior is available. Indices are computed on comparable grounds for comparison. 

Data was cleaned and is currently being analyzed to understand trends between mobility and cases for specific regions, mobility and GDP, mobility and air quality index, and mobility and labor force trends. In order to fill NaN values, kNN imputation is being used to compute these missing values. Data for specific counties only ranges from February 15th, 2020 to December 31st, 2021, so certain analysis is limited for county-level analysis. National, state, and some counties have data that has been regularly updated since February 15th, 2020, and these regions are being used for further analysis. Logistic and linear regressions relating residuals of mobility to residuals of other variables of interest are the primary visualizations being worked on for this project. 

In order to account for variances in regional comparisons, inspiration from this paper was utilized( https://www.nature.com/articles/s41467-017-02064-4). Regions are being grouped by seasonality and major holidays are removed from analysis to provide more accurate results.

Most analysis was done using Python 3.7 and Jupyter Notebooks. Relevant libraries including pandas, matplotlib, and seaborn were used. 

# Data Sources:
US Social Mobility Index
Google Community Mobility Reports
Bureau of Labor Statistics 
EPA Air Quality Index
Johns Hopkins CSSE COVID-19 Case Statistics

# Future Plans:
After meeting with Dr. Webber yesterday, we plan to continue to work on this project over the summer. After producing a comprehensive Jupyter notebook with all analysis and information centralized, we will then determine the feasibility of transitioning this data analysis into a working paper. Updates and visualizations will be posted periodically to this repository: https://github.com/scottblender/economic-mobility-covid-19. 
