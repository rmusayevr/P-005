// let isConfirmed = confirm("Do you want to start?"); // true or false

// if (isConfirmed) {
//     alert("You confirmed!");
// } else {
//     alert("You didn't confirm!");
// }


// let firstName = prompt("What is your name?");
// if (firstName === 'Rashad') {
//     alert(`Your name is Rashad`);
// } else {
//     alert(`Your name isn't Rashad. It is ${firstName}!`);
// }

// let age = '21';
// if (age === 21) {
//     console.log(age);
// } else {
//     console.log(age + 2);
// }


// document.write(age);
// document.getElementById('h1').innerHTML += ' JS'


// const surname = 'Musayev';
// surname = 'Rashad';
// console.log(surname);

// let firstName = 'Rashad';
// firstName = 'Musayev';
// console.log(firstName);

// var age = 21;
// var age = 23;
// age = 22.2;

// console.log(age);

// function newFunc2() {
//     console.log(age);
//     return age;
// };

// let firstName;

// console.log(typeof(firstName));

// console.log(typeof(newFunc2));

// console.log(typeof(age));

// console.log(newFunc2());

// let day = 'Monday';
// if (day == 'Monday') {
//     alert("It's not Thursday. It's Monday.");
// } else if (day === 'Tuesday') {
//     alert("It's not Thursday. It's Tuesday.");
// } else if (day === 'Wednesday') {
//     alert("It's not Thursday. It's Wednesday.");
// } else if (day === 'Friday') {
//     alert("It's not Thursday. It's Friday.");
// } else if (day === 'Saturday') {
//     alert("It's not Thursday. It's Saturday.");
// } else if (day === 'Sunday') {
//     alert("It's not Thursday. It's Sunday.");
// } else {
//     alert(`It's ${day}`);
// }

// var myNumber = 11;

// while (myNumber < 10) {
//     console.log(myNumber);
//     myNumber++;
// }

// do {
//     console.log(myNumber);
//     myNumber++;
// } while (myNumber < 10);

// let country = 'Sweden';
// for (let i = 0; i < country.length; i++) {
//     console.log(country[i]);
// }


// for (let i = 1; i < 5; i++) {
// console.log("*".repeat(i * 2 - 1));
// }

// let countries = ['Sweden', 'Finland', 'Norway', 'Iceland'];
// for (const selectedCountry of countries) {
//     console.log(selectedCountry);
// }

// let person = {
//     "firstName": "Rashad",
//     "lastName": "Musayev",
//     "age": 21
// };

// for (const key in person) {
//     console.log(`${key}: ${person[key]}`);
// };

// for (var i = 0; i < 5; i++) {}
// if (5 < 9) {}

// function showYourAge(age, year) {
//     let birthdayYear = year - age;
//     return birthdayYear;
// }

// console.log(typeof(showYourAge));
// console.log(typeof(showYourAge()));

// let result = showYourAge(28, 1972);

// console.log(result);
// console.log(typeof(result));

// const colors = ['Green', 'Orange', 'Purple', 'Pink', 'Brown'];
// let fruits = ['Apple', 'Orange', 'Eggplant', 'Dragon Fruit', 'Kiwi'];
// for (var i = 0; i < colors.length; i++) {
//     console.log(colors[i], '--> name of color');
//     console.log(i, '--> index of color');
// }

// for (const color of colors) {
//     console.log(color, '--> name of the color');
// }

// colors.forEach((color, i) => console.log(color, i));

// const newArray = fruits.concat(colors);
// console.log(newArray);
// const copiedArray = fruits.copyWithin(2, 0, 2);
// console.log(copiedArray);
// const arrayEntries = fruits.entries()
// for (const entry of arrayEntries) {
//     console.log(entry);
// }
// fruits.pop();
// console.log(fruits);
// fruits.push('Banana');
// console.log(fruits);
// fruits.shift();
// console.log(fruits);
// fruits.unshift('Pear', 'Strawberry', 'Mango');
// console.log(fruits);
// const slicedFruits = fruits.slice(2, 5);
// console.log(slicedFruits);
// const splicedFruits = fruits.splice(4, 5);
// console.log(splicedFruits);
// console.log(fruits);
// const reversedFruits = fruits.slice().reverse()
// console.log(reversedFruits);
// console.log(fruits);
// console.log(colors.join(' ---> '));



// const colorfulFruits = colors.map((color, i) => createColors(color, i));
// console.log(colorfulFruits);
// console.log(colors);

// function createColors(color, i) {
//     return `${color} ${fruits[i]}`;
// }

// const mergedColors = colors.reduce((previousColor, color) => mergeColors(previousColor, color));
// console.log(mergedColors);
// console.log(colors);

// function mergeColors(previousColor, color) {
//     return `${previousColor} ${color}`;
// }

// const comparedData = colors.filter((color, i) => compareData(color, i));
// console.log(comparedData);

// function compareData(color, i) {
//     if (color.length === fruits[i].length) {
//         return `${color} ${fruits[i]}`;
//     }
// }


// console.log(document.body);
// console.log(document.title);
// console.log(document.head);
// console.log(document.contentType);
// console.log(document.styleSheets);

// const body = document.getElementsByTagName('body')[0];
// console.log(body.innerHTML);
// console.log(body.innerText);

// const head = document.getElementsByTagName('head')[0].innerHTML;
// console.log(head);
// const h1 = document.getElementsByTagName('h1')[0].innerHTML;
// console.log(h1);

// const divID1 = document.getElementById('id1');
// console.log(divID1.innerHTML);
// const divClass1 = document.getElementsByClassName('class1');
// console.log(divClass1);


// const divQuery = document.querySelector('#id1')
// divQuery.innerHTML = '<h1>This is changed div element</h1>'
// const divQueryText = document.querySelector('#classText')
// divQueryText.innerText = '<h1>This is changed div element</h1>'
// console.log(divQuery);
// const divQueryAll = document.querySelectorAll('.class1')[1]
// console.log(divQueryAll);
// const divQuery = document.querySelectorAll('#class1')[2]
// console.log(divQuery);

// const divQuery = document.querySelectorAll('#class1')[0]
// divQuery.textContent = 'Wow'
// console.log(divQuery.textContent);

// const pQuery = document.querySelector('p')
// console.log(pQuery.parentElement.parentElement);
// console.log(pQuery.closest('.class12'));

// const childrenQuery = document.getElementById('class1')
// console.log(childrenQuery.children);
// console.log(childrenQuery.children[1].children);
// console.log(childrenQuery.nextElementSibling.nextElementSibling);
// console.log(childrenQuery.previousElementSibling);


// const idElement = document.getElementById("h1");
// console.log(idElement.getAttribute('style'));
// idElement.setAttribute('class', 'h1_class');
// idElement.setAttribute('id', 'h1_id');
// idElement.id = 'idElement_id'
// console.log(idElement);

// const aElement = document.querySelector('a');
// console.log(aElement.href);

const class1IDiv = document.querySelector('#class1')
console.log(class1IDiv.classList);
class1IDiv.classList.add('class4');
console.log(class1IDiv.classList);
class1IDiv.classList.remove('class1');
console.log(class1IDiv.classList);
class1IDiv.classList.replace('class2', 'class5');
console.log(class1IDiv.classList);
console.log(class1IDiv.classList.contains('class2'));
console.log(class1IDiv.classList.contains('class5'));
function toggleClass() {
    class1IDiv.classList.toggle('class6');
    console.log(class1IDiv.classList);
    class1IDiv.innerHTML = 'aaaaaaaaaaa';
}

