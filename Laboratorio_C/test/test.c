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
    //avvio la connessione
    char conninfo[250];
    sprintf(conninfo, "user=%s password=%s dbname=%s host=%s port=%d", PG_USER, PG_PASS, PG_DB, PG_HOST, PG_PORT);
    PGconn *conn = PQconnectdb(conninfo);

    //controllo lo stato della connessione
    checkConnection(conn);

    // Definisco la query parametrica
    char *query = "SELECT origin , destination , departure_time , arrival_time FROM hubs JOIN legs on origin = hub WHERE country = $1 ::varchar";

    // Preparo la query prima che venga eseguita
    PGresult* res = PQprepare(conn, "query1", query, 1, NULL);
    char country[50];
    printf("Inserire codice paese di origine: ");
    scanf("%s", country);
    const char *parameter = country;

    // Eseguo lo statement query1 passando come parametro l'ID del paese di origine
    res = PQexecPrepared(conn, "query1", 1, &parameter, NULL, 0, 0);

    //controllo i risultati
    checkTuples(res, conn);

    //creo il file di output
    FILE* myfile = createFile(conn, res);

    //stampo i risultati della query nel file creato
    printFile(res, myfile);
    
    fclose(myfile);
    PQclear(res);
    PQfinish(conn);
    return 0;
}