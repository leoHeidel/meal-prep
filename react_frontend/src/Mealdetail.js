// Mealdetail.js
import React, { useState } from 'react';
import './Mealdetail.css'; // Import the CSS for this component

function Mealdetail() {
  // Replace these example values with your actual data from the backend
  const recipe = 'Example Recipe';
  const preparationSteps = '1. Step one\n2. Step two\n3. Step three';
  const ingredients = '1 cup flour\n1/2 cup sugar\n2 eggs';

  const [selectedFor, setSelectedFor] = useState({
    darcy: false,
    leo: false,
  });

  const [request, setRequest] = useState(''); // Add this state for handling user requests

  const handleSelectionChange = (event) => {
    const { name, checked } = event.target;
    setSelectedFor({ ...selectedFor, [name]: checked });
  };

  const handleRequestChange = (event) => {
    setRequest(event.target.value);
  };

  const handleSubmitRequest = () => {
    // Add your logic to handle user requests here
    console.log('User request:', request);
  };


  return (
    <div className="mealdetail" style={{ backgroundColor: '#FFE5B4' }}>
      <h2>{recipe}</h2>
      <div className="rectangle">
        <h3>Preparation Steps</h3>
        <p>{preparationSteps}</p>
      </div>
      <div className="rectangle">
        <h3>Ingredients</h3>
        <p>{ingredients}</p>
      </div>
      <div className="for-who">
        <h3>This meal is for?</h3>
        <label>
          <input
            type="checkbox"
            name="darcy"
            checked={selectedFor.darcy}
            onChange={handleSelectionChange}
          />
          Darcy
        </label>
        <label>
          <input
            type="checkbox"
            name="leo"
            checked={selectedFor.leo}
            onChange={handleSelectionChange}
          />
          Leo
        </label>
      </div>
      <div className="user-request">
        <h3>Any special requests?</h3>
        <textarea
          placeholder="Leo is dumb dumb"
          value={request}
          onChange={handleRequestChange}
        />
        <button onClick={handleSubmitRequest}>Submit request</button>
      </div>
    </div>
  );
}

export default Mealdetail;
