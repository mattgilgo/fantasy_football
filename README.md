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
* Fantasy Football Calculator for Fantasy Draft ADP (https://fantasyfootballcalculator.com/adp/ppr/12-team/all)

## Data Engineering
...

## Exploratory Data Analysis (EDA)
Once the datasets weere created and engineered, the next step was to explore the datasets visually. As a first step in the process, it is simply important to know what the data is shaped like. With this is mind, the plot below was created to show how Fantasy Point production slopes off for each individual position.

![alt text](https://github.com/mattgilgo/fantasy_football/blob/cleanup/plots/points_by_position.png?raw=true)

## Model Generation
...

## Results Visualization
...

## Draft Simulations
...

## Model Performance Tracker
2022 Performance for teams drafted using these projections
...
* All-star Amigos (12tm/PPR, Drafted 11th) - 
* Carolina H2H (10tm/PPR, Drafted 6th) -