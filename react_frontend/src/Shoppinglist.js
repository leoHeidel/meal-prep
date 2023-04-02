
import "./Shoppinglist.css"
import React, { useState } from 'react';
export default function ShoppingList(props) {
  const [checkedItems, setCheckedItems] = useState([]);

  const handleItemCheck = (item) => {
    if (checkedItems.includes(item)) {
      setCheckedItems(checkedItems.filter((checkedItem) => checkedItem !== item));
    } else {
      setCheckedItems([...checkedItems, item]);
    }
  };

  return (
    <div>
      <h2>Your Shopping List</h2>
      <ul>
        {props.ingredients.map((ingredient) => (
          <li key={ingredient.name} className={checkedItems.includes(ingredient) ? 'checked' : ''} onClick={() => handleItemCheck(ingredient)}>
            {ingredient.name} ({ingredient.quantity})
          </li>
        ))}
      </ul>
    </div>
  );
}
