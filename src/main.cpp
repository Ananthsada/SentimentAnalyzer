#include <iostream>
#include <string>

#include "spacy/spacy"
#include "csv.hpp"

const std::string dataSet = "/mnt/c/Study/NLP/FreeCodeCamp/IMDB_Dataset_Stripped.csv";
int main()
{
    Spacy::Spacy spacy;
    auto nlp = spacy.load("en_core_web_sm");

    csv::CSVReader reader(dataSet);
    auto firstRow = reader.begin();
    auto firstField = firstRow->begin();
    std::string example = firstField->get();

    auto Doc = nlp.parse(example);

    std::vector<Spacy::Token> _filteredTokens;
    for (auto& token : Doc.tokens())
    {
        if(!token.is_stop())
        {
            _filteredTokens.emplace_back(token);
        }
    }

    for(auto each : _filteredTokens)
    {
        std::cout << each.text() << " ";
    }
        

    return 0;
}
