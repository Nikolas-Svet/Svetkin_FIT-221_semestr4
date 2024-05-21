console.log("\nТретье");

// Пример асинхронных функций
async function f1(x) {
  return new Promise(resolve => setTimeout(() => resolve(x * x), 100));
}

async function f2(x) {
  return new Promise(resolve => setTimeout(() => resolve(2 * x), 100));
}

async function f3(x) {
  return new Promise(resolve => setTimeout(() => resolve(-2), 100));
}

async function f4(x) {
  return new Promise(resolve => setTimeout(() => resolve(x + 10), 100));
}

async function f5(x) {
  return new Promise(resolve => setTimeout(() => resolve(x / 2), 100));
}

async function f6(x) {
  return new Promise(resolve => setTimeout(() => resolve(3 * x), 100));
}

// Функция для вычисления F(x) = f1(x) + f2(x) + … + fn(x)
async function calculateFx(x, functions) {
  let result = 0;
  for (let func of functions) {
    const value = await func(x);
    result += value;
    console.log(`Вызов ${func.name} дает значение ${value}, промежуточный результат ${result}`);
  }
  return result;
}

// Примеры использования для разного n
function main() {
  const x = 3;
  const funcsForN2 = [f1, f2];
  const funcsForN4 = [f1, f2, f3, f4];
  const funcsForN6 = [f1, f2, f3, f4, f5, f6];

  calculateFx(x, funcsForN2).then(result => console.log(`Ответ для F(x) при n=2: ${result}`));
  calculateFx(x, funcsForN4).then(result => console.log(`Ответ для F(x) при n=4: ${result}`));
  calculateFx(x, funcsForN6).then(result => console.log(`Ответ для F(x) при n=6: ${result}`));
}

main();
