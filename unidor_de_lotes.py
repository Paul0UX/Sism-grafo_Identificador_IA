import pandas as pd
import glob
import os

# Caminho da pasta onde estão os arquivos de lote
pasta_lotes = r"C:\Users\aluno\Desktop\identificador\Sism-grafo_Identificador_IA-1\lotes"

# Encontra todos os arquivos CSV na pasta (ordenado por nome)
arquivos_csv = sorted(glob.glob(os.path.join(pasta_lotes, "*.csv")))

print(f"🔍 Encontrados {len(arquivos_csv)} arquivos CSV na pasta '{pasta_lotes}'.")

# Lê e junta todos os DataFrames
df_total = pd.concat([pd.read_csv(arquivo) for arquivo in arquivos_csv], ignore_index=True)

# Organiza por imagem e tempo
df_total = df_total.sort_values(by=["imagem", "hora", "minuto", "segundo"]).reset_index(drop=True)

# Salva como único arquivo
df_total.to_csv("todos_eventos_sismicos.csv", index=False)
print("✅ Arquivo 'todos_eventos_sismicos.csv' criado com sucesso.")

# Estatísticas/resumo
resumo = {
    "total_eventos": len(df_total),
    "total_imagens": df_total["imagem"].nunique(),
    "media_eventos_por_imagem": round(len(df_total) / df_total["imagem"].nunique(), 2)
}
pd.DataFrame([resumo]).to_csv("resumo_eventos.csv", index=False)
print("📊 Resumo salvo em 'resumo_eventos.csv'")
