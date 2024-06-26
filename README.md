# Reddit tend topics

Reddit trend topics is a python script designed for finding the trend topics from the last submissions of a subreddit.

## Before you begin

First of all you must go to [Reddit Apps](https://old.reddit.com/prefs/apps/), login and create and App.

Based on the [PRAW tutorial](https://praw.readthedocs.io/en/stable/getting_started/authentication.html#password-flow), create a JSON file named *reddit_config.json* inside the project root folder.
```json
{
    "client_id": "",
    "client_secret": "",
    "password": "[From the same account where the App was created]",
    "username": "[From the same account where the App was created]",
    "user_agent": "reddit trend topics by u/[username]"
}
```

Next, install project dependencies
```bash
pip install -r requirements.txt
```

## Usage
Go to the project folder and open terminal.
```bash
python main.py
```
Or
```bash
python main.py -n 10 -l 150 -s skincancer
```

### Variables
#### N (default 10)
Number of trend topics generated by the program.
```bash
python main.py -n 10
```
#### Limit (default 150)
Max number of submissions to be pulled from reddit for analysis.
```bash
python main.py -l 150
```
```bash
python main.py --limit 150
```

#### Subreddit (default 'skincancer')
Name of the subreddit from where submissions will be pulled.

Insert 'all' for a general search.
```bash
python main.py -s skincancer
```
```bash
python main.py --subreddit skincancer
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)