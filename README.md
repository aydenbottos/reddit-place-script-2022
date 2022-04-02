# Reddit Place Script 2022

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## About

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c0a2c23 (Update README)
This is a script to draw a JPG onto r/place (<https://www.reddit.com/r/place/>).

## Features

- Support for multiple accounts
- Determines the cooldown time remaining for each account
- Detects existing matching pixels on the r/place map and skips them
- Automatically converts colors to the r/place color palette
<<<<<<< HEAD
<<<<<<< HEAD
=======
Script to draw an image onto r/place (https://www.reddit.com/r/place/)
>>>>>>> 4a56f06 (Update README.md)
=======
Script to draw an image onto r/place (<https://www.reddit.com/r/place/>)
>>>>>>> 2118905 (Fetch cooldown, formatting changes (#22))
=======
>>>>>>> c0a2c23 (Update README)
=======
>>>>>>> 5511077 (Update README)

My Version of rdeepak2002's reddit bot, it's too different now to easily merge so i'm not going to bother, feel free to do it you're self though

## Changes(From the originally forked version)

- Multiple Account support (rdeepak2002 has it as well now)
- Getting the current board image and only drawing what's necessary (rdeepak2002 has it as well now)
- Transparency
=======
>>>>>>> d1213bc (Update README)

## Requirements

<<<<<<< HEAD
<<<<<<< HEAD
- [Python 3](https://www.python.org/downloads/)
- [A Reddit App Client ID and App Secret Key](https://www.reddit.com/prefs/apps)
=======
Python 3 (<https://www.python.org/downloads/>)
>>>>>>> 2118905 (Fetch cooldown, formatting changes (#22))
=======
- [Python 3](https://www.python.org/downloads/)
- [A Reddit App Client ID and App Secret Key](https://www.reddit.com/prefs/apps)
>>>>>>> c0a2c23 (Update README)

## How to Get App Client ID and App Secret Key

You need to generate an app client id and app secret key for each account in order to use this script.

Steps:

<<<<<<< HEAD
<<<<<<< HEAD
1. Visit <https://www.reddit.com/prefs/apps>
=======
1. Visit https://www.reddit.com/prefs/apps
>>>>>>> 521a14b (Scuffed multi account support)
=======
1. Visit https://www.reddit.com/prefs/apps
=======
1. Visit <https://www.reddit.com/prefs/apps>
>>>>>>> aa7e04c (Fetch cooldown, formatting changes (#22))
>>>>>>> 2118905 (Fetch cooldown, formatting changes (#22))
2. Click "create (another) app" button at very bottom
3. Select the "script" option and fill in the fields with anything

If you don't want to create a development app for each account, you can add each username as a developer in the developer app settings. You will need to duplicate the client ID and secret in .env, though.

## Python Package Requirements

Install requirements from 'requirements.txt' file.

```shell
pip3 install -r requirements.txt
```

## Get Started

Create a file called '.env'

Put in the following content:

```text
<<<<<<< HEAD
<<<<<<< HEAD
ENV_PLACE_USERNAME='["developer_username"]'
ENV_PLACE_PASSWORD='["developer_password"]'
ENV_PLACE_APP_CLIENT_ID='["app_client_id"]'
ENV_PLACE_SECRET_KEY='["app_secret_key"]'
=======
=======
>>>>>>> 3a4679a (Added support for multiple threads)
ENV_PLACE_USERNAME=["username","username2"]
ENV_PLACE_PASSWORD=["password","password2"]
ENV_PLACE_APP_CLIENT_ID=["app_client_id","app_client_id2"]
ENV_PLACE_SECRET_KEY=["app_secret_key","app_secret_key2"]
<<<<<<< HEAD
>>>>>>> 521a14b (Scuffed multi account support)
ENV_DRAW_X_START="x_position_start_integer"
ENV_DRAW_Y_START="y_position_start_integer"
<<<<<<< HEAD
ENV_R_START='["0"]'
ENV_C_START='["0"]'
=======
ENV_R_START="0"
ENV_C_START="0"
>>>>>>> 5ce334c (Add ability to specify starting row and starting column for image to draw from)
```

<<<<<<< HEAD
- ENV_PLACE_USERNAME is an array of usernames of developer accounts
- ENV_PLACE_PASSWORD is an array of the passwords of developer accounts
- ENV_PLACE_APP_CLIENT_ID is an array of the client ids for the app / script registered with Reddit
- ENV_PLACE_SECRET_KEY is an array of the secret keys for the app / script registered with Reddit
- ENV_DRAW_X_START specifies the x position to draw the image on the r/place canvas
- ENV_DRAW_Y_START specifies the y position to draw the image on the r/place canvas
- ENV_R_START is an array which specifies which x position of the original image to start at while drawing it
- ENV_C_START is an array which specifies which y position of the original image to start at while drawing it

Note: Multiple fields can be passed into the arrays to spawn a thread for each one.

Change image.jpg to specify what image to draw. One pixel is drawn every 5 minutes and only jpeg images are supported.
=======
Change unknown.png to specify what image to draw. Note: one pixel is drawn every 5 minutes per account
>>>>>>> 2191e27 (mroe just in case stuff, as well as updated readme slightly)
=======
=======
ENV_PLACE_USERNAME='["developer_username"]'
ENV_PLACE_PASSWORD='["developer_password"]'
ENV_PLACE_APP_CLIENT_ID='["app_client_id"]'
ENV_PLACE_SECRET_KEY='["app_secret_key"]'
>>>>>>> 12ab83e (Added support for multiple threads)
ENV_DRAW_X_START="x_position_start_integer"
ENV_DRAW_Y_START="y_position_start_integer"
ENV_R_START='["0"]'
ENV_C_START='["0"]'
```

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
Change unknown.png to specify what image to draw. Note: one pixel is drawn every 5 minutes per account
=======
=======
- ENV_PLACE_USERNAME is the username of the developer account
- ENV_PLACE_PASSWORD is the password of the developer account
- ENV_PLACE_APP_CLIENT_ID is the client id for the app / script registered with Reddit
- ENV_PLACE_SECRET_KEY is the secret key for the app / script registered with Reddit
=======
- ENV_PLACE_USERNAME is an array of usernames of developer accounts
- ENV_PLACE_PASSWORD is an array of the passwords of developer accounts
- ENV_PLACE_APP_CLIENT_ID is an array of the client ids for the app / script registered with Reddit
- ENV_PLACE_SECRET_KEY is an array of the secret keys for the app / script registered with Reddit
>>>>>>> aa7e04c (Fetch cooldown, formatting changes (#22))
- ENV_DRAW_X_START specifies the x position to draw the image on the r/place canvas
- ENV_DRAW_Y_START specifies the y position to draw the image on the r/place canvas
- ENV_R_START is an array which specifies which x position of the original image to start at while drawing it
- ENV_C_START is an array which specifies which y position of the original image to start at while drawing it

>>>>>>> 4c956a0 (Added support for multiple threads)
Note: Multiple fields can be passed into the arrays to spawn a thread for each one.

Change image.jpg to specify what image to draw. One pixel is drawn every 5 minutes and only jpeg images are supported.
>>>>>>> 12ab83e (Added support for multiple threads)
>>>>>>> 3a4679a (Added support for multiple threads)

## Run the Script

```python
python3 main.py
```

## Multiple Workers

If you want two threads drawing the image at once you could have a setup like this:

```text
<<<<<<< HEAD
<<<<<<< HEAD
ENV_PLACE_USERNAME='["developer_username_1", "developer_username_2"]'
=======
ENV_PLACE_USERNAME='["developer_username", "developer_username_2"]'
>>>>>>> 5cc71e0 (Update readme with instructions for multiple workers)
=======
ENV_PLACE_USERNAME='["developer_username_1", "developer_username_2"]'
>>>>>>> 2db7da6 (Update README.md)
ENV_PLACE_PASSWORD='["developer_password_1", "developer_password_2"]'
ENV_PLACE_APP_CLIENT_ID='["app_client_id_1", "app_client_id_2"]'
ENV_PLACE_SECRET_KEY='["app_secret_key_1", "app_secret_key_2"]'
ENV_DRAW_X_START="x_position_start_integer"
ENV_DRAW_Y_START="y_position_start_integer"
ENV_R_START='["0", "0"]'
ENV_C_START='["0", "50"]'
```

<<<<<<< HEAD
<<<<<<< HEAD
The same pattern can be used for multiple drawing at once. Note that the "ENV_PLACE_USERNAME", "ENV_PLACE_PASSWORD", "ENV_PLACE_APP_CLIENT_ID", "ENV_PLACE_SECRET_KEY", "ENV_R_START", and "ENV_C_START" variables MUST be string arrays of the same size.
=======
The same pattern can be used for 3 or more threads drawing at once. Note that the "ENV_PLACE_USERNAME", "ENV_PLACE_PASSWORD", "ENV_PLACE_APP_CLIENT_ID", "ENV_PLACE_SECRET_KEY", "ENV_R_START", and "ENV_C_START" variables should all be string arrays of the same size.
>>>>>>> 5cc71e0 (Update readme with instructions for multiple workers)
=======
The same pattern can be used for multiple drawing at once. Note that the "ENV_PLACE_USERNAME", "ENV_PLACE_PASSWORD", "ENV_PLACE_APP_CLIENT_ID", "ENV_PLACE_SECRET_KEY", "ENV_R_START", and "ENV_C_START" variables MUST be string arrays of the same size.
>>>>>>> c0a2c23 (Update README)

Also note that I did the following in the above example:

```text
ENV_R_START='["0", "0"]'
ENV_C_START='["0", "50"]'
```

<<<<<<< HEAD
<<<<<<< HEAD
In this case, the first worker will start drawing from (0, 0) and the second worker will start drawing from (0, 50) from the input image.jpg file.

This is useful if you want different threads drawing different parts of the image with different accounts.

If you'd like, you can enable Verbose Mode by editing the Python file. This will output a lot more information, and not neccessarily in the right order, but it is useful for development and debugging.
<<<<<<< HEAD
=======
In this case, the first worker will start drawing from (0, 0) and the second worker will start drawing from (0, 50) from the input image.jpg file. 

This is useful if you want different threads drawing different parts of the image with different accounts. 
<<<<<<< HEAD
>>>>>>> 5cc71e0 (Update readme with instructions for multiple workers)
=======
>>>>>>> 2db7da6 (Update README.md)
=======
In this case, the first worker will start drawing from (0, 0) and the second worker will start drawing from (0, 50) from the input image.jpg file.

This is useful if you want different threads drawing different parts of the image with different accounts.
>>>>>>> 2118905 (Fetch cooldown, formatting changes (#22))
=======
>>>>>>> c0a2c23 (Update README)
