import React, { useState } from 'react';

function App() {
  const [arr, setArr] = useState('');

  const handleInputChange = (e) => {
    setArr(e.target.value);
  };

  return (
    <div className="App">
      <br />
      <form action="http://localhost:8080/api/home" method="post">
        <div>Input Array for processing</div>
        <input
          type="text"
          name="name"
          value={arr}
          onChange={handleInputChange}
        />
        <input type="submit" />
      </form>
    </div>
  );
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