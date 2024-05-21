function ask_password(login, password, success, failure) {
    const vowels = "aeiouy";
    let vowelCount = 0;
    const consonantsInPassword = [];

    login = login.toLowerCase();
    password = password.toLowerCase();

    for (let char of password) {
        if (vowels.includes(char)) {
            vowelCount++;
        } else {
            consonantsInPassword.push(char);
        }
    }

    const consonantsInLogin = [...login].filter(char => !vowels.includes(char) && char !== ' ').join('');
    const sortedConsonantsInPassword = consonantsInPassword.sort().join('');
    const sortedConsonantsInLogin = [...consonantsInLogin].sort().join('');

    const wrongVowelNumber = vowelCount !== 3;
    const wrongConsonants = sortedConsonantsInPassword !== sortedConsonantsInLogin;

    if (!wrongVowelNumber && !wrongConsonants) {
        success(login);
    } else {
        let errorMessage = "Everything is wrong";
        if (wrongVowelNumber && !wrongConsonants) {
            errorMessage = "Wrong number of vowels";
        } else if (!wrongVowelNumber && wrongConsonants) {
            errorMessage = "Wrong consonants";
        }
        failure(login, errorMessage);
    }
}

function success(login) {
    console.log(`Привет, ${login}!`);
}

function failure(login, message) {
    console.log(`Кто-то пытался притвориться пользователем ${login}, но в пароле допустил ошибку: ${message.toUpperCase()}.`);
}

function main(login, password) {
    ask_password(login, password, success, failure);
}

main('login', 'aaalgn');
main('login', 'aaaign');