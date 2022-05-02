#include <iostream>
#include "spacy/spacy"
#include <fstream>
#include <string>
#include "csv.hpp"

const std::string dataSet = "/mnt/c/Study/NLP/FreeCodeCamp/IMDB_Dataset.csv";
int main()
{
    Spacy::Spacy spacy;
    auto nlp = spacy.load("en_core_web_sm");

    csv::CSVReader reader(dataSet);

    auto columnNames = reader.get_col_names();

    for(auto each : columnNames)
    {
        std::cout << each << "\n";
    }

    return 0;
}
