Необходимо:
Используя фреймворк py.test написать unit-тесты с моком запросов к сети на 3 основные функции клиента: 
Работа с reddit-api (посылка, обработка запросов)
Поиск и вывод сабреддитов
Получение комментариев к ветке
Используя плагин pytest-bdd написать 1 функциональный сценарий, который будет эмулировать работу пользователя с данным клиентом:
Поиск и вывод сабреддитов
Поиск и вывод тем в сабреддите
Вывод комментариев к любой теме

# reddit-cli
Reddit command-line client

# Installation
```pip install git+https://github.com/Scalr/test-reddit.git```

# Usage:

Search subreddits by name
```bash
reddit-cli search <search_query>
```

Show subreddit submissions
```bash
reddit-cli subreddit <subreddit_name> --limit=20 --order=hot
```

Show submission comments
```bash
reddit-cli submission <subreddit_id>
```
