import os
import cv2
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import joblib

def extrair_caracteristicas(imagem, limiar):
    _, binarizada = cv2.threshold(imagem, limiar, 255, cv2.THRESH_BINARY)
    caracteristicas = binarizada.flatten()
    return caracteristicas

# Caminho para as pastas de imagens
caminho_positivos = './dados/treinamento/positivo/'
caminho_negativos = './dados/treinamento/negativo/'

# Tamanho desejado para redimensionar as imagens
tamanho_desejado = (100, 100)

# Lista para armazenar imagens e rótulos
imagens = []
rotulos = []
limiar = 150

# Ler imagens positivas
for arquivo in os.listdir(caminho_positivos):
    if arquivo.endswith(".png"):
        imagem = cv2.imread(os.path.join(caminho_positivos, arquivo), cv2.IMREAD_GRAYSCALE)
        imagem_redimensionada = cv2.resize(imagem, tamanho_desejado)
        caracteristicas = extrair_caracteristicas(imagem_redimensionada, limiar)
        imagens.append(caracteristicas)
        rotulos.append(1)  # Rótulo 1 para imagens positivas

# Ler imagens negativas
for arquivo in os.listdir(caminho_negativos):
    if arquivo.endswith(".png"):
        imagem = cv2.imread(os.path.join(caminho_negativos, arquivo), cv2.IMREAD_GRAYSCALE)
        imagem_redimensionada = cv2.resize(imagem, tamanho_desejado)
        caracteristicas = extrair_caracteristicas(imagem_redimensionada, limiar)
        imagens.append(caracteristicas)
        rotulos.append(0)  # Rótulo 0 para imagens negativas

# Converter listas para arrays numpy
imagens_treinamento = np.array(imagens)
rotulos_treinamento = np.array(rotulos)

if len(imagens_treinamento) == 0:
    print("Erro: Não há imagens suficientes para treinamento.")
else:
    # Divisão treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(imagens_treinamento, rotulos_treinamento, test_size=0.2, random_state=42)

    # Treinamento do modelo SVM
    modelo_svm = SVC(kernel='linear')
    modelo_svm.fit(X_train, y_train)

    # Salvar o modelo treinado
    caminho_modelo = './modelos/modelo_svm.pkl'
    joblib.dump(modelo_svm, caminho_modelo)
    print(f'Modelo treinado salvo em {caminho_modelo}')
