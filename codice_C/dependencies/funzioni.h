#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include "include/libpq-fe.h"

void checkTuples(PGresult* res, const PGconn* conn);
void checkCommand(PGresult *res, const PGconn *conn);
void checkConnection(PGconn* conn);
FILE* createFile(PGconn* conn, PGresult* res, char* name);
void printFile(PGresult* res, FILE* myfile);
char* readQueryFromFile(const char* filepath);

void checkTuples(PGresult *res, const PGconn *conn)
{
    if (PQresultStatus(res) != PGRES_TUPLES_OK)
    {
        printf(" Risultati inconsistenti %s\n", PQerrorMessage(conn));
        PQclear(res);
        exit(1);
    }
}

void checkCommand(PGresult *res, const PGconn *conn)
{
    if (PQresultStatus(res) != PGRES_COMMAND_OK)
    {
        fprintf(stderr, "Errore durante l'esecuzione: %s\n", PQerrorMessage(conn));
        PQclear(res);
        exit(1);
    }
    else
    {
        printf("Inserimento riuscito.\n");
    }
}

void checkConnection(PGconn *conn) {
    if (PQstatus(conn) != CONNECTION_OK)
    {
        printf("Errore di connessione: %s\n", PQerrorMessage(conn));
        PQfinish(conn);
        exit(1);
    }
    else
    {
        printf("Connessione avvenuta correttamente\n");
    }
}

FILE* createFile(PGconn* conn, PGresult* res, char* name) {
    FILE *myfile;
    myfile = fopen(name, "w");

    if (myfile == NULL) {
        printf("Errore nell'aprire il file CSV\n");
        PQclear(res);
        PQfinish(conn);
        exit(1);
    }
    return myfile;
}

void printFile(PGresult* res, FILE* myfile) {
    int tuple = PQntuples(res);
    int campi = PQnfields(res);

    // Stampo le intestazioni delle colonne
    for (int i = 0; i < campi; i++)
    {
        fprintf(myfile, "%s,", PQfname(res, i));
    }
    fprintf(myfile, "\n");

    // Stampo i valori selezionati
    for (int i = 0; i < tuple; i++)
    {
        for (int j = 0; j < campi; j++)
        {
            fprintf(myfile, "%s,", PQgetvalue(res, i, j));
        }
        fprintf(myfile, "\n");
    }
}

// Funzione per leggere l'intero contenuto di un file in una stringa dinamica
char* readQueryFromFile(const char* filepath) {
    FILE *file = fopen(filepath, "r");
    if (!file) {
        perror("Errore nell'apertura del file SQL");
        exit(EXIT_FAILURE);
    }

    struct stat st;
    stat(filepath, &st);
    long length = st.st_size;

    char *query = (char*) malloc(length + 1);
    if (!query) {
        perror("Errore di allocazione");
        exit(EXIT_FAILURE);
    }

    fread(query, 1, length, file);
    query[length] = '\0'; // null-terminate
    fclose(file);
    return query;
}