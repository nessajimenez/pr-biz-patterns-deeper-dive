
# Puerto Rico Business Establishment (2013-2022): A deeper dive
A deeper dive into Puerto Rico business establishment patterns from 2013 to 2022 by Vanessa Jimenez based on the original analysis by Vanessa Jimenez and Danielle Steede.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Data](#data)
3. [Methodology](#methodology)
4. [Results](#results)
5. [Project Structure](#project-structure)
6. [Challenges and Limitations](#challenges-and-limitations)
7. [Further Questions](#further-questions)
8. [Contributions](#contributions)


## Project Overview
This project delves into a decade of census data to uncover the shifting landscape of business establishments across Puerto Rico from 2013 to 2022. Moving beyond the broad island-wide analysis of the first phase, this study zeroes in on the differences between regions and towns, exploring the unique factors that shape each area's business environment. By honing in on these local nuances, I aim to illuminate the impact of significant events like Hurricane Maria and the Covid-19 pandemic, revealing how these challenges have reshaped business trends and patterns across the island.

To achieve this, I conducted a comparison of graphs representing various industries by region and town. Through these visualizations, I identified key trends and shifts in business establishments over time. I then cross-referenced these trends with major events—specifically, Hurricane Maria in 2017 and the onset of the Covid-19 pandemic in 2020—to assess their potential impact on the business landscape. This method allowed me to pinpoint how these disruptions may have influenced specific industries and regions, offering insights into the resilience and vulnerabilities of Puerto Rico’s local economies.


## Data
### Data Source
The datasets used came directly from estadisticas.pr and mercadolaboral.pr while cross referencing census.gov

### Data Description
The final data set consists of the following columns:
- `town_code`: The federal identification number for the town
- `naics`: the NAICS code that identifies the industry of the businesses
- `establishments`: the number of establishments
- `year`: the year the information was collected for
- `town_name`: the name of the town the establishments are located
- `region`: the region of Puerto Rico the establishments are located

### Data Cleaning
- Standardized and Concatenated 10 years worth of data.
- Translated data from spanish to english.
- Handled missing values, misspellings and duplicates.
- Converted data types to consistent formats.
- Extracted,standardized and converted town and NAICS information.
- Mapped town names to region names for better analysis.

## Methodology
- Used Python (Pandas, NumPy and my own functions) for data manipulation.
- Visualized trends with Matplotlib and Seaborn.
- Visualized in PowerBi

## Results
### Key Findings
- While the metro area has the largest number of establishments in Puerto Rico by far, they also saw the largest decrease in establishment across their top 5 industries from 2019 to 2021, with San Juan being the hardest hit. They went from a little over 50,000 establishments down to less than 25,000 establishments at it's lowest in 2021. There was relatively little change between 2017 and 2018. 
- The rest of the regions on the island saw a downward trend in number of establishments across the decade, but nowhere near as drastic as in the metro area. For the rest of the towns, the downward trend began from 2016 to 2017, reaching its lowest points in 2020 and slightly improving in 2020. 
- 44: Retail Trade and 62: Health Care and Social Assistance, were consistently the top 2 industries in each region. There's been a consistent downward trend in these industries across the regions as well, the mountain area saw the least drastic decline and the metro area saw the biggest dip in 2020 but quickly improved the next year(though still nowhere near their highest numbers).
- In a distant third for every region except the metro area, Administrative,Support, Waste Management and Remediation Services has remained relatively steady across the decade. In the metro area, Professional, Scientific, and Technical Services, took the third spot with the similar dip after 2020.
- Every town in each region with the largest number of establishments saw the largest decreases from 2017-2020. Generally speaking, the rest of the towns remained consistent or even saw slight increases in establishments by the end of the decade.

### Visualizations
Visualizations were created in PowerBI and can be accessed here: deeper-dive-visualizations.pbix 

### Interpretation
The data suggests a correlation between the impact of COVID-19 and the geographic distribution of business establishments. COVID-19 may have played a significant role in the decline in large industries within highly populated areas, which in turn created opportunities for less populated regions and towns to either maintain their number of establishments or even experience a slight increase. In some cases, these smaller areas saw notable improvements, indicating a shift in economic activity away from traditional urban centers during the pandemic.

Similarly, the data also suggests a correlation between the impact of Hurricane Maria and the geographic distribution of business establishments, albeit with a more subtle effect. While there was a noticeable decrease in establishments in 2017, it is not as dramatic as the dip observed during 2020. The downward trend in the number of establishments had already begun before Hurricane Maria struck in 2017, with the mountain towns being disproportionately affected over time compared to other regions.

### Further questions
Do health emergencies themselves have a more intense impact on economies than natural disasters, or is it the response to each of these that played a bigger role?

Would a more even distribution of establishments across the island have made businesses more resilient to COVID-19? Only the most densely populated areas saw the worse decrease while other regions saw no change at all (or even saw growth!). What does this tell us about the relationship between distribution and resilience and what opportunities does that open up for the smaller towns? 


## Project Structure
/pr-biz-patterns-deeper-dive
├── /Data Sets
│   ├── raw data csv's
├── Clean and Concat DFs.ipynb
├── EDA by Industry.ipynb
├── EDA by Region and Town.ipynb
├── full_clean_df.pkl
├── Metadata NAIC code reference.txt
├── pr_biz_dataset_clean.csv
└── README.md

## Challenges and Limitations
- There were many establishments considered 'multi-town' with no indication of what regions or towns they could be from, which I could not use as part of my analysis.
- These are official numbers that do not take into account unregistered/unlicensed businesses.
- While rare, there is a possibility of businesses changing their industry instead of closing, which I have no way of knowing from the data I have. 
- There was 1 industry that was not counted for a number of years (without any kind of explanation), so I decided to eliminate it from the analysis because there was not enough consisten data.
