#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//#define SZ 5000
int main(int argc, char const *argv[])
{


    time_t t;
    srand((unsigned) time(&t));
 
    int SZ;
    printf("Tamanho da entrada:\n");
    scanf ("%d", &SZ);
    FILE *ptr;
    ptr = fopen("random.bin", "wb");
    unsigned char buffer[SZ];
    for (int i = 0; i < SZ; ++i)
    {
        buffer[i]=(char)rand();
    }
    fwrite(buffer, SZ, 1, ptr);
    return 0;
}
