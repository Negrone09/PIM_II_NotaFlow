#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL,"Portuguese_Brazil"); 
    setlocale(LC_NUMERIC,"C");

    FILE *arquivo; 
    //Criação de um ponteiro para arquivo que servirá para abrir e ler o .txt
    char disciplina[50];
    char nome[100], ra[20], turma[10];
    float nota1, nota2, nota3, nota4, media;

    printf("=== Sistema NotaFlow ===\n\n");
    printf("Informe o nome da disciplina(sem acentos): ");
    scanf("%s", disciplina);
    /*Aqui tem um passo importante, solicita ao usuário
      o nome da disciplina que ele quer ver, que foi salvo
      no código em python
    */

    char nomeArquivo[100];
    sprintf(nomeArquivo, "%s.txt", disciplina);  
    /* o Spritf serve para formatar o nome da disciplina
    armazenada na variável que o usuário cadastrou
    e formata essa variável (.TXT) que será utilizado a seguir
    */
 
    arquivo = fopen(nomeArquivo, "r");
    /* O ponteiro arquivo que foi criado no começo
    vai ser usado paro abrir o arquivo formato txt que
    foi salvo no código em Python, então essa linha diz
    o seguinte = "No ponteiro arquivo, abra o nome arquivo
    (que dentro dele tem o nome da disciplina), e abra no modo
    leitura."
    */
    if (arquivo == NULL) {
        printf("Erro: não foi possível abrir o arquivo '%s'.\n", nomeArquivo);
        return 1;
    /* Caso a busca do arquivo resultar em nulo, printe 
    a mensagem de erro, e retorne 1.
    */
    }

    printf("\n--- Relatório da Disciplina: %s ---\n\n", disciplina);

    while (fscanf(arquivo, "%[^;];%[^;];%[^;];%f;%f;%f;%f;%f\n",
                  nome, ra, turma, &nota1, &nota2, &nota3, &nota4, &media) != EOF) {
    /* Essa linha é chave no sistema, pois ela é responsavel pelo seguinte:
    "Enquanto existir linhas no arquivo, peguei as informações salvas, e transforme
    em variaveis, caso não tiver mais linhas, pare o while.
    
    resumindo de forma mais técnica: O fscanf lê uma linha do arquivo e
    separa cada campo usando o ponto e vírgula como delimitador.
    %[^;] lê texto até encontrar ';' (nome, RA e turma)
    %f    lê as notas e a média como números
    O while continua executando enquanto ainda houver linhas no arquivo.
*/              
        printf("Aluno: %s\n", nome);
        printf("RA: %s\n", ra);
        printf("Turma: %s\n", turma);
        printf("Notas: %.2f | %.2f | %.2f | %.2f\n", nota1, nota2, nota3, nota4);
        printf("Média Final: %.2f\n", media);
        printf("------------------------------\n");
    }
    // print de todas as médias e informações do aluno.
    fclose(arquivo);
    //fechamento do ponteiro.
    return 0;
}

