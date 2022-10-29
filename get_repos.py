import requests
import yaml
import os
import logging


header = {
    "Accept": "application/vnd.github+json",
    "Authorization":"Bearer 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" 
}
create_repo_url = 'https://api.github.com/repos/peeweep-test/template-repository/generate'

def read_yml():
    with open("repos.yml", "r+") as intergration_file:
        return yaml.load(intergration_file, Loader=yaml.BaseLoader)
def check_repo(repo):
    res = requests.get("https://api.github.com/repos/peeweep-test/{repo}".format(repo=repo))
    if res.status_code == 200:
        return repo
def create_repo(repo):
    data_repo = {
            'owner':'peeweep-test',
            'name': repo
            }
    res = requests.post(create_repo_url, json = data_repo, headers = header) 
try:
    data = read_yml()
    for repo in data.get("repos"):
        if check_repo(repo.get('repo')) == None:
#            print(repo.get('repo'))
            create_repo(repo.get('repo'))
except BaseException as e:
    logging.error(e)
    exit(-10)
