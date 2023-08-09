## Data Scrapping
Here the codes are available for scrapping data from GitHub, Twitter, and Zillow.

## Scrapping from GitHub
This code, [get_github.py](get_github.py) helps to scrap data from GitHub if the address is available.

### Dependencies
Install the following libraries.

```console
pip install requests
```

### Access Token
To generate a new token from GitHub, open this [GitHub_Token_Link](https://github.com/settings/tokens/new), and you will create the token.

### Running Code
Save the address in the json file. Please check the given file format.
Put the correct file names for file_name and saving_file_name variables.
Run the get_github.py

## Scrapping from Twitter
This code, [get_tweets.py](get_tweets.py) helps to scrap data from Twitter if the address is available.

### Dependencies
Install the following libraries.

```console
pip install tweepy
```

### Access Token
To generate a new token from Twitter, follow this [Twitter_Link](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens), and you will create the token.

### Running Code
Save the address in the text file. Please check the given file format.
Put the correct file names for file_name and saving_file_name variables.
Run the get_tweets.py

## Scrapping from Zillow
This code, [get_zillow.py](get_zillow.py) helps to scrap data from Zillow if the address is available.

### Dependencies
Install the following libraries.

```console
pip install pandas
```
```console
pip install bs4
```
### Running Code
Save the address in the text file. Please check the given file format.
Put the correct file names for file_name and saving_file_name variables.
Run the get_zillow.py

### Acknowledgement
This [tutorial](https://www.youtube.com/watch?v=pzptMqULnyE) was very helpful to complete the code for Zillow.

