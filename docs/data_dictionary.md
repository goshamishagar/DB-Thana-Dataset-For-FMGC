# Data Dictionary — Bangladesh Thana Dataset

## thana_reference.csv

| # | Field | Type | Example | Notes |
|---|---|---|---|---|
| 1 | Division | Text | `Dhaka` | One of 8 divisions |
| 2 | District | Text | `Gazipur` | One of 63 districts |
| 3 | Thana / Upazila | Text | `Sreepur` | Sub-district unit |
| 4 | Thana Type | Category | `Upazila` | `Upazila` = rural sub-district; `City Thana` = urban police station / ward cluster within a City Corporation |
| 5 | Population (Est. 2022) | Integer | `473000` | BBS 2022 Census preliminary estimate |
| 6 | Area (sq km) | Decimal | `453.0` | Land area in square kilometres |
| 7 | Pop. Density (per sq km) | Integer | `1044` | Population ÷ Area, rounded |
| 8 | Division Code | Text | `30` | 2-digit BBS administrative code |
| 9 | District Code | Text | `3005` | Division code + 2-digit sequential district code |

---

## thana_economic_activity.csv

| # | Field | Type | Example | Notes |
|---|---|---|---|---|
| 1 | Division | Text | `Sylhet` | — |
| 2 | District | Text | `Moulvibazar` | — |
| 3 | Thana / Upazila | Text | `Sreemangal` | — |
| 4 | Primary Sector | Category | `Agriculture` | `Agriculture` / `Industry` / `Services` / `Mixed` |
| 5 | Sub-Activity | Text | `Tea / rubber / tourism` | Dominant livelihood / economic driver for the thana |
| 6 | FMCG Trade Class | Category | `General Trade` | See trade class definitions below |
| 7 | Market Classification | Category | `Semi-Urban` | `Urban` / `Semi-Urban` / `Rural` / `Industrial` |

### FMCG Trade Class Definitions

| Trade Class | Description |
|---|---|
| `General Trade` | Traditional retail — kirana stores, wholesalers, mom-and-pop shops. Dominant in rural and semi-urban areas. |
| `Modern Trade` | Supermarkets, chain stores, pharmacy chains, branded outlets. Concentrated in urban centres. |
| `Mixed (GT+MT)` | Significant presence of both general and modern trade. Typical in large towns and district HQs. |
| `Industrial GT` | General trade catering primarily to industrial workers and factory populations. Lower consumer spend per basket. |

### Market Classification Definitions

| Class | Description |
|---|---|
| `Urban` | City Corporation or Pourashava areas; high density, formalised retail |
| `Semi-Urban` | District or upazila HQ towns; growing retail, transitional between rural and urban |
| `Rural` | Predominantly agricultural; traditional trade, low organised retail penetration |
| `Industrial` | EPZ, port zones, or heavy industrial belts; worker-dominated consumer base |

---

## thana_fmcg_consumer_profile.csv

| # | Field | Type | Example | Notes |
|---|---|---|---|---|
| 1 | Division | Text | `Chattogram` | — |
| 2 | District | Text | `Chattogram` | — |
| 3 | Thana / Upazila | Text | `Khulshi` | — |
| 4 | Market Classification | Category | `Urban` | Repeated from economic activity for convenience |
| 5 | FMCG Trade Class | Category | `Modern Trade` | Repeated for convenience |
| 6 | Primary Sector | Category | `Services` | Repeated for convenience |
| 7 | Consumer Profile Tag | Text | `Premium Urban Consumer` | Derived consumer segment label |
| 8 | Likely Top FMCG Categories | Text | `Personal care, packaged food, beverages, household care` | Key product categories by likely consumption |
| 9 | Distribution Priority | Category | `A` | `A` = High priority / `B` = Medium / `C` = Low |

### Consumer Profile Tags

| Tag | Typical Thana Type | Priority |
|---|---|---|
| Premium Urban Consumer | Urban, Modern Trade | A |
| Urban GT Shopper | Urban, General Trade | A |
| Aspiring Semi-Urban Buyer | Semi-Urban | A |
| Service Economy Consumer | Semi-Urban, Services sector | B |
| Remittance-Driven Consumer | Semi-Urban, remittance economy | B |
| Tea Belt Rural Consumer | Rural, tea-growing areas | B |
| Agri-Surplus Rural Consumer | Rural, mango / fruit / cash crops | B |
| Border / Port Trade Consumer | Semi-Urban, border / port areas | B |
| Industrial Worker / Blue-Collar | Industrial, garments / EPZ zones | B |
| Mass Rural Consumer | Rural, rice / subsistence farming | C |
| Riverine / Haor Rural Consumer | Rural, haor / char / flood-prone areas | C |
| Coastal Aquaculture Community | Rural, shrimp / salt / fishing coast | C |

### Distribution Priority Logic

| Priority | Criteria |
|---|---|
| A | Urban or semi-urban; Modern Trade or Mixed GT+MT; service/aspiring consumer profile |
| B | Semi-urban GT; rural with cash crop or remittance income; industrial zones |
| C | Remote rural; haor / char / coastal; subsistence agriculture |

---

## summary_division.csv

Division-level aggregate. Fields: Division, Division Code, No. of Thanas/Upazilas, Total Population (Est.), Total Area (sq km), Pop. Density (per sq km).

## summary_district.csv

District-level aggregate. Fields: Division, District, No. of Thanas, Total Population, Total Area (sq km), Pop. Density (per sq km).

## summary_sector.csv

Three stacked tables in one file — Primary Sector breakdown, FMCG Trade Class breakdown, Market Classification breakdown — each with Thana Count and % of Total.
