#include <stdio.h>
#include <sqlite3.h>

int main(void)
{
    sqlite3 *db;
    sqlite3_stmt *statement;

    int result;

    printf("====================================\n");
    printf("       UNIVERSAL CYBER RANGE\n");
    printf("          LEVEL 1\n");
    printf("====================================\n\n");

    printf("TARGET: Secure Database\n");
    printf("STATUS: ONLINE\n\n");

    result = sqlite3_open("database/target.db", &db);

    if (result != SQLITE_OK)
    {
        printf("DATABASE CONNECTION FAILED\n");
        return 1;
    }

    printf("DATABASE CONNECTION: SUCCESS\n\n");

    result = sqlite3_prepare_v2(
        db,
        "SELECT username, role, access_level FROM users;",
        -1,
        &statement,
        NULL
    );

    if (result != SQLITE_OK)
    {
        printf("DATABASE QUERY FAILED\n");
        sqlite3_close(db);
        return 1;
    }

    printf("DATABASE RECORDS:\n\n");

    while (sqlite3_step(statement) == SQLITE_ROW)
    {
        const unsigned char *username =
            sqlite3_column_text(statement, 0);

        const unsigned char *role =
            sqlite3_column_text(statement, 1);

        int access_level =
            sqlite3_column_int(statement, 2);

        printf(
            "User: %s | Role: %s | Access Level: %d\n",
            username,
            role,
            access_level
        );
    }

    sqlite3_finalize(statement);
    sqlite3_close(db);

    printf("\nDATABASE CLOSED.\n");

    return 0;
}