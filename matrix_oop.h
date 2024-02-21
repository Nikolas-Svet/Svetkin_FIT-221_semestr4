#ifndef UNTITLED3_MATRIX_OOP_H
#define UNTITLED3_MATRIX_OOP_H
#include <iostream>

class Matrix {
private:

    // Attributes
    int rows_, cols_;    // Rows and columns
    double **matrix_;    // Pointer to the memory where the
    // matrix is allocated

public:
    Matrix();            // Default constructor
    Matrix(int rows, int cols);

    Matrix(const Matrix &other);

    Matrix(Matrix &&other);

    ~Matrix();           // Destructor

    int get_rows_();

    int get_cols_();

    void Print() const;

    bool EqMatrix(const Matrix &other) const;

    void SumMatrix(const Matrix &other);

    void SubMatrix(const Matrix &other);

    void MulNumber(const double num);

    void MulMatrix(const Matrix &other);

    Matrix Transpose();

    Matrix CalcComplements() const;

    double Determinant();

    Matrix InverseMatrix();

    Matrix &operator+=(const Matrix &other);

    Matrix &operator-=(const Matrix &other);

    Matrix &operator*=(const Matrix &other);

    double &operator()(int i, int j);

    Matrix &operator=(const Matrix &other);

    bool operator==(const Matrix &other) const;

    Matrix operator*(const Matrix &other) const;

    Matrix operator*(const double num) const;

    Matrix operator+(const Matrix &other) const;

    Matrix operator-(const Matrix &other) const;

    Matrix create_minor(Matrix &result, int current_rows, int current_cols) const;
};


#endif //UNTITLED3_MATRIX_OOP_H
