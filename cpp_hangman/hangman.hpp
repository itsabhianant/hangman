#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <unistd.h>


// Namespaces
using std::cout;
using std::endl;
using std::cin;
using std::string;
using std::vector;
using std::flush;


// Functions
void welcome_prompt();
void score_decide_prompt();
string get_word(const vector<string> &w);
string valid_word(const char &l, const vector<string> &w);
string make_word_usable(string &s);
char get_level();
int get_life(const char &l);
char ask_for_play_again();
string make_play_word(const string &str);
string check_input(const string &w, string &pw, const char l);
string play_game(char input);
int get_score(char &lev , int &l);