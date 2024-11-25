import cv2
from deepface import DeepFace

#ler imagem
imagem_feliz = cv2.imread("feliz.jpg")
imagem_triste = cv2.imread("triste.jpg")
imagem_surpreso = cv2.imread("surpresa.jpg")

#passar imagem para deepface
resultado_feliz = DeepFace.analyze(imagem_feliz, actions=("age", "emotion",'gender', 'race'), enforce_detection=False)
resultado_triste = DeepFace.analyze(imagem_triste, actions=("age", "emotion",'gender', 'race'), enforce_detection=False)
resultado_surpreso = DeepFace.analyze(imagem_surpreso, actions=("age", "emotion",'gender', 'race'), enforce_detection=False)
#ver resultados
print(resultado_feliz)
print("\n",resultado_triste)
print("\n",resultado_surpreso)