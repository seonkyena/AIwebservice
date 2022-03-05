import numpy as np
from tensorflow.keras.models import load_model
import cv2

model = load_model('./model/12classes.h5')
class_names = ["Blue Curacao", "Gordon's Gin", "Absolute", "Barcardi Carta Blanca", "Disaronno Amaretto", "Jack Daniel's", 
               "Bombay Sapphire", "Jose Cuervo", "Johnnie Walker", "Peach Tree", "Kahlua", "Smirnoff"]

def predict(path):
    img = cv2.imdecode(np.fromfile(path, np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_LINEAR)
    img = np.array(img)/255.0
    img = img.reshape(1,224,224,3)
    
    prediction = model.predict(img)

    
    return class_names[np.argmax(prediction)]

print(predict('./data/train/Absolute/Absolute_100.jpg'))
print(predict('./data/train/Bacardi Carta Blanca/Bacardi Carta Blanca_100.jpg'))
print(predict('./data/train/Blue Curacao/Blue Curacao_100.jpg'))
print(predict('./data/train/Bombay Sapphire/Bombay Sapphire_100.jpg'))
print(predict('./data/train/Disaronno Amaretto/Disaronno Amarettåo_100.jpg'))
print(predict("./data/train/Gordon's Gin/Gordon's Gin_100.jpg"))
print(predict("./data/train/Jack Daniel's/Jack Daniel's_100.jpg"))
print(predict('./data/train/Johnnie Walker/Johnnie Walker_100.jpg'))
print(predict('./data/train/Jose Cuervo/Jose Cuervo_100.jpg'))
print(predict('./data/train/Kahlua/Kahlua_100.jpg'))
print(predict('./data/train/Peach Tree/Peach Tree_100.jpg'))
print(predict('./data/train/Smirnoff/Smirnoff_100.jpg'))