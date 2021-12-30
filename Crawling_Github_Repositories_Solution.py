import requests
import pandas as pd

# 0. INITIALIZE VARIABLES
all_responses = []

# 1. PERFORM SEARCH
github_response = requests.get('https://api.github.com/search/repositories?q=MNIST+classification+language:python&per_page=25')

# 2. PULL DATA
info = ['name','description','owner','url','created_at','watchers']
for item in github_response.json()['items']:
    single_response = []
    # add each individual item to list
    for value in info:
        if value=='owner':
            single_response.append(item[value]['login'])
        else:
            single_response.append(item[value])
    # add list to overarching list
    all_responses.append(single_response)

# 3. VIEW DATA AS (SORTED) PANDAS DATAFRAME
dataframe = pd.DataFrame(all_responses, columns=info).sort_values(by=['watchers'], ascending=False)
dataframe

# 4. DOWNLOAD CONTENT
for index, repo in dataframe.iterrows():
    read_me_content = requests.get(
        repo['url']+'/contents/README.md',
        headers={'Accept': 'application/vnd.github.v3.html'}
    ).content
    with open(str(repo["name"])+'_readme.html',"wb") as file:
        file.write(read_me_content)

# 5. INSPECT FILES
