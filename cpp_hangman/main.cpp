#include "words.hpp"

int main() {
   
    welcome_prompt();
    score_decide_prompt();
    bool flag = true;
   
    do{
        string temp;
        string word;
        char level = tolower(get_level());
        vector<char> used_letters {'-'};
        int dash = 0, c = 0;
        static int score = 0;
        string t;
        int life = get_life(level);

        
        // If the player chooses to quit
        char play_again;
        if (level == 'q')
            goto quit;

        temp = valid_word(level, words);
        word = make_word_usable(temp);
        temp = make_play_word(word);
        for (long unsigned int i = 0; i < temp.length(); i++) {
            if (temp.at(i) == '-')
                dash++;
        }
        t = temp;
        cout << "Your word: " << t << endl;
        
        // Looping life times to play the game
        for (int i = life - 1; i >= 0; i--) {

            // Breaking the loop if the word is correctly guessed by the player
            if (c == dash) {
                cout << "\nOh shoot...you came out alive... the word is: " << t << endl;
                int leaf = i+ 1;
                cout << "Points gained from this round: " << get_score(level, leaf) << endl;
                cout << ".................................................\n" << endl;
                score += get_score(level, leaf);
                break;
            }
            char letter;
            bool repeat = true;
            cout << ".................................................\n" << endl;
            cout << "Letter: ";
            cin >> letter;
            long unsigned int a = 0;
            

            // Checking if the input letter is already used
            for (long unsigned int v = 0; v < used_letters.size(); v++) {
                if (used_letters.at(v) != toupper(letter)) 
                    a++;
                else
                    break;
            }

            
            // Adding the input letter in used_letter if it isn't there at the first place 
            if (a == used_letters.size()) {
                used_letters.push_back(toupper(letter));
                repeat = false;
            }
            

            // Prompting the user for a new letter if the input letter was already used
            if (repeat) {
                cout << "\nYou have already used " << letter << " . Please a try a new one" <<endl;
                i++;
                cout << "Lives left: " << i << endl;
                continue;
            }


            // Replacing the '-' with the input letter if it is present in the answer word
            for (long unsigned int j = 0; j < word.length(); j++) {
                if (word.at(j) == toupper(letter) && t.at(j) == '-') {
                    t.at(j) = toupper(letter);
                    c++;
                }
            }


            // Displaying the user if the answer is wrong/right and then updating the temp string for future comparision
            if (t == temp){
                cout << "\nOops!!! wrong letter" << endl;
                cout << visuals.at(i) << endl;
                cout << "Used letters: [ ";
                for (long unsigned int z = 1; z < used_letters.size(); z++) {
                    cout << used_letters.at(z) << ", ";
                }
                cout << "]" << endl;
                cout << "Your word: " << t << endl;
                cout << "Lifes left: " << i << endl;
            } else {
                cout << "\nCool... correct letter" << endl;
                cout << "Used letters: [ ";
                for (long unsigned int z = 1; z < used_letters.size(); z++) {
                    cout << used_letters.at(z) << ", ";
                }
                cout << "]" << endl;
                cout << "Your word: " << t << endl;
                i++;
                cout << "Lifes left: " << i << endl;
                temp = t;
            }
            if (i == 0) {
                cout << "\nHAHA...you were hanged... the word is " << word << endl;
                cout << "You got 0 points from this round" << endl;
                cout << ".................................................\n" << endl;
            }
        }
        
        // Asking the player for continuing the game
        play_again = ask_for_play_again();


        // If the player chooses to quit
        quit:
        if (level == 'q' || play_again != 'y') {
            flag = false;
            cout << "\nYour final score: " << score << endl;
            cout << "++++++++++++++++++++++++++++++++++++++++++++++" << endl;
        }
    }
    while(flag);
   

    return 0;
}