# 🚀 Projeto: Pipeline de Engenharia de Dados com Airflow, Azure Databricks e Slack

Este repositório documenta o projeto desenvolvido durante a **Formação Engenharia de Dados com Databricks** da **ALURA**, com foco em **integração entre APIs, Databricks, Airflow e automação em nuvem**.

---

## 🎯 Objetivo

Construir um **pipeline de dados completo**, desde a **extração de dados de uma API** até a **transformação, armazenamento e notificação automática** no Slack, aplicando boas práticas de **engenharia de dados em ambiente cloud**.

---

## ☁️ Arquitetura do Projeto

O projeto foi desenvolvido em ambiente **Azure**, com integração de diversos serviços e ferramentas open source.

### 🔹 **Fluxo Geral**
1. **Extração** – Consumo de dados via **API de taxas de câmbio (Exchange Rates)**.  
2. **Transformação** – Processamento e limpeza dos dados no **Azure Databricks**.  
3. **Armazenamento** – Escrita dos resultados em **Parquet e CSV** no Databricks.  
4. **Orquestração** – Automação das execuções com o **Apache Airflow**.  
5. **Notificação** – Envio de arquivos e gráficos automaticamente para o **Slack** via bot.

---

## 🧰 Tecnologias e Ferramentas Utilizadas

| Categoria | Ferramenta | Descrição |
|------------|-------------|-----------|
| **Ambiente Cloud** | Azure | Gerenciamento e monitoramento de recursos |
| **Processamento** | Databricks | Execução e transformação dos dados |
| **Orquestração** | Airflow | Controle e agendamento das DAGs |
| **Linguagem** | Python | Lógica de negócio e scripts de ETL |
| **Automação** | Slack API | Bot para envio de mensagens e arquivos |
| **Formatos de Dados** | Parquet / CSV | Armazenamento otimizado e compatível com análise |
| **Ambiente local** | WSL2 | Execução do ambiente Linux no Windows |

---

## 🧩 Estrutura do Pipeline

```
API (Exchange Rates)
     ↓
Airflow DAG → Extrai os dados via requisição HTTP
     ↓
Databricks Notebook → Limpa, transforma e cria DataFrame
     ↓
Databricks Storage → Salva em Parquet e CSV
     ↓
Slack Bot → Notifica e envia o arquivo final
```

---

## ⚙️ Principais Etapas do Desenvolvimento

### 🪄 **Fundamentos e Preparação do Ambiente**
- Configuração do **WSL2** e ambiente virtual Python.  
- Instalação e setup do **Apache Airflow**.  
- Criação de conta na **Azure** e definição de alertas de gastos.  
- Configuração do acesso ao **Azure Databricks**.

### 📡 **Extração e Armazenamento**
- Conexão com a **API de taxas de câmbio (Exchange Rate)**.  
- Uso de **Payloads e Headers** para autenticação.  
- Estruturação e salvamento dos dados em **Parquet** no Databricks.  
- Introdução ao conceito de **Arquitetura Medalhão (Bronze, Silver, Gold)**.

### 🔁 **Transformação e Enriquecimento**
- Leitura dos dados em Parquet.  
- **Filtragem, organização e pivotagem** do DataFrame.  
- Exportação dos resultados em formato **CSV**.  
- Execução automatizada da transformação com **Airflow DAGs**.

### 🤖 **Automação e Integração**
- Criação de um **bot no Slack**.  
- Envio automático dos arquivos gerados pelo Databricks.  
- Notificação de sucesso e compartilhamento de gráficos.

### 🧹 **Encerramento e Boas Práticas**
- Limpeza e **deleção dos recursos na Azure**.  
- Entendimento sobre **custos (DBUs)** e controle de billing.  
- Revisão geral do pipeline e arquitetura final.

---

## 📊 Resultados

✅ Pipeline automatizado e escalável, do **consumo da API até a notificação no Slack**.  
✅ Escrita de dados em formatos otimizados (**Parquet** e **CSV**).  
✅ Infraestrutura em nuvem replicável e com controle de custos via **Azure Monitor**.  
✅ Aplicação prática de orquestração com **Airflow** e integração entre múltiplos serviços.
