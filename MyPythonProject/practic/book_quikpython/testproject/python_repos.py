import requests,pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("status code"+str(r.status_code))
response_dirct=r.json()
print(response_dirct.keys())
print(response_dirct['total_count'])
repo_dircts=response_dirct['items']

names,stars=[],[]
for repo_dirct in repo_dircts:
    names.append(repo_dirct['name'])
    stars.append(repo_dirct['stargazers_count'])

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')