#include<stdio.h>
#include<string.h>

typedef struct {
    char eng[32];
    char uzb[32];
} word;

void show_menu(){
    printf("1. Add new word\n");
    printf("2. List of words\n");
    printf("3. Search word\n");
    printf("4. Exit\n");
    printf("\n>>> ");
}

void addNewWord(){
    word new;
    FILE *p = fopen("dict.txt", "a");
        printf("Eng: "); scanf("%s", new.eng);
        printf("Uzb: "); scanf("%s", new.uzb);
        fprintf(p,"%s ", new.eng);printf("%10s|%-10s\n", "English", "Uzbek");
    printf("---------------------\n");
        fprintf(p,"%s\n", new.uzb);
    fclose(p);
}

int listOfWords(){
    FILE *p = fopen("dict.txt", "r");
    if(p == NULL){
        printf("Error\n");
        return 1;
    }
    word list;
    printf("||%10s|%-10s||\n", "##English", "Uzbek##");
    printf("---------------------\n");

    while(fscanf(p, "%s", list.eng) != EOF){
        fscanf(p, "%s", list.uzb);
        printf("%10s|%-10s\n", list.eng, list.uzb);
    }
    fclose(p);
}

int search(){
    char s_word[32];
    printf("Search word: "); scanf("%s", s_word);
    FILE *p = fopen("dict.txt", "r");
    if(p == NULL){
        printf("Error\n");
        return 1;
    }
    word list;
    
    while(fscanf(p, "%s", list.eng) != EOF){
        fscanf(p, "%s", list.uzb);
        if(!strcmp(s_word, list.eng) || !strcmp(s_word, list.uzb)){
            printf("%10s|%-10s\n", list.eng, list.uzb);
            return 0;
        }
    }
    fclose(p);
    return -1;
}


int main(){
    int ch;
    show_menu();
    scanf("%d", &ch);
    switch(ch){
        case 1: 
            addNewWord();
            break;
        case 2: 
            listOfWords();
            break;
        case 3:
            search();
            break;
        case 4:
            break;
        default:
            printf("Sorry\n");
    }

    return 0;
}