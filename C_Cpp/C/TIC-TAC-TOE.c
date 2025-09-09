#include <stdio.h>

void displayBoard(char board[3][3]);
int checkWinner(char board[3][3]);
int isBoardFull(char board[3][3]);

int main() {
    char board[3][3] = {
        {' ', ' ', ' '},
        {' ', ' ', ' '},
        {' ', ' ', ' '}
    };
    
    int row, col;
    char currentPlayer = 'X';
    int gameWon = 0;
    int moves = 0;
    
    printf("=== TIC-TAC-TOE GAME ===\n");
    printf("Players: X and O\n");
    printf("Enter row (0-2) and column (0-2)\n\n");
    
    while (!gameWon && moves < 9) {
        displayBoard(board);
        
        printf("Player %c's turn\n", currentPlayer);
        printf("Enter row and column: ");
        scanf("%d %d", &row, &col);
        
        // Validate move
        if (row < 0 || row > 2 || col < 0 || col > 2) {
            printf("Invalid position! Try again.\n");
            continue;
        }
        
        if (board[row][col] != ' ') {
            printf("Position already taken! Try again.\n");
            continue;
        }
        
        // Make move
        board[row][col] = currentPlayer;
        moves++;
        
        // Check for winner
        gameWon = checkWinner(board);
        if (gameWon) {
            displayBoard(board);
            printf("Player %c wins!\n", currentPlayer);
            break;
        }
        
        // Switch player
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }
    
    if (!gameWon && moves == 9) {
        displayBoard(board);
        printf("It's a tie!\n");
    }
    
    return 0;
}

void displayBoard(char board[3][3]) {
    int i, j;
    
    printf("\n   0   1   2\n");
    for (i = 0; i < 3; i++) {
        printf("%d ", i);
        for (j = 0; j < 3; j++) {
            printf(" %c ", board[i][j]);
            if (j < 2) printf("|");
        }
        printf("\n");
        if (i < 2) printf("  -----------\n");
    }
    printf("\n");
}

int checkWinner(char board[3][3]) {
    int i;
    
    // Check rows
    for (i = 0; i < 3; i++) {
        if (board[i][0] != ' ' && 
            board[i][0] == board[i][1] && 
            board[i][1] == board[i][2]) {
            return 1;
        }
    }
    
    // Check columns
    for (i = 0; i < 3; i++) {
        if (board[0][i] != ' ' && 
            board[0][i] == board[1][i] && 
            board[1][i] == board[2][i]) {
            return 1;
        }
    }
    
    // Check diagonals
    if (board[0][0] != ' ' && 
        board[0][0] == board[1][1] && 
        board[1][1] == board[2][2]) {
        return 1;
    }
    
    if (board[0][2] != ' ' && 
        board[0][2] == board[1][1] && 
        board[1][1] == board[2][0]) {
        return 1;
    }
    
    return 0;
}
