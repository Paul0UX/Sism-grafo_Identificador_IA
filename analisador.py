import cv2
import numpy as np
import pandas as pd
import os
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
import time
from math import ceil
import glob

# Configurações do sismograma
minutos_por_linha = 60
linhas_por_dia = 24

# Caminho das imagens
caminho_das_imagens = r"C:\Users\aluno\Desktop\Estudando\Replicadas"
arquivos = [f for f in os.listdir(caminho_das_imagens) if f.endswith(".png")]
arquivos.sort()

# Pasta de saída dos lotes
os.makedirs("lotes", exist_ok=True)

def processar_imagem(nome_arquivo):
    try:
        caminho_completo = os.path.join(caminho_das_imagens, nome_arquivo)
        img = cv2.imread(caminho_completo, cv2.IMREAD_GRAYSCALE)
        if img is None:
            return []

        blur = cv2.GaussianBlur(img, (3, 3), 0)
        inv = cv2.bitwise_not(blur)
        _, thresh = cv2.threshold(inv, 200, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        h, w = img.shape
        pixel_por_minuto = w / minutos_por_linha
        pixel_por_linha = h / linhas_por_dia

        eventos = []
        for cnt in contours:
            x, y, w_cnt, h_cnt = cv2.boundingRect(cnt)
            area = cv2.contourArea(cnt)
            if area < 5:
                continue

            linha_idx = int(y // pixel_por_linha)
            minuto_idx = int(x // pixel_por_minuto)
            segundo_idx = int((x % pixel_por_minuto) * 60 / pixel_por_minuto)

            eventos.append({
                "imagem": nome_arquivo,
                "hora": linha_idx,
                "minuto": minuto_idx,
                "segundo": int(segundo_idx),
                "intensidade": int(area)
            })

        return eventos

    except Exception as e:
        print(f"Erro ao processar {nome_arquivo}: {e}")
        return []

if __name__ == "__main__":
    inicio = time.time()
    total_imagens = len(arquivos)
    print(f"Processando {total_imagens} imagens com {cpu_count()} núcleos...")

    # Definindo tamanho do lote
    lote_tamanho = 2000
    n_lotes = ceil(total_imagens / lote_tamanho)

    for i in range(n_lotes):
        print(f"\n🔄 Processando lote {i + 1}/{n_lotes}...")
        inicio_lote = i * lote_tamanho
        fim_lote = min((i + 1) * lote_tamanho, total_imagens)
        arquivos_lote = arquivos[inicio_lote:fim_lote]

        with Pool(cpu_count()) as pool:
            resultados = list(tqdm(pool.imap_unordered(processar_imagem, arquivos_lote), total=len(arquivos_lote)))

        eventos = [e for sublist in resultados for e in sublist]
        df_lote = pd.DataFrame(eventos)
        df_lote.to_csv(f"lotes/lote_{i:03d}.csv", index=False)

    # Concatenar todos os lotes
    print("\n📦 Unindo arquivos de todos os lotes...")
    arquivos_lotes = sorted(glob.glob("lotes/lote_*.csv"))
    df_final = pd.concat([pd.read_csv(f) for f in arquivos_lotes])
    df_final = df_final.sort_values(by=["imagem", "hora", "minuto", "segundo"]).reset_index(drop=True)

    # Salvar arquivo final
    df_final.to_csv("todos_eventos_sismicos.csv", index=False)
    print("✅ Todos os eventos salvos em 'todos_eventos_sismicos.csv'")

    # Estatísticas/resumo
    resumo = {
        "total_eventos": len(df_final),
        "total_imagens": total_imagens,
        "media_eventos_por_imagem": round(len(df_final) / total_imagens, 2)
    }
    pd.DataFrame([resumo]).to_csv("resumo_eventos.csv", index=False)
    print("📊 Resumo salvo em 'resumo_eventos.csv'")

    # Eventos por imagem
    df_final["eventos_por_imagem"] = df_final.groupby("imagem")["imagem"].transform("count")

    # (Opcional) Apagar arquivos intermediários
    # for f in arquivos_lotes:
    #     os.remove(f)

    fim = time.time()
    print(f"⏱️ Tempo total de execução: {round(fim - inicio, 2)} segundos")
