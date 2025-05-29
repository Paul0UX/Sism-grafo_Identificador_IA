import os
import shutil

# Caminho para a pasta com as imagens 
pasta_imagens = r"C:\Users\aluno\Desktop\Sismografo\Sism-grafo_Identificador_IA"
# Pasta onde as cópias serão salvas
pasta_destino = r"C:\Users\aluno\Desktop\Sismografo\Sism-grafo_Identificador_IA\Replicadas"
os.makedirs(pasta_destino, exist_ok=True)

# Tamanho máximo 10GB
tamanho_maximo = 10 * 1024 * 1024 * 1024  

# Inicialização de variáveis
tamanho_total = 0
num_imagens = 0
imagens = [f for f in os.listdir(pasta_imagens) if f.lower().endswith(".png")]

# Verifica o tamanho total das imagens originais
for imagem in imagens:
    caminho_imagem = os.path.join(pasta_imagens, imagem)
    tamanho_total += os.path.getsize(caminho_imagem)
    num_imagens += 1

# Contador para nomear as cópias
contador_copias = 1

# Duplicar imagens até atingir o tamanho desejado
while tamanho_total < tamanho_maximo:
    for imagem in imagens:
        caminho_imagem = os.path.join(pasta_imagens, imagem)
        nome_base, ext = os.path.splitext(imagem)
        
        # Cria um novo nome para a cópia
        novo_nome = f"{nome_base}_copia_{contador_copias:04}{ext}"
        caminho_novo = os.path.join(pasta_destino, novo_nome)
        
        # Copia a imagem
        shutil.copy(caminho_imagem, caminho_novo)
        
        # Atualiza o tamanho total e o contador de cópias
        tamanho_total += os.path.getsize(caminho_imagem)
        contador_copias += 1
        
        # Ao alcançar o tamanho desejado ele sai
        if tamanho_total >= tamanho_maximo:
            break

# Conversão para MB e GB para exibição
tamanho_total_mb = tamanho_total / (1024 * 1024)  # em MB
tamanho_total_gb = tamanho_total / (1024 * 1024 * 1024)  # em GB

print(f"Total de imagens duplicadas: {contador_copias - 1}")
print(f"Tamanho total após duplicar: {tamanho_total_mb:.2f} MB")
print(f"Tamanho total após duplicar: {tamanho_total_gb:.2f} GB")

import os
import shutil

# Caminho para a pasta com as imagens 
pasta_imagens = r"C:\Users\aluno\Desktop\Estudando"
# Pasta onde as cópias serão salvas
pasta_destino = r"C:\Users\aluno\Desktop\Estudando\Replicadas"
os.makedirs(pasta_destino, exist_ok=True)

# Tamanho máximo
tamanho_maximo = 8 * 1024 * 1024 * 1024  

# Inicialização de variáveis
tamanho_total = 0
num_imagens = 0
imagens = [f for f in os.listdir(pasta_imagens) if f.lower().endswith(".png")]

# Verifica o tamanho total das imagens originais
for imagem in imagens:
    caminho_imagem = os.path.join(pasta_imagens, imagem)
    tamanho_total += os.path.getsize(caminho_imagem)
    num_imagens += 1

# Contador para nomear as cópias
contador_copias = 1

# Duplicar imagens até atingir o tamanho desejado
while tamanho_total < tamanho_maximo:
    for imagem in imagens:
        caminho_imagem = os.path.join(pasta_imagens, imagem)
        nome_base, ext = os.path.splitext(imagem)
        
        # Cria um novo nome para a cópia
        novo_nome = f"{nome_base}_copia_{contador_copias:04}{ext}"
        caminho_novo = os.path.join(pasta_destino, novo_nome)
        
        # Copia a imagem
        shutil.copy(caminho_imagem, caminho_novo)
        
        # Atualiza o tamanho total e o contador de cópias
        tamanho_total += os.path.getsize(caminho_imagem)
        contador_copias += 1
        
        # Ao alcançar o tamanho desejado ele sai
        if tamanho_total >= tamanho_maximo:
            break

# Conversão de MB e GB para exibição
tamanho_total_mb = tamanho_total / (1024 * 1024) #MB
tamanho_total_gb = tamanho_total / (1024 * 1024 * 1024) #GB

print(f"Total de imagens duplicadas: {contador_copias - 1}")
print(f"Tamanho total após duplicar: {tamanho_total_mb:.2f} MB")
print(f"Tamanho total após duplicar: {tamanho_total_gb:.2f} GB")
