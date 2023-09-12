const toDoList = [];

function addTask() {
    const inputElement = document.querySelector('.js-name-input');
    const task = inputElement.value; 
    toDoList.push(task);
    console.log(toDoList);
    inputElement.value = '';
}
