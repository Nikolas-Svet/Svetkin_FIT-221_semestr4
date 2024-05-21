// console.log("\nПервое")
//
// let user = {};
// user.name = "John";
// console.log(user);
// user.surname = "Smith";
// console.log(user);
// user.name = "Pete";
// console.log(user);
// delete user.name
// console.log(user);
//
// console.log("\nВторое")
//
// let myBrowser = {
//     name: "Microsoft Internet Explorer",
//     version: "9.0"
// };
//
// for (let i in myBrowser) {
//     console.log(myBrowser[i]);
// }
//
//
// console.log("\nТретье")
//
// function isEmpty(obj) {
//     for (let key in obj) {
//         return false;
//     }
//     return true;
// }
//
// const emptyObj = {};
// const nonEmptyObj = {a: 1, b: 2};
//
// console.log(isEmpty(emptyObj));
// console.log(isEmpty(nonEmptyObj));
//
// console.log("\nЧетвертое");
//
// //
// // const user = {
// //     name: "John"
// // };
//
// //Первый код user.name = "Pete"; будет работать, потому
// // что мы изменяем свойство name объекта, на который
// // ссылается user, но не меняем саму ссылку user.
//
// // user.name = "Pete";
// // user = 123;
//
// //Попытка изменить саму ссылку user, как во
// // втором случае user = 123; , вызовет ошибку, потому что
// // const запрещает присваивание нового значения переменной.
//
// console.log("\nПятое");
//
// function multiplyNumeric(obj) {
//     for (i in obj) {
//         obj[i] *= 2;
//     }
// }
//
// let obj = {
//     name: "Test",
//     age: 18
// }
//
// multiplyNumeric(obj);
//
// console.log(obj);
//
// console.log("\nШестое");
//
// let calc = {
//     n1: null,
//     n2: null,
//     read(a, b) {
//         this.n1 = a;
//         this.n2 = b;
//     },
//     sum() {
//         console.log(this.n1 + this.n2);
//     },
//     mul() {
//         console.log(this.n1 * this.n2);
//     }
// }
//
// calc.read(1, 3);
// calc.sum();
// calc.read(5, 5);
// calc.mul();
//
// console.log("\nСедьмое");
//
// let ladder = {
//     step: 0,
//     up() {
//         this.step++;
//         return this;
//     },
//     down() {
//         this.step--;
//         return this;
//     },
//     showStep() {
//         console.log(this.step);
//         return this;
//     }
// };
//
// ladder.up().up().down().showStep().down().showStep(); // выводит 1 затем 0
//
// console.log("\nВосьмое");
//
// class Browser {
//     constructor(name, version) {
//         let myBrowser = {
//             name: name,
//             version: version
//         }
//     }
//
//     aboutBrowser() {
//         console.log(myBrowser.name, myBrowser.version);
//     }
// }
//
// let b = new Browser("Chrome", "3.5");
// b.aboutBrowser();
//
// console.log("\nДевятое");
//
// function Employee(name, department, phone, salary) {
//     this.name = name;
//     this.department = department;
//     this.phone = phone;
//     this.salary = salary;
//
//     this.displayInfo = function () {
//         console.log("Name:", this.name);
//         console.log("Department:", this.department);
//         console.log("Phone:", this.phone);
//         console.log("Salary:", this.salary);
//     };
// }
//
// const employee1 = new Employee("John Doe", "IT", "123-456-7890", 50000);
//
// employee1.displayInfo();
//
// console.log("\nДесятое");
//
// function Calculator() {
//     this.n1 = 0;
//     this.n2 = 0;
//
//     this.read = function (a, b) {
//         this.n1 = a;
//         this.n2 = b;
//     }
//
//     this.sum = function () {
//         console.log(this.n1 + this.n2);
//     }
//
//     this.mul = function () {
//         console.log(this.n1 * this.n2);
//     }
// }
//
// const calculator = new Calculator();
// calculator.read(2, 3);
// calculator.sum();
// calculator.mul();
//
// console.log("\nОдиннадцатое");
//
// function Accumulator(StartingValue) {
//     this.value = StartingValue;
//     this.read = function (a) {
//         this.value += a;
//     }
// }
//
// let accumulator = new Accumulator(1); // начальное значение 1
// accumulator.read(10); // прибавляет 10 к текущему значению
// accumulator.read(5); // прибавляет 5 к текущему значению
// console.log(accumulator.value); // выведет 16
//
// console.log("\nРабота с прототипами \nПервое");
//
// let animal = {
//     jumps: null
// };
// let rabbit = {
//     __proto__: animal,
//     jumps: true
// };
// console.log(rabbit.jumps);
// delete rabbit.jumps;
// console.log(rabbit.jumps);
// delete animal.jumps;
// console.log(rabbit.jumps);
//
// // Первый console.log(rabbit.jumps);
// // Здесь мы спрашиваем значение свойства jumps у объекта
// // rabbit.Так как это свойство явно определено в rabbit как
// // true, оно и будет выведено.
// // Эта команда удаляет свойство jumps из объекта rabbit. После
// // этого, когда мы пытаемся получить rabbit.jumps, JavaScript
// // будет искать это свойство сначала в самом объекте rabbit, не
// // найдет его там (так как мы его удалили), и затем перейдет к
// // его прототипу, то есть объекту animal, где найдет jumps со
// // значением null.
// // delete animal.jumps;
// // Эта команда удаляет свойство jumps из объекта animal,
// // который является прототипом для rabbit. Теперь, когда
// // мы пытаемся получить rabbit.jumps, JavaScript снова будет
// // искать это свойство сначала в rabbit, не найдет его там,
// // затем перейдет к прототипу animal, и тоже не найдет его там,
// // потому что мы его удалили.
//
// console.log("\nВторое");
//
// // Когда метод eat() вызывается на объекте rabbit,
// // ключевое слово this внутри метода eat() будет
// // ссылаться на объект, для которого был вызван метод,
// // то есть на rabbit. Это означает, что свойство full
// // будет установлено именно для объекта rabbit, а не
// // для его прототипа animal.
//
// // let animal = {
// //     eat() {
// //         this.full = true;
// //     }
// // };
// //
// // let rabbit = {
// //     __proto__: animal
// // };
// //
// // rabbit.eat();
// //
// // console.log(rabbit.full); // true
// // console.log(animal.full); // undefined
//
// console.log("\nТретье");
//
// // Проблема здесь заключается в том, что свойство stomach
// // является общим для обоих хомяков, так как оно определено
// // в прототипе hamster, который и используют оба объекта
// // speedy и lazy в качестве своего прототипа. Когда один
// // хомяк ест (т.е., когда в stomach добавляется еда), изменения
// // видны для обоих хомяков, так как они оба ссылаются на один и
// // тот же массив stomach в прототипе.
//
// let hamster = {
//     eat(food) {
//         if (!this.stomach) {
//             this.stomach = [];
//         }
//         this.stomach.push(food);
//     }
// };
//
// let speedy = {
//     __proto__: hamster
// };
//
// let lazy = {
//     __proto__: hamster
// };
//
// speedy.eat("apple");
// console.log(speedy.stomach); // apple
// console.log(lazy.stomach); // должен быть пустым
//
// console.log("\nЧетвертое");
//
// // Добавление свойства по умолчанию к встроенному объекту
// String.prototype.color = "black";
// // Добавление (изменение) метода к встроенному объекту
// String.prototype.write = stringWrite;
//
// function stringWrite() {
//     console.log("Цвет текста: " + this.color);
//     console.log("Текст: " + this.toString())
// }
//
// // используем измененный класс
// let s = new String("Это строка");
// s.color = "red";
// s.write();
// let s2 = new String("Вторая строка");
// s2.write();
//
// // String.prototype.color = "black"; - Добавляет новое
// // свойство color к прототипу String, устанавливая его
// // значение по умолчанию как "black".
// // String.prototype.write = stringWrite; - Добавляет
// // новый метод write к прототипу String, указывая на
// // функцию stringWrite, которая выводит цвет текста
// // и сам текст в консоль.
// // function stringWrite() { ... } - Определяет
// // функцию stringWrite, которая будет вызываться
// // при вызове метода write для объектов типа String.
// // Создаются два экземпляра класса String: s и s2.
// // s.color = "red"; - Для первого объекта s
// // переопределяется свойство color на "red".
// // s.write(); - Вызывается метод write для объекта s,
// // который выведет в консоль "Цвет текста: red" и
// // "Текст: Это строка", потому что для объекта s
// // было установлено свойство color в "red".
// // s2.write(); - Вызывается метод write для объекта s2,
// // который выведет в консоль "Цвет текста: black" и
// // "Текст: Вторая строка", потому что для объекта s2
// // свойство color не было переопределено, и
// // используется значение по умолчанию "black",
// // установленное в прототипе.
//
// console.log("\nПятое");
//
// // function Rabbit() {
// // }
// //
// // Rabbit.prototype = {
// //     eats: true
// // };
// // let rabbit = new Rabbit();
// // console.log(rabbit.eats); // true
//
// // Rabbit.prototype = {};
// // После этой операции rabbit.eats будет равно
// // undefined, потому что мы полностью заменили
// // прототип объекта Rabbit на пустой объект, а
// // свойство eats уже не существует в новом прототипе.
// // Rabbit.prototype.eats = false;
// // После этой операции rabbit.eats будет равно
// // false, потому что мы изменили значение свойства
// // eats в прототипе объекта Rabbit на false, и это
// // значение будет наследоваться всеми экземплярами
// // объекта Rabbit.
// // delete rabbit.eats;
// // После этой операции rabbit.eats снова будет равно
// // true, потому что мы удалили свойство eats из самого
// // объекта rabbit, но оно осталось в его прототипе.
// // delete Rabbit.prototype.eats;
// // После этой операции rabbit.eats снова будет равно
// // undefined, потому что мы удалили свойство eats из
// // прототипа объекта Rabbit, и оно перестало наследоваться
// // всеми экземплярами этого объекта.
//
// console.log("\nКлассы\nПервое");
//
// class Clock {
//     constructor(hours, minutes, seconds) {
//         this.hours = hours || 0;
//         this.minutes = minutes || 0;
//         this.seconds = seconds || 0;
//     }
//
//     // Метод для установки времени
//     setTime(hours, minutes, seconds) {
//         this.hours = hours || 0;
//         this.minutes = minutes || 0;
//         this.seconds = seconds || 0;
//     }
//
//     // Метод для вывода времени в консоль
//     displayTime() {
//         console.log(`Current time: ${this.hours}:${this.minutes}:${this.seconds}`);
//     }
// }
//
// // Пример использования класса Clock
// let clock = new Clock(10, 30, 15); // Создание нового объекта класса Clock с заданным временем
// clock.displayTime(); // Вывод текущего времени в консоль
//
// console.log("\nВторое");
//
// // class Animal {
// //     constructor(name) {
// //         this.name = name;
// //     }
// // }
// //
// // class Rabbit extends Animal {
// //     constructor(name) {
// //         super(name); // Вызываем конструктор родительского класса Animal с аргументом name
// //         this.created = Date.now();
// //     }
// // }
// //
// // let rabbit = new Rabbit("Белый кролик");
// // console.log(rabbit.name); // Выводит "Белый кролик"
//
// console.log("\nТретье");
//
// // class Clock {
// //     constructor(template) {
// //         this.template = template;
// //     }
// //
// //     render() {
// //         let date = new Date();
// //         let hours = date.getHours();
// //         if (hours < 10) hours = '0' + hours;
// //         let mins = date.getMinutes();
// //         if (mins < 10) mins = '0' + mins;
// //         let secs = date.getSeconds();
// //         if (secs < 10) secs = '0' + secs;
// //         let output = this.template
// //             .replace('h', hours)
// //             .replace('m', mins)
// //             .replace('s', secs);
// //         console.log(output);
// //     }
// //
// //     stop() {
// //         clearInterval(this.timer);
// //     }
// //
// //     start() {
// //         this.render();
// //         this.timer = setInterval(() => this.render(), 1000);
// //     }
// // }
// //
// // class ExtendedClock extends Clock {
// //     constructor(template, precision = 1000) {
// //         super(template); // Вызываем конструктор родительского класса Clock
// //         this.precision = precision; // Устанавливаем значение precision
// //     }
// //
// //     // Переопределяем метод start
// //     start() {
// //         this.render(); // Вызываем метод render из родительского класса
// //         this.timer = setInterval(() => this.render(), this.precision); // Используем значение precision для интервала
// //     }
// // }
//
// console.log("\nЧетвертое");
//
// class Stock {
//     constructor() {
//         this.boxes = [];
//     }
//
//     add(w, v) {
//         this.boxes.push({weight: w, volume: v, serialNumber: this.boxes.length});
//     }
//
//     getByW(min_w) {
//         let suitableBoxes = this.boxes.filter(box => box.weight >= min_w);
//         if (suitableBoxes.length === 0) return -1;
//         suitableBoxes.sort((a, b) => a.serialNumber - b.serialNumber);
//         return suitableBoxes[0].serialNumber;
//     }
//
//     getByV(min_v) {
//         let suitableBoxes = this.boxes.filter(box => box.volume >= min_v);
//         if (suitableBoxes.length === 0) return -1;
//         suitableBoxes.sort((a, b) => a.serialNumber - b.serialNumber);
//         return suitableBoxes[0].serialNumber;
//     }
// }
//
// // Пример использования
// let stock = new Stock();
// stock.add(10, 20); // Добавляем коробку с грузоподъемностью 10 и объемом 20
// stock.add(15, 25); // Добавляем коробку с грузоподъемностью 15 и объемом 25
// stock.add(8, 30); // Добавляем коробку с грузоподъемностью 8 и объемом 30
//
// console.log(stock.getByW(10)); // Возвращает номер коробки с грузоподъемностью хотя бы 10
// console.log(stock.getByV(25)); // Возвращает номер коробки с объемом хотя бы 25
// console.log(stock.getByW(20)); // Возвращает номер коробки с грузоподъемностью хотя бы 20
// console.log(stock.getByV(40)); // Возвращает номер коробки с объемом хотя бы 40
