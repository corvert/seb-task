### Simple ETL process: 
Extract the Euro foreign exchange reference rates from the ECB, 
transform the data, and load the cleaned data into a separate Markdown file in table format. 

#### 1. Extract
- Extract and read ECB rates from ECB APIs

#### 2. Transform
- Load daily and historical exchange rates
- Select only USD, SEK, GBP, and JPY
- Calculate the historical mean rates for the four selected currencies based on historical data

#### 3. Load
Write info Markdown table with the following columns:
- Currency Code
- Rate
- Mean Historical Rate

### AI history
https://claude.ai/share/f35e5e77-06d6-423e-92ea-989111acac10
