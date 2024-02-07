#include "matrix_oop.h"
#include <iostream>

using namespace std;

bool Matrix::EqMatrix(const Matrix &other) {
    return false;
}

void Matrix::SumMatrix(const Matrix &other) {

}

void Matrix::SubMatrix(const Matrix &other) {

}

void Matrix::MulNumber(const double num) {

}

void Matrix::MulMatrix(const Matrix &other) {

}

Matrix Matrix::Transpose() {
    return Matrix(rows_, cols_);
}

Matrix Matrix::CalcComplements() {
    return Matrix(rows_, cols_);
}

double Matrix::Determinant() {
    return 0;
}

Matrix Matrix::InverseMatrix() {
    return Matrix(rows_, cols_);
}

Matrix::Matrix() {
    cout << "Constructor Matrix() was called successful!" << endl;
}

Matrix::Matrix(int rows, int cols) {
    rows_ = rows;
    cols_ = cols;
    cout << "Constructor Matrix(int rows, int cols) was called successful!" << endl;
}

Matrix::Matrix(const Matrix &other) {
    cout << "Constructor (const Matrix &other) was called successful!" << endl;
}

Matrix::Matrix(Matrix &&other) {
    cout << "Constructor (Matrix &other) was called successful!" << endl;
}

Matrix::~Matrix() {
    cout << "Calling destructor" << endl;
}
