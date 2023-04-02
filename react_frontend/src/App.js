import React from 'react';
import './App.css';
import TimeTable from './TimeTable';
import Mealdetail from './Mealdetail';
import ShoppingList from './Shoppinglist';
import '@fortawesome/fontawesome-free/css/all.css';

export default function App() {
  const ingredients = [
    { name: 'Eggs', quantity: 12 },
    { name: 'Milk', quantity: 1 },
    { name: 'Flour', quantity: 2 },
  ];

  return (
    <div className="container">
      <div className="panel left">
        <TimeTable />
      </div>
      <div className="panel right">
        <div className="top-section">
          <div className="panel-section">
            <Mealdetail />
          </div>
        </div>
        <div className="bottom-section">
          <div className="panel-section">
            <ShoppingList ingredients={ingredients} />
          </div>
        </div>
      </div>
    </div>
  );
}
