import requests
import logging

url = "https://ocr-text-recognition.p.rapidapi.com/ocr"

headers = {
    "content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "dc521e16e1msh8a91d612c2d7f38p1e17cajsnd665a5824996",
	"X-RapidAPI-Host": "ocr-text-recognition.p.rapidapi.com"
    }
# test payload
# payload = "imageUrl=https%3A%2F%2Fobjectcut.com%2Fassets%2Fimg%2Fraven.jpg"

async def remove_background(img_url):
    payload = f"imageUrl={img_url}"
    response = requests.request("POST", url, data=payload, headers=headers)
    # logging.info(response.json()['response']['image_url'])
    return response.text