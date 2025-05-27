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
    char conninfo[250];
    sprintf(conninfo, "user=%s password=%s dbname=%s host=%s port=%d", PG_USER, PG_PASS, PG_DB, PG_HOST, PG_PORT);
    PGconn *conn = PQconnectdb(conninfo);
    checkConnection(conn);

    const char *query = "SELECT DISTINCT trip_number, origin FROM legs l WHERE l.origin = $1";
    PGresult *res = PQprepare(conn, "trip_number", query, 2, NULL);
    checkCommand(res, conn);
    
    FILE* myfile = createFile(conn, res);
    for (int i = 0; i < 10; i++)
    {
        char hub[50];
        printf("Inserire il nome di un hub: ");
        scanf("%49s", hub);
        if(hub[0] == '0') break;

        const char* parameter = hub;
        res = PQexecPrepared(conn, "trip_number", 1, &parameter, NULL, NULL, 0);
        checkTuples(res, conn);
        printFile(res, myfile);
        PQclear(res);
    }
    fclose(myfile);
    PQfinish(conn);
    return 0;
}