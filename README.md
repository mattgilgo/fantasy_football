# Fantasy Football Analysis w/ Data Science Models
Documented in this repository will be my attempts at:
* Gathering data 
* Engineering to data to useful and concise datasets
* Exploratory data analysis for insights to datasets
* Creating models to predict future fantasy performance 
* Visualizing results of predictions
* Simulating drafts using various strategies to find optimal approach

## Results
Choose from the csvs below to view ranked projection for your fantasy football draft:
* Projections using top performing model/position pairing for each position:
    - [QB] (https://github.com/mattgilgo/fantasy_football/blob/main/projections/QB/BayesianRidge2022_projections_20220830-142824.csv)
    - [RB] (https://github.com/mattgilgo/fantasy_football/blob/main/projections/RB/RandomForestRegressor2022_projections_20220830-142827.csv)
    - [WR] (https://github.com/mattgilgo/fantasy_football/blob/main/projections/WR/BayesianRidge2022_projections_20220830-142827.csv)
    - [TE] (https://github.com/mattgilgo/fantasy_football/blob/main/projections/TE/LinearRegression2022_projections_20220830-142828.csv)


* Projections using aggregate of all 8 ML models for each position:
    - [QB] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_083022/QB/qb_combined_projs.csv)
    - [RB] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_083022/RB/rb_combined_projs.csv)
    - [WR] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_083022/WR/wr_combined_projs.csv)
    - [TE] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_083022/TE/te_combined_projs.csv)

## Gathering Data
To kick off this project, data needed to be consolidated from various sources connect the picture between player statistics through where they project in a Fantasy Football Draft.
The following sources were used to extract this data:
* Pro Football Reference for player game and combine stats (https://www.pro-football-reference.com/)
* CBS Sports for target projections (https://www.cbssports.com/fantasy/football/stats/)
* Fantasy Pros for aggregate 2022 PPR-format points projections (https://www.fantasypros.com/nfl/projections/qb.php?week=draft)
* Fantasy Football Calculator for Fantasy Draft ADP (https://fantasyfootballcalculator.com/adp/ppr/12-team/all)

## Data Engineering
...

## Exploratory Data Analysis (EDA)
Once the datasets weere created and engineered, the next step was to explore the datasets visually. As a first step in the process, it is simply important to know what the data is shaped like. With this is mind, the plot below was created to show how Fantasy Point production slopes off for each individual position.

![alt text](https://github.com/mattgilgo/fantasy_football/blob/main/plots/points_by_position.PNG?raw=true)

## Model Generation
...

## Results Visualization
...

## Draft Simulations
...

## Model Performance Tracker
2022 Performance for teams drafted using these models:

| League          | #Teams/League | Scoring Style | Draft Position | Total Points  | League Finish |
| --------------- | ------------- | ------------- | -------------- | ------------- | ------------- |
| All-star Amigos | 12            | PPR           | 11th           | 1685          | 3rd           |
| Carolina H2H    | 10            | PPR           | 6th            | 1646          | 6th           |
| Seattle H2H     | 10            | PPR           | 7th            | 1664          | 2nd           |
| Biloxis Best Fm | 10            | PPR           | 7th            | 1781          | 1st           |
| Couples De Lead | 10            | PPR           | 6th            | 1725          | 1st           |

## Average Position Finishes by Draftees
Average Position Rank by Drafted Starting Players (number of top players averaged for position in parenthesis):

| League          | QB (1) | RB (2) | WR (3) | TE (1) |
| --------------- | -----  | ------ | ------ | ------ |
| All-star Amigos | 11     | 12     | 6      | 3      |
| Carolina H2H    | 13     | 18     | 8      | 1      |
| Seattle H2H     | 13     | 9      | 8      | 7      |
| Biloxis Best Fm | 12     | 23     | 5      | 1      |
| Couples De Lead | 12     | 8      | 8      | 12     |



