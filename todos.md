# TODOS December / Early January
## Plan for Outbound API

### Endpoints
#### Country Code
SELECT CountryCode FROM whed_state WHERE Country = "?"
Returns country code for specified country, to facilitate searching by country names


#### Institutions General
Show general information about institutions, with country as a required item
e.g. SELECT OrgID, OrgName, InstNameEnglish, City FROM whed_org WHERE it's a whed recognised institution and not a branch
Query includes Country Code, for example the endpoint would be
whed.net/institutions?CountryCode="AU"

#### Institutions Detailed
Basically a copy of the full extractions we send to the UN
Heavily rate-limited and with limited access (i.e. trusted partners such as UNESCO)


#### Divisions Detailed
Basically a copy of the full extractions we send to the UN
Heavily rate-limited with limited access

#### Degrees Detailed
Basically a copy of the full extractions we send to the UN
Heavily rate-limited with limited access

#### Degree Matching
Will return **Full Match**, **Level Match**, **Field Match**, **Partial Field Match**, **Institution Not Found**, **Credential Not Found**, **No Match At Inst** if there is a matching degree found at the specified institutions
Input would be e.g. United States, Harvard University, Bachelor, Computer Science
- Search through institutions 


### Administration
- How to manage users, send access tokens
- NDA?
- Conditions of use for API
- Pricing structure
For example if we need to create a custom API endpoint, if they want access to full extractions


## Plan for Interns
### Project overview
We want to focus on the inbound data pipeline, this will include the following key components

#### Submission Portal
A platform to allow for the upload of an excel spreadsheet with educational data.
Testing / validation will occur to ensure that the spreadsheet follows the correct format, 
helpful error messages will assist the user in fixing any import issues


#### Import Processing
The heart of the platform will process the submitted data, and pre-process this to be manually
categorised by WHED staff


#### Data Officer Portal
This will allow Data Officers to see the pre-processed data, manually categorise anything that requires
input, and stage the data for ingestion.


#### Ingestion
This will import the data to be ingested into the system. Institutions not in the WHED will have an entry made for them and will require later update by Data Officers. 


#### Dashboards (not priority)
This will display summaries to users, Data Officers will see summaries (institutions updated, institutions created, credentials updated, credentials automatically categorised), as well as a world map with colour coded countries based on the time since their latest update.


#### Mockups of Improved WHED UI (not priority for scope of internship)
Creation of new displays of credential and institution pages