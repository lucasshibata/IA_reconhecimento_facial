import cv2
from deepface import DeepFace

#ler imagem
imagem = cv2.imread("feliz.jpeg")
#passar imagem para deepface
resultado = DeepFace.analyze(imagem, actions=("age", "emotion"))
#ver resultados
print(resultado)