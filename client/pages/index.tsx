import React, {useEffect, useState} from 'react';




function App() {

  const [arr, setArr] = useState("");
  const handleSubmit = (e) => {
    //fill this in
    e.preventDefault();
    alert(arr);
  }

  return (
    <div className="App">

      <br></br>
      <form onSubmit={handleSubmit}>
        <div>Input Array for processing</div>
        <input type="text" value={arr} onChange={(e) => setArr(e.target.value)} />
        <input type="submit"  />
      </form>
    </div>
  )
}

export default App;



/* 
function index() {

  const [message, setMessage] = useState("Loading");


  useEffect(() => {
    fetch('http://localhost:8080/api/home').then(
      response => response.json()
    ).then(
      data => {
        setMessage(data.message);
      });
  }, []);

  return <div>{message}</div>;
}

export default index;
 */