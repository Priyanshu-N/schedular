import { useState } from "react";

function TaskForm(){

    const [taskName, setTaskName] = useState("");
    const [taskType, setTaskType] = useState("kill_process");
    const [processName, setProcessName] = useState("");
    const [filePath, setFilePath] = useState("");
    const [startTime, setStartTime] = useState("");
    const [endTime, setEndTime] = useState("");
    const [interval, setInterval] = useState(0);

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log({taskName, taskType, processName, filePath, startTime, interval})
    };

    return(
        <form onSubmit={handleSubmit} className="p-4 bg-gray-100 rounded shadow">
            <input type="text" placeholder="Task Name" value={taskName} onChange={e => setTaskName(e.target.value)} className="mb-2 p-2 border rounded w-full"/>
            <select value={taskType} onChange={e => setTaskType(e.target.value)} className="mb-2 p-2 border rounded w-full">
                <option value="kill_process">Kill Process</option>
                <option value="open_file">Open File</option>
            </select>
            <input type="text" placeholder="Process Name" value={processName} onChange={e => setProcessName(e.target.value)} className="mb-2 p-2 border rounded w-full"/>
            <input type="text" placeholder="File Path" value={filePath} onChange={e => setFilePath(e.target.value)} className="mb-2 p-2 border rounded w-full"/>
            <input type="datetime-local" value={startTime} onChange={e => setStartTime(e.target.value)} className="mb-2 p-2 border rounded w-full"/>
            <input type="datetime-local" value={endTime} onChange={e => setEndTime(e.target.value)} className="mb-2 p-2 border rounded w-full"/>
            <input type="number" placeholder="Interval (seconds)" value={interval} onChange={e => setInterval(e.target.value)} className="mb-2 p-2 border rounded w-full"/>
            <button type="submit" className="p-2 bg-blue-500 text-white rounded w-full">Add Task</button>
        </form> 

    );

}

export default TaskForm;