#include <stdio.h>
int main(int argc, char const *argv[])
{
    int size = 128;

    char riff_header[4]; // Contains "RIFF"
    int wav_size=36+size; // Size of the wav portion of the file, which follows the first 8 bytes. File size - 8
    char wave_header[4]; // Contains "WAVE"

    // Format Header
    char fmt_header[4]; // Contains "fmt " (includes trailing space)
    int fmt_chunk_size=16; // Should be 16 for PCM
    short audio_format=1; // Should be 1 for PCM. 3 for IEEE Float
    short num_channels=1;
    int sample_rate=44100;
    int byte_rate=sample_rate*num_channels*1; // Number of bytes per second. sample_rate * num_channels * Bytes Per Sample
    short sample_alignment=num_channels*1; // num_channels * Bytes Per Sample
    short bit_depth=8; // Number of bits per sample

    // Data
    char data_header[4]; // Contains "data"
    int data_bytes=size; // Number of bytes in data. Number of samples * num_channels * sample byte size
    // uint8_t bytes[]; // Remainder of wave file is bytes
    riff_header[0]='R';
    riff_header[1]='I';
    riff_header[2]='F';
    riff_header[3]='F';

    wave_header[0]='W';
    wave_header[1]='A';
    wave_header[2]='V';
    wave_header[3]='E';

    fmt_header[0]='f';
    fmt_header[1]='m';
    fmt_header[2]='t';
    fmt_header[3]=' ';

    data_header[0]='d';
    data_header[1]='a';
    data_header[2]='t';
    data_header[3]='a';

    FILE *ptr;
    ptr = fopen("waveHeader.bin", "wb");
    unsigned char wav_size2[4];
    int sz = wav_size;
    for (int i = 0; i < 4; ++i)
    {
        wav_size2[i]=sz%256;
        sz=sz/256;
        printf("%d\n",wav_size2[i] );
    }
    
    /*fwrite(riff_header, 1, 4, ptr);
    fwrite((const void*) & wav_size, 4, 1, ptr);
    fwrite(wave_header, 1, 4, ptr);*/
   

    fwrite(fmt_header, 1, 4, ptr);
    fwrite((const void*) & fmt_chunk_size, 4, 1, ptr);
    fwrite((const void*) & audio_format, 2, 1, ptr);
    fwrite((const void*) & num_channels, 2, 1, ptr);
    fwrite((const void*) & sample_rate, 4, 1, ptr);
    fwrite((const void*) & byte_rate, 4, 1, ptr);
    fwrite((const void*) & sample_alignment, 2, 1, ptr);
    fwrite((const void*) & bit_depth, 2, 1, ptr);
    

    /*fwrite(data_header, 1, 4, ptr);
    fwrite((const void*) & data_bytes, 4, 1, ptr);
    unsigned char buffer[128];
    for (int i = 0; i < 128; ++i)
    {
        buffer[i]=i;
    }
    for (int i = 0; i < size; ++i)
        fwrite(buffer, 1, 128, ptr);
    fclose(ptr);
    printf("%d\n",wav_size );*/


    return 0;
} 
