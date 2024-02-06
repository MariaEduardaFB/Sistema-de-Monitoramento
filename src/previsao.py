import cv2
import numpy as np
import joblib

# Carregar o modelo treinado
caminho_modelo = './modelos/modelo_svm.pkl'
modelo_svm = joblib.load(caminho_modelo)
limiar = 150

def extrair_caracteristicas_nova_imagem(caminho_imagem, limiar):
    imagem = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
    imagem_redimensionada = cv2.resize(imagem, (100, 100))  
    caracteristicas = imagem_redimensionada.flatten()
    return caracteristicas, imagem_redimensionada


caminho_nova_imagem = './dados/teste/positivo/Imagem1.png'
print(f'Caminho da imagem: {caminho_nova_imagem}')


# Extrair características da nova imagem
caracteristicas_nova_imagem, imagem_redimensionada = extrair_caracteristicas_nova_imagem(caminho_nova_imagem, limiar)

# Reshape das características para coincidir com o formato esperado pelo modelo
caracteristicas_nova_imagem = caracteristicas_nova_imagem.reshape(1, -1)

# Fazer a previsão usando o modelo treinado
previsao = modelo_svm.predict(caracteristicas_nova_imagem)

# Visualizar o resultado da previsão
if previsao[0] == 1:
    # Destacar a região onde o foco foi detectado (por exemplo, desenhar um retângulo)
    x, y, w, h = 10, 10, 80, 80  # Coordenadas do retângulo (ajuste conforme necessário)
    imagem_resultado = cv2.rectangle(imagem_redimensionada.copy(), (x, y), (x + w, y + h), (0, 255, 0), 2)  # Cor verde, espessura 2
    cv2.imshow('Resultado da Detecção', imagem_resultado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Foco de El Niño detectado.")
else:
    print("Sem foco de El Niño detectado.")
