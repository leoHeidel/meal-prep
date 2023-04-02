import React, { useState, useCallback } from "react";
import { HTML5Backend } from "react-dnd-html5-backend";
import { DndProvider } from "react-dnd";
import update from "immutability-helper";
import { Recipe } from "./Recipe";

import "./TimeTable.css";

function TimeTable() {
  const days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
];

  const [recipes, setRecipes] = useState([
    {
      id: 1,
      text: "Recipe 1",
      day: "Monday",
    },
    {
      id: 2,
      text: "Recipe 2",
      day: "Monday",
    },
    {
        id: 3,
        text: "Recipe 3",
        day: "Tuesday",
      },
      {
        id: 4,
        text: "Recipe 4",
        day: "Monday",
      },
      ]);

const moveRecipe = useCallback((dragIndex, hoverIndex, hoverDay) => {
  setRecipes((prevRecipes) =>
    update(prevRecipes, {
      $splice: [
        [dragIndex, 1],
        [hoverIndex, 0, { ...prevRecipes[dragIndex], day: hoverDay }],
      ],
    }),
  );
}, []);

const renderRecipe = useCallback(
  (recipe, index) => {
    return (
      <Recipe
        key={recipe.id}
        index={index}
        id={recipe.id}
        day={recipe.day}
        text={recipe.text}
        moveRecipe={moveRecipe}
      />
    );
  },
  [moveRecipe]
);

function handleAdd(day) {
  const text = prompt("Enter the name of the new recipe:");
  if (text) {
    const newRecipe = { day: day, text: text };
    setRecipes([...recipes, newRecipe]);
  }
}

  return (
    <DndProvider backend={HTML5Backend}>
      <div>
        <h2>Time Table Content</h2>
        <div className="timetable-grid">
          {days.map((day) => (
            <div key={day} className="day">
              <div className="widgets">
                <div className="day-widget">{day}</div>
                {recipes
                  .filter((recipe) => recipe.day === day)
                  .map((recipe) => renderRecipe(recipe, recipes.indexOf(recipe)))
                }
                <div className="add-recipe-widget" onClick={() => handleAdd(day)}>
                  <i className="fas fa-plus"></i>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </DndProvider>
  );
}

export default TimeTable;
