# 🔤 Verificador Ortográfico (CS50)

Este projeto faz parte do curso CS50 de Harvard e tem como foco a construção de um
**verificador ortográfico** rápido usando uma estrutura de dados de tabela hash implementada em C.

## 📌 Visão Geral

O programa lê um arquivo de texto palavra por palavra e verifica cada uma em relação a
um dicionário carregado, reportando quaisquer erros ortográficos junto com benchmarks
de desempenho para cada operação.

O principal desafio é implementar um dicionário eficiente usando:

-   Uma **tabela hash** para buscas rápidas
-   **Listas encadeadas** para tratar colisões
-   **Gerenciamento manual de memória** em C

---

## 🎯 Objetivo

O objetivo deste programa é:

1.  Carregar um dicionário de palavras em uma tabela hash
2.  Ler um arquivo de texto palavra por palavra
3.  Verificar cada palavra em relação ao dicionário
4.  Reportar todas as palavras com erros ortográficos
5.  Medir o tempo gasto em cada operação

---

## 📂 Estrutura do Projeto

    .
    ├── speller.c
    ├── dictionary.c
    ├── dictionary.h
    ├── Makefile
    ├── dictionaries/
    │   ├── small
    │   └── large
    ├── texts/
    │   ├── alice.txt
    │   ├── holmes.txt
    │   └── ...
    └── README.md

---

## 🗃️ Estrutura de Dados

Cada palavra é armazenada em um `node` dentro de uma tabela hash com `456.977` buckets:

```c
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;
```

As colisões são resolvidas com **encadeamento** — cada bucket contém uma lista encadeada de nós.

---

## 🔍 Como Funciona

1.  O programa carrega o dicionário na tabela hash
2.  Cada palavra do arquivo de texto é convertida em um índice de bucket via hash
3.  A lista encadeada naquele bucket é percorrida em busca de uma correspondência
4.  Palavras com erros ortográficos são exibidas no console
5.  Os benchmarks são reportados para as quatro operações

### Exemplo:

Se o texto contém a palavra `"speling"`:

-   Ela é convertida em um índice de bucket
-   A lista encadeada naquele bucket é percorrida
-   Nenhuma correspondência é encontrada

❌ Saída:

    speling

Se a palavra `"spelling"` é verificada:

-   Ela é convertida em seu bucket
-   `strcasecmp` encontra uma correspondência na lista encadeada

✅ Nenhuma saída (palavra está corretamente escrita)

---

## ▶️ Como Executar

Certifique-se de ter `clang` e `make` instalados.

``` bash
make speller
```

``` bash
# Usando o dicionário grande padrão
./speller texts/alice.txt

# Usando um dicionário personalizado
./speller dictionaries/small texts/alice.txt
```

### Exemplo de Saída:

```
PALAVRAS COM ERROS ORTOGRÁFICOS

foo
baz

PALAVRAS COM ERRO:        2
PALAVRAS NO DICIONÁRIO:   143091
PALAVRAS NO TEXTO:        17756
TEMPO EM load:            0.03
TEMPO EM check:           0.04
TEMPO EM size:            0.00
TEMPO EM unload:          0.02
TEMPO TOTAL:              0.09
```

---

## 🧠 Conceitos-Chave

-   Tabelas hash e listas encadeadas
-   Alocação dinâmica de memória (`malloc`, `free`)
-   Entrada e saída de arquivos em C
-   Manipulação e comparação de strings
-   Algoritmos recursivos
-   Prevenção de vazamentos de memória com `valgrind`

---

## ⚠️ Honestidade Acadêmica

Este repositório contém minha solução pessoal para um conjunto de problemas do CS50.

Por favor, não copie este código diretamente.\
Use-o apenas para aprendizado e referência.

---

## 🚀 Melhorias Futuras

-   Experimentar uma função hash melhor para reduzir colisões
-   Comparar o desempenho com uma implementação baseada em trie
-   Adicionar suporte para palavras com mais de 45 caracteres

---
