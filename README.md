# 🤖 RPA Neoservice → AppMiss

Automação desenvolvida em **Node.js** para preenchimento automático de formulários em sistemas distintos (**Neoservice** e **AppMiss**), utilizando dados provenientes de uma **planilha Excel**.

---

## 📌 Objetivo

- Ler dados de uma planilha Excel
- Acessar o site **Neoservice**
- Realizar login automaticamente
- Preencher formulários
- Gerar um código no Neoservice
- Utilizar esse código no **AppMiss**
- Gerar um **relatório simples (.txt)** ao final da execução

---

## 🧱 Stack / Tecnologias

- Node.js
- Playwright (automação de navegador)
- Arquitetura MVC adaptada para RPA
- Execução local (Windows)

---

## 📁 Estrutura de Pastas

```txt
src/
 ├── controllers/        # Orquestração dos fluxos
 ├── services/           # Automações e regras de negócio
 ├── repositories/       # Leitura de Excel / persistência
 ├── models/             # Estruturas de dados
 ├── selectors/          # IDs e seletores dos sites
 ├── utils/              # Funções auxiliares
 ├── reports/            # Relatórios de execução
 ├── config/             # Configurações e variáveis
 └── index.js            # Ponto de entrada da aplicação

data/
 └── input.xlsx          # Planilha de entrada
