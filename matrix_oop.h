#ifndef UNTITLED3_MATRIX_OOP_H
#define UNTITLED3_MATRIX_OOP_H


class Matrix {
    private:
        // Attributes
        int rows_, cols_;    // Rows and columns
        double **matrix_;    // Pointer to the memory where the
        // matrix is allocated

    public:
        Matrix();            // Default constructor
        Matrix(int rows, int cols);
        Matrix(const Matrix& other);
        Matrix(Matrix&& other);
        ~Matrix();           // Destructor

    bool EqMatrix(const Matrix& other);

    void SumMatrix(const Matrix& other);

    void SubMatrix(const Matrix& other);

    void MulNumber(const double num);

    void MulMatrix(const Matrix& other);

    Matrix Transpose();

    Matrix CalcComplements();

    double Determinant();

    Matrix InverseMatrix();
};


#endif //UNTITLED3_MATRIX_OOP_H
