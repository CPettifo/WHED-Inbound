import categorise, creds

# The goal of this script is to allow for the analysis of structured HEI data to allow for insertion into the 
# World Higher Education Database, the first iteration uses CRICOS but given time I plan to modify this to take
# any structured data as input
#TODO move this into a README

# I'm not planning for this to be particularly well optimised, as it is a script that will only be run periodically, and likely on local systems in the background.

masterlist_path = "masterlist.xlsx"
output_path = "output.xlsx"

# Test db connection
print("Testing Connection to WHED")
# create test query
query = "SELECT OrgID AS 'Connection Test' FROM whed_org WHERE OrgID < 25 LIMIT 5"
try:
    creds.whed_test_connect(query)
    print("WHED Connection Successful")
except Exception as e:
    print("Could not connect to MySQL database", e)
    exit(1)


# Ask for user input if categorisation is required
user_input = input("categorise institutions? [Y/ N]: ").strip().upper()

if user_input == "Y":
    
    # list of level codes that categorise a degree as postgrad in the WHED
    postgrad_codes = ["6C", "7A", "7B", "7C", "7D"]

    # Categorise institutions (WHED-Recognised, WHED-Candidate, etc.) and export to an excel spreadsheet
    categorise.main(masterlist_path, postgrad_codes)

user_input = input("do you want to attempt to insert into the whed using masterlist credentials? [Y/ N]: ").strip().upper()
if user_input == "Y":
    creds.main(masterlist_path, output_path)    
    exit(0)