#include "hangman.hpp"


// Welcome prompt for the user
void welcome_prompt() {
    cout << "++++++++++|Welcome to the HANGMAN game|++++++++++" << endl;
    char a;
    cout << "\nDo you want the rules to be displayed?(y/n) ";
    cin >> a;
    if (a == 'y') {
        cout << "\nYou will get lives depending upon your choice of level" << endl;
        cout << "\nYou need to guess the missing letters of the given words in those many lives(chances)" << endl;
        cout << "\nYou will be given points based on how many lives you were left with before guessing the whole word" << endl;
        cout << "\nYour points will be added to your overall score which will be displayed at the end of the game" << endl;
        cout << "\nHave fun playing... and getting yourself hanged" << endl;
        cout << "======================================================================" << endl;
    } else if (a == 'n') {
        cout << "\nHave fun playing... and getting yourself hanged" << endl;
        cout << "======================================================================" << endl;
    } else {
        cout << "\nPlease learn to follow instructions" << endl;
        cout << "======================================================================" << endl;
    }
}


// Asking the user if they want to view how the score is distributed
void score_decide_prompt() {
    char response;
    cout << "======================================================================" << endl;
    cout << "Do you want to know how is the score given?(y/n) ";
    cin >> response;

    if (response == 'y') {
        cout << "\nThe points for each round will be given on the basis of difficulty level you choose." << endl;
        cout << "\nThe remaining lives will be multiplied by a fixed amount of points for a particular level." << endl;
        cout << "\nThe point per life are as follows:" << endl;
        cout << "\nEasy -> 1 point/life" << endl;
        cout << "\nMedium -> 5 points/life" << endl;
        cout << "\nHard -> 10 points/life" << endl;
        cout << "\nImpossible -> 15 points/life" << endl;
        cout << "\nBest of luck... Hope to see you win impossible level" << endl;
        cout << "======================================================================" << endl;
    }
    else if (response == 'n') {
        cout << "\nBest of luck... Hope to see you win impossible level" << endl;
        cout << "======================================================================" << endl;
    }
    else {
        cout << "\nNow I know the reason why you have no friends... such a looser" << endl; 
        cout << "======================================================================" << endl;
    }
}


// Getting the level from the user
char get_level() {
    char lev;
    bool correct = true;
    cout << "======================================================================" << endl;
    cout << "\nLevel Selection: " << endl;
    cout << "----- ---------_" << endl;
    while (correct) {
        static int n = 3;
        cout << "\ne -> Easy(6 lives)" << endl;
        cout << "m -> Medium(5 lives)" << endl;
        cout << "h -> Hard(4 lives)" << endl;
        cout << "i -> Impossible(3 lives)" << endl;
        cout << "q -> Quit" << endl;
        cout << "Your choice: ";
        cin >> lev;
        cout << "\nWAIT... your fate is being decided...\n" << endl;
        if (lev == 'e' || lev == 'm' || lev == 'h' || lev == 'i' || lev == 'q')
            correct = false;
        else {
            n--;
            if ( n == 0){
                lev = 'q';
                correct = false;
                break;
            } else {
                cout << "-------------------------------------------------------------------------" << endl;
                cout << "\n|Please give a correct response. " << n << " more wrong response and you are out.|" << endl;
                cout << "-------------------------------------------------------------------------" << endl;
            }
        }
    }

    return lev;
}


// Getting the life for the choice of the level
int get_life(const char &l) {
    int a;
    if (l == 'e') 
        a = 6;
    else if (l == 'm')
        a = 5;
    else if (l == 'h')
        a = 4; 
    else if (l == 'i')
        a = 3;

    return a;
}


// Get a random word from the words vector
string get_word(const vector<string> &w) {
    int r{};
    int min{};
    int max{2455};      //2455 because the words consists fo 2455 words

    srand(time(nullptr));

    r = rand() % max + min;
    
    return w.at(r);
}

// Verifies the word on the basis of level
string valid_word(const char &l, const vector<string> &w) {
    bool active = true;
    string valid;
    do {

        valid = get_word(w);
        if (l == 'e' && valid.length() <= 6 && valid.length() > 4)
            active = false;
        else if (l == 'm' && valid.length() <= 8 && valid.length() > 6)
            active = false;
        else if (l == 'h' && valid.length() <= 10 && valid.length() > 8)
            active = false;
        else if (l == 'i' && valid.length() > 10)
            active = false;

    } while(active);

    return valid;
}


// Functions that will get rid of all the non-alpha chars
string make_word_usable(string &s) {
    string word;
    for (auto i: s) {
        if (isalpha(i))
            word.push_back(i);
    }
    return word;
}


// Asking the player to play again or quit
char ask_for_play_again() {
    char pa;
    cout << "\nDo you want to play again?(y / anything else) ";
    cin >> pa;
    cout << "\n--------------------------------------------" << endl;
    return pa;
}


// Making the playable string
string make_play_word(const string &str) {
   string s;
   for (long unsigned int i = 0; i < str.length(); i++) {
       s.push_back('-');
   }

   return s;
}


// Gets the score of the game
int get_score(char &lev, int &l) {
    int s;
    switch (lev) {
    case 'e':
        s = l * 1;
        break;
    
    case 'm':
        s = l * 5;
        break;
    
    case 'h':
        s = l * 10;
        break;
        
    case 'i':
        s = l * 15; 
        break;

    default:
        break;
    }

    return s;
}


