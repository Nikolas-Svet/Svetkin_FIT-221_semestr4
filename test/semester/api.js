// api.js

async function fetchImage() {
  try {
    const response = await fetch("https://dog.ceo/api/breeds/image/random");
    const data = await response.json();
    return data.message;
  } catch (error) {
    throw new Error('Ошибка при получении данных:' + error);
  }
}

