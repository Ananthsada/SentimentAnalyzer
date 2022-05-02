#include <iostream>
#include "spacy/spacy"
#include <fstream>
#include <string>

const std::string wikiText = "/mnt/c/Study/NLP/FreeCodeCamp/resources/test.txt";
int main()
{
    Spacy::Spacy spacy;
    auto nlp = spacy.load("en_core_web_sm");

    std::ifstream _ifstream(wikiText);
    std::string _inputText;
    auto doc = nlp.parse("This is a sentence.");
    for (auto& token : doc.tokens())
        std::cout << token.text() << " [" << token.pos_() << "]\n";
    return 0;
}
