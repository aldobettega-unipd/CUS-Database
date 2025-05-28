#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../dependencies/include/libpq-fe.h"
#include "../../dependencies/funzioni.h"

#define PG_HOST "localhost"
#define PG_USER "postgres"
#define PG_DB "progetto_basi"
#define PG_PASS "gigino"
#define PG_PORT 5432

int main(int argc, char **argv)
{
    // avvio la connessione
    char conninfo[250];
    sprintf(conninfo, "user=%s password=%s dbname=%s host=%s port=%d", PG_USER, PG_PASS, PG_DB, PG_HOST, PG_PORT);
    PGconn *conn = PQconnectdb(conninfo);
    checkConnection(conn);

    //leggo la query e la preparo
    char *query = readQueryFromFile("../../query/iscritti_range.sql");
    PGresult *res = PQprepare(conn, "iscritti_range", query, 2, NULL);
    free(query); // libera la memoria dopo la prepare
    checkCommand(res, conn);

    FILE *myfile = createFile(conn, res, "iscritti_range.csv");

    //prendo in input il range
    const char lower[10];
    const char upper[10];
    printf("Inserire lower bound iscritti: ");
    scanf("%9s", lower);
    printf("Inserire upper bound iscritti: ");
    scanf("%9s", upper);
    const char *paramValues[2] = {lower, upper};

    //eseguo la query e stampo il risultato in output
    res = PQexecPrepared(conn, "iscritti_range", 2, paramValues, NULL, NULL, 0);
    checkTuples(res, conn);
    printFile(res, myfile);
    PQclear(res);

    fclose(myfile);
    PQfinish(conn);
    return 0;
}