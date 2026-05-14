# 🧬 Perfil de DNA (CS50)

Este projeto faz parte do curso CS50 de Harvard e tem como foco a
identificação de DNA usando **Repetições Curtas em Tandem (STRs)**.

## 📌 Visão Geral

O DNA é composto por sequências de nucleotídeos representados pelas letras:

-   A (Adenina)
-   C (Citosina)
-   G (Guanina)
-   T (Timina)

Certas regiões do DNA contêm **Repetições Curtas em Tandem (STRs)** --- sequências
curtas que se repetem várias vezes.\
O número de repetições varia entre indivíduos, tornando as STRs úteis
para identificação.

------------------------------------------------------------------------

## 🎯 Objetivo

O objetivo deste programa é:

1.  Ler uma sequência de DNA
2.  Analisar padrões de STR
3.  Comparar os resultados com um banco de dados
4.  Identificar o indivíduo OU retornar `Nenhuma correspondência`

------------------------------------------------------------------------

## 📂 Estrutura do Projeto

    .
    ├── dna.py
    ├── databases/
    │   ├── small.csv
    │   └── large.csv
    ├── sequences/
    │   ├── 1.txt
    │   ├── 2.txt
    │   ├── ... .txt
    │   └── 20.txt
    └── README.md

------------------------------------------------------------------------

## 🗃️ Formato do Banco de Dados

O banco de dados é um arquivo CSV estruturado assim:

``` csv
nome,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Carlos,36,18,25
```

------------------------------------------------------------------------

## 🔍 Como Funciona

1.  O programa varre a sequência de DNA
2.  Encontra a **maior sequência consecutiva** de cada STR
3.  Compara as contagens com cada pessoa no banco de dados
4.  Exibe o nome correspondente

### Exemplo:

Se a sequência contém:

-   AGAT → 17 repetições\
-   AATG → 22 repetições\
-   TATC → 19 repetições

✅ Saída:

    Bob

Se nenhuma correspondência for encontrada:

❌ Saída:

    Nenhuma correspondência

------------------------------------------------------------------------

## ▶️ Como Executar

Certifique-se de ter o Python instalado.

``` bash
python dna.py databases/small.csv sequences/sequence1.txt
```

------------------------------------------------------------------------

## 🧠 Conceitos-Chave

-   Processamento de strings
-   Correspondência de padrões
-   Manipulação de arquivos CSV
-   Dicionários e listas
-   Algoritmos para análise de sequências

------------------------------------------------------------------------

## ⚠️ Honestidade Acadêmica

Este repositório contém minhas soluções pessoais para os conjuntos de problemas do CS50.

Por favor, não copie este código diretamente.\
Use-o apenas para aprendizado e referência.

------------------------------------------------------------------------

## 🚀 Melhorias Futuras

-   Adicionar visualização das correspondências de STR
-   Otimizar o desempenho da busca
-   Criar uma interface simples para entrada e saída

------------------------------------------------------------------------
