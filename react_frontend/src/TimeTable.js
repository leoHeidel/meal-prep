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

      const moveRecipe = useCallback((dragIndex, hoverIndex) => {
        setRecipes((prevRecipes) =>
          update(prevRecipes, {
            $splice: [
              [dragIndex, 1],
              [hoverIndex, 0, prevRecipes[dragIndex]],
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
          text={recipe.text}
          moveRecipe={moveRecipe}
        />
      );
    },
    [moveRecipe]
  );

  return (
    <DndProvider backend={HTML5Backend}>
      <div>
        <h1>Time Table Content</h1>
        <div className="timetable-grid">
          {days.map((day) => (
            <div key={day} className="day">
              <div className="widgets">
                <div className="day-widget">{day}</div>
                {recipes
                  .filter((recipe) => recipe.day === day)
                  .map((recipe, i) => renderRecipe(recipe, i))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </DndProvider>
  );
}

export default TimeTable;
