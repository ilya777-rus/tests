import unittest

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPO_NAME = os.getenv('GITHUB_REPO_NAME')

API_URL = ' https://api.github.com/user/repos'

HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def create_repository(repo_name):
    data = {
        'name': repo_name,
        'private':False
    }
    response = requests.post(API_URL, headers=HEADERS, json = data)
    return response

def check_repository_exists(repo_name):
    response = requests.get(API_URL, headers=HEADERS)
    repos = response.json()
    for repo in repos:
        if repo['name']==repo_name:
            return True

def delete_repository(repo_name):
    repo_url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}'
    print('REPOOOOOOOOOO',repo_url)
    response = requests.delete(repo_url, headers=HEADERS)
    return response

def test_github_repository_operations():
    repo_name = GITHUB_REPO_NAME

    # Создание репозитория
    print('Создание репозитория...')
    response = create_repository(repo_name)
    print(response)
    assert response.status_code == 201, 'Не удалось создать репозиторий'
    print('Репозиторий создан')

    print('Проверка наличия репозитория...')
    exists = check_repository_exists(repo_name)
    assert exists, "Нет репозитория"
    print('Репозиторий найден')

    print('Удаление репозитория...')
    response = delete_repository(repo_name)
    print(response)
    assert response.status_code==204, "Не удалось удалить репозиторий"
    print('Репозиторий удален')

if __name__ == '__main__':
    test_github_repository_operations()