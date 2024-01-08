`
SETTING UP REACT
i. $npm create vite@latest [app name]
ii. cd into dir of app
ii. $npm install
iii. to run application: $npm run dev

1. The atom of react - A Component, from which the entire
  react app is derived
  MyButton is a component

2. Diplaying data - jsx let's you put markup into js. use curly braces to 
  escape back into js, allowing you to embed a var into your code

3. Conditional rendering - similar to js

4. Rendering Lists - rely on for loops and map(). keep in mind that
  when using map, there will be a "placeholder var" required for iteration.
  "botName" is a placeholder that points to the items within the list object.
  the other part is the "key" attribute which requires the passing of a value that
  uniquely identifies the subitems within the item object

5. Responding to Events - using an event handler function inside components

6. Updating the Screen with States - if you want a component to remember information, you can use react 
  states
  functions that start with "se" are also called hooks. Hooks are more specific
  use-case and you can make your own.


7. Passing Props - when the component that contains a sate and handler, both are passed down as props
  when a new value is shown across multiple components at the same time, this is called "lifting state up"
  within the component, call the property object and app.js will render that
  specific prop

8. Object Destructuring - 

9. Rendering Lists - to manipulate an array of data and when trying to display multiple components from 
  a collection of data using the map() or filter() methods.
`

import React from 'react'
import { useState } from 'react'
import './App.css'
import PassProps from './Components/PassProps'

function App() {
  //6
  const [count, setCount] = useState(0)

  //1
  function MyButton(){
    //5
    function handleClick(){
      alert('button was clicked')
    }
    return(
      <button onClick={handleClick}>this button will give an alert</button>
    )
  }
  //2
  const user = {
    name: "react bot",
    version: "1"
  }
  //3
  function IfFormatting(){
    let content;
    if (1 > 0){
      return (
        content = "this is conditional rendering"
      )
    }
  }
  //?
  function IfFormattingCompact(){
    let compact = "this is a compacted form of conditional rendering"
    x = 1 ? (compact) : false
    return (
    {x}
    )
  }
  //4
  function RenderList(){
    const items = [
      {name: "bot kusanagi", version: 2.5},
      {name: "bot myung", version: 2.6}
    ]
    const listItems = items.map(botName => 
    <li key={botName}>
      {botName.name} is version {botName.version}
    </li>)
    return (
      <ul>{listItems}</ul>
    )
  
  }
  //6
  function CountButton(){
    setCount(count + 1)
  }
  //8
  function Desctructuring(){
    const person = {
      name: "person",
      title: "decontructed person object"
    }
    const {name, title} = person 
    return(
      <>
        <h2>This is an Object Deconstructured</h2>
        <p>{name}</p>
        <p>{title}</p>
      </>
    )
    
  }
  //9
  function RenderList(){
    const arr = [1,2,3]
    const rend = arr.map(x => <li>{x}</li>)
    console.log("test")
    return(
      <>
        <h3>
          Render Lists
        </h3>
        <p>
          <ul>
          {arr.map(x => <ul>{x}</ul>)}
          </ul>
        </p>
      </>
      
    )
  }
  return(
  <div>
    <p>
    <MyButton /> {/*1 & 5*/}
    </p>
    <p>
      {user.name} {/*2*/}
    </p>
    <p>
      <IfFormatting /> {/*3*/}
    </p>
    <p>
      <RenderList /> {/*4*/}
    </p>    
    <p>
      two buttons updated simulataneously
      <button onClick={CountButton}>{count}</button>
      <button onClick={CountButton}>{count}</button>
    </p>
    <p>
      <PassProps
        name="1520"
        title="prop one" /> {/*7*/}
      <PassProps 
        name="kusanagi"
        title="prop two"/> {/*7*/}
      <PassProps
        name="duncan"
        title="prop three" /> {/*7*/}
    </p>
    <p>
      <Desctructuring />decontructed
    </p>
    <p>
      <RenderList />
    </p>
  </div>

    )
}

export default App;