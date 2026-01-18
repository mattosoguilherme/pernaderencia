import os
import time
import random
import json
import pandas as pd
import unicodedata
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoAlertPresentException,
    TimeoutException,
    ElementNotInteractableException,
    StaleElementReferenceException
)
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager




# ======== GERAR JSON ========

def gerar_json_de_excel(caminho_excel, caminho_json):
    try:
        os.makedirs(os.path.dirname(caminho_json), exist_ok=True)
        print("📥 Lendo planilha Excel...")

        df = pd.read_excel(caminho_excel, dtype=str)
        df.columns = [
            unicodedata.normalize("NFKD", str(c))
            .encode("ASCII", "ignore")
            .decode("utf-8")
            .replace(" ", "")
            .replace("_", "")
            .upper()
            for c in df.columns
        ]
        print("🔍 Colunas detectadas:", df.columns.tolist())

        colunas_necessarias = ["NOME", "CPF", "CARTAO"]
        for c in colunas_necessarias:
            if c not in df.columns:
                raise ValueError(f"❌ Coluna ausente na planilha: {c}")

        dados = [
            {
                "EVENTO": str(row["EVENTO"]).strip(),
                "MATRICULA": str(row["MATRICULA"]).strip(),
                "DATA": str(row["DATA"]).strip(),
                "HORA INICIO": str(row["HORA INICIO"]).strip(),
                "HORA FIM": str(row["HORA FIM"]).strip(),
                "CHAMADO": str(row["CHAMADO"]).strip(),
                "STATUS": "ANDAMENTO"
            }
            for _, row in df.iterrows()
        ]

        with open(caminho_json, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

        print(f"✅ JSON gerado com sucesso: {caminho_json}")
        print(f"📊 Total de registros exportados: {len(dados)}")

    except Exception as e:
        print(f"❌ Erro ao gerar JSON: {e}")