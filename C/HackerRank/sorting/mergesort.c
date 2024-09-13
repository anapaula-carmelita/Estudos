#include <stdio.h>
#include <stdlib.h>

void intercala(int inicio, int meio, int fim, int* arr) {

    int i = inicio, j = meio, k = 0, *tmp;

    tmp = malloc((fim - inicio) * sizeof(int));

    while (i < meio && j < fim) {
        if (arr[i] < arr[j]) tmp[k++] = arr[i++];
        else tmp[k++] = arr[j++];
    }

    while (i < meio) tmp[k++] = arr[i++];
    while (j < fim) tmp[k++] = arr[j++];


    for (i = inicio; i < fim; i++) arr[i] = tmp[i-inicio];

    free(tmp);

}

void mergesort(int i, int j, int* arr) {
    if (i < j - 1) {

        int meio = (i+j) / 2;

        mergesort(i, meio, arr);
        mergesort(meio, j, arr);

        intercala(i, meio, j, arr);
    }
}

int main(void)
{
    int *list = malloc(10*sizeof(int));

    list[0] = 13;
    list[1] = 7;
    list[2] = 2;
    list[3] = 5;
    list[4] = 9;
    list[5] = 11;
    list[6] = 4;
    list[7] = 15;
    list[8] = 8;
    list[9] = 10;

    mergesort(0, 10, list);

    for (int i = 0; i < 10; i++) printf("%d ", list[i]);

    free(list);

    return 0;
}
