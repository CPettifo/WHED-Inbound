# TODOS December / Early January
## Plan for Outbound API
### Planned infrastructure
Likely a VM hosting a MariaDB database, with a sample of the WHED with certain fields obfuscated
Either App Service or other VM for the API itself
Obviously also a VNET
Azure Key Vault


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

#### Database Copy
An older version of the WHED will be put into a test VM, interns can test creating streamlined
backup, update, and other processes. Importantly, a new object will be created to keep the full credential
name, or a new row will be added to an existing table such as that linking degree to fos


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


### Planned infrastructure
- Database on a dedicated debian VM with our oldest data
- Small VM for each intern?
- Testing VM


### Breakdown of tasks
January 12 - Feb 12
First fortnight: learning of WHED back-office, meeting other staff, project overview and initial meetings, collaboration, small development tasks, review of current codebase with complete freedom to try to import standardised excel sheets
Second fortnight: gauge interest and choose a focus point for the internship (front-end, back-end, database) together. Develop project requirements together, testing plan, etc.
February: Elizabeth joins? First fortnight for her meeting team & same process as Angelina, choose focus point together 
March: 
April: 
May: 
June: 
July: 



## Other SysAdmin Projects
### Teams Calendar
- Learn how to view other calendars, create instructions
- Learn how to import google calendar
- Instructions for creating Teams meetings, privacy, etc.


### UNESCO Device Registration
- Create MS Form for required software, etc.


### Membership Reminder Call 
- Create instructions, organise meeting with JH & HB in January
- How to create a template in S-Docs
- Discuss with HvL my involvement in the project (technical implementation)


### Hardware
- Create MS Form for staff to fill out survey for hardware and peripheral requirements


## Send Summary to Andreas
Include all of the above, responsibilities breakdown for each project, touch on plans for other projects