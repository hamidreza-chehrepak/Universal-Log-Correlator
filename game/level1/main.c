#include <stdio.h>
#include <string.h>

int main(void)
{
    char password[50];

    const char correct_password[] = "cyber123";

    printf("====================================\n");
    printf("       UNIVERSAL CYBER RANGE\n");
    printf("          LEVEL 1\n");
    printf("====================================\n\n");

    printf("TARGET: Secure Database\n");
    printf("STATUS: Protected\n\n");

    printf("MISSION OBJECTIVE:\n");
    printf("Gain access to the test database.\n\n");

    printf("Enter password: ");
    scanf("%49s", password);

    if (strcmp(password, correct_password) == 0)
    {
        printf("\nACCESS GRANTED!\n");
        printf("Mission completed.\n");
        printf("Level 2 unlocked.\n");
    }
    else
    {
        printf("\nACCESS DENIED!\n");
        printf("Mission failed.\n");
    }

    return 0;
}