#include <iostream>
#include "matrix_oop.h"

using namespace std;

int main() {
    // Создание матрицы 3x3 и инициализация ее значений
    Matrix matrix1(3, 3);
    matrix1(0, 0) = 1; matrix1(0, 1) = 3; matrix1(0, 2) = 3;
    matrix1(1, 0) = 4; matrix1(1, 1) = 8; matrix1(1, 2) = 6;
    matrix1(2, 0) = 7; matrix1(2, 1) = 8; matrix1(2, 2) = 9;

    // Создание еще одной матрицы 3x3
    Matrix matrix2(3, 3);
    matrix2(0, 0) = 9; matrix2(0, 1) = 8; matrix2(0, 2) = 7;
    matrix2(1, 0) = 6; matrix2(1, 1) = 5; matrix2(1, 2) = 4;
    matrix2(2, 0) = 3; matrix2(2, 1) = 2; matrix2(2, 2) = 1;

//    cout << "Determinant: " << matrix1.Determinant() << endl;
    cout << "CalcComplements:" << endl;
    matrix1.CalcComplements().Print();
    cout << "InverseMatrix:" << endl;
    matrix1.InverseMatrix().Print();
//    matrix1.CalcComplements();

    // Вывод значений матрицы 1
    cout << "Matrix 1:" << endl;
    matrix1.Print();
    cout << endl;

    // Вывод значений матрицы 2
    cout << "Matrix 2:" << endl;
    matrix2.Print();
    cout << endl;

    // Выполнение операций над матрицами
    cout << "Matrix 1 + Matrix 2:" << endl;
    (matrix1 + matrix2).Print(); // Сложение матриц
    cout << endl;

    cout << "Matrix 1 - Matrix 2:" << endl;
    (matrix1 - matrix2).Print(); // Вычитание матриц
    cout << endl;

    cout << "Matrix 1 * Matrix 2:" << endl;
    (matrix1 * matrix2).Print(); // Умножение матриц
    cout << endl;

    cout << "Matrix 1 * 2.5:" << endl;
    (matrix1 * 2.5).Print(); // Умножение матрицы на число
    cout << endl;

    // Проверка на равенство матриц
    cout << "Matrix 1 is equal to Matrix 2: ";
    cout << boolalpha << (matrix1 == matrix2) << endl;

    // Присвоение матрицы
    Matrix matrix3 = matrix1;
    cout << "Matrix 3 (assigned from Matrix 1):" << endl;
    matrix3.Print();
    cout << endl;

    // Изменение матрицы через операторы +=
    cout << "Matrix 1 += Matrix 2:" << endl;
    matrix1 += matrix2;
    matrix1.Print();
    cout << endl;

    // Изменение матрицы через операторы -=
    cout << "Matrix 1 -= Matrix 2:" << endl;
    matrix1 -= matrix2;
    matrix1.Print();
    cout << endl;

    // Изменение матрицы через операторы *=
    cout << "Matrix 1 *= Matrix 2:" << endl;
    matrix1 *= matrix2;
    matrix1.Print();
    cout << endl;

    // Изменение элемента матрицы через оператор ()
    cout << "Element at (0, 0) of Matrix 1 before change: " << matrix1(0, 0) << endl;
    matrix1(0, 0) = 100;
    cout << "Element at (0, 0) of Matrix 1 after change: " << matrix1(0, 0) << endl;

    return 0;
}
