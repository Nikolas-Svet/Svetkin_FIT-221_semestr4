
async function readConfig(name) {
  return new Promise(resolve => {
    setTimeout(() => {
      console.log('(1) config from ' + name + ' loaded');
      resolve();
    }, Math.floor(Math.random() * 1000));
  });
}

async function doQuery(statement) {
  return new Promise(resolve => {
    setTimeout(() => {
      console.log('(2) SQL query executed: ' + statement);
      resolve();
    }, Math.floor(Math.random() * 1000));
  });
}

async function httpGet(url) {
  return new Promise(resolve => {
    setTimeout(() => {
      console.log('(3) Page retrieved: ' + url);
      resolve();
    }, Math.floor(Math.random() * 1000));
  });
}

async function readFile(path) {
  return new Promise(resolve => {
    setTimeout(() => {
      console.log('(4) Readme file from ' + path + ' loaded');
      resolve();
    }, Math.floor(Math.random() * 1000));
  });
}

// Функция для выполнения всех асинхронных операций последовательно
async function main() {
  console.log('start');

  try {
    await readConfig('myConfig');
    await doQuery('select * from cities');
    await httpGet('http://google.com');
    await readFile('README.md');
    console.log('It is done!');
  } catch (error) {
    console.error('Error:', error);
  } finally {
    console.log('end');
  }
}

main();
