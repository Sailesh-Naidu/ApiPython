import requests
import plotly.express as px

#Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#convert the response object to a dictionary
response_dict = r.json()

#process results
print(response_dict.keys())

print(f"Total repositories: {response_dict["total_count"]}")
print(f"Complete results:{not response_dict["incomplete_results"]}")

#explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

repo_links, stars, hover_texts = [], [], []
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
   repo_name = repo_dict['name']
   repo_url = repo_dict['html_url']
   repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
   repo_links.append(repo_link)
   stars.append(repo_dict["stargazers_count"])

   #Build hover text
   owner = repo_dict['owner']['login']
   description = repo_dict['description']
   hover_text =  f"{owner}<br />{description}"
   hover_texts.append(hover_text)

#make visualization
title = "Most-Starred Python projects on github"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y = stars, labels=labels, title= title, hover_name= hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()