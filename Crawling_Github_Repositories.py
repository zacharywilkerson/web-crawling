! python -m pip install pandas

import requests
import pandas as pd

# 0. INITIALIZE VARIABLES
all_responses = []

# 1. PERFORM SEARCH
github_response = requests.get(#INSERT HERE)

# 2. PULL DATA
info = ['name','description','owner','url','created_at','watchers']
for item in github_response.json()['items']:
    single_response = []
    # append each individual item to list -- single_response
    #INSERT HERE
    # append list to overarching list -- all_responses
    #INSERT HERE

# 3. VIEW DATA AS (SORTED) PANDAS DATAFRAME
dataframe = pd.DataFrame(all_responses, columns=info).sort_values(by=['watchers'], ascending=False)
dataframe

# 4. DOWNLOAD CONTENT
for index, repo in dataframe.iterrows():
    read_me_content = requests.get(
        #INSERT HERE
    ).content
with open(str(repo["name"])+'_readme.html',"wb") as file:
        file.write(read_me_content)

# 5. INSPECT FILES
