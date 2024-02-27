#include <iostream>
#include "matrix_oop.h"


using namespace std;

int main() {
    // Создание матрицы 3x3 и инициализация ее значений
    Matrix matrix1(3, 3);
    matrix1(0, 0) = 1;
    matrix1(0, 1) = 3;
    matrix1(0, 2) = 3;
    matrix1(1, 0) = 4;
    matrix1(1, 1) = 8;
    matrix1(1, 2) = 6;
    matrix1(2, 0) = 7;
    matrix1(2, 1) = 8;
    matrix1(2, 2) = 9;

    // Создание еще одной матрицы 3x3
    Matrix matrix2(3, 3);
    matrix2(0, 0) = 9;
    matrix2(0, 1) = 8;
    matrix2(0, 2) = 7;
    matrix2(1, 0) = 6;
    matrix2(1, 1) = 5;
    matrix2(1, 2) = 4;
    matrix2(2, 0) = 3;
    matrix2(2, 1) = 2;
    matrix2(2, 2) = 1;

    // Вывод значений матрицы 1
    cout << "Matrix 1:" << endl;
    matrix1.Print();
    cout << endl;

    // Вывод значений матрицы 2
    cout << "Matrix 2:" << endl;
    matrix2.Print();
    cout << endl;

    cout << "CalcComplements Matrix1:" << endl;
    matrix1.CalcComplements().Print();
    cout << endl;
    cout << "Online calculator solution: \n24\t6\t-24\n-3\t-12\t13\n-6\t6\t-4" << endl << endl;

    cout << "InverseMatrix Matrix1:" << endl;
    matrix1.InverseMatrix().Print();
    cout << endl;
    cout << "Online calculator solution: \n-0.8\t0.1\t0.2\n-0.2\t0.4\t-0.2\n0.8\t-0.43\t0.13" << endl << endl;

    cout << "Determinant Matrix1:" << endl;
    cout << matrix1.Determinant() << endl;
    cout << endl;
    cout << "Online calculator solution: -30" << endl << endl;

    cout << "Transpose Matrix1:" << endl;
    matrix1.Transpose().Print();
    cout << endl;
    cout << "Online calculator solution: \n1\t4\t7\n3\t8\t8\n3\t6\t9" << endl << endl;

    // Выполнение операций над матрицами
    cout << "Matrix 1 + Matrix 2:" << endl;
    (matrix1 + matrix2).Print(); // Сложение матриц
    cout << endl;
    cout << "Online calculator solution: \n10\t11\t10\n10\t13\t10\n10\t10\t10" << endl << endl;

    cout << "Matrix 1 - Matrix 2:" << endl;
    (matrix1 - matrix2).Print(); // Вычитание матриц
    cout << endl;
    cout << "Online calculator solution: \n-8\t-5\t-4\n-2\t3\t2\n4\t6\t8" << endl << endl;

    cout << "Matrix 1 * Matrix 2:" << endl;
    (matrix1 * matrix2).Print(); // Умножение матриц
    cout << endl;
    cout << "Online calculator solution: \n36\t29\t22\n102\t84\t66\n138\t114\t90" << endl << endl;

    cout << "Matrix 1 * 2.5:" << endl;
    (matrix1 * 2.5).Print(); // Умножение матрицы на число
    cout << endl;
    cout << "Online calculator solution: \n2.5\t7.5\t7.5\n10\t20\t15\n18\t20\t22" << endl << endl;

    // Проверка на равенство матриц
    cout << "Matrix 1 is equal to Matrix 2: ";
    cout << boolalpha << (matrix1 == matrix2) << endl;
    cout << "Online calculator solution: false" << endl << endl;

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
    cout << "Online calculator solution: \n10\t11\t10\n10\t13\t10\n10\t10\t10" << endl << endl;

    // Изменение матрицы через операторы -=
    cout << "Matrix 1 -= Matrix 2:" << endl;
    matrix1 -= matrix2;
    matrix1.Print();
    cout << endl;
    cout << "Online calculator solution: \n1\t3\t3\n4\t8\t6\n7\t8\t9" << endl << endl;

    // Изменение матрицы через операторы *=
    cout << "Matrix 1 *= Matrix 2:" << endl;
    matrix1 *= matrix2;
    matrix1.Print();
    cout << endl;
    cout << "Online calculator solution: \n36\t29\t22\n102\t84\t66\n138\t114\t90" << endl << endl;

    // Изменение элемента матрицы через оператор ()
    cout << "Element at (0, 0) of Matrix 1 before change: " << matrix1(0, 0) << endl;
    matrix1(0, 0) = 10;
    cout << "Element at (0, 0) of Matrix 1 after change: " << matrix1(0, 0) << endl;

    return 0;
}
