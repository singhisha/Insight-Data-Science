# INSIGHT DATA SCIENCE H1B Statistics
## Coding Challenge completed by Isha Singh

### Programming language used:
Python 3.6.6

### Table of Contents:
1. Problem Statement
2. Approach
3. Run Instructions
4. Testing and Results

### Problem Statement
We are given the input data file with immigration data trends on H1B visa application processing. We have to analyse the data to find the following two metrices:
Top 10 Occupations for certified visa applications
Top 10 States for certified visa applications

### Approach
1. I started with the idea of just storing the required fields from the input file. Only the data from the following fields will be needed for further analysis:
```
CASE_STATUS
SOC_NAME
WORKSITE_STATE
```
As it was noticed, that one of the datasets provided for reference has a slightly different column names, so the code is written accordingly.
I used a dictionary to read each row and fetch just the required columns based on the header which resulted in this:
```
[['CERTIFIED', '"SOFTWARE DEVELOPERS, APPLICATIONS"', 'WA'], ['CERTIFIED', 'ACCOUNTANTS AND AUDITORS', 'CA'], ['CERTIFIED', 'DATABASE ADMINISTRATORS', 'TX'], ['CERTIFIED', '"SOFTWARE DEVELOPERS, APPLICATIONS"', 'DE'], ['CERTIFIED', '"SOFTWARE DEVELOPERS, APPLICATIONS"', 'AL'], ['CERTIFIED', '"SOFTWARE DEVELOPERS, APPLICATIONS"', 'FL'], ['CERTIFIED', '"SOFTWARE DEVELOPERS, APPLICATIONS"', 'FL'], ['CERTIFIED', 'COMPUTER SYSTEMS ANALYST', 'MD'], ['CERTIFIED', '"COMPUTER OCCUPATIONS, ALL OTHER"', 'NJ'], ['CERTIFIED', '"SOFTWARE DEVELOPERS, APPLICATIONS"', 'GA']]
```

2. Next I am filtering and returning just the certified applicants.
3. For the final metrices, to count the number of certified applicants, I am using a dictionary where key is state/occupation and value  is the count and calculating the percentage by
```
Percentage = Total no. of certified applicants for State/
			 Total certified applicants
```

### Run Instructions
No specific instructions are required to run the code.

### Testing and Results
The results are stored in the output folder in top_10_states.txt and top_10_occupations.txt


