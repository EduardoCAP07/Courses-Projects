// Implements a dictionary's functionality
#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Number of buckets in hash table
const unsigned int N = 456977;

// Hash table
node *table[N];

// Variable to store number of words loaded into dictionary
int dicsum = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Use hash function to get the words key
    int key = hash(word);
    // If pointer not NULL, than make traversal node and
    // compare word by word until pointer is NULL or word is found.
    if (table[key] != NULL)
    {
        node *trav = table[key];
        while (trav != NULL)
        {
            if (strcasecmp(word, trav->word) == 0)
            {
                return true;
            }
            trav = trav->next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Get 3 first leters of the word
    int asc[3];
    int sum = 0;
    int countback = 3;
    // If the word has 2 letters than create a hash
    if (word[2] == '\0')
    {
        for (int i = 0; i < 2; i++)
        {
            asc[i] = toupper(word[i]) - 'A';
            asc[i] = (int) pow(10, countback);
            sum += asc[i];
            countback--;
        }
    }
    // If the word has at least 3 letters create a hash
    else if (word[3] == '\0')
    {
        for (int i = 0; i < 3; i++)
        {
            asc[i] = toupper(word[i]) - 'A';
            asc[i] = (int) pow(10, countback);
            sum += asc[i];
            countback--;
        }
    }
    else
    {
        for (int i = 0; i < 4; i++)
        {
            asc[i] = toupper(word[i]) - 'A';
            asc[i] = (int) pow(10, countback);
            sum += asc[i];
            countback--;
        }
    }
    return round(sum / 14.3668);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // open file
    FILE *dic = fopen(dictionary, "r");
    if (dic == NULL)
    {
        printf("The file was empty\n");
        return false;
    }
    char buffer[LENGTH + 1];
    int scanresult;
    // Scanning the words in dictionary
    while ((scanresult = fscanf(dic, "%s", buffer)) != EOF)
    {
        if (scanresult != 1)
        {
            fclose(dic);
            return false;
        }
        dicsum++;
        // Make a key for the word
        int key = hash(buffer);
        // Create linked list
        node *n = malloc(sizeof(node));
        strcpy(n->word, buffer);
        n->next = table[key];
        table[key] = n;
    }
    fclose(dic);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (dicsum != 0)
    {
        return dicsum;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            unloadm(table[i]);
        }
    }
    return true;
}

void unloadm(node *n)
{
    if (n == NULL)
        return;

    // Recursively freeing n
    unloadm(n->next);

    free(n);
}
