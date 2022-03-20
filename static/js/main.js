const tasks = document.querySelectorAll('.task-state');
const tasksTexts = document.querySelectorAll('.task-text');


tasks.forEach((task, index) => {
    if(task.checked) {
        tasksTexts[index].classList.add("text-muted");
        tasksTexts[index].classList.add("text-decoration-line-through");
    }else{
        tasksTexts[index].classList.remove("text-muted");
        tasksTexts[index].classList.remove("text-decoration-line-through");
    }
    task.addEventListener('click', () => {
        if(task.checked) {
            tasksTexts[index].classList.add("text-muted");
            tasksTexts[index].classList.add("text-decoration-line-through");
        }else{
            tasksTexts[index].classList.remove("text-muted");
            tasksTexts[index].classList.remove("text-decoration-line-through");
        }
    })
});