# APGym Data Requirements

This file defines the minimum data contract to train and validate APGym in a way that can support farmer-facing recommendations.

## 1) Required Inputs

### Site Identity

Minimum fields:

- `site_id`
- `latitude`, `longitude`, `elevation_m`
- `region` and `season_year`
- `crop` and `cultivar` (if known)

Schema: [`site_identity.schema.json`](./schemas/site_identity.schema.json)

### Daily Weather

Minimum daily fields:

- `date`
- `tmin_c`, `tmax_c`
- `rain_mm`
- `rad_mj_m2`

Preferred additions:

- `wind_m_s`
- `vp_kpa` or humidity equivalents

Schema: [`weather_daily.schema.json`](./schemas/weather_daily.schema.json)

### Soil Profile

Layer-level minimum fields:

- `layer_top_mm`, `layer_bottom_mm`
- `bulk_density`
- `ll15`, `dul`, `sat`
- `ph`
- `oc_pct`

Preferred additions:

- `no3_kg_ha`, `nh4_kg_ha`
- `sand_pct`, `silt_pct`, `clay_pct`

Schema: [`soil_profile.schema.json`](./schemas/soil_profile.schema.json)

### Management Events

Minimum management history:

- planting date
- harvest date
- fertilizer timing and amount (at least total seasonal N)

Preferred additions:

- fertilizer source and method
- irrigation dates and amounts
- tillage and residue operations

Schema: [`management_events.schema.json`](./schemas/management_events.schema.json)

### Economics Inputs

Minimum economic assumptions:

- grain price (`USD/ton`)
- fertilizer N price (`USD/kg`)
- irrigation/energy cost if irrigation is modeled

## 2) Required Outputs For Validation

### Simulator Outputs

Track per run:

- `yield_t_ha`
- `total_n_applied_kg_ha`
- `leaching_kg_ha`
- `season_et_mm`
- `profit_usd_ha`

Schema: [`simulation_outputs.schema.json`](./schemas/simulation_outputs.schema.json)

### Observed Outputs

Validation minimum:

- observed `yield_t_ha`
- matched site/year identity keys

Recommended:

- phenology dates
- biomass
- irrigation totals
- ET and soil water where available

Schema: [`observed_outputs.schema.json`](./schemas/observed_outputs.schema.json)

## 3) Validation Gate Before RL Deployment

A scenario family should be marked "validated" before policy recommendations when:

- weather/soil/management records pass QA checks;
- APSIM predicted-vs-observed fit is acceptable (RMSE, MAE, bias, R2, NSE tracked);
- RL policy beats baseline management on expected profit without hiding risk metrics.

Use the validation utilities in [`/apgym/validation`](../validation).
