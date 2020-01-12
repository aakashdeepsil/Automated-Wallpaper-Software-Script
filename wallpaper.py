import requests
import wget
import ctypes
import time

def get_wallpaper():
  access = '999bf26be30b247454de4dde732bf9a3a2881abf10446daf70a0a427bc7d176d'
  
  url = 'https://api.unsplash.com/photos/random/?client_id=999bf26be30b247454de4dde732bf9a3a2881abf10446daf70a0a427bc7d176d'
  
  params = {
    "query": "HD wallpapers",
    "orientation": "landscape",
  }
  
  response = requests.get(url).json()
  
  image_url = response['urls']['full']
  
  image = wget.download(image_url, r"C:\Users\Aakashdeep Sil\AppData\Local\Temp\wallpaper.jpg")
  
  return image


def change_wallpaper():
    imagePath = get_wallpaper()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, imagePath, 3)
    return

def main():
  try:

    while True:
      change_wallpaper()
      time.sleep(10)
  
  except KeyboardInterrupt:
    print("\nHope you like this one! Quitting!")
  
  except Exception as e:
    pass

if __name__ == "__main__":
  main()
