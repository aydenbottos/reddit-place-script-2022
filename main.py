<<<<<<< HEAD
<<<<<<< HEAD
import os
import os.path
=======
=======
>>>>>>> 26695d5 (verbose mode to reduce output)
# imports
<<<<<<< HEAD
import os, random
<<<<<<< HEAD
>>>>>>> b567773 (stuff)
=======
=======
=======
>>>>>>> d0b24c3 (verbose mode to reduce output)
import os
import os.path
>>>>>>> d69811d (Add files via upload)
>>>>>>> 86a06e3 (Add files via upload)
import math
import requests
import json
import time
<<<<<<< HEAD
<<<<<<< HEAD
import threading
=======
>>>>>>> b567773 (stuff)
=======
>>>>>>> df71c41 (Added simple threading example)
from io import BytesIO
from websocket import create_connection
=======
import threading
<<<<<<< HEAD
>>>>>>> 1b25969 (Added simple threading example)
=======
from io import BytesIO
from websocket import create_connection
>>>>>>> 04a6a3f (Merge codebase to avoid writing correct color tile)
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from PIL import ImageColor
from PIL import Image
import random

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# set verbose mode to increase output (messy)
verbose_mode = False
=======
if(os.path.exists("./.env")):
=======
=======
# set verbose mode to increase output (messy)
verbose_mode = False

>>>>>>> 26695d5 (verbose mode to reduce output)
if os.path.exists("./.env"):
>>>>>>> 50654f5 (format with black)
    # load env variables
    load_dotenv()
else:
<<<<<<< HEAD
    print("No .env file found")
    exit()
>>>>>>> 86a06e3 (Add files via upload)
=======
    exit("No .env file found. Read the README")
>>>>>>> 26695d5 (verbose mode to reduce output)

<<<<<<< HEAD
if os.path.exists("./.env"):
    # load env variables
    load_dotenv()
else:
    envfile = open(".env", "w")
    envfile.write(
        """ENV_PLACE_USERNAME='["developer_username"]'
ENV_PLACE_PASSWORD='["developer_password"]'
ENV_PLACE_APP_CLIENT_ID='["app_client_id"]'
ENV_PLACE_SECRET_KEY='["app_secret_key"]'
ENV_DRAW_X_START="x_position_start_integer"
ENV_DRAW_Y_START="y_position_start_integer"
ENV_R_START='["0"]'
ENV_C_START='["0"]\'"""
    )
    print(
        "No .env file found. A template has been created for you.",
        "Read the README and configure it properly.",
        "Right now, it's full of example data, so you ABSOLUTELY MUST edit it.",
    )
    exit("Error: No .env file found")

