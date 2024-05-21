// // Объявление переменных с различными типами данных
// let var1 = 10;                 // Целое число
// let var2 = "Hello, world!";    // Строка
// let var3 = true;               // Булевое значение
// let var4 = {                   // Объект
//     name: "John", age: 30
// };
// let var5 = [1, 2, 3, 4, 5];    // Массив
//
// // Вывод типов переменных на экран с помощью функции typeof()
// console.log("Тип переменной var1:", typeof (var1));
// console.log("Тип переменной var2:", typeof (var2));
// console.log("Тип переменной var3:", typeof (var3));
// console.log("Тип переменной var4:", typeof (var4));
// console.log("Тип переменной var5:", typeof (var5));
//
// // Задача 2
// let firstVariable = 5;
// let secondVariable = 10;
//
// console.log("Первая переменная равна второй:", firstVariable === secondVariable);
// console.log("Первая переменная меньше второй:", firstVariable < secondVariable);
// console.log("Первая переменная меньше или равна второй:", firstVariable <= secondVariable);
// console.log("Первая переменная больше второй:", firstVariable > secondVariable);
//
// // Задача 3
// let a = false;
// let b = null;
// let c;
//
// console.log("Значение переменной a:", a);
// console.log("Значение переменной b:", b);
// console.log("Значение переменной c:", c);
//
//
// // Задача 4
// console.log("Результат выражения '1' + 2 + 3:", "1" + 2 + 3); // "123"
// console.log("Результат выражения 1 + 2 + '3':", 1 + 2 + "3"); // "33"
// console.log("Результат выражения '1' - 2:", "1" - 2); // -1
// console.log("Результат выражения '1' + -2:", "1" + -2); // "1-2"
// console.log("Результат выражения '1' + '1' - '1':", "1" + "1" - "1"); // 10
// console.log("Результат выражения 'foo' + - 'bar':", "foo" + -"bar"); // NaN
// console.log("Результат выражения 0 == '0':", 0 === "0"); // true
// console.log("Результат выражения 0.5 + 0.1 == 0.6:", 0.5 + 0.1 === 0.6); // false
// console.log("Результат выражения 0.1 + 0.2 == 0.3:", 0.1 + 0.2 === 0.3); // false
// console.log("Результат выражения true + true + true == 3:", true + true + true === 3); // true
// console.log("Результат выражения true == 1:", true === 1); // true
// console.log("Результат выражения true === 1:", true === 1); // false
// console.log("Результат выражения 1 < 2 < 3:", 1 < 2 < 3); // true
// console.log("Результат выражения 3 > 2 > 1:", 3 > 2 > 1); // false
// console.log("Результат выражения 9007199254740991 + 1 == 9007199254740991 + 2:", 9007199254740991 + 1 === 9007199254740991 + 2); // true
// console.log("Результат выражения Math.sqrt(-1) == Math.sqrt(-1):", Math.sqrt(-1) === Math.sqrt(-1)); // false
//
//
// // Задача 5
// let str1 = 'Кто ';
// let str2 = 'ты ';
// let str3 = 'такой?';
// let concatenation = str1 + str2 + str3;
// console.log(concatenation);
//
// // Задача 6
// let str = "20";
// let a1 = 5;
// console.log(str + a1); // "205" (конкатенация строк)
// console.log(str - a1); // 15 (строка "20" преобразуется в число)
// console.log(str * "2"); // 40 (строка "20" преобразуется в число)
// console.log(str / 2); // 10 (строка "20" преобразуется в число)
//
// // Задача 7
// let aStr = "12";
// let bStr = "7.15";
// let aNum = parseInt(aStr); // Преобразуем строку в число
// let bNum = parseFloat(bStr); // Преобразуем строку в число с плавающей точкой
// let remainder = aNum % bNum; // Находим остаток от деления числа a на b
// console.log("Остаток от деления a на b:", remainder); // 5
//
// // Задача 8
//
// let x = 5.555;
//
// console.log( (x * x - 7 * x + 10) / (x * x - 8 * x + 12) );
//
// // Задача 9
//
// // Пример адреса электронной почты
// let email = "example.com";
//
// // Проверяем наличие символа "@" в адресе электронной почты
// if (!email.includes("@")) {
//     console.log("Предупреждение: Введенный адрес электронной почты не содержит символа '@'.");
// } else {
//     console.log("Адрес электронной почты содержит символ '@'.");
// }
//
//
//
//
//
//
