/*
 *  Nome do arquivo: flip_solution_1.c
 *  Descrição: Primeira tentativa para a solução do problema Flipping The Matrix do site Hacker Rank
 *  URL: https://www.hackerrank.com/challenges/flipping-the-matrix/problem
 *  Autor: Ana Paula da Silva Souza
 *  Data: 09/2024
 *  Versão: 1.0
 *  Licença: Apache
 */
#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* readline();
char* ltrim(char*);
char* rtrim(char*);
char** split_string(char*);

int parse_int(char*);

int soma(int n, int quadrante, int **matrix, int* soma_linhas, int* soma_colunas) {
    int total = 0;
    int i;
    int j;
    int k;
    int m;
    if (quadrante == 4) {
        i = n/2;
        k = 0;
        m = n;
        for (; i < n; i++, k++){
            soma_colunas[k] = 0;
            soma_linhas[k] = 0;
            for (j = n/2; j < m; j++){
                soma_colunas[k] += matrix[j][i];
                soma_linhas[k] += matrix[i][j];
            }
            total += soma_colunas[k];
        }
    } else if (quadrante == 3) {
        i = n/2;
        j = 0;
        m = n/2;
        k = 0;
        int l = n/2;
        for (i = n/2; i < n; i++, k++){
            soma_colunas[k] = 0;
            soma_linhas[k] = 0;
            for (j = 0, l = n/2; j < m; j++){
                soma_colunas[k] += matrix[l+j][j];
                soma_linhas[k] += matrix[i][j];
            }
            total += soma_colunas[k];
        }
    } else if (quadrante == 2) {
        i = 0;
        k = 0;
        m = n;
        n = n/2;
        for (; k < n && i < n; i++, k++){
            soma_linhas[k] = 0;
            for (j = n; j < m; j++) {
                soma_linhas[k] += matrix[i][j];
            }
            total += soma_linhas[k];
        }
        for (j = n, k = 0; j < m; j++, k++) {
            soma_colunas[k] = 0;
            for (i = 0; i < n; i++) {
                soma_colunas[k] += matrix[i][j];
            }
        }

    } else {
        i = 0;
        k = 0;
        n = n/2;
        m = n;
        for (; i < n; i++, k++){
            soma_linhas[k] = 0;
            soma_colunas[k] = 0;
            for (j = 0; j < m; j++){
                soma_colunas[k] += matrix[j][i];
                soma_linhas[k] += matrix[i][j];
            }
            total += soma_colunas[k];
        }
    }
    return total;
 }

// devolve o quadrante que tem a soma maior
int maior_quadrante(int soma1, int soma2, int soma3, int soma4) {

    if (soma1 < soma2 || soma1 < soma3 || soma1 < soma4){
        if (soma2 < soma3 || soma2 < soma4){
            if (soma3 < soma4){
                return 4;
            }
            return 3;
        }
        return 2;
    }
    return 1;
}

void inverte_coluna(int coluna, int** matrix, int n) {
    int aux;
    for (int i = 0; i < n / 2; i++){
        aux = matrix[i][coluna];
        matrix[i][coluna] = matrix[n - 1 - i][coluna];
        matrix[n - 1 - i][coluna]= aux;
    }
}

void inverte_linha(int linha, int** matrix, int n) {
    int aux;
    for (int i = 0; i < n / 2; i++){
        aux = matrix[linha][i];
        matrix[linha][i] = matrix[linha][n - 1 - i];
        matrix[linha][n - 1 - i] = aux;
    }
}

/*
 * Complete the 'flippingMatrix' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY matrix as parameter.
 */

