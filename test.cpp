#include <iostream>
#include "matrix_oop.h"

using namespace std;

int main() {
    Matrix matrix1(3, 3);
    matrix1(1, 1) = 1;
    matrix1(1, 2) = 3;
    matrix1(1, 3) = 3;
    matrix1(2, 1) = 4;
    matrix1(2, 2) = 8;
    matrix1(2, 3) = 6;
    matrix1(3, 1) = 7;
    matrix1(3, 2) = 8;
    matrix1(3, 3) = 9;

    // Создание еще одной матрицы 3x3
    Matrix matrix2(3, 3);
    matrix2(1, 1) = 9;
    matrix2(1, 2) = 8;
    matrix2(1, 3) = 7;
    matrix2(2, 1) = 6;
    matrix2(2, 2) = 5;
    matrix2(2, 3) = 4;
    matrix2(3, 1) = 3;
    matrix2(3, 2) = 2;
    matrix2(3, 3) = 1;

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
    cout << "Online calculator solution: \t\n24\t\t6\t\t-24\t\n-3\t\t-12\t\t13\t\n-6\t\t6\t\t-4" << endl << endl;

    cout << "InverseMatrix Matrix1:" << endl;
    matrix1.InverseMatrix().Print();
    cout << endl;
    cout << "Online calculator solution: \t\n-0.8\t\t0.1\t\t0.2\t\n-0.2\t\t0.4\t\t-0.2\t\n0.8\t\t-0.43\t\t0.13" << endl << endl;

    cout << "Determinant Matrix1:" << endl;
    cout << matrix1.Determinant() << endl;
    cout << endl;
    cout << "Online calculator solution: -30" << endl << endl;

    cout << "Transpose Matrix1:" << endl;
    matrix1.Transpose().Print();
    cout << endl;
    cout << "Online calculator solution: \t\n1\t\t4\t\t7\t\n3\t\t8\t\t8\t\n3\t\t6\t\t9" << endl << endl;

    // Выполнение операций над матрицами
    cout << "Matrix 1 + Matrix 2:" << endl;
    (matrix1 + matrix2).Print(); // Сложение матриц
    cout << endl;
    cout << "Online calculator solution: \n10\t\t11\t\t10\n10\t\t13\t\t10\n10\t\t10\t\t10" << endl << endl;

    cout << "Matrix 1 - Matrix 2:" << endl;
    (matrix1 - matrix2).Print(); // Вычитание матриц
    cout << endl;
    cout << "Online calculator solution: \n-8\t\t-5\t\t-4\n-2\t\t3\t\t2\n4\t\t6\t\t8" << endl << endl;

    cout << "Matrix 1 * Matrix 2:" << endl;
    (matrix1 * matrix2).Print(); // Умножение матриц
    cout << endl;
    cout << "Online calculator solution: \n36\t\t29\t\t22\n102\t\t84\t\t66\n138\t\t114\t\t90" << endl << endl;

    cout << "Matrix 1 * 2.5:" << endl;
    (matrix1 * 2.5).Print(); // Умножение матрицы на число
    cout << endl;
    cout << "Online calculator solution: \n2.5\t\t7.5\t\t7.5\n10\t\t20\t\t15\n18\t\t20\t\t22" << endl << endl;

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
    cout << "Online calculator solution: \n10\t\t11\t\t10\n10\t\t13\t\t10\n10\t\t10\t\t10" << endl << endl;

    // Изменение матрицы через операторы -=
    cout << "Matrix 1 -= Matrix 2:" << endl;
    matrix1 -= matrix2;
    matrix1.Print();
    cout << endl;
    cout << "Online calculator solution: \n1\t\t3\t\t3\n4\t\t8\t\t6\n7\t\t8\t\t9" << endl << endl;

    // Изменение матрицы через операторы *=
    cout << "Matrix 1 *= Matrix 2:" << endl;
    matrix1 *= matrix2;
    matrix1.Print();
    cout << endl;
    cout << "Online calculator solution: \n36\t\t29\t\t22\n102\t\t84\t\t66\n138\t\t114\t\t90" << endl << endl;



    // Изменение элемента матрицы через оператор ()
    cout << "Element at (1, 1) of Matrix 1 before change: " << matrix1(1, 1) << endl;
    matrix1(1, 1) = 10;
    cout << "Element at (1, 1) of Matrix 1 after change: " << matrix1(1, 1) << endl;

    //Создаем матрицу так, чтобы определитель был равен нулю
    matrix1(1, 1) = 1;
    matrix1(1, 2) = 2;
    matrix1(1, 3) = 3;
    matrix1(2, 1) = 4;
    matrix1(2, 2) = 5;
    matrix1(2, 3) = 6;
    matrix1(3, 1) = 7;
    matrix1(3, 2) = 8;
    matrix1(3, 3) = 9;

    matrix1.InverseMatrix();

    Matrix matrix4(4, 5);
    matrix4(1, 1) = 4;
    matrix4(1, 2) = 2;
    matrix4(1, 3) = 3;
    matrix4(1, 4) = 3;
    matrix4(1, 5) = 2;
    matrix4(2, 1) = 4;
    matrix4(2, 2) = 7;
    matrix4(2, 3) = 6;
    matrix4(2, 4) = 6;
    matrix4(2, 5) = 4;
    matrix4(3, 1) = 7;
    matrix4(3, 2) = 8;
    matrix4(3, 3) = 9;
    matrix4(3, 4) = 3;
    matrix4(3, 5) = 9;
    matrix4(4, 1) = 4;
    matrix4(4, 2) = 1;
    matrix4(4, 3) = 1;
    matrix4(4, 4) = 5;
    matrix4(4, 5) = 3;



//  Складываю матрицу 3 на 3 и 4 на 5
    matrix1 += matrix4;
    matrix1 + matrix4;
//  Умножаю матрицу 3 на 3 и 4 на 5
    matrix1 *= matrix4;
//  Вычитаю матрицу 3 на 3 и 4 на 5
    matrix4 -= matrix1;
    matrix4 - matrix1;
//  Матрица Алегбраических дополнений 4 на 5
    matrix4.CalcComplements();
//  Определитель матрицы 4 на 5
    matrix4.Determinant();
//  Обратная матрица 4 на 5
    matrix4.Determinant();

//  Обратная матрица, когда определитель равен нулю
    matrix1(1, 1) = 1;
    matrix1(1, 2) = 2;
    matrix1(1, 3) = 3;
    matrix1(2, 1) = 4;
    matrix1(2, 2) = 5;
    matrix1(2, 3) = 6;
    matrix1(3, 1) = 7;
    matrix1(3, 2) = 8;
    matrix1(3, 3) = 9;

    matrix1.InverseMatrix();

//  Умножение матриц разного размера
    matrix1 *= matrix4;

//  Присвоение значения в матрицу, где строка или стобец выходят за границы
    matrix1(10, 10) = 10;

    return 0;


}