# Instagram Spotify Bio Updater

This is a Python program that automatically updates your Instagram bio to show what you are listening to on Spotify. It's a cool way to share your music taste with your followers.


# BIG NOTES

You might get rate limited dont cry to me u can change wait value in line 96

I forgot that in lines 124-129 you need to fill out some oath stuff
simply get those parameters from the dev portal
just google it i forgot how i filled those
https://developer.spotify.com


## Installation

To install the necessary packages, run:

```
pip install -r requirements.txt
```

## Setup

1. Open the `setup.py` file and fill in your Instagram username and password. The setup file will dump a session ID, which prevents Instagram from blocking your login and saves you from having to log in every time you run the main program.

2. Run the following command to set up your session:

   ```
   python3 setup.py
   ```

3. In `main.py`, go to line 18 and add your Spotify refresh token. Refer to [this article](https://dev.to/sabareh/how-to-get-the-spotify-refresh-token-176) to learn how to get your Spotify refresh token.

4. If you encounter login issues, go to line 120 in `main.py` and fill in your Instagram username and password. This usually means that your setup was not done correctly.

## Usage

1. Open the `setup.py` file and fill in your Instagram username and password.

    The `setup.py` file dumps a session ID that prevents Instagram from blocking your login and saves you from logging in every time in `main.py`.

2. Run the `setup.py` file using the following command:

```bash
python3 setup.py
```

3. In `main.py`, go to line 18 and replace `YOUR_REFRESH_TOKEN` with your Spotify refresh token. Refer to [this guide](https://dev.to/sabareh/how-to-get-the-spotify-refresh-token-176) to get your refresh token.


Note that the access token is left blank as the program generates a new access token every time the token info is expired, which saves you from some headaches.

4. Run the `main.py` file using the following command:

```bash
python3 main.py
```

    If you can't log in, go to line 120 and fill in your username and password again. You probably did the setup wrong.

That's it! Your bio will now be updated automatically based on the song you're listening to on Spotify.

## Examples

Here's an example of how the bio will look with a long song name:

![Instagram Bio Example - Long Song Name](https://media.discordapp.net/attachments/621686347387764746/1101751027885158450/Screenshot_20230429-020507_Instagram.jpg?width=788&height=676)

And here's an example with a short song name:

![Instagram Bio Example - Short Song Name](https://media.discordapp.net/attachments/621686347387764746/1101751056653881444/Screenshot_20230429-012440_Instagram.jpg?width=971&height=676)

## Support

If you find this project useful, you can show your support by sending a donation to $psypolatic on Cash App.

## Concerns

If you have any concerns or issues with this program, you can reach out to the developer at joseml07@outlook.com.
