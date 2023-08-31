# Fantasy Football Analysis w/ Data Science Models
Documented in this repository will be my attempts at:
* Gathering and engineering datasets 
* Exploratory data analysis for insights to datasets
* Creating models to predict future fantasy performance 
* Visualizing results of predictions
* Simulating drafts using various strategies to find optimal approach
* Real-life application of models across various fantasy leagues
* Model Performance vs Experts Projections (ESPN/NFL)

## Choose from these Predictions for your Fantasy Draft!
Choose from the csvs below to view ranked projection for your fantasy football draft:
### 2023 Full Fantasy Player Rankings:
- [OVR] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/OVR/2023_projections_20230830-193027.csv)

### 2023 Projections using top performing model/position pairing for each position:
- [QB] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/QB/2023_projections_20230830-171708.csv)
- [RB] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/RB/2023_projections_20230830-171708.csv)
- [WR] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/WR/2023_projections_20230830-172942.csv)
- [TE] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/TE/2023_projections_20230830-172942.csv)

### 2023 Stars of the Show:
Based on past performance, these players have what it takes to be an All-Pro at their position this year:
- [QB] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/QB/qb_star_criteria.csv)
- [RB] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/RB/rb_star_criteria.csv)
- [WR] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/WR/wr_star_criteria.csv)
- [TE] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/TE/te_star_criteria.csv)

<details>
  <summary>2022 Projections</summary>
    
### Projections using top performing model/position pairing for each position:
- [QB] (https://github.com/mattgilgo/fantasy_football/blob/main/projections/QB/BayesianRidge2022_projections_20220830-142824.csv)
- [RB] (https://github.com/mattgilgo/fantasy_football/blob/main/projections/RB/RandomForestRegressor2022_projections_20220830-142827.csv)
- [WR] (https://github.com/mattgilgo/fantasy_football/blob/main/projections/WR/BayesianRidge2022_projections_20220830-142827.csv)
- [TE] (https://github.com/mattgilgo/fantasy_football/blob/main/projections/TE/LinearRegression2022_projections_20220830-142828.csv)

### Projections using aggregate of all 8 ML models for each position:
- [QB] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_083022/QB/qb_combined_projs.csv)
- [RB] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_083022/RB/rb_combined_projs.csv)
- [WR] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_083022/WR/wr_combined_projs.csv)
- [TE] (https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_083022/TE/te_combined_projs.csv)
</details>



## Data Engineering
To kick off this project, data needed to be consolidated from various sources connect the picture between player statistics through where they project in a Fantasy Football Draft.
The following sources were used to extract this data:
* Pro Football Reference for each Player's game and combine stats (https://www.pro-football-reference.com/)
* CBS Sports for target projections (https://www.cbssports.com/fantasy/football/stats/)
* Fantasy Pros for aggregate 2022 PPR-format points projections (https://www.fantasypros.com/nfl/projections/qb.php?week=draft)
* Fantasy Football Calculator for Fantasy Draft ADP (https://fantasyfootballcalculator.com/adp/ppr/12-team/all)

## Exploratory Data Analysis (EDA)
Once the datasets were created and engineered, the next step was to explore the datasets visually. As a first step in the process, it is simply important to know what the data is shaped like. With this is mind, the plot below was created to show how Fantasy Point production slopes off for each individual position.

![alt text](https://github.com/mattgilgo/fantasy_football/blob/main/plots/points_by_position.PNG?raw=true)

## Model Generation
For the first iteration of generating models, the sklearn library was used to explore various regression model types and test their accuracy against the given datasets. 
The model types tested were:
- Linear Regression
- Lasso
- Ridge
- Bayesian Ridge
- Elastic Net
- kNN
- Random Forest
- MLP (Neural Net)

Based on the preliminary model training results, these model types were found to have the best performance and were used to rank each position group for the draft:
- Passing Yards - kNeighborsRegressor
- Rushing Yards - kNeighborsRegressor
- Receiving Yards - MLPRegressor

<details>
  <summary>2022 Best Models</summary>

- QB: Bayesian Ridge
- RB: Random Forest
- WR: Bayesian Ridge
- TE: Linear Regression
</details>


## Model Performance Tracker

<details>
  <summary>2022 Performance</summary>

### Team Results
2022 Performance for teams drafted using these models:

| League          | #Teams/League | Scoring Style | Draft Position | Total Points  | League Finish |
| --------------- | ------------- | ------------- | -------------- | ------------- | ------------- |
| All-star Amigos | 12            | PPR           | 11th           | 1685          | 3rd           |
| Carolina H2H    | 10            | PPR           | 6th            | 1646          | 6th           |
| Seattle H2H     | 10            | PPR           | 7th            | 1664          | 2nd           |
| Biloxis Best Fm | 10            | PPR           | 7th            | 1781          | 1st           |
| Couples De Lead | 10            | PPR           | 6th            | 1725          | 1st           |

### Average Position Finishes by Draftees
Average Position Rank by Drafted Starting Players (number of top players averaged for position in parenthesis):

| League          | QB (1) | RB (2) | WR (3) | TE (1) |
| --------------- | -----  | ------ | ------ | ------ |
| All-star Amigos | 11     | 12     | 6      | 3      |
| Carolina H2H    | 13     | 18     | 8      | 1      |
| Seattle H2H     | 13     | 9      | 8      | 7      |
| Biloxis Best Fm | 12     | 23     | 5      | 1      |
| Couples De Lead | 12     | 8      | 8      | 12     |

### Model Loss Stats
Mean Absolute Error of Model's Projected Points vs Actual Points:
***(Bolded/Italicized Scores Reflect Performance higher than industry experts)***

| Position   | Experts | Gilgo      |
| ---------- | ------- | ---------- |
| ***QB***   | 78.7    | ***76.9*** |
| RB         | 51.3    | 58.9       |
| ***WR***   | 59.5    | ***47.3*** |
| ***TE***   | 46.8    | ***35.5*** |
</details>

## Next Steps
- [x] Further model improvement, with a focus on RB position group to get performing above industry competitors
- [ ] New model development for D/ST and K position groups
- [ ] Inclusion of additional datasets (PFF, O-Line stats, etc.)
- [ ] Exploring more complex modeling libraries (TensorFlow, Pytorch, etc.)




