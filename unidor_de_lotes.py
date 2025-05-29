import pandas as pd
import glob
import os

# Caminho da pasta onde estão os arquivos de lote
pasta_lotes = r"C:\Users\aluno\Desktop\Sismografo\Sism-grafo_Identificador_IA\lotes"  # <-- edite aqui se necessário

# Encontra todos os arquivos CSV na pasta (ordenado por nome)
arquivos_csv = sorted(glob.glob(os.path.join(pasta_lotes, "*.csv")))

print(f"🔍 Encontrados {len(arquivos_csv)} arquivos CSV na pasta '{pasta_lotes}'.")

# Lê e junta todos os DataFrames
df_total = pd.concat([pd.read_csv(arquivo) for arquivo in arquivos_csv], ignore_index=True)

# Salva como único arquivo
df_total.to_csv("todos_eventos_sismicos.csv", index=False)
print("✅ Arquivo 'todos_eventos_sismicos.csv' criado com sucesso.")
