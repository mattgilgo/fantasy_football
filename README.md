# Fantasy Football Analysis w/ Data Science Models
Documented in this repository will be my attempts at:
* Gathering data 
* Engineering to data to useful and concise datasets 
* Creating models to predict future fantasy performance 
* Visualizing results of predictions
* Simulating drafts using various strategies to find optimal approach

## Results
Choose from the csvs below to view ranked projection for your fantasy football draft:
* Projections using top performing model/position pairing for each position:

    - QB: (draft_proj_083022/QB/BayesianRidge2022_projections_20220830-142824.csv)
    - RB: (draft_proj_083022/RB/RandomForestRegressor2022_projections_20220830-142827.csv)
    - WR: (draft_proj_083022/WR/BayesianRidge2022_projections_20220830-142827.csv)
    - TE: (draft_proj_083022/TE/LinearRegression2022_projections_20220830-142828.csv)


* Projections using aggregate of all 8 ML models for each position:
```
- QB: draft_proj_083022/QB/qb_combined_projs.csv
- RB: draft_proj_083022/RB/rb_combined_projs.csv
- WR: draft_proj_083022/WR/wr_combined_projs.csv
- TE: draft_proj_083022/TE/te_combined_projs.csv
```

## Gathering Data
To kick off this project, data needed to be consolidated from various sources connect the picture between player statistics through where they project in a Fantasy Football Draft.
The following sources were used to extract this data:
* Pro Football Reference for player game and combine stats (https://www.pro-football-reference.com/)
* CBS Sports for target projections (https://www.cbssports.com/fantasy/football/stats/)
* Fantasy Football Calculator for Fantasy Draft ADP (https://fantasyfootballcalculator.com/adp/ppr/12-team/all)

## Data Engineering
...

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