#include "matrix_oop.h"
#include <iostream>
#include "matrix_exception.h"
#include <iomanip>

using namespace std;

Matrix::Matrix() : rows_(0), cols_(0), matrix_(nullptr) {
}

Matrix::Matrix(int rows, int cols) : rows_(rows), cols_(cols) {
    // Выделение памяти под матрицу
    matrix_ = new double *[rows_];
    for (int i = 0; i < rows_; ++i) {
        matrix_[i] = new double[cols_];
    }
}

Matrix::Matrix(const Matrix &other) : rows_(other.rows_), cols_(other.cols_) {
    // Выделение памяти и копирование элементов из другой матрицы
    matrix_ = new double *[rows_];
    for (int i = 0; i < rows_; ++i) {
        matrix_[i] = new double[cols_];
        for (int j = 0; j < cols_; ++j) {
            matrix_[i][j] = other.matrix_[i][j];
        }
    }
}

Matrix::Matrix(Matrix &&other) : rows_(other.rows_), cols_(other.cols_), matrix_(other.matrix_) {
    // Переносим ресурсы из другой матрицы и обнуляем ее
    other.rows_ = 0;
    other.cols_ = 0;
    other.matrix_ = nullptr;
}

Matrix::~Matrix() {
    if (matrix_ != nullptr) {
        for (int i = 0; i < rows_; ++i) {
            delete[] matrix_[i];
        }
        delete[] matrix_;
    }
}

int Matrix::get_cols_() {
    return cols_;
}

int Matrix::get_rows_() {
    return rows_;
}

void Matrix::Print() const {
    int setprec_num = 2;
    for (int i = 0; i < rows_; ++i) {
        for (int j = 0; j < cols_; ++j) {
            if (matrix_[i][j] > 99) setprec_num = 3;
            cout << setprecision(setprec_num) << matrix_[i][j] << "\t";
            setprec_num = 2;
        }
        cout << endl;
    }
}

// Функция для сравнения матриц
bool Matrix::EqMatrix(const Matrix &other) const {
    // Проверяем, имеют ли матрицы одинаковый размер
    if (rows_ != other.rows_ || cols_ != other.cols_)
        return false;
    // Сравниваем каждый элемент матрицы
    for (int i = 0; i < rows_; ++i) {
        for (int j = 0; j < cols_; ++j) {
            if (matrix_[i][j] != other.matrix_[i][j])
                return false; // Если найден хотя бы один несовпадающий элемент, возвращаем false
        }
    }
    return true; // Если все элементы совпадают, возвращаем true
}

// Функция для сложения матриц
void Matrix::SumMatrix(const Matrix &other) {
    // Проверяем, имеют ли матрицы одинаковый размер
    if (rows_ != other.rows_ || cols_ != other.cols_) {
        throw MatrixException("Matrices have different dimensions."); // Генерируем исключение
    }
    // Складываем соответствующие элементы матриц
    for (int i = 0; i < rows_; ++i) {
        for (int j = 0; j < cols_; ++j) {
            matrix_[i][j] += other.matrix_[i][j];
        }
    }
}

// Функция для вычитания матриц
void Matrix::SubMatrix(const Matrix &other) {
    // Проверяем, имеют ли матрицы одинаковый размер
    if (rows_ != other.rows_ || cols_ != other.cols_) {
        throw MatrixException("Matrices have different dimensions."); // Генерируем исключение
    }
    // Вычитаем соответствующие элементы матриц
    for (int i = 0; i < rows_; ++i) {
        for (int j = 0; j < cols_; ++j) {
            matrix_[i][j] -= other.matrix_[i][j];
        }
    }
}

// Функция для умножения матрицы на число
void Matrix::MulNumber(const double num) {
    // Умножаем каждый элемент матрицы на число
    for (int i = 0; i < rows_; ++i) {
        for (int j = 0; j < cols_; ++j) {
            matrix_[i][j] *= num;
        }
    }
}

// Функция для умножения матриц
void Matrix::MulMatrix(const Matrix &other) {
    // Проверяем, можно ли умножить матрицы
    if (cols_ != other.rows_) {
        throw MatrixException(
                "Number of columns of first matrix must be equal to number of rows of second matrix."); // Генерируем исключение
    }
    // Создаем новую матрицу для хранения результата умножения
    Matrix result(rows_, other.cols_);
    // Выполняем умножение матриц
    for (int i = 0; i < rows_; ++i) {
        for (int j = 0; j < other.cols_; ++j) {
            for (int k = 0; k < cols_; ++k) {
                result.matrix_[i][j] += matrix_[i][k] * other.matrix_[k][j];
            }
        }
    }
    *this = result;
}

// Функция для транспонирования матрицы
Matrix Matrix::Transpose() {
    Matrix transposed(rows_, cols_);
    for (int i = 0; i < rows_; ++i) {
        for (int j = 0; j < cols_; ++j) {
            transposed.matrix_[j][i] = matrix_[i][j];
        }
    }
    return transposed;
}