int flippingMatrix(int matrix_rows, int matrix_columns, int** matrix) {


    if (matrix_rows != matrix_columns)
        return -1;

    int n = matrix_rows;
    int* totais_linha_q1 = malloc (n/2 * sizeof(int));
    int* totais_linha_q2 = malloc (n/2 * sizeof(int));
    int* totais_linha_q3 = malloc (n/2 * sizeof(int));
    int* totais_linha_q4 = malloc (n/2 * sizeof(int));

    // soma as colunas
    int* totais_coluna_q1 = malloc (n/2 * sizeof(int));
    int* totais_coluna_q2 = malloc (n/2 * sizeof(int));
    int* totais_coluna_q3 = malloc (n/2 * sizeof(int));
    int* totais_coluna_q4 = malloc (n/2 * sizeof(int));

    int total1 = soma(n, 1, matrix, totais_linha_q1, totais_coluna_q1);
    int total2 = soma(n, 2, matrix, totais_linha_q2, totais_coluna_q2);
    int total3 = soma(n, 3, matrix, totais_linha_q3, totais_coluna_q3);
    int total4 = soma(n, 4, matrix, totais_linha_q4, totais_coluna_q4);

    int teste = 0;
    while (teste == 0) {
        int quadrante = maior_quadrante(total1, total2, total3, total4);
        int isInverte = -1;
        if (quadrante == 4) {
            if (total3 < total2){
                for (int i = 0; i < n/2; i++){
                    if (totais_coluna_q4[i] > totais_coluna_q2[i]) {
                        inverte_coluna(n/2+i, matrix, n);
                        isInverte = 0;
                    }
                }
                if (isInverte == 0){
                    total2 = soma(n, 2, matrix, totais_linha_q2, totais_coluna_q2);
                    total4 = soma(n, 4, matrix, totais_linha_q4, totais_coluna_q4);
                }

            } else {

                for (int i = 0; i < n/2; i++){
                    if (totais_linha_q4[i] > totais_linha_q3[i]) {
                        inverte_linha(n/2+i, matrix, n);
                        isInverte = 0;
                    }
                }
                if (isInverte == 0) {
                    total3 = soma(n, 3, matrix, totais_linha_q3, totais_coluna_q3);
                    total4 = soma(n, 4, matrix, totais_linha_q4, totais_coluna_q4);
                }
            }

        } else if (quadrante == 3){
            if (total1 <= total2 && total1 <= total4) {
                //verifica se inverte as linhas do 3 com o 4
                for (int j = 0; j < n/2; j++) {
                    if (totais_linha_q3[j] > totais_linha_q4[j]) {
                        inverte_linha(n/2+j, matrix, n);
                        isInverte = 0;
                    }
                }

                if (isInverte == 0){
                    total3 = soma(n, 3, matrix, totais_linha_q3, totais_coluna_q3);
                    total4 = soma(n, 4, matrix, totais_linha_q4, totais_coluna_q4);
                }
                isInverte = -1;

                //verifica se inverte as colunas do 2 com o do 4
                for (int i = 0; i < n/2; i++){
                    if (totais_coluna_q4[i] > totais_coluna_q2[i]) {
                        inverte_coluna(n/2+i, matrix, n);
                        isInverte = 0;
                    }
                }
                if (isInverte == 0) {
                    total2 = soma(n, 2, matrix, totais_linha_q2, totais_coluna_q2);
                    total4 = soma(n, 4, matrix, totais_linha_q4, totais_coluna_q4);
                }
            } else {

                // verifica se inverte as colunas do 1 com o do 3
                for (int i = 0; i < n/2; i++){
                    if (totais_coluna_q3[i] > totais_coluna_q1[i]) {
                        inverte_coluna(i, matrix, n);
                        isInverte = 0;
                    }
                }
                if (isInverte == 0) {
                    total1 = soma(n, 1, matrix, totais_linha_q1, totais_coluna_q1);
                    total3 = soma(n, 3, matrix, totais_linha_q3, totais_coluna_q3);
                }
            }

        } else if (quadrante == 2) {
            isInverte = -1;
            if (total1 < total3 && total1 < total4) {
                // verifica se inverte as linhas do 3 com o 4
                for (int i = 0; i < n/2; i++){
                    if (totais_linha_q3[i] > totais_linha_q4[i]) {
                        inverte_linha(n/2+i, matrix, n);
                        isInverte = 0;
                    }
                }
                if (isInverte == 0) {
                    total3 = soma(n, 3, matrix, totais_linha_q3, totais_coluna_q3);
                    total4 = soma(n, 4, matrix, totais_linha_q4, totais_coluna_q4);
                }
                isInverte = -1;
                //verifica se inverte as colunas do 2 com o 4
                for (int i = 0; i < n/2; i++){
                    if (totais_coluna_q4[i] > totais_coluna_q2[i]) {
                        isInverte = 0;
                        inverte_coluna(n/2+i, matrix, n);
                    }
                }
                if (isInverte == 0){
                    total2 = soma(n, 2, matrix, totais_linha_q2, totais_coluna_q2);
                    total4 = soma(n, 4, matrix, totais_linha_q4, totais_coluna_q4);
                }
                isInverte = -1;
            }
            //verifica se inverte o 1 com o do 2
            for (int i = 0; i < n/2; i++){
                if (totais_linha_q2[i] > totais_linha_q1[i]) {
                    inverte_linha(i, matrix, n);
                    isInverte = 0;
                }
            }
            if (isInverte == 0) {
                total1 = soma(n, 1, matrix, totais_linha_q1, totais_coluna_q1);
                total2 = soma(n, 2, matrix, totais_linha_q2, totais_coluna_q2);
            }
        } else {

            //verifica se inverte linhas do 1 com o 2
            for (int i = 0; i < n/2; i++){
                if (totais_linha_q2[i] > totais_linha_q1[i]) {
                    inverte_linha(0, matrix, n);
                    isInverte = 0;
                }
            }
            if (isInverte == 0) {
                total1 = soma(n, 1, matrix, totais_linha_q1, totais_coluna_q1);
                total2 = soma(n, 2, matrix, totais_linha_q2, totais_coluna_q2);
            }
            isInverte = -1;


            //verifica se inverte colunas do 3 com o 1
            for (int i = 0; i < n/2; i++){
                if (totais_coluna_q3[i] > totais_coluna_q1[i]) {
                    inverte_coluna(i, matrix, n);
                    isInverte = 0;
                }
            }
            if (isInverte == 0) {
                total1 = soma(n, 1, matrix, totais_linha_q1, totais_coluna_q1);
                total3 = soma(n, 3, matrix, totais_linha_q3, totais_coluna_q3);
            }
            if (total2 > total3) {
                isInverte = -1;
                //verifica se inverte as colunas do 2 com o 4
                for (int i = 0; i < n/2; i++){
                    if (totais_coluna_q4[i] > totais_coluna_q2[i]) {
                        isInverte = 0;
                        inverte_coluna(n/2+i, matrix, n);
                    }
                }
                if (isInverte == 0){
                    total2 = soma(n, 2, matrix, totais_linha_q2, totais_coluna_q2);
                    total4 = soma(n, 4, matrix, totais_linha_q4, totais_coluna_q4);
                }
            } else {
                isInverte = -1;
                // verifica se inverte as linhas do 3 com o 4
                for (int i = 0; i < n/2; i++){
                    if (totais_linha_q3[i] > totais_linha_q4[i]) {
                        inverte_linha(n/2+i, matrix, n);
                        isInverte = 0;
                    }
                }
                if (isInverte == 0) {
                    total3 = soma(n, 3, matrix, totais_linha_q3, totais_coluna_q3);
                    total4 = soma(n, 4, matrix, totais_linha_q4, totais_coluna_q4);
                }
                isInverte = -1;
                // verifica se troca colunas do 2 com o 4
                for (int i = 0, k = n/2; i < n/2 && k < n; i++, k++){
                    if (totais_coluna_q4[i] > totais_coluna_q2[i]) {
                        inverte_coluna(k, matrix, n);
                        isInverte = 0;
                    }
                }
                if (isInverte == 0) {
                    total2 = soma(n, 2, matrix, totais_linha_q2, totais_coluna_q2);
                    total4 = soma(n, 4, matrix, totais_linha_q4, totais_coluna_q4);
                }
            }

            if (total1 >= total2 && total1 >= total3 && total1 >= total4)
                break;
        }
    }

    free(totais_coluna_q1);
    free(totais_coluna_q2);
    free(totais_coluna_q3);
    free(totais_coluna_q4);

    free(totais_linha_q1);
    free(totais_linha_q2);
    free(totais_linha_q3);
    free(totais_linha_q4);

    return total1;
}

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    int q = parse_int(ltrim(rtrim(readline())));

    for (int q_itr = 0; q_itr < q; q_itr++) {
        int n = parse_int(ltrim(rtrim(readline())));

        int** matrix = malloc((2 * n) * sizeof(int*));

        for (int i = 0; i < 2 * n; i++) {
            *(matrix + i) = malloc((2 * n) * (sizeof(int)));

            char** matrix_item_temp = split_string(rtrim(readline()));

            for (int j = 0; j < 2 * n; j++) {
                int matrix_item = parse_int(*(matrix_item_temp + j));

                *(*(matrix + i) + j) = matrix_item;
            }
        }

        int result = flippingMatrix(2 * n, 2 * n, matrix);

        fprintf(fptr, "%d\n", result);
    }

    fclose(fptr);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;

    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) {
            break;
        }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') {
            break;
        }

        alloc_length <<= 1;

        data = realloc(data, alloc_length);

        if (!data) {
            data = '\0';

            break;
        }
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';

        data = realloc(data, data_length);

        if (!data) {
            data = '\0';
        }
    } else {
        data = realloc(data, data_length + 1);

        if (!data) {
            data = '\0';
        } else {
            data[data_length] = '\0';
        }
    }

    return data;
}

char* ltrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    while (*str != '\0' && isspace(*str)) {
        str++;
    }

    return str;
}

char* rtrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    char* end = str + strlen(str) - 1;

    while (end >= str && isspace(*end)) {
        end--;
    }

    *(end + 1) = '\0';

    return str;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);

        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}

int parse_int(char* str) {
    char* endptr;
    int value = strtol(str, &endptr, 10);

    if (endptr == str || *endptr != '\0') {
        exit(EXIT_FAILURE);
    }

    return value;
}
