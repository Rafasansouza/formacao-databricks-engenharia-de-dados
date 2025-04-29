# Manipulação de Arquivos com PySpark no Databricks

Este repositório apresenta as práticas desenvolvidas durante o curso de Engenharia de Dados, com foco na **leitura, escrita, compressão e particionamento de arquivos** utilizando **PySpark** no **Databricks**.

## Tópicos aprendidos

### 📁 Trabalhando com DBFS e dbutils
- Criação de diretórios no Databricks File System (DBFS) usando `dbutils.fs.mkdirs`.
- Listagem de arquivos e diretórios com `dbutils.fs.ls`.
- Carregamento de arquivos JSON para o Spark.

### 📄 Manipulação de DataFrames
- Renomeação de colunas para nomes mais descritivos usando `withColumnRenamed`.
- Filtragem de dados inválidos.
- Conversão de tipos de dados utilizando `cast` do `pyspark.sql.functions`.

### 🗜️ Escrita e compressão de arquivos
- Escrita de arquivos JSON com compressão GZIP.
- Escrita de arquivos CSV com e sem cabeçalho e aplicação de compressão GZIP.
- Escrita de arquivos de texto (`TXT`), separando colunas com delimitador `|` e compactando em GZIP.

### 🧹 Limpeza e padronização dos dados
- Substituição de valores nulos em colunas específicas utilizando `na.fill`.
- Releitura de arquivos após compressão e renomeação adequada das colunas.

### 📦 Trabalho com formatos AVRO
- Escrita de dados no formato AVRO.
- Aplicação de compressão no AVRO utilizando o codec `deflate`.
- Configurações avançadas como nível de compressão no AVRO (`spark.sql.avro.deflate.level`).

### 📊 Trabalho com formato PARQUET
- Escrita de dados no formato Parquet.
- Aplicação de compressão GZIP em arquivos Parquet.
- Leitura e exibição dos dados Parquet.
- Uso de `select().distinct().show()` para exploração de valores únicos em colunas específicas.

### 🔥 Particionamento de dados
- Particionamento dos dados Parquet por uma ou mais colunas (ex.: `nivel_territorial` e `cod_doenca`).
- Leitura seletiva de partições específicas.

### 📂 Trabalho com formato ORC
- Escrita de dados em formato ORC.
- Aplicação de compressão `zlib` no ORC.
- Uso de `coalesce(1)` para unir os arquivos ORC em um único arquivo comprimido.

## 📚 Resumo das tecnologias e formatos utilizados
- **DBFS**: Armazenamento de arquivos no Databricks.
- **dbutils**: Utilitários para manipulação de diretórios e arquivos no Databricks.
- **PySpark**: API Python para manipulação de Big Data distribuído.
- **JSON**: Leitura, escrita e compressão.
- **CSV**: Leitura, escrita, compressão e inferência de esquema.
- **TXT**: Escrita com delimitador customizado e compressão.
- **AVRO**: Escrita e compressão de arquivos compactos e esquematizados.
- **PARQUET**: Escrita, compressão e particionamento para otimização de leitura.
- **ORC**: Escrita e compressão eficiente de arquivos em Big Data.

---

## 🚀 Sobre o aprendizado
Durante a prática, pudemos compreender:
- A diferença de formatos de arquivos e compressões.
- A importância de tipos corretos de dados para eficiência.
- Como o particionamento afeta a performance em grandes volumes de dados.
- Como manipular diferentes tipos de arquivos para preparar os dados para análises.

---

> ⚡ Este projeto reforçou os conceitos fundamentais de manipulação de dados no Databricks usando PySpark, consolidando as melhores práticas para lidar com grandes volumes de dados em diferentes formatos e compressões.