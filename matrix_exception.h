#ifndef UNTITLED2_MATRIX_EXCEPTION_H
#define UNTITLED2_MATRIX_EXCEPTION_H


#include <stdexcept>
#include <string>

class MatrixException : public std::runtime_error {
public:
    // Конструктор с сообщением об ошибке
    MatrixException(const std::string& message) : std::runtime_error(message) {}
};

#endif //UNTITLED2_MATRIX_EXCEPTION_H
