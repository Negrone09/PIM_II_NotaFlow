#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL,"Portuguese_Brazil"); 
    setlocale(LC_NUMERIC,"C");

    FILE *arquivo;
    char disciplina[50];
    char nome[100], ra[20], turma[10];
    float nota1, nota2, nota3, nota4, media;

    printf("=== Sistema NotaFlow ===\n\n");
    printf("Informe o nome da disciplina (sem acentos): ");
    scanf("%s", disciplina);

    char nomeArquivo[100];
    sprintf(nomeArquivo, "%s.txt", disciplina); 

    arquivo = fopen(nomeArquivo, "r");
    if (arquivo == NULL) {
        printf("Erro: não foi possível abrir o arquivo '%s'.\n", nomeArquivo);
        return 1;
    }

    printf("\n--- Relatório da Disciplina: %s ---\n\n", disciplina);

    while (fscanf(arquivo, "%[^;];%[^;];%[^;];%f;%f;%f;%f;%f\n",
                  nome, ra, turma, &nota1, &nota2, &nota3, &nota4, &media) != EOF) {
        printf("Aluno: %s\n", nome);
        printf("RA: %s\n", ra);
        printf("Turma: %s\n", turma);
        printf("Notas: %.2f | %.2f | %.2f | %.2f\n", nota1, nota2, nota3, nota4);
        printf("Média Final: %.2f\n", media);
        printf("------------------------------\n");
    }

    fclose(arquivo);
    return 0;
}