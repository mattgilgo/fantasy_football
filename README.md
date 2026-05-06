# Fantasy Football ML

> Machine learning models for NFL fantasy football player projections — built and battle-tested across real leagues since 2022.

## Overview

This project trains regression models on historical NFL player statistics to generate pre-draft fantasy football rankings for QB, RB, WR, and TE. Each season the models are retrained, their accuracy is benchmarked against industry expert projections (ESPN/NFL), and the rankings are applied to real league drafts.

Since 2022, drafts guided by these rankings have finished 1st in multiple leagues, and the models have outperformed expert projections on three of four position groups.

## Features

- Data pipeline from Pro Football Reference, CBS Sports, FantasyPros, and ADP sources
- 8 sklearn model types evaluated per position each season (Linear, Lasso, Ridge, Bayesian Ridge, Elastic Net, kNN, Random Forest, MLP)
- XGBoost models introduced in 2025
- "Star criteria" identification — players likely to finish as positional elites
- Year-over-year MAE benchmarking against expert consensus projections
- Notebooks for EDA, model development, and post-season performance analysis

## Requirements

- Python 3.8+
- Jupyter Notebook / JupyterLab
- `scikit-learn`, `xgboost`, `pandas`, `numpy`, `matplotlib`

## Draft Projections

### 2025 Rankings (XGBoost)

- [QB](https://github.com/mattgilgo/fantasy_football/blob/main/projections/2025_xgboost_qb_rankings.csv)
- [RB](https://github.com/mattgilgo/fantasy_football/blob/main/projections/2025_xgboost_rb_rankings.csv)
- [WR](https://github.com/mattgilgo/fantasy_football/blob/main/projections/2025_xgboost_wr_rankings.csv)
- [TE](https://github.com/mattgilgo/fantasy_football/blob/main/projections/2025_xgboost_te_rankings.csv)

<details>
<summary>2024 Rankings</summary>

- [QB](https://github.com/mattgilgo/fantasy_football/blob/main/projections/2024/qb_projections.csv)
- [RB](https://github.com/mattgilgo/fantasy_football/blob/main/projections/2024/rb_projections.csv)
- [WR](https://github.com/mattgilgo/fantasy_football/blob/main/projections/2024/wr_projections.csv)
- [TE](https://github.com/mattgilgo/fantasy_football/blob/main/projections/2024/te_projections.csv)

</details>

<details>
<summary>2023 Rankings</summary>

Overall: [OVR](https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/OVR/2023_projections_20230830-193027.csv)

Best model per position:
- [QB](https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/QB/2023_projections_20230830-171708.csv) · [RB](https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/RB/2023_projections_20230830-171708.csv) · [WR](https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/WR/2023_projections_20230830-172942.csv) · [TE](https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/TE/2023_projections_20230830-172942.csv)

Star criteria (projected positional elites):
- [QB](https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/QB/qb_star_criteria.csv) · [RB](https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/RB/rb_star_criteria.csv) · [WR](https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/WR/wr_star_criteria.csv) · [TE](https://github.com/mattgilgo/fantasy_football/blob/main/draft_proj_new_083023/TE/te_star_criteria.csv)

</details>

<details>
<summary>2022 Rankings</summary>

Best model per position:
- [QB](https://github.com/mattgilgo/fantasy_football/blob/main/projections/QB/BayesianRidge2022_projections_20220830-142824.csv) · [RB](https://github.com/mattgilgo/fantasy_football/blob/main/projections/RB/RandomForestRegressor2022_projections_20220830-142827.csv) · [WR](https://github.com/mattgilgo/fantasy_football/blob/main/projections/WR/BayesianRidge2022_projections_20220830-142827.csv) · [TE](https://github.com/mattgilgo/fantasy_football/blob/main/projections/TE/LinearRegression2022_projections_20220830-142828.csv)

</details>

## Data Sources

| Source | Data |
|--------|------|
| [Pro Football Reference](https://www.pro-football-reference.com/) | Game stats, combine data |
| [CBS Sports](https://www.cbssports.com/fantasy/football/stats/) | Target projections |
| [FantasyPros](https://www.fantasypros.com/nfl/projections/qb.php?week=draft) | Aggregate PPR projections |
| [Fantasy Football Calculator](https://fantasyfootballcalculator.com/adp/ppr/12-team/all) | Draft ADP |

See `steps_to_update_data.txt` for instructions on incorporating new season data.

## Model Performance

Models are evaluated by Mean Absolute Error (MAE) of projected vs. actual fantasy points, benchmarked against expert consensus projections.

### 2022 Results

**Bold = model outperformed experts**

| Position | Experts MAE | Model MAE  |
|----------|-------------|------------|
| **QB**   | 78.7        | **76.9**   |
| RB       | 51.3        | 58.9       |
| **WR**   | 59.5        | **47.3**   |
| **TE**   | 46.8        | **35.5**   |

### 2022 Real-League Outcomes

| League          | Teams | Format | Draft Pick | Points | Finish   |
|-----------------|-------|--------|------------|--------|----------|
| All-star Amigos | 12    | PPR    | 11th       | 1685   | 3rd      |
| Carolina H2H    | 10    | PPR    | 6th        | 1646   | 6th      |
| Seattle H2H     | 10    | PPR    | 7th        | 1664   | 2nd      |
| Biloxis Best Fm | 10    | PPR    | 7th        | 1781   | **1st**  |
| Couples De Lead | 10    | PPR    | 6th        | 1725   | **1st**  |

## Notebooks

| Notebook | Description |
|----------|-------------|
| `eda.ipynb` | Exploratory data analysis across all positions |
| `2025_predictions.ipynb` | 2025 season model training and projections |
| `2024_predictions.ipynb` | 2024 season projections |
| `2024_models.ipynb` | 2024 model development |
| `2023_models.ipynb` | 2023 model development |
| `2022_models.ipynb` | Initial model development |
| `results.ipynb` | Post-season model performance evaluation |

## Roadmap

- [x] Beat expert projections on QB, WR, TE (2022)
- [x] XGBoost models (2025)
- [ ] Improve RB model to outperform experts
- [ ] Add D/ST and K position models
- [ ] Incorporate PFF and O-Line datasets

## License

GPL-3.0 — see [LICENSE](LICENSE)