Matrix Matrix::CalcComplements() const {
    if (rows_ != cols_) {
        throw MatrixException("Matrix is not square."); // Генерируем исключение
    }
    Matrix result(rows_ - 1, cols_ - 1);
    // Создаем новую матрицу для хранения результата умножения
    Matrix calc(rows_, cols_);
    int current_rows_result, current_cols_result;
    for (int current_rows = 0; current_rows < rows_; ++current_rows)
        for (int current_cols = 0; current_cols < cols_; ++current_cols) {
            current_rows_result = 0;
            current_cols_result = 0;
            for (int i = 0; i < rows_; ++i)
                for (int j = 0; j < cols_; ++j) {
                    if (j == current_cols || i == current_rows) {
                        continue;
                    }
                    else {
                        result.matrix_[current_rows_result][current_cols_result] = matrix_[i][j];
                        if (current_cols_result == result.get_cols_() - 1) {
                            current_rows_result ++;
                            current_cols_result = 0;
                        }
                        else {
                            current_cols_result ++;
                        }
                    }
                }
            calc.matrix_[current_rows][current_cols] = result.Determinant();
        }
    for (int i = 0; i < rows_; i++)
        for (int j = 0; j < cols_; j++) {
            if (j % 2 == 1 && i % 2 == 0) {
                calc.matrix_[i][j] *= -1;
            }
            else if (j % 2 == 0 && i % 2 == 1) {
                calc.matrix_[i][j] *= -1;
            }
        }
    return calc;
}

double Matrix::Determinant() {
    if (rows_ != cols_) {
        throw MatrixException("Matrix is not square.");
    }
    // Создаем копию матрицы в виде вектора для удобства обработки
    std::vector<std::vector<int>> matrixData(rows_, std::vector<int>(cols_));
    for (int i = 0; i < rows_; ++i) {
        for (int j = 0; j < cols_; ++j) {
            matrixData[i][j] = matrix_[i][j];
        }
    }

    // Получаем размерность матрицы (количество строк или столбцов)
    int n = matrixData.size();

    // Инициализируем вектор перестановок
    std::vector<int> permutation(n);
    for (int i = 0; i < n; ++i) {
        permutation[i] = i;
    }

    // Инициализируем переменную для хранения определителя
    double det = 0;

    // Перебираем все перестановки индексов строк
    do {
        // Вычисляем значение определителя для текущей перестановки
        int term = 1;
        for (int i = 0; i < n; ++i) {
            term *= matrixData[i][permutation[i]];
        }
        int sign = 1;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (permutation[i] > permutation[j]) {
                    sign *= -1;
                }
            }
        }
        // Добавляем значение к общему результату
        det += sign * term;
    } while (std::next_permutation(permutation.begin(), permutation.end()));

    // Возвращаем вычисленное значение определителя
    return det;
}

Matrix Matrix::InverseMatrix() {
    if (rows_ != cols_) {
        throw MatrixException("Matrix is not square."); // Генерируем исключение
    }
    double det = Determinant();
    if (det == 0) {
        throw MatrixException("Determinant of the matrix is zero."); // Генерируем исключение
    }
    return CalcComplements().Transpose() * (1.0 / Determinant());
}

//                      Операторы
// Оператор сложения матриц
Matrix Matrix::operator+(const Matrix &other) const {
    Matrix result(*this); // Создаем копию текущей матрицы
    result.SumMatrix(other);
    return result;
}

// Оператор вычитания матриц
Matrix Matrix::operator-(const Matrix &other) const {
    Matrix result(*this); // Создаем копию текущей матрицы
    result.SubMatrix(other);
    return result;
}

// Оператор умножения матрицы на число
Matrix Matrix::operator*(const double num) const {
    Matrix result(*this); // Создаем копию текущей матрицы
    result.MulNumber(num);
    return result;
}

Matrix Matrix::operator*(const Matrix &other) const {
    if (cols_ != other.rows_) {
        throw MatrixException(
                "Number of columns of first matrix must be equal to number of rows of second matrix."); // Генерируем исключение
    }
    Matrix result = *this;
    result.MulMatrix(other);
    return result;
}

// Оператор проверки на равенство матриц
bool Matrix::operator==(const Matrix &other) const {
    return EqMatrix(other);
}

// Оператор присваивания
Matrix &Matrix::operator=(const Matrix &other) {
    // Проверяем на самоприсваивание
    if (this == &other)
        return *this;
    // Освобождаем память текущей матрицы
    if (matrix_ != nullptr) {
        for (int i = 0; i < rows_; ++i) {
            delete[] matrix_[i];
        }
        delete[] matrix_;
    }
    // Выделяем память для новой матрицы
    rows_ = other.rows_;
    cols_ = other.cols_;
    matrix_ = new double *[rows_];
    for (int i = 0; i < rows_; ++i) {
        matrix_[i] = new double[cols_];
        for (int j = 0; j < cols_; ++j) {
            matrix_[i][j] = other.matrix_[i][j];
        }
    }
    return *this;
}

// Оператор +=
Matrix &Matrix::operator+=(const Matrix &other) {
    SumMatrix(other);
    return *this;
}

// Оператор -=
Matrix &Matrix::operator-=(const Matrix &other) {
    SubMatrix(other);
    return *this;
}

// Оператор *=
Matrix &Matrix::operator*=(const Matrix &other) {
    MulMatrix(other);
    return *this;
}

// Оператор для доступа к элементам матрицы по индексам
double &Matrix::operator()(int i, int j) {
    // Проверяем, находятся ли индексы в пределах матрицы
    if (i < 0 || i >= rows_ || j < 0 || j >= cols_) {
        throw MatrixException("Index out of range.");
    }
    return matrix_[i][j];
}
