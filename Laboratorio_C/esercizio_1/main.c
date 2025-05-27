#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../dependencies/include/libpq-fe.h"
#include "../funzioni.h"

#define PG_HOST "localhost"
#define PG_USER "postgres"
#define PG_DB "LAB3"
#define PG_PASS "gigino"
#define PG_PORT 5432

int main(int argc, char **argv)
{
    // avvio la connessione
    char conninfo[250];
    sprintf(conninfo, "user=%s password=%s dbname=%s host=%s port=%d", PG_USER, PG_PASS, PG_DB, PG_HOST, PG_PORT);
    PGconn *conn = PQconnectdb(conninfo);
    checkConnection(conn);

    // prepara una sola volta
    const char *query = "INSERT INTO hubs (hub, country) VALUES ($1, $2)";
    PGresult *res = PQprepare(conn, "insert_hub", query, 2, NULL);
    checkCommand(res, conn);

    for (int i = 0; i < 3; i++)
    {
        char hub[50], country[50];
        printf("Inserire il nome dell'hub: ");
        scanf("%49s", hub);

        printf("Inserire codice paese di origine: ");
        scanf("%49s", country);

        const char *paramValues[2] = {hub, country};

        res = PQexecPrepared(conn, "insert_hub", 2, paramValues, NULL, NULL, 0);
        checkCommand(res, conn);
        PQclear(res);
    }

    PQfinish(conn);
    return 0;
}