=======
>>>>>>> c0dfb14 (Split code into functions for multithreading)
# map of colors for pixels you can place
color_map = {
    "#FF4500": 2,  # bright red
    "#FFA800": 3,  # orange
    "#FFD635": 4,  # yellow
    "#00A368": 6,  # darker green
    "#7EED56": 8,  # lighter green
    "#2450A4": 12,  # darkest blue
    "#3690EA": 13,  # medium normal blue
    "#51E9F4": 14,  # cyan
    "#811E9F": 18,  # darkest purple
    "#B44AC0": 19,  # normal purple
    "#FF99AA": 23,  # pink
    "#9C6926": 25,  # brown
    "#000000": 27,  # black
    "#898D90": 29,  # grey
    "#D4D7D9": 30,  # light grey
    "#FFFFFF": 31,  # white
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# map of pixel color ids to verbose name (for debugging)
name_map = {
    2: "Bright Red",
    3: "Orange",
    4: "Yellow",
    6: "Dark Green",
    8: "Light Green",
    12: "Dark Blue",
    13: "Blue",
    14: "Cyan",
    18: "Dark Purple",
    19: "Purple",
    23: "Pink",
    25: "Brown",
    27: "Black",
    29: "Grey",
    30: "Light Grey",
    31: "White",
}

=======
=======
>>>>>>> c0dfb14 (Split code into functions for multithreading)
=======
=======
=======
# map of pixel color ids to verbose name (for debugging)
name_map = {
    2: "Bright Red",
    3: "Orange",
    4: "Yellow",
    6: "Dark Green",
    8: "Light Green",
    12: "Dark Blue",
    13: "Blue",
    14: "Cyan",
    18: "Dark Purple",
    19: "Purple",
    23: "Pink",
    25: "Brown",
    27: "Black",
    29: "Grey",
    30: "Light Grey",
    31: "White",
}

>>>>>>> ed52c90 (Add User Readable Color Names to Log Messages (#29))
>>>>>>> fec2636 (Add User Readable Color Names to Log Messages (#29))
# color palette
rgb_colors_array = []

# auth variables
<<<<<<< HEAD
<<<<<<< HEAD
access_tokens = []
access_token_expires_at_timestamp = []
=======
access_token = None
access_token_expires_at_timestamp = math.floor(time.time())
>>>>>>> c0dfb14 (Split code into functions for multithreading)
=======
access_tokens = []
access_token_expires_at_timestamp = []
>>>>>>> 77301e6 (Attempting to fix multi threading via access token array)

# image.jpg information
pix = None
image_width = None
image_height = None

<<<<<<< HEAD
<<<<<<< HEAD
# place a pixel immediately
# first_run = True
first_run_counter = 0

# function to convert rgb tuple to hexadecimal string
=======
>>>>>>> 131f6a3 (a just in case error thing)
=======
=======
# place a pixel immediately
<<<<<<< HEAD
first_run = True
>>>>>>> e21509e (Added ability for script to place the first pixel immediately)

=======
# first_run = True
first_run_counter = 0
>>>>>>> 8050736 (Add counter to fix first run issue with multithreading)

# function to convert rgb tuple to hexadecimal string
>>>>>>> 6683491 (Split code into functions for multithreading)
>>>>>>> c0dfb14 (Split code into functions for multithreading)
def rgb_to_hex(rgb):
    return ("#%02x%02x%02x" % rgb).upper()


<<<<<<< HEAD
<<<<<<< HEAD
# Get a more verbose color indicator from a pixel color ID
def color_id_to_name(color_id):
    if color_id in name_map.keys():
        return "{} ({})".format(name_map[color_id], str(color_id))
    return "Invalid Color ({})".format(str(color_id))


=======
>>>>>>> c0dfb14 (Split code into functions for multithreading)
=======
# Get a more verbose color indicator from a pixel color ID
def color_id_to_name(color_id):
    if color_id in name_map.keys():
        return "{} ({})".format(name_map[color_id], str(color_id))
    return "Invalid Color ({})".format(str(color_id))


>>>>>>> fec2636 (Add User Readable Color Names to Log Messages (#29))
# function to find the closest rgb color from palette to a target rgb color
def closest_color(target_rgb, rgb_colors_array_in):
    r, g, b, a = target_rgb
    #print(r,g,b,a)
    if a < 255 or (r,g,b) == (69,42,0):
        return (69,42,0)
    color_diffs = []
    for color in rgb_colors_array_in:
        cr, cg, cb = color
        color_diff = math.sqrt((r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]


<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> c0dfb14 (Split code into functions for multithreading)
rgb_colors_array = []

for color_hex, color_index in color_map.items():
    rgb_array = ImageColor.getcolor(color_hex, "RGB")
    rgb_colors_array.append(rgb_array)

print("available colors (rgb): ", rgb_colors_array)

image_path = os.path.join(os.path.abspath(os.getcwd()), 'unknown.png')
im = Image.open(image_path)

pix = im.load()
print("image size: ", im.size)  # Get the width and hight of the image for iterating over
image_width, image_height = im.size

# test drawing image to file called new_image before drawing to r/place
current_r = int(os.getenv('ENV_R_START'))
current_c = int(os.getenv('ENV_C_START'))

while True:
    r = current_r
    c = current_c

    target_rgb = pix[r, c]
    new_rgb = closest_color(target_rgb, rgb_colors_array)
    # print("closest color: ", new_rgb)
    pix[r, c] = new_rgb

    current_r += 1

    if current_r >= image_width:
        current_c += 1
        current_r = 0

    if current_c >= image_height:
        print("done drawing image locally to new_image.png")
        break

new_image_path = os.path.join(os.path.abspath(os.getcwd()), 'new_image.png')
im.save(new_image_path)

# developer's reddit username and password
#username = os.getenv('ENV_PLACE_USERNAME')
#password = os.getenv('ENV_PLACE_PASSWORD')
# note: use https://www.reddit.com/prefs/apps
#app_client_id = os.getenv('ENV_PLACE_APP_CLIENT_ID')
#secret_key = os.getenv('ENV_PLACE_SECRET_KEY')
accounts = {
}

# this is horrible, but i'm too lazy to make it not bad
def fill_accounts():
    print("aaaa",len(json.loads(os.getenv('ENV_PLACE_USERNAME'))),
        len(json.loads(os.getenv('ENV_PLACE_PASSWORD'))),
        len(json.loads(os.getenv('ENV_PLACE_APP_CLIENT_ID'))),
        len(json.loads(os.getenv('ENV_PLACE_SECRET_KEY'))))

    if len(json.loads(os.getenv('ENV_PLACE_USERNAME'))) != (len(json.loads(os.getenv('ENV_PLACE_USERNAME'))) + len(json.loads(os.getenv('ENV_PLACE_PASSWORD'))) + len(json.loads(os.getenv('ENV_PLACE_APP_CLIENT_ID'))) + len(json.loads(os.getenv('ENV_PLACE_SECRET_KEY'))))/4:
        print("Your .env file is messed up")
        quit()

    i = 0
    for name in json.loads(os.getenv('ENV_PLACE_USERNAME')):
        account = {
            "password": json.loads(os.getenv('ENV_PLACE_PASSWORD'))[i],
            "app_client_id": json.loads(os.getenv('ENV_PLACE_APP_CLIENT_ID'))[i],
            "secret_key": json.loads(os.getenv('ENV_PLACE_SECRET_KEY'))[i],
            "access_token": None,
            "access_token_type": "",
            "expires_at_timestamp": 0,
            "access_token_scope": "",
        }

        accounts[name] = account

        i += 1

# note: reddit limits us to place 1 pixel every 5 minutes, so I am setting it to 5 minutes and 30 seconds per pixel
pixel_place_frequency = 320

# global variables for script
access_token = None
current_timestamp = math.floor(time.time())
#last_time_placed_pixel = math.floor(time.time())-310 # Uncomment to make start instantly
access_token_expires_at_timestamp = math.floor(time.time())

def get_valid_auth(name):
    #print(name,accounts[name])
    #print(accounts[name]['access_token'] is None, current_timestamp >= accounts[name]['expires_at_timestamp'])
    # refresh access token if necessary
    if accounts[name]['access_token'] is None or current_timestamp >= accounts[name]['expires_at_timestamp']:
        print("refreshing access token for",name,"...")

        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; PPC Mac OS X 10_8_7 rv:5.0; en-US) AppleWebKit/533.31.5 (KHTML, like Gecko) Version/4.0 Safari/533.31.5',
        }

        data = {
            'grant_type': 'password',
            'username': name,
            'password': accounts[name]['password']
        }

        r = requests.post("https://ssl.reddit.com/api/v1/access_token",
                          data=data,
                          auth=HTTPBasicAuth(accounts[name]['app_client_id'], accounts[name]['secret_key']),
                          headers=headers)

        print("received response: ", r.text)

        response_data = r.json()

        accounts[name]['access_token'] = response_data["access_token"]
        accounts[name]['access_token_type'] = response_data["token_type"]  # this is just "bearer"
        accounts[name]['expires_at_timestamp'] = current_timestamp + int(response_data["expires_in"])  # this is usually "3600"
        accounts[name]['access_token_scope'] = response_data["scope"]  # this is usually "*"

        print("received new access token: ", accounts[name]['access_token'])


fill_accounts()

error_count = 0
error_limit = 10

>>>>>>> b567773 (stuff)
# method to draw a pixel at an x, y coordinate in r/place with a specific color
<<<<<<< HEAD
def set_pixel_and_check_ratelimit(
    access_token_in, x, y, color_index_in=18, canvas_index=0
):
    print("placing " + color_id_to_name(color_index_in) + " pixel at " + str((x, y)))
=======
def set_pixel(access_token_in, x, y, color_index_in=18, canvas_index=0):
    global error_count
    global error_limit
    print("placing pixel")
<<<<<<< HEAD
>>>>>>> 2191e27 (mroe just in case stuff, as well as updated readme slightly)
=======
=======
# method to draw a pixel at an x, y coordinate in r/place with a specific color
<<<<<<< HEAD
def set_pixel(access_token_in, x, y, color_index_in=18, canvas_index=0):
    print("placing pixel with color index " + str(color_index_in) + " at " + str((x, y)))
>>>>>>> 6683491 (Split code into functions for multithreading)
<<<<<<< HEAD
>>>>>>> c0dfb14 (Split code into functions for multithreading)
=======
=======
def set_pixel_and_check_ratelimit(
    access_token_in, x, y, color_index_in=18, canvas_index=0
):
<<<<<<< HEAD
    print(
        "placing "
        + color_id_to_name(color_index_in)
        + " pixel at "
        + str((x, y))
    )
>>>>>>> aa7e04c (Fetch cooldown, formatting changes (#22))
<<<<<<< HEAD
>>>>>>> 2118905 (Fetch cooldown, formatting changes (#22))
=======
=======
    print("placing " + color_id_to_name(color_index_in) + " pixel at " + str((x, y)))
>>>>>>> 1f2969e (Automatically format with Black)
>>>>>>> bae7e48 (Automatically format with Black)

    url = "https://gql-realtime-2.reddit.com/query"

    payload = json.dumps(
        {
            "operationName": "setPixel",
            "variables": {
                "input": {
                    "actionName": "r/replace:set_pixel",
                    "PixelMessageData": {
                        "coordinate": {"x": x, "y": y},
                        "colorIndex": color_index_in,
                        "canvasIndex": canvas_index,
                    },
                }
            },
            "query": "mutation setPixel($input: ActInput!) {\n  act(input: $input) {\n    data {\n      ... on BasicMessage {\n        id\n        data {\n          ... on GetUserCooldownResponseMessageData {\n            nextAvailablePixelTimestamp\n            __typename\n          }\n          ... on SetPixelResponseMessageData {\n            timestamp\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
        }
    )
    headers = {
        "origin": "https://hot-potato.reddit.com",
        "referer": "https://hot-potato.reddit.com/",
        "apollographql-client-name": "mona-lisa",
        "Authorization": "Bearer " + access_token_in,
        "Content-Type": "application/json",
    }

    response = requests.request("POST", url, headers=headers, data=payload)
<<<<<<< HEAD
<<<<<<< HEAD
    if verbose_mode:
        print("received response: ", response.text)
    # There are 2 different JSON keys for responses to get the next timestamp.
    # If we don't get data, it means we've been rate limited.
    # If we do, a pixel has been successfully placed.
    if response.json()["data"] == None:
        waitTime = math.floor(
            response.json()["errors"][0]["extensions"]["nextAvailablePixelTs"]
        )
        print("placing failed: rate limited")
    else:
        waitTime = math.floor(
            response.json()["data"]["act"]["data"][0]["data"][
                "nextAvailablePixelTimestamp"
            ]
        )
        print("placing succeeded")
=======
<<<<<<< HEAD
>>>>>>> 26695d5 (verbose mode to reduce output)
=======
<<<<<<< HEAD
>>>>>>> ec9701b (maybe fix verbose mode going too fast)

<<<<<<< HEAD
<<<<<<< HEAD
    # THIS COMMENTED CODE LETS YOU DEBUG THREADS FOR TESTING
    # Works perfect with one thread.
    # With multiple threads, every time you press Enter you move to the next one.
    # Move the code anywhere you want, I put it here to inspect the API responses.

    # import code

    # code.interact(local=locals())

    # Reddit returns time in ms and we need seconds, so divide by 1000
    return waitTime / 1000
=======
=======
>>>>>>> df71c41 (Added simple threading example)
    print(response.text)
    if 'errors' in json.loads(response.text):
        error_count += 1
        if error_count > error_limit:
            print("Some thing bad has happened, you've passed the error limit")
            quit()
        print("that's probably not good",error_count,"error(s)")
<<<<<<< HEAD
>>>>>>> 131f6a3 (a just in case error thing)
=======
=======
    print("received response: ", response.text)
<<<<<<< HEAD
>>>>>>> 1b25969 (Added simple threading example)
<<<<<<< HEAD
>>>>>>> df71c41 (Added simple threading example)
=======
=======
=======
    if verbose:
=======
    if verbose_mode:
>>>>>>> 8fa288e (maybe fix verbose mode going too fast)
        print("received response: ", response.text)
>>>>>>> d0b24c3 (verbose mode to reduce output)
    # There are 2 different JSON keys for responses to get the next timestamp.
    # If we don't get data, it means we've been rate limited.
    # If we do, a pixel has been successfully placed.
    if response.json()["data"] == None:
        waitTime = math.floor(
            response.json()["errors"][0]["extensions"]["nextAvailablePixelTs"]
        )
        print("placing failed: rate limited")
    else:
        waitTime = math.floor(
            response.json()["data"]["act"]["data"][0]["data"][
                "nextAvailablePixelTimestamp"
            ]
        )
        print("placing succeeded")

    # THIS COMMENTED CODE LETS YOU DEBUG THREADS FOR TESTING
    # Works perfect with one thread.
    # With multiple threads, every time you press Enter you move to the next one.
    # Move the code anywhere you want, I put it here to inspect the API responses.

    # import code

    # code.interact(local=locals())

    # Reddit returns time in ms and we need seconds, so divide by 1000
    return waitTime / 1000
>>>>>>> aa7e04c (Fetch cooldown, formatting changes (#22))
>>>>>>> 2118905 (Fetch cooldown, formatting changes (#22))

<<<<<<< HEAD
<<<<<<< HEAD
def get_board(bearer):
    print("Getting board")
    ws = create_connection("wss://gql-realtime-2.reddit.com/query")
    ws.send(json.dumps({"type":"connection_init","payload":{"Authorization":"Bearer "+bearer}}))
=======
def get_board(access_token_in):
    print("Getting board")
    ws = create_connection("wss://gql-realtime-2.reddit.com/query")
    ws.send(json.dumps({"type":"connection_init","payload":{"Authorization":"Bearer "+ access_token_in}}))
>>>>>>> 04a6a3f (Merge codebase to avoid writing correct color tile)
=======

def get_board(access_token_in):
    print("Getting board")
    ws = create_connection(
        "wss://gql-realtime-2.reddit.com/query", origin="https://hot-potato.reddit.com"
    )
    ws.send(
        json.dumps(
            {
                "type": "connection_init",
                "payload": {"Authorization": "Bearer " + access_token_in},
            }
        )
    )
>>>>>>> 87cbded (format with black)
    ws.recv()
    ws.send(
        json.dumps(
            {
                "id": "1",
                "type": "start",
                "payload": {
                    "variables": {
                        "input": {
                            "channel": {
                                "teamOwner": "AFD2022",
                                "category": "CONFIG",
                            }
                        }
                    },
                    "extensions": {},
                    "operationName": "configuration",
                    "query": "subscription configuration($input: SubscribeInput!) {\n  subscribe(input: $input) {\n    id\n    ... on BasicMessage {\n      data {\n        __typename\n        ... on ConfigurationMessageData {\n          colorPalette {\n            colors {\n              hex\n              index\n              __typename\n            }\n            __typename\n          }\n          canvasConfigurations {\n            index\n            dx\n            dy\n            __typename\n          }\n          canvasWidth\n          canvasHeight\n          __typename\n        }\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
                },
            }
        )
    )
    ws.recv()
    ws.send(
        json.dumps(
            {
                "id": "2",
                "type": "start",
                "payload": {
                    "variables": {
                        "input": {
                            "channel": {
                                "teamOwner": "AFD2022",
                                "category": "CANVAS",
                                "tag": "0",
                            }
                        }
                    },
                    "extensions": {},
                    "operationName": "replace",
                    "query": "subscription replace($input: SubscribeInput!) {\n  subscribe(input: $input) {\n    id\n    ... on BasicMessage {\n      data {\n        __typename\n        ... on FullFrameMessageData {\n          __typename\n          name\n          timestamp\n        }\n        ... on DiffFrameMessageData {\n          __typename\n          name\n          currentTimestamp\n          previousTimestamp\n        }\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
                },
            }
        )
    )

    file = ""
    while True:
        temp = json.loads(ws.recv())
<<<<<<< HEAD
        if temp['type'] == 'data':
            msg = temp['payload']['data']['subscribe']
            if msg['data']['__typename'] == 'FullFrameMessageData':
                file = msg['data']['name']
                break;
<<<<<<< HEAD
    ws.close()

    img = BytesIO(requests.get(file, stream = True).content)
    print("Got image:", file)

    return img

def get_unset_pixel(img):
    x = 0
    y= 0
    pix2 = Image.open(img).convert('RGB').load()
    everything_done = False
=======

=======
        if temp["type"] == "data":
            msg = temp["payload"]["data"]["subscribe"]
            if msg["data"]["__typename"] == "FullFrameMessageData":
                file = msg["data"]["name"]
                break
>>>>>>> 87cbded (format with black)

    ws.close()

    boardimg = BytesIO(requests.get(file, stream=True).content)
    print("Got image:", file)

    return boardimg


def get_unset_pixel(boardimg, x, y):
<<<<<<< HEAD
    pixel_x_start = int(os.getenv('ENV_DRAW_X_START'))
    pixel_y_start = int(os.getenv('ENV_DRAW_Y_START'))
    pix2 = Image.open(boardimg).convert('RGB').load()
>>>>>>> 04a6a3f (Merge codebase to avoid writing correct color tile)
=======
    pixel_x_start = int(os.getenv("ENV_DRAW_X_START"))
    pixel_y_start = int(os.getenv("ENV_DRAW_Y_START"))
    pix2 = Image.open(boardimg).convert("RGB").load()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 87cbded (format with black)
=======
    num_loops=0
>>>>>>> 34389bf (Allow get_unset_pixel to loop)
=======
    num_loops = 0
>>>>>>> 8581a3a (Automatically format with Black)
=======
    num_loops=0
>>>>>>> 48608c6 (Set values to 0 instead of canvas coordinates)
    while True:
        x += 1

        if x >= image_width:
            y += 1
            x = 0

        if y >= image_height:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            time.sleep(30)
            everything_done = True
            x = 0
            y = 0

        #print(x+pixel_x_start,y+pixel_y_start)
        #print(x, y,"img",image_width,image_height)
        target_rgb = pix[x, y]
        new_rgb = closest_color(target_rgb, rgb_colors_array)
        if pix2[x+pixel_x_start,y+pixel_y_start] != new_rgb:
            #print(pix2[x+pixel_x_start,y+pixel_y_start], new_rgb,new_rgb != (69,42,0), pix2[x,y] != new_rgb)
            if new_rgb != (69,42,0):
                print("Different Pixel found at:",x+pixel_x_start,y+pixel_y_start,"With Color:",pix2[x+pixel_x_start,y+pixel_y_start],"Replacing with:",new_rgb)
                pix2[x+pixel_x_start,y+pixel_y_start] = new_rgb
                break;
            else:
                pass#print("TransparrentPixel")
        elif everything_done:
            if new_rgb != (69,42,0):
                print("Nothing to do")
                pix2[x+pixel_x_start,y+pixel_y_start] = new_rgb
                break;
            else:
                pass#print("TransparrentPixel")
=======
            break;
=======
            break
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 87cbded (format with black)

        print(x + pixel_x_start, y + pixel_y_start)
        print(x, y, "boardimg", image_width, image_height)
=======
        if verbose:
=======
=======
            if num_loops > 1:
<<<<<<< HEAD
<<<<<<< HEAD
                target_rgb=pix[pixel_x_start,pixel_y_start]
                new_rgb=closest_color(target_rgb, rgb_colors_array)
                return pixel_x_start,pixel_y_start,new_rgb
            y=pixel_y_start
            num_loops+=1;
>>>>>>> 34389bf (Allow get_unset_pixel to loop)
=======
                target_rgb = pix[pixel_x_start, pixel_y_start]
                new_rgb = closest_color(target_rgb, rgb_colors_array)
                return pixel_x_start, pixel_y_start, new_rgb
            y = pixel_y_start
            num_loops += 1
>>>>>>> 8581a3a (Automatically format with Black)
=======
                target_rgb=pix[0,0]
                new_rgb=closest_color(target_rgb, rgb_colors_array)
                return 0,0,new_rgb
            y=0
            num_loops+=1;
>>>>>>> 48608c6 (Set values to 0 instead of canvas coordinates)
        if verbose_mode:
>>>>>>> 8fa288e (maybe fix verbose mode going too fast)
            print(x + pixel_x_start, y + pixel_y_start)
            print(x, y, "boardimg", image_width, image_height)
>>>>>>> d0b24c3 (verbose mode to reduce output)
        target_rgb = pix[x, y]
        new_rgb = closest_color(target_rgb, rgb_colors_array)
        if pix2[x + pixel_x_start, y + pixel_y_start] != new_rgb:
            if verbose_mode:
                print(
                    pix2[x + pixel_x_start, y + pixel_y_start],
                    new_rgb,
                    new_rgb != (69, 42, 0),
                    pix2[x, y] != new_rgb,
                )
            if new_rgb != (69, 42, 0):
                if verbose_mode:
                    print(
                        "Different Pixel found at:",
                        x + pixel_x_start,
                        y + pixel_y_start,
                        "With Color:",
                        pix2[x + pixel_x_start, y + pixel_y_start],
                        "Replacing with:",
                        new_rgb,
                    )
                break
            else:
                print("TransparrentPixel")
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04a6a3f (Merge codebase to avoid writing correct color tile)
    return x,y
=======
    return x,y,new_rgb
>>>>>>> a625de8 (Use color selected in the get_unset_pixel function)
=======
    return x, y, new_rgb

>>>>>>> 87cbded (format with black)

<<<<<<< HEAD
<<<<<<< HEAD
def get_board(access_token_in):
    print("Getting board")
    ws = create_connection(
        "wss://gql-realtime-2.reddit.com/query", origin="https://hot-potato.reddit.com"
    )
    ws.send(
        json.dumps(
            {
                "type": "connection_init",
                "payload": {"Authorization": "Bearer " + access_token_in},
            }
        )
    )
    ws.recv()
    ws.send(
        json.dumps(
            {
                "id": "1",
                "type": "start",
                "payload": {
                    "variables": {
                        "input": {
                            "channel": {
                                "teamOwner": "AFD2022",
                                "category": "CONFIG",
                            }
                        }
                    },
                    "extensions": {},
                    "operationName": "configuration",
                    "query": "subscription configuration($input: SubscribeInput!) {\n  subscribe(input: $input) {\n    id\n    ... on BasicMessage {\n      data {\n        __typename\n        ... on ConfigurationMessageData {\n          colorPalette {\n            colors {\n              hex\n              index\n              __typename\n            }\n            __typename\n          }\n          canvasConfigurations {\n            index\n            dx\n            dy\n            __typename\n          }\n          canvasWidth\n          canvasHeight\n          __typename\n        }\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
                },
            }
        )
    )
    ws.recv()
    ws.send(
        json.dumps(
            {
                "id": "2",
                "type": "start",
                "payload": {
                    "variables": {
                        "input": {
                            "channel": {
                                "teamOwner": "AFD2022",
                                "category": "CANVAS",
                                "tag": "0",
                            }
                        }
                    },
                    "extensions": {},
                    "operationName": "replace",
                    "query": "subscription replace($input: SubscribeInput!) {\n  subscribe(input: $input) {\n    id\n    ... on BasicMessage {\n      data {\n        __typename\n        ... on FullFrameMessageData {\n          __typename\n          name\n          timestamp\n        }\n        ... on DiffFrameMessageData {\n          __typename\n          name\n          currentTimestamp\n          previousTimestamp\n        }\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
                },
            }
        )
    )

    file = ""
    while True:
        temp = json.loads(ws.recv())
        if temp["type"] == "data":
            msg = temp["payload"]["data"]["subscribe"]
            if msg["data"]["__typename"] == "FullFrameMessageData":
                file = msg["data"]["name"]
                break

    ws.close()

    boardimg = BytesIO(requests.get(file, stream=True).content)
    print("Got image:", file)

    return boardimg


def get_unset_pixel(boardimg, x, y):
    pixel_x_start = int(os.getenv("ENV_DRAW_X_START"))
    pixel_y_start = int(os.getenv("ENV_DRAW_Y_START"))
    pix2 = Image.open(boardimg).convert("RGB").load()
    num_loops = 0
    while True:
        x += 1
=======
# current pixel row and pixel column being drawn
current_r = 0
current_c = 0
=======
# method to define the color palette array
def init_rgb_colors_array():
    global rgb_colors_array
>>>>>>> c0dfb14 (Split code into functions for multithreading)

<<<<<<< HEAD
<<<<<<< HEAD
# loop to keep refreshing tokens when necessary and to draw pixels when the time is right
while True:
<<<<<<< HEAD
    current_timestamp = math.floor(time.time())
>>>>>>> b567773 (stuff)

        if x >= image_width:
            y += 1
            x = 0

<<<<<<< HEAD
        if y >= image_height:
            if num_loops > 1:
                target_rgb = pix[0, 0]
                new_rgb = closest_color(target_rgb, rgb_colors_array)
                return 0, 0, new_rgb
            y = 0
            num_loops += 1
        if verbose_mode:
            print(x + pixel_x_start, y + pixel_y_start)
            print(x, y, "boardimg", image_width, image_height)
        target_rgb = pix[x, y]
=======
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; PPC Mac OS X 10_8_7 rv:5.0; en-US) AppleWebKit/533.31.5 (KHTML, like Gecko) Version/4.0 Safari/533.31.5',
        }
=======
    placing = False

    #does things
    for name, info in accounts.items():
        current_timestamp = math.floor(time.time())
        get_valid_auth(name)

        # draw pixel onto screen
        if info['access_token'] is not None:# and (current_timestamp >= last_time_placed_pixel + pixel_place_frequency or placing):
            # get current pixel position from input image
>>>>>>> 521a14b (Scuffed multi account support)

            # this is probably really bad, and reddit will probably not like it
            # I need to update this to be better, but i am lazy
            board = get_board(info['access_token'])
            r, c = get_unset_pixel(board)

            target_rgb = pix[r, c]
            # get converted color
            new_rgb = closest_color(target_rgb, rgb_colors_array)
            new_rgb_hex = rgb_to_hex(new_rgb)
            pixel_color_index = color_map[new_rgb_hex]

            print("\nAccount Placing: ",name,"\n")

            # draw the pixel onto r/place
            try:
                set_pixel(info['access_token'], pixel_x_start + r, pixel_y_start + c, pixel_color_index)
            except Exception as e:
                print(e)

            if not placing:
                last_time_placed_pixel = math.floor(time.time())

            current_r += 1
            current_c += 1

            # go back to first column when reached end of a row while drawing
            if current_r >= image_width:
                current_r = 0
            placing = True

            # exit when all pixels drawn
            if current_c >= image_height:
                print("done drawing image to r/place")
                current_c = 0

<<<<<<< HEAD
<<<<<<< HEAD
    # draw pixel onto screen
    if access_token is not None and current_timestamp >= last_time_placed_pixel + pixel_place_frequency:
        # get current pixel position from input image
        r, c = get_unset_pixel(get_board(access_token))

        target_rgb = pix[r, c]
        # get converted color
>>>>>>> b567773 (stuff)
        new_rgb = closest_color(target_rgb, rgb_colors_array)
        if pix2[x + pixel_x_start, y + pixel_y_start] != new_rgb:
            if verbose_mode:
                print(
                    pix2[x + pixel_x_start, y + pixel_y_start],
                    new_rgb,
                    new_rgb != (69, 42, 0),
                    pix2[x, y] != new_rgb,
                )
            if new_rgb != (69, 42, 0):
                if verbose_mode:
                    print(
                        "Different Pixel found at:",
                        x + pixel_x_start,
                        y + pixel_y_start,
                        "With Color:",
                        pix2[x + pixel_x_start, y + pixel_y_start],
                        "Replacing with:",
                        new_rgb,
                    )
                break
            else:
                print("TransparrentPixel")
    return x, y, new_rgb

<<<<<<< HEAD

# method to define the color palette array
def init_rgb_colors_array():
    global rgb_colors_array

    # generate array of available rgb colors we can use
    for color_hex, color_index in color_map.items():
        rgb_array = ImageColor.getcolor(color_hex, "RGB")
        rgb_colors_array.append(rgb_array)
    if verbose_mode:
        print("available colors for palette (rgb): ", rgb_colors_array)


# method to read the input image.jpg file
def load_image():
    global pix
    global image_width
    global image_height
    # read and load the image to draw and get its dimensions
    image_path = os.path.join(os.path.abspath(os.getcwd()), "image.jpg")
    im = Image.open(image_path)
    pix = im.load()
    print(
        "image size: ", im.size
    )  # Get the width and height of the image for iterating over
    image_width, image_height = im.size


# task to draw the input image
def task(credentials_index):
    # whether image should keep drawing itself
    repeat_forever = True

    while True:
        # try:
        # global variables for script
=======
        print(pixel_color_index)

        # draw the pixel onto r/place
        set_pixel(access_token, pixel_x_start + r, pixel_y_start + c, pixel_color_index)
>>>>>>> b567773 (stuff)
        last_time_placed_pixel = math.floor(time.time())

        # note: reddit limits us to place 1 pixel every 5 minutes, so I am setting it to
        # 5 minutes and 30 seconds per pixel
        # pixel_place_frequency = 330
        pixel_place_frequency = 330

        # pixel drawing preferences
        pixel_x_start = int(os.getenv("ENV_DRAW_X_START"))
        pixel_y_start = int(os.getenv("ENV_DRAW_Y_START"))

<<<<<<< HEAD
        try:
            # current pixel row and pixel column being drawn
            current_r = int(json.loads(os.getenv("ENV_R_START"))[credentials_index])
            current_c = int(json.loads(os.getenv("ENV_C_START"))[credentials_index])
        except IndexError:
            print(
                "Array length error: are you sure you have an ENV_R_START and ENV_C_START item for every account?\n",
                "Example for 5 accounts:\n",
                'ENV_R_START=\'["0","5","6","7","9"]\'\n',
                'ENV_C_START=\'["0","5","6","8","9"]\'\n',
                "Note: There can be duplicate entries, but every array must have the same amount of items.",
            )
            exit(1)

        # string for time until next pixel is drawn
        update_str = ""

        # reference to globally shared variables such as auth token and image
        global access_tokens
        global access_token_expires_at_timestamp

        # boolean to place a pixel the moment the script is first run
        # global first_run
        global first_run_counter

        # refresh auth tokens and / or draw a pixel
        while True:
            # reduce CPU usage
            time.sleep(1)

            # get the current time
            current_timestamp = math.floor(time.time())

            # log next time until drawing
            time_until_next_draw = (
                last_time_placed_pixel + pixel_place_frequency - current_timestamp
            )
            new_update_str = (
                str(time_until_next_draw) + " seconds until next pixel is drawn"
            )
            if update_str != new_update_str and time_until_next_draw % 10 == 0:
                update_str = new_update_str
                print(
                    "-------Thread #"
                    + str(credentials_index)
                    + "-------\n"
                    + update_str
                )

            # refresh access token if necessary
            if (
                access_tokens[credentials_index] is None
                or current_timestamp
                >= access_token_expires_at_timestamp[credentials_index]
            ):
                print(
                    "-------Thread #"
                    + str(credentials_index)
                    + "-------\n"
                    + "Refreshing access token..."
                )

                # developer's reddit username and password
                try:
                    username = json.loads(os.getenv("ENV_PLACE_USERNAME"))[
                        credentials_index
                    ]
                    password = json.loads(os.getenv("ENV_PLACE_PASSWORD"))[
                        credentials_index
                    ]
                    # note: use https://www.reddit.com/prefs/apps
                    app_client_id = json.loads(os.getenv("ENV_PLACE_APP_CLIENT_ID"))[
                        credentials_index
                    ]
                    secret_key = json.loads(os.getenv("ENV_PLACE_SECRET_KEY"))[
                        credentials_index
                    ]
                except IndexError:
                    print(
                        "Array length error: are you sure your credentials have an equal amount of items?\n",
                        "Example for 2 accounts:\n",
                        'ENV_PLACE_USERNAME=\'["Username1", "Username2]\'\n',
                        'ENV_PLACE_PASSWORD=\'["Password", "Password"]\'\n',
                        'ENV_PLACE_APP_CLIENT_ID=\'["NBVSIBOPVAINCVIAVBOVV", "VNOPSNSJVQNVNJVSNVDV"]\'\n',
                        'ENV_PLACE_SECRET_KEY=\'["INSVDSINDJV_SVTNNJSNVNJV", "ANIJCINLLPJCSCOJNCA_ASDV"]\'\n',
                        "Note: There can be duplicate entries, but every array must have the same amount of items.",
                    )
                    exit(1)

                data = {
                    "grant_type": "password",
                    "username": username,
                    "password": password,
                }

                r = requests.post(
                    "https://ssl.reddit.com/api/v1/access_token",
                    data=data,
                    auth=HTTPBasicAuth(app_client_id, secret_key),
                    headers={"User-agent": f"placebot{random.randint(1, 100000)}"},
                )

                if verbose_mode:
                    print("received response: ", r.text)

                response_data = r.json()
                access_tokens[credentials_index] = response_data["access_token"]
                # access_token_type = response_data["token_type"]  # this is just "bearer"
                access_token_expires_in_seconds = response_data[
                    "expires_in"
                ]  # this is usually "3600"
                # access_token_scope = response_data["scope"]  # this is usually "*"

                # ts stores the time in seconds
                access_token_expires_at_timestamp[
                    credentials_index
                ] = current_timestamp + int(access_token_expires_in_seconds)

                print(
                    "received new access token: ",
                    access_tokens[credentials_index],
                )

            # draw pixel onto screen
            if access_tokens[credentials_index] is not None and (
                current_timestamp >= last_time_placed_pixel + pixel_place_frequency
                or first_run_counter <= credentials_index
            ):

                # place pixel immediately
                # first_run = False
                first_run_counter += 1

                # get target color
                # target_rgb = pix[current_r, current_c]

                # get current pixel position from input image and replacement color
                current_r, current_c, new_rgb = get_unset_pixel(
                    get_board(access_tokens[credentials_index]),
                    current_r,
                    current_c,
                )

                # get converted color
                new_rgb_hex = rgb_to_hex(new_rgb)
                pixel_color_index = color_map[new_rgb_hex]

                # draw the pixel onto r/place
                last_time_placed_pixel = set_pixel_and_check_ratelimit(
                    access_tokens[credentials_index],
                    pixel_x_start + current_r,
                    pixel_y_start + current_c,
                    pixel_color_index,
                )

                current_r += 1

                # go back to first column when reached end of a row while drawing
                if current_r >= image_width:
                    current_r = 0
                    current_c += 1

                # exit when all pixels drawn
                if current_c >= image_height:
                    print(
                        "--------Thread #"
                        + str(credentials_index)
                        + "--------\n"
                        + "done drawing image to r/place\n"
                    )
                    break
        # except:
        #     print("__________________")
        #     print("Thread #" + str(credentials_index))
        #     print("Error refreshing tokens or drawing pixel")
        #     print("Trying again in 5 minutes...")
        #     print("__________________")
        #     time.sleep(5 * 60)

        if not repeat_forever:
            break


# get color palette
init_rgb_colors_array()

# load the pixels for the input image
load_image()

# get number of concurrent threads to start
num_credentials = len(json.loads(os.getenv("ENV_PLACE_USERNAME")))

# define delay between starting new threads
if os.getenv("ENV_THREAD_DELAY") != None:
    delay_between_launches_seconds = int(os.getenv("ENV_THREAD_DELAY"))
else:
    delay_between_launches_seconds = 3

# launch a thread for each account specified in .env
for i in range(num_credentials):
    # run the image drawing task
    access_tokens.append(None)
    access_token_expires_at_timestamp.append(math.floor(time.time()))
    thread1 = threading.Thread(target=task, args=[i])
    thread1.start()
    time.sleep(delay_between_launches_seconds)
=======
        # exit when all pixels drawn
        if current_c >= image_height:
            print("done drawing image to r/place")
            current_c = 0
            exit(0)
<<<<<<< HEAD
    time.sleep(10000)
>>>>>>> b567773 (stuff)
=======
=======
        time.sleep(pixel_place_frequency/len(accounts))
>>>>>>> 521a14b (Scuffed multi account support)
=======
        time.sleep((pixel_place_frequency/len(accounts))+2)
>>>>>>> f48745b (Slight changes)
    time.sleep(10)
<<<<<<< HEAD
>>>>>>> f1820df (fuck)
=======
=======
# whether image should keep drawing itself
repeat_forever = True
=======
    # generate array of available rgb colors we can use
    for color_hex, color_index in color_map.items():
        rgb_array = ImageColor.getcolor(color_hex, "RGB")
        rgb_colors_array.append(rgb_array)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6683491 (Split code into functions for multithreading)

    print("available colors for palette (rgb): ", rgb_colors_array)
=======
    if verbose:
=======
    if verbose_mode:
>>>>>>> 8fa288e (maybe fix verbose mode going too fast)
        print("available colors for palette (rgb): ", rgb_colors_array)
>>>>>>> d0b24c3 (verbose mode to reduce output)


# method to read the input image.jpg file
def load_image():
    global pix
    global image_width
    global image_height
    # read and load the image to draw and get its dimensions
    image_path = os.path.join(os.path.abspath(os.getcwd()), "image.jpg")
    im = Image.open(image_path)
    pix = im.load()
    print(
        "image size: ", im.size
    )  # Get the width and height of the image for iterating over
    image_width, image_height = im.size


# task to draw the input image
def task(credentials_index):
    # whether image should keep drawing itself
    repeat_forever = True

    while True:
        # try:
        # global variables for script
        last_time_placed_pixel = math.floor(time.time())

        # note: reddit limits us to place 1 pixel every 5 minutes, so I am setting it to
        # 5 minutes and 30 seconds per pixel
        # pixel_place_frequency = 330
        pixel_place_frequency = 330

        # pixel drawing preferences
        pixel_x_start = int(os.getenv("ENV_DRAW_X_START"))
        pixel_y_start = int(os.getenv("ENV_DRAW_Y_START"))

        try:
            # current pixel row and pixel column being drawn
            current_r = int(json.loads(os.getenv("ENV_R_START"))[credentials_index])
            current_c = int(json.loads(os.getenv("ENV_C_START"))[credentials_index])
        except IndexError:
            print(
                "Array length error: are you sure you have an ENV_R_START and ENV_C_START item for every account?\n",
                "Example for 5 accounts:\n",
                'ENV_R_START=\'["0","5","6","7","9"]\'\n',
                'ENV_C_START=\'["0","5","6","8","9"]\'\n',
                "Note: There can be duplicate entries, but every array must have the same amount of items.",
            )
            exit(1)

<<<<<<< HEAD
<<<<<<< HEAD
    if not repeat_forever:
        break
>>>>>>> d5a279b (Added ability for image to keep redrawing itself)
<<<<<<< HEAD
>>>>>>> c000d57 (Added ability for image to keep redrawing itself)
=======
=======
            # string for time until next pixel is drawn
            update_str = ""
=======
        # string for time until next pixel is drawn
        update_str = ""
>>>>>>> 9ddfd16 (Comment out try except since it is hiding issues)

        # reference to globally shared variables such as auth token and image
        global access_tokens
        global access_token_expires_at_timestamp

        # boolean to place a pixel the moment the script is first run
        # global first_run
        global first_run_counter

        # refresh auth tokens and / or draw a pixel
        while True:
            # reduce CPU usage
            time.sleep(1)

            # get the current time
            current_timestamp = math.floor(time.time())

            # log next time until drawing
            time_until_next_draw = (
                last_time_placed_pixel + pixel_place_frequency - current_timestamp
            )
            new_update_str = (
                str(time_until_next_draw) + " seconds until next pixel is drawn"
            )
            if update_str != new_update_str and time_until_next_draw % 10 == 0:
                update_str = new_update_str
                print(
                    "-------Thread #"
                    + str(credentials_index)
                    + "-------\n"
                    + update_str
                )

            # refresh access token if necessary
            if (
                access_tokens[credentials_index] is None
                or current_timestamp
                >= access_token_expires_at_timestamp[credentials_index]
            ):
                print(
                    "-------Thread #"
                    + str(credentials_index)
                    + "-------\n"
                    + "Refreshing access token..."
                )

                # developer's reddit username and password
                try:
                    username = json.loads(os.getenv("ENV_PLACE_USERNAME"))[
                        credentials_index
                    ]
                    password = json.loads(os.getenv("ENV_PLACE_PASSWORD"))[
                        credentials_index
                    ]
                    # note: use https://www.reddit.com/prefs/apps
                    app_client_id = json.loads(os.getenv("ENV_PLACE_APP_CLIENT_ID"))[
                        credentials_index
                    ]
                    secret_key = json.loads(os.getenv("ENV_PLACE_SECRET_KEY"))[
                        credentials_index
                    ]
                except IndexError:
                    print(
                        "Array length error: are you sure your credentials have an equal amount of items?\n",
                        "Example for 2 accounts:\n",
                        'ENV_PLACE_USERNAME=\'["Username1", "Username2]\'\n',
                        'ENV_PLACE_PASSWORD=\'["Password", "Password"]\'\n',
                        'ENV_PLACE_APP_CLIENT_ID=\'["NBVSIBOPVAINCVIAVBOVV", "VNOPSNSJVQNVNJVSNVDV"]\'\n',
                        'ENV_PLACE_SECRET_KEY=\'["INSVDSINDJV_SVTNNJSNVNJV", "ANIJCINLLPJCSCOJNCA_ASDV"]\'\n',
                        "Note: There can be duplicate entries, but every array must have the same amount of items.",
                    )
                    exit(1)

                data = {
                    "grant_type": "password",
                    "username": username,
                    "password": password,
                }

                r = requests.post(
                    "https://ssl.reddit.com/api/v1/access_token",
                    data=data,
                    auth=HTTPBasicAuth(app_client_id, secret_key),
                    headers={"User-agent": f"placebot{random.randint(1, 100000)}"},
                )

                if verbose_mode:
                    print("received response: ", r.text)

                response_data = r.json()
                access_tokens[credentials_index] = response_data["access_token"]
                # access_token_type = response_data["token_type"]  # this is just "bearer"
                access_token_expires_in_seconds = response_data[
                    "expires_in"
                ]  # this is usually "3600"
                # access_token_scope = response_data["scope"]  # this is usually "*"

                # ts stores the time in seconds
                access_token_expires_at_timestamp[
                    credentials_index
                ] = current_timestamp + int(access_token_expires_in_seconds)

                print(
                    "received new access token: ",
                    access_tokens[credentials_index],
                )

            # draw pixel onto screen
<<<<<<< HEAD
            if access_tokens[credentials_index] is not None and (current_timestamp >= last_time_placed_pixel
<<<<<<< HEAD
<<<<<<< HEAD
                                                                 + pixel_place_frequency or first_run):
=======
                                                                 + pixel_place_frequency
                                                                 or first_run_counter <= credentials_index):
>>>>>>> a625de8 (Use color selected in the get_unset_pixel function)
                
                
=======
                                                                 + pixel_place_frequency
                                                                 or first_run_counter <= credentials_index):
>>>>>>> 0c9f07a (Add counter to fix first run issue with multithreading)
=======
            if access_tokens[credentials_index] is not None and (
                current_timestamp >= last_time_placed_pixel + pixel_place_frequency
                or first_run_counter <= credentials_index
            ):

>>>>>>> aa7e04c (Fetch cooldown, formatting changes (#22))
                # place pixel immediately
                # first_run = False
                first_run_counter += 1

                # get target color
                # target_rgb = pix[current_r, current_c]

                # get current pixel position from input image and replacement color
                current_r, current_c, new_rgb = get_unset_pixel(
                    get_board(access_tokens[credentials_index]),
                    current_r,
                    current_c,
                )

                # get converted color
                new_rgb_hex = rgb_to_hex(new_rgb)
                pixel_color_index = color_map[new_rgb_hex]

                # draw the pixel onto r/place
                last_time_placed_pixel = set_pixel_and_check_ratelimit(
                    access_tokens[credentials_index],
                    pixel_x_start + current_r,
                    pixel_y_start + current_c,
                    pixel_color_index,
                )

                current_r += 1

                # go back to first column when reached end of a row while drawing
                if current_r >= image_width:
                    current_r = 0
                    current_c += 1

                # exit when all pixels drawn
                if current_c >= image_height:
                    print(
                        "--------Thread #"
                        + str(credentials_index)
                        + "--------\n"
                        + "done drawing image to r/place\n"
                    )
                    break
        # except:
        #     print("__________________")
        #     print("Thread #" + str(credentials_index))
        #     print("Error refreshing tokens or drawing pixel")
        #     print("Trying again in 5 minutes...")
        #     print("__________________")
        #     time.sleep(5 * 60)

        if not repeat_forever:
            break


# get color palette
init_rgb_colors_array()

# load the pixels for the input image
load_image()

<<<<<<< HEAD
# run the image drawing task
<<<<<<< HEAD
task()
>>>>>>> 6683491 (Split code into functions for multithreading)
<<<<<<< HEAD
>>>>>>> c0dfb14 (Split code into functions for multithreading)
=======
=======
thread1 = threading.Thread(target=task, args=())
thread1.start()
>>>>>>> 1b25969 (Added simple threading example)
<<<<<<< HEAD
>>>>>>> df71c41 (Added simple threading example)
=======
=======
# get number of concurrent threads to start
num_credentials = len(json.loads(os.getenv("ENV_PLACE_USERNAME")))

# define delay between starting new threads
if os.getenv("ENV_THREAD_DELAY") != None:
    delay_between_launches_seconds = int(os.getenv("ENV_THREAD_DELAY"))
else:
    delay_between_launches_seconds = 3

# launch a thread for each account specified in .env
for i in range(num_credentials):
    # run the image drawing task
    access_tokens.append(None)
    access_token_expires_at_timestamp.append(math.floor(time.time()))
    thread1 = threading.Thread(target=task, args=[i])
    thread1.start()
<<<<<<< HEAD
>>>>>>> 12ab83e (Added support for multiple threads)
<<<<<<< HEAD
>>>>>>> 3a4679a (Added support for multiple threads)
=======
=======
    time.sleep(delay_between_launches_seconds)
>>>>>>> 73075cf (Add delay between launching threads)
>>>>>>> e886c12 (Add delay between launching threads)
