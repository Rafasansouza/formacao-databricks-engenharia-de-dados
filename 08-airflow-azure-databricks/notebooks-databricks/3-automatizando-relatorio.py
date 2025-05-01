# Databricks notebook source
from slack_sdk import WebClient
import pyspark.pandas as ps

# COMMAND ----------

slack_token = "coloque_o_seu_token_do_slack"
client = WebClient(token=slack_token)

# COMMAND ----------

nome_arquivo = dbutils.fs.ls("dbfs:/databricks-results/prata/valores_reais/")[-1].name

# COMMAND ----------

path = "../../dbfs/databricks-results/prata/valores_reais/" + nome_arquivo

# COMMAND ----------

enviando_arquivo_csv = client.files_upload_v2(
    channel="C08PZJBE8TC",  
    title="Arquivo no formato CSV do valor do real convertido",
    file=path,
    filename="valores_reais.csv",
    initial_comment="Segue em anexo o arquivo CSV:",
)

# COMMAND ----------

df_valores_reais = ps.read_csv("dbfs:/databricks-results/prata/valores_reais/")

# COMMAND ----------

!mkdir imagens

# COMMAND ----------

df_valores_reais.columns[1:]

# COMMAND ----------

for moeda in df_valores_reais.columns[1:]:
  fig = df_valores_reais.plot.line(x="data", y=moeda)
  fig.write_image(f"./imagens/{moeda}.png")

# COMMAND ----------

def enviando_imagens(moeda_cotacao):
    enviando_imagens = client.files_upload_v2(
        channel="C08PZJBE8TC",  
        title="Enviando imagens de cotacoes",
        file=f"./imagens/{moeda}.png"
    )

# COMMAND ----------

for moeda in df_valores_reais.columns[1:]:
    enviando_imagens(moeda)