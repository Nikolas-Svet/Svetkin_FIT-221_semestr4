
let imageUrls = []; // Массив для хранения ссылок на изображения
let currentIndex = -1; // Индекс текущего отображаемого изображения
let imageSizes = {}; // Объект для хранения размеров изображений

function showImg() {
    if (imageUrls.length > 14) {
        alert("Больше 15 изображений нельзя вывести")
    } else {
        fetchImage()
            .then(imageUrl => {
                if (!imageUrls.includes(imageUrl)) {
                    imageUrls.push(imageUrl);
                    imageSizes[imageUrl] = { width: 200, height: 200 }; // Инициализируем размер
                    showImages();
                }
            })
            .catch(error => console.error(error));
    }
}


function showImages() {
    const mainElement = document.querySelector('main');
    mainElement.innerHTML = ''; // Очищаем содержимое <main>
    imageUrls.forEach((imageUrl, index) => {
        const imageElement = document.createElement('img');
        imageElement.src = imageUrl;
        // imageElement.classList.add('fade-in');
        imageElement.style.width = imageSizes[imageUrl].width + 'px';
        imageElement.style.height = imageSizes[imageUrl].height + 'px';
        imageElement.style.border = index === currentIndex ? "4px solid white" : "none";
        mainElement.appendChild(imageElement);
    });
}

function deleteImg() {
    const mainElement = document.querySelector('main');
    const images = document.querySelectorAll('main img');
    images.forEach((image, index) => {
        if (image.style.border === "4px solid white") {
            // image.classList.remove('fade-in');
            image.classList.add('fade-out');
            image.addEventListener('animationend', () => {
                mainElement.removeChild(image);
                imageUrls.splice(index, 1); // Удаляем элемент из массива imageUrls
                delete imageSizes[image.src]; // Удаляем размеры изображения
                if (currentIndex >= imageUrls.length) {
                    currentIndex = imageUrls.length - 1; // Корректируем currentIndex
                }
                showImages(); // Обновляем отображение
            }, { once: true });
        }
    });
}

function NextImg() {
    if (imageUrls.length === 0) {
        alert("Нет загруженных изображений!");
        return;
    }
    currentIndex++; // Увеличиваем индекс

    if (currentIndex >= imageUrls.length) {
        currentIndex = 0; // Если достигли конца массива, переходим к первому изображению
    }

    showImages(); // Отображаем все изображения
}

function IncreaseImg() {
    const images = document.querySelectorAll('main img');
    images.forEach(image => {
        if (image.style.border === "4px solid white") {
            const currentWidth = parseInt(imageSizes[image.src].width);
            const currentHeight = parseInt(imageSizes[image.src].height);
            imageSizes[image.src] = { width: currentWidth + 50, height: currentHeight + 50 };
            image.style.width = imageSizes[image.src].width + 'px';
            image.style.height = imageSizes[image.src].height + 'px';
        }
    });
}

function DecreaseImg() {
    const images = document.querySelectorAll('main img');
    images.forEach(image => {
        if (image.style.border === "4px solid white") {
            const currentWidth = parseInt(imageSizes[image.src].width);
            const currentHeight = parseInt(imageSizes[image.src].height);
            imageSizes[image.src] = { width: currentWidth - 50, height: currentHeight - 50 };
            image.style.width = imageSizes[image.src].width + 'px';
            image.style.height = imageSizes[image.src].height + 'px';
        }
    });
}

function RotateImg() {
    const images = document.querySelectorAll('main img');
    images.forEach(image => {
        if (image.style.border === "4px solid white") {
            const currentTransform = image.style.transform || "";
            image.style.transform = currentTransform + "rotate(90deg)";
        }
    });
}

function ResetImg() {
    const images = document.querySelectorAll('main img');
    images.forEach(image => {
        imageSizes[image.src] = { width: 200, height: 200 };
        image.style.width = '200px';
        image.style.height = '200px';
    });
    showImages();
}
