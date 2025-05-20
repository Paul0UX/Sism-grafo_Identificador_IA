import cv2
import numpy as np
import os

# Configurações
total_imagens = 20
imagens_necessarias = 9216
duplicacoes = imagens_necessarias // total_imagens

diretorio_entrada = r"C:\Users\MICRO\Desktop\Arquivos_sismicos"
diretorio_saida = r"C:\Users\MICRO\Desktop\Arquivos_sismicos\Replicado"

# Criar pasta de saída se não existir
os.makedirs(diretorio_saida, exist_ok=True)

# Parâmetro para controlar o tamanho do lote (quantas vezes repetir por arquivo)
duplicacoes_por_arquivo = 10  # Ajuste para caber na memória (ex: 10)

# Quantos arquivos batch serão salvos
num_arquivos = duplicacoes // duplicacoes_por_arquivo
if duplicacoes % duplicacoes_por_arquivo != 0:
    num_arquivos += 1

# Carregar imagens originais
imagens = []
for i in range(1, total_imagens + 1):
    caminho_img = os.path.join(diretorio_entrada, f"{i}.png")
    img = cv2.imread(caminho_img)
    if img is None:
        print(f"❌ Erro ao carregar: {caminho_img}")
        exit(1)
    imagens.append(img)
imagens_array = np.array(imagens)  # (20, H, W, C)

# Salvar em batches
total_salvas = 0
for batch_id in range(num_arquivos):
    # Quantidade a replicar neste batch (para o último batch não ultrapassar)
    replicar = min(duplicacoes_por_arquivo, duplicacoes - batch_id * duplicacoes_por_arquivo)
    imagens_batch = np.tile(imagens_array, (replicar, 1, 1, 1))
    
    nome_arquivo = os.path.join(diretorio_saida, f"imagens_batch_{batch_id + 1}.npz")
    np.savez_compressed(nome_arquivo, imagens=imagens_batch)
    total_salvas += imagens_batch.shape[0]

    print(f"[OK] Salvou batch {batch_id + 1} com {imagens_batch.shape[0]} imagens em {nome_arquivo}")

print(f"✅ Total de imagens salvas: {total_salvas}")
print(f"✅ Arquivos salvos em: {diretorio_saida}")
