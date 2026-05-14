# 🧬 Simulação de Herança de Tipo Sanguíneo (CS50)

Este projeto faz parte do curso CS50 de Harvard e tem como foco simular
como os tipos sanguíneos são herdados ao longo das gerações usando a
linguagem de programação C.

------------------------------------------------------------------------

## 📌 Visão Geral

O tipo sanguíneo de uma pessoa é determinado por **dois alelos** (diferentes formas
de um gene):

-   A
-   B
-   O

Cada indivíduo herda: - Um alelo da mãe - Um alelo
do pai

------------------------------------------------------------------------

## 🧬 Combinações Possíveis de Tipo Sanguíneo

Cada pessoa possui dois alelos, resultando nas seguintes combinações:

-   OO
-   OA
-   OB
-   AO
-   AA
-   AB
-   BO
-   BA
-   BB

------------------------------------------------------------------------

## 👨‍👩‍👧 Regras de Herança

Cada pai passa aleatoriamente **um dos seus dois alelos** para o filho.

### Exemplo 1

-   Pai 1: AO\
-   Pai 2: BB

Tipos sanguíneos possíveis para o filho: - AB - OB

### Exemplo 2

-   Pai 1: AO\
-   Pai 2: OB

Tipos sanguíneos possíveis para o filho: - AO - OB - AB - OO

------------------------------------------------------------------------

## 🎯 Objetivo

Escrever um programa em C que:

1.  Simule uma árvore genealógica com um número definido de gerações
2.  Atribua alelos de tipo sanguíneo a cada pessoa
3.  Modele a herança dos pais para os filhos
4.  Utilize alocação dinâmica de memória

------------------------------------------------------------------------

## 📂 Estrutura do Projeto

    .
    └── inheritance/
        └── inheritance.c

------------------------------------------------------------------------

## ⚙️ Detalhes de Implementação

### 🔹 Função create_family

-   Recebe um inteiro `generations` como entrada
-   Aloca memória para cada pessoa usando `malloc`
-   Retorna um ponteiro para a **geração mais jovem**

### 🔹 Estrutura da Família

-   Cada pessoa possui:
    -   Dois alelos
    -   Dois pais (ponteiros)

### 🔹 Geração Mais Antiga

-   Os alelos são atribuídos aleatoriamente usando `random_allele`
-   Os pais são definidos como `NULL`

### 🔹 Gerações Mais Jovens

-   Cada pessoa:
    -   Herda um alelo aleatoriamente de cada pai
    -   Possui dois pais (ponteiros para outras structs `person`)

------------------------------------------------------------------------

## ▶️ Como Executar

Compile o programa:

``` bash
gcc inheritance.c -o inheritance
```

Execute o programa:

``` bash
./inheritance
```

------------------------------------------------------------------------

## 🧠 Conceitos-Chave

-   Recursão (construção de árvores genealógicas)
-   Alocação dinâmica de memória (`malloc`)
-   Ponteiros e structs em C
-   Geração de números aleatórios
-   Simulação de genética do mundo real

------------------------------------------------------------------------

## ⚠️ Honestidade Acadêmica

Este repositório contém minha solução pessoal para um problema do CS50.

Não copie este código diretamente.\
Use-o apenas para aprendizado e referência.

------------------------------------------------------------------------

## 🚀 Melhorias Futuras

-   Representação visual da árvore genealógica
-   Tamanho de geração definido por entrada do usuário
-   Controle aprimorado de aleatoriedade

------------------------------------------------------------------------
