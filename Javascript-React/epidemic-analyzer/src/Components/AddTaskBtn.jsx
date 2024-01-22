//TODO: get hook to update and add text from input to list once button pressed
import React from "react";
import { useState } from "react";

function UpdateTaskList(){
  const [taskList, setTaskList] = useState([])
  const handleSubmitTask = (e) => {
    e.preventDefault()
    const data = new FormData(e.target);
    const taskText = data.get('addTask');
    
    const rendList = taskList.map(() => <li key={setTaskList(taskText)}></li>)    
      //setTask([...task, taskText])
  
}


    return (
      <>
        <form id="addTaskForm" onSubmit={handleSubmitTask}>
          <label htmlFor="addTask" className="mr-2">Add a Task</label>
          <input type="text" name="addTask" id="addTask" className="border border-blue-500" />
          <button onClick={handleSubmitTask}>Add Task</button>
        </form>
        <p>
          
        </p>
      </>
      
    )
}

export default UpdateTaskList;