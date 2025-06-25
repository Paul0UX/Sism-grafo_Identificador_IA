import os
import shutil

# Caminho para a pasta com as 20 imagens
pasta_imagens = r"C:\Users\Leandro\Desktop\Sism-grafo_Identificador_IA\imagens_sis"
# Pasta onde as cópias serão salvas
pasta_destino = r"C:\Users\Leandro\Desktop\Sism-grafo_Identificador_IA\replicas"
os.makedirs(pasta_destino, exist_ok=True)

# Tamanho máximo em bytes (50 GB)
tamanho_maximo = 2 * 1024 * 1024 * 1024  

# Inicialização de variáveis
tamanho_total = 0
contador_copias = 1

# Lista apenas arquivos .png
imagens = [f for f in os.listdir(pasta_imagens) if f.lower().endswith(".png")]

if not imagens:
    print("Nenhuma imagem .png encontrada na pasta.")
    exit()

# Soma o tamanho das imagens originais (opcional, se quiser saber quanto pesa o conjunto base)
for imagem in imagens:
    caminho = os.path.join(pasta_imagens, imagem)
    tamanho_total += os.path.getsize(caminho)

# Começa a replicar até atingir 10 GB
while tamanho_total < tamanho_maximo:
    for imagem in imagens:
        caminho = os.path.join(pasta_imagens, imagem)
        nome_base, ext = os.path.splitext(imagem)
        
        # Nome único para a cópia
        novo_nome = f"{nome_base}_copia_{contador_copias:05}{ext}"
        caminho_novo = os.path.join(pasta_destino, novo_nome)
        
        shutil.copy(caminho, caminho_novo)
        
        tamanho_total += os.path.getsize(caminho)
        contador_copias += 1
        
        if tamanho_total >= tamanho_maximo:
            break

# Impressão do total replicado
print(f"Total de imagens duplicadas: {contador_copias - 1}")
print(f"Tamanho final: {tamanho_total / (1024 * 1024):.2f} MB / {tamanho_total / (1024 * 1024 * 1024):.2f} GB")