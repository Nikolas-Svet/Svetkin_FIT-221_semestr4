// console.log("\nПервое")
//
// function sub(a, b) {
//     console.log(a - b)
// }
//
// sub(5, 3)
//
// function sub2(a, b) {
//     return a - b
// }
//
// console.log(sub2(5, 2))
//
// console.log("\nВторое")
//
// function old_year(n) {
//     if (n < 18) {
//         console.log("Привет, малыш!")
//     } else {
//         console.log("Здравствуйте, юноша!")
//     }
// }
//
// old_year(18)
// old_year(17)
//
// console.log("\nТретье")
//
// function maxOfThreeNumbers(num1, num2, num3) {
//     if (num1 >= num2 && num1 >= num3) {
//         return num1;
//     } else if (num2 >= num1 && num2 >= num3) {
//         return num2;
//     } else {
//         return num3;
//     }
// }
//
// let result = maxOfThreeNumbers(10, 5, 8);
// console.log("Наибольшее из трех чисел:", result);
//
// console.log("\nЧетвертое")
//
// // f() выведет "Локальная переменная", потому что, если глобальные и
// // локальные переменные совпадают по названию, то приоритет у локальной
// // переменной выше и она будет использоваться в функции
// // console.log(variable) соответственно выведет "Глобальная переменная", потому что никак не задействуется с функцией
// let variable = "Глобальная переменная";
//
// function f() {
//     let variable = "Локальная переменная";
//     console.log(variable);
// }
//
// f();
// console.log(variable);
//
// console.log("\nПятое")
//
// function get_u(x, y, z) {
//     return (maxOfThreeNumbers(x, y, null) + maxOfThreeNumbers(x + y, z, null))
//         / (maxOfThreeNumbers(0.5, x + z, null)) ** 2;
// }
//
// console.log(get_u(1, 2, 3))
//
// console.log("\nШестое")
//
// function calculatePolygonPerimeter(...coordinates) {
//     // Проверяем, что передано четное количество координат (по две координаты на каждую вершину)
//     if (coordinates.length % 2 !== 0) {
//         return "Ошибка: Количество координат должно быть четным";
//     }
//
//     let perimeter = 0;
//
//     // Проходим по координатам вершин и вычисляем расстояние между каждой парой соседних вершин
//     for (let i = 0; i < coordinates.length - 2; i += 2) {
//         let x1 = coordinates[i];
//         let y1 = coordinates[i + 1];
//         let x2 = coordinates[i + 2];
//         let y2 = coordinates[i + 3];
//
//         // Вычисляем длину отрезка между вершинами по формуле расстояния между точками в декартовой системе координат
//         let distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
//
//         // Добавляем расстояние к периметру
//         perimeter += distance;
//     }
//
//     // Добавляем расстояние от последней вершины к первой, чтобы закрыть контур
//     let x1 = coordinates[coordinates.length - 2];
//     let y1 = coordinates[coordinates.length - 1];
//     let x2 = coordinates[0];
//     let y2 = coordinates[1];
//     let distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
//     perimeter += distance;
//
//     return perimeter;
// }
//
// // Пример использования функции
// let perimeter = calculatePolygonPerimeter(0, 0, 3, 0, 3, 4, 0, 4);
// console.log("Периметр пятиугольника:", perimeter); // Ожидаемый результат: 14
//
// console.log("\nСедьмое")
//
// function sequenceMember(n, sum = 0) {
//     // Базовый случай: если n равно 1, возвращаем 1
//     if (n === 1) {
//         return 1;
//     }
//
//     // Вычисляем сумму всех предыдущих членов
//     for (let i = 1; i < n; i++) {
//         sum += sequenceMember(i);
//     }
//
//     // Возвращаем синус суммы всех предыдущих членов
//     return Math.sin(sum);
// }
//
// // Пример использования функции для вычисления 5-го члена последовательности
// console.log("5-й член последовательности:", sequenceMember(5));
//
// //Массивы
//
// console.log("\nПервое")
//
// let arr = ["Orange", "Apple", "Banana"]
// console.log(arr[2], "\nLength: ", arr.length)
// arr.splice(1, 1)
// for (let fruit in arr) {
//     console.log(arr[fruit])
// }
//
// console.log("\nВторое")
//
// // Массив стран
// let countries = ["USA", "China", "India", "Russia", "Brazil"];
//
// // Массив населения
// let population = [331, 1441, 1380, 146, 213];
//
// // Функция для вывода названия страны и ее населения с помощью цикла for
// function printPopulationForLoop() {
//     for (let i = 0; i < countries.length; i++) {
//         console.log("Страна:", countries[i], "Население:", population[i]);
//     }
// }
//
// // Функция для вывода названия страны и ее населения с помощью цикла for-in
// function printPopulationForInLoop() {
//     for (let country in countries) {
//         console.log("Страна:", countries[country], "Население:", population[country]);
//     }
// }
//
// // Вывод с помощью цикла for
// console.log("Вывод с помощью цикла for:");
// printPopulationForLoop();
//
// // Перенос строки для чистоты вывода
// console.log();
//
// // Вывод с помощью цикла for-in
// console.log("Вывод с помощью цикла for-in:");
// printPopulationForInLoop();
//
//
// console.log("\nТретье")
//
// let arr1 = ["January", "February", "March", "April", "May", "June"];
// let len = arr1.pop()
// console.log(arr1.join(" "));
// console.log(len);
//
// console.log("\nЧетвертое")
//
// let a = [1, 2, 3, 4, 5, 6, 7];
// let t = a.slice(0, 3)
// console.log(t);
//
// console.log("\nПятое")
//
// let a1 = [1, 2, 3, 4, 5, 6, 7];
// let d = a1.splice(1, 3)
// console.log(a1);
//
// console.log("\nШестое")
// let a2 = [1, 2, 3, 4, 5]
// console.log(a2.reverse())
//
// console.log("\nСедьмое")
// let a3 = ["c", 5, 2, "b", 3, 1, 4, "a"]
// console.log(a3.sort())
//
// console.log("\nВосьмое")
// let a4 = [1, 2, 3, 4, 5]
// console.log(a4.join("+"))
//
// console.log("\nДевятое")
//
// function mediana(a) {
//
// }
//
// let a5 = [1, 2, 5, 4, 6]
// let a6 = [8, 2, 5, 9, 5]
// console.log(a5.sort()[(a5.length / 2) - 0.5])
// console.log(a6.sort()[(a6.length / 2) - 0.5])
//
// console.log("\nДесятое")
//
// let a7 = [2, 52, 31, 2, 13, 3, 1]
// let max = 0, min = 10 ** 10
// for (let i = 0; i < a7.length; i++) {
//     if (max < a7[i]) {
//         max = a7[i]
//     }
//     if (min > a7[i]) {
//         min = a7[i]
//     }
// }
// let index_min = a7.indexOf(min), index_max = a7.indexOf(max)
// a7[index_min] = max
// a7[index_max] = min
// console.log(a7)
//
// console.log("\nОдиннадцатое")
//
// let a8 = [5, 4, 3, 2, 2], flag = true
//
// for (let i = 0; i < a8.length - 1; i++) {
//     if (a8[i] < a8[i + 1]) {
//         flag = false
//         console.log(a8[i + 1])
//         break
//     }
// }
//
// if (flag) {
//     console.log(a8.reverse())
// }
//
// console.log("\nДвенадцатое")
//
// let a9 = [-11, 4, -64, -23, 15, -93, 32, 27];
//
// for (let i = 0; i < a9.length; i++) {
//     if (i % 2 !== 0 && a9[i] > 0) {
//         a9[i] = a9[i] * 3;
//     }
//     if (i % 2 === 0 && a9[i] < 0) {
//         a9[i] = a9[i] / 5;
//     }
// }
//
// console.log(a9);
//
// console.log("\nТринадцатое")
//
// let matrix = [
//     [1, 10, -3, 4, 5],
//     [6, -7, 8, 9, 10],
//     [11, -2, 13, 14, 15],
//     [16, 17, 18, -4, 19],
//     [-5, 20, 21, 22, 7]
// ];
//
// function printElementsInRange(matrix) {
//     for (let i = 0; i < matrix.length; i++) {
//         for (let j = 0; j < matrix[i].length; j++) {
//             if (matrix[i][j] >= -5 && matrix[i][j] <= 7) {
//                 console.log("Элемент [" + i + "][" + j + "]: " + matrix[i][j]);
//             }
//         }
//     }
// }
//
// printElementsInRange(matrix);
//
// console.log("\nЧетырнадцатое")
//
// function sumOfMaxRowValues(matrix1) {
//     let sum = 0;
//     for (let i = 0; i < matrix1.length; i++) {
//         let maxInRow = Math.max(...matrix1[i]);
//         sum += maxInRow;
//     }
//     return sum;
// }
//
// function productOfMinColumnValues(matrix1) {
//     let product = 1;
//     for (let j = 0; j < matrix1[0].length; j++) {
//         let minInColumn = matrix1[0][j];
//         for (let i = 1; i < matrix1.length; i++) {
//             if (matrix1[i][j] < minInColumn) {
//                 minInColumn = matrix1[i][j];
//             }
//         }
//         product *= minInColumn;
//     }
//     return product;
// }
//
// let matrix1 = [
//     [1, 5, 3],
//     [7, 2, 4],
//     [6, 9, 8]
// ];
//
// let sum = sumOfMaxRowValues(matrix1);
// let product = productOfMinColumnValues(matrix1);
//
// console.log("Сумма наибольших значений в строках:", sum);
// console.log("Произведение наименьших значений в столбцах:", product);
//
// console.log("\nПятнадцатое")
//
// let booksByAuthors = {
//     "Пушкин": ["Евгений Онегин", "Руслан и Людмила"],
//     "Есенин": ["Зимняя дорога", "Анна Снегина"],
//     "Данцова": ["Детективы неженского пола", "Верные друзья"]
// };
//
// for (let author in booksByAuthors) {
//     console.log("Автор:", author);
//     console.log("Книги:", booksByAuthors[author].join(", "));
// }
//
