function sumWithDelay(a, b) {
  return new Promise((resolve, reject) => {
    if (typeof a !== 'number' || typeof b !== 'number') {
      reject(new Error('Оба аргумента должны быть числами'));
      return;
    }

    let sum = a;
    let count = 0;

    const interval = setInterval(() => {
      sum += b;
      count++;
      console.log(`Сумма: ${sum}, Количество вызовов: ${count}`);

      if (count === 5) {
        clearInterval(interval);
        resolve(sum);
      }
    }, 2000);
  });
}

// Успешное выполнение
// sumWithDelay(1, 2).then(result => console.log(`Итоговая сумма: ${result}`)).catch(console.error);

// Ошибка
sumWithDelay(1, '2').then(result => console.log(`Итоговая сумма: ${result}`)).catch(console.error);
