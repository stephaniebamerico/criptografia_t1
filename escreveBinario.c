#include <stdio.h>
#define SZ 50000
int main(int argc, char const *argv[])
{
    FILE *ptr;
    ptr = fopen("test.bin", "wb");
    unsigned char buffer[SZ];
    for (int i = 0; i < SZ; ++i)
    {
        buffer[i]=i;
    }
    fwrite(buffer, SZ, 1, ptr);
    fclose(ptr);
    /*ptr = fopen("waveHeader.bin", "rb");
    fread(buffer, 128, 1, ptr);
    for (int i = 0; i < 128; ++i)
    {
        printf("%3d %c\n", buffer[i],buffer[i]);
    }*/
    return 0;
}