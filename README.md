# Bureau of Labor Statistics Simulated Pipeline

A simulated pipeline for importing and processing labor statistics modeled on the real U.S. Bureau of Labor Statistics (BLS). The project is set in an alternate historical timeline of the United States, allowing for creative scenarios while staying anchored to real-world BLS data structures and reporting methods.

This portfolio focuses on demonstrating core competencies in the Microsoft SQL Server ecosystem (SQL Server, SSIS, Python integrations). All data used in this project is synthetically generated or randomly produced; no actual BLS or Census data is included.

## Source Data
The primary data sources for this pipeline are as follows:
- Mock CPS data (based on schema of [BLS - Current Population Survey](https://www.census.gov/programs-surveys/cps.html))
- Mock CES data (based on schema of [BLS - Current Employment Statistics](https://www.bls.gov/ces/))
- Mock LAUS data (based on schema of [BLS - Local Area Unemployment Statistics](https://www.bls.gov/lau/))
- Mock population (based on schema of [Census](https://data.census.gov/))
- Mock JOLTS data (based on schema of [Job Openings and Labor Turnover Survey](https://www.bls.gov/jlt/))
- Mock CPI Micro Prices dataset (based on schema of [Consumer Price Index](https://www.bls.gov/cpi/))
- Mock PPI items dataset (based on schema of [Producer Price Index](https://www.bls.gov/ppi/))
- Mock dimension tables: regions, occupations, items, industries, other metadata as needed

## Deliverables
This pipeline should compute the following KPIs:
- Labor force participation 
- Unemployment rate
- Job turnover rate
- Average wages or earnings
- Wages by industry
- Union membership
- Consumer Price Index (CPI)
- Producer Price Index (PPI)
- Job growth forecasting by industry and occupation

## Special Considerations
This pipeline should simulate:
- Seasonal adjustment
- Revisions (handling updated releases)
- Weights rebase (periodic CPI reweighting)
- Benchmarking (aligning survey estimates to annual controls)