from requests_oauthlib import OAuth1Session
import io, cv2, tweepy, random




def I(req):
    consumer_key = "DfZOSaPl5etxaweh44qtHHro1"
    consumer_secret = "FpPdcpoIscaGOuADEASpSzMsf6ScW6V6MEI76JIAog6ruIotCW"
    access_token = "1682818789451104257-nrM3pkwKh2pgkp60QGw4bmIfyqNf1V"
    access_token_secret = "nYKGKYuKeVz8pCGebU05rBLL53g1QZFmcMZsOYrqviOI6"
    num_of_eps = 20
    upload_url = "https://api.twitter.com/2/tweets"
    headers = {"Content-Type": "application/json"}
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)




    file=random.randint(1,num_of_eps)
    if file == 1:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1gNvjLQsCZ2NIvrYvaVRoqVnuwbEXtc_N&export=download&t=90")
        s, e, t = "1", "1", "The Boy in the Iceberg"
    elif file == 2:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1sTaAqMQkKCwYrWqeHgcLjyvtXibPOOrn&export=download&t=90")
        s, e, t = "1", "2", "The Avatar Returns"
    elif file == 3:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=12KPxX-IaNexoC64ZsTAreuwHExh6LKbH&export=download&t=90")
             
        s, e, t = "1", "3", "The Southern Air Temple"
    elif file == 4:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1MhWcJe8REe8rUeEVsyU9p1b24EUwm1Tf&export=download&t=90")
        s, e, t = "1", "4", "The Warriors of Kyoshi"
    elif file == 5:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1Mrv2_ycnYVqRA7Fc4WhsZh1ZX8dJXIKj&export=download&t=90")
        s, e, t = "1", "5", "The King of Omashu"
    elif file == 6:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1NG5ioEDXZ4B7MDn6WB924LAUsKQgtcWF&export=download&t=90")
        s, e, t = "1", "6", "Imprisoned"
    elif file == 7:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1BfJaXaCRtdZ6DpTjpHmrzvOM6dHIlwG8&export=download&t=90")
        s, e, t = "1", "7", "Winter Solstice, Part 1--The Spirit World"
    elif file == 8:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1-ksvJ4fmw6Evhzq88LJYxUmDZn4ZIvSk&export=download&t=90")
        s, e, t = "1", "8", "Winter Solstice, Part 2- Avatar Roku"
    elif file == 9:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1xZ2WDPfcay8A2dTJLLZlil7n64OVT_q9&export=download&t=90")
        s, e, t = "1", "9", "The Waterbending Scroll"
    elif file == 10:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1xWNCBFDlYVk2qWCFb_eOXa8mWtQUEYIh&export=download&t=90")
        s, e, t = "1", "10", "Jet"
    elif file == 11:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1yf_RvWfstyTqEeRd_FXEH25DDVE9hz4N&export=download&t=90")
        s, e, t = "1", "11", "The Great Divide"
    elif file == 12:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1sYlz9ZG9Nnn4VssC0h1fUiCH1dpcvYVL&export=download&t=90")
        s, e, t = "1", "12", "The Storm"
    elif file == 13:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1lvHK3G7S2ptZl3bpXwcGc21pUdU11kW1&export=download&t=90")
        s, e, t = "1", "13", "The Blue Spirit"
    elif file == 14:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1DoPu6H3f5GKLkWjFTI66pDcUCjwcF7V-&export=download&t=90")
        s, e, t = "1", "14", "The Fortune Teller"
    elif file == 15:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=12iaDrXIgzx0t4GQ0n8Ozk5CAoRtwYDU4&export=download&t=90")
        s, e, t = "1", "15", "Bato of the Water Tribe"
    elif file == 16:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1bGPtb6YNgozrTlrK7pqwXevu19zy9g3S&export=download&t=90")
        s, e, t = "1", "16", "The Deserter"
    elif file == 17:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1V5Vgp37BJxf3sI0_sauZS-qJs9aws09M&export=download&t=90")
        s, e, t = "1", "17", "The Northern Air Temple"
    elif file == 18:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1PTs5oHrJ0I1PwwlaPj9ANnKjiApftN64&export=download&t=90")
        s, e, t = "1", "18", "The Waterbending Master"
    elif file == 19:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1xsGs5mSC4xcStY2GAqWO46PRA_nrwa56&export=download&t=90")
        s, e, t = "1", "19", "The Siege of the North, Part 1"
    elif file == 20:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1E9GAB334vONDewjoqyIJSrltjnR5QXf-&export=download&t=90")
        s, e, t = "1", "20", "The Siege of the North, Part 2"
    elif file == 21:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1gNvjLQsCZ2NIvrYvaVRoqVnuwbEXtc_N&export=download&t=90")
        s, e, t = "2", "1", "The Boy in the Iceberg"
    elif file == 22:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1sTaAqMQkKCwYrWqeHgcLjyvtXibPOOrn&export=download&t=90")
        s, e, t = "2", "2", "The Avatar Returns"
    elif file == 23:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=12KPxX-IaNexoC64ZsTAreuwHExh6LKbH&export=download&t=90")             
        s, e, t = "2", "3", "The Southern Air Temple"
    elif file == 24:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1MhWcJe8REe8rUeEVsyU9p1b24EUwm1Tf&export=download&t=90")
        s, e, t = "2", "4", "The Warriors of Kyoshi"
    elif file == 25:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1Mrv2_ycnYVqRA7Fc4WhsZh1ZX8dJXIKj&export=download&t=90")
        s, e, t = "2", "5", "The King of Omashu"
    elif file == 26:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1NG5ioEDXZ4B7MDn6WB924LAUsKQgtcWF&export=download&t=90")
        s, e, t = "2", "6", "Imprisoned"
    elif file == 27:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1BfJaXaCRtdZ6DpTjpHmrzvOM6dHIlwG8&export=download&t=90")
        s, e, t = "2", "7", "Winter Solstice, Part 1--The Spirit World"
    elif file == 28:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1-ksvJ4fmw6Evhzq88LJYxUmDZn4ZIvSk&export=download&t=90")
        s, e, t = "2", "8", "Winter Solstice, Part 2- Avatar Roku"
    elif file == 29:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1xZ2WDPfcay8A2dTJLLZlil7n64OVT_q9&export=download&t=90")
        s, e, t = "2", "9", "The Waterbending Scroll"
    elif file == 30:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1xWNCBFDlYVk2qWCFb_eOXa8mWtQUEYIh&export=download&t=90")
        s, e, t = "2", "10", "Jet"
    elif file == 31:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1yf_RvWfstyTqEeRd_FXEH25DDVE9hz4N&export=download&t=90")
        s, e, t = "2", "11", "The Great Divide"
    elif file == 32:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1sYlz9ZG9Nnn4VssC0h1fUiCH1dpcvYVL&export=download&t=90")
        s, e, t = "2", "12", "The Storm"
    elif file == 33:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1lvHK3G7S2ptZl3bpXwcGc21pUdU11kW1&export=download&t=90")
        s, e, t = "2", "13", "The Blue Spirit"
    elif file == 34:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1DoPu6H3f5GKLkWjFTI66pDcUCjwcF7V-&export=download&t=90")
        s, e, t = "2", "14", "The Fortune Teller"
    elif file == 35:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=12iaDrXIgzx0t4GQ0n8Ozk5CAoRtwYDU4&export=download&t=90")
        s, e, t = "2", "15", "Bato of the Water Tribe"
    elif file == 36:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1bGPtb6YNgozrTlrK7pqwXevu19zy9g3S&export=download&t=90")
        s, e, t = "2", "16", "The Deserter"
    elif file == 37:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1V5Vgp37BJxf3sI0_sauZS-qJs9aws09M&export=download&t=90")
        s, e, t = "2", "17", "The Northern Air Temple"
    elif file == 38:
        cam = cv2.VideoCapture(
            "https://drive.google.com/u/0/uc?id=1PTs5oHrJ0I1PwwlaPj9ANnKjiApftN64&export=download&t=90")
        s, e, t = "2", "18", "The Waterbending Master"
    






    num=int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
    current_frame = random.randint(1,num)




    cam.set(1,current_frame-1)
    ret,frame=cam.read()
    ret,ff=cv2.imencode('.jpg',frame)
    ff = api.media_upload(filename="0.jpg",file=io.BytesIO(ff))


    payload = {
        "media": {"media_ids": [ff.media_id_string]},
        "text": "#AvatarTheLastAirbender"+ "\n" + t+" (S"+s+"E"+e+")\nFrame: "+str(current_frame)+"/"+str(num)
    }

    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )
    oauth.headers = {"Content-Type": "application/json"}
    response = oauth.post(
        upload_url,
        json=payload,
        headers = headers
    )

    return("OK")
