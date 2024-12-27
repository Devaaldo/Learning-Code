#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

class Question {
public:
    std::string questionText;
    std::vector<std::string> options;
    int correctOption;

    Question(const std::string& text, const std::vector<std::string>& opts, int correct)
        : questionText(text), options(opts), correctOption(correct) {}
};

class Quiz {
public:
    std::vector<Question> questions;
    int score;

    Quiz() : score(0) {}

    void addQuestion(const std::string& text, const std::vector<std::string>& opts, int correct) {
        questions.emplace_back(text, opts, correct);
    }
};

// void displayQuestion(int index) const{
//     const Question& q = questions[index];
//     std::cout << "Question" << index + 1 << ": " 
//         << q.questionText << "\n";

//     for (size_t i=0;i<q.options.size(); ++i) {
//         std::cout << " " << i + 1 << ". "
//         << q.options[i] << "\n";
//     }
// };

// void startQuiz() {
//     score = 0;
//     for (size_t i=0; i < questions.size(); ++i) {
//         displayQuestion(i);
//         int userChoice = getUserChoice();
//         if (userChoice == questions[i].correctOption) {
//             std::cout << "Correct!\n";
//             score++;
//         } else {
//             std::cout << "Incorrect! Correct option is: "
//             << question[i].correctOption << "\n";
//         }
//     }
//         std::cout << "Quiz completed! Your score: "
//         << score << "/" <<question.size() << "\n";
// };