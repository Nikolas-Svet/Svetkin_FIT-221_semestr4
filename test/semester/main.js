let flag = true;

function showMain() {
    var userInput = document.querySelector('input[type="text"]').value;

    // Проверка на пустое поле
    if (userInput.trim() === '') {
        alert("Поле ввода пустое!");
        return;
    }

    // Проверка на длину имени
    if (userInput.length < 2 || userInput.length > 30) {
        alert("Имя пользователя должно быть длиной от 2 до 30 символов.");
        return;
    }

    // Проверка на допустимые символы (буквы и пробелы)
    if (!/^[a-zA-Zа-яА-ЯёЁ\s]+$/.test(userInput)) {
        alert("Имя пользователя должно содержать только буквы и пробелы.");
        return;
    }

    if (flag) {
        var mainDiv = document.querySelector('.main');
        mainDiv.style.display = 'block';
        var mainDiv2 = document.querySelector('.login');
        mainDiv2.style.display = 'none';
        flag = false;
        document.getElementById('NameUser').textContent = "Привет, " + userInput + "!";
    } else {
        var mainDiv = document.querySelector('.main');
        mainDiv.style.display = 'none';
        var mainDiv2 = document.querySelector('.login');
        mainDiv2.style.display = 'flex';
        flag = true;
    }
}
