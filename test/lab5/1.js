let promise = new Promise(function(resolve, reject) {
resolve(1);
setTimeout(() => resolve(2), 1000);
});
promise.then(console.log);
// Когда resolve(1) вызывается, промис переходит в состояние
// "resolved" с значением 1. Второй вызов resolve(2) игнорируется,
//     потому что промис может быть разрешен только один раз.
//     Поэтому, console.log в then выводит 1.