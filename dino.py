from PIL import ImageGrab
import pyautogui
 
def isCollision(data):
    for i in range( 740, 825):
        for j in range (350, 390):
           if data[i, j] < 100:
               print("Pulando") 
               pyautogui.keyDown("up")
               return
    return
  
while True:
    image = ImageGrab.grab().convert("L")
    data = image.load()
    isCollision(data)

    
 
    # break