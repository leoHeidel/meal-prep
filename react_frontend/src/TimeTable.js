import React, { useState } from "react";
import { useDrag, useDrop, DndProvider } from "react-dnd";
import { HTML5Backend } from "react-dnd-html5-backend";
import { ItemTypes } from "./ItemTypes";

import './TimeTable.css';

const RecipeWidget = ({ name, day, onDrop }) => {
  const [{ isDragging }, drag] = useDrag({
    type: ItemTypes.RECIPE,
    item: () => ({ name }),
    collect: (monitor) => ({
      isDragging: monitor.isDragging(),
    }),
    begin: (monitor) => {
        console.log(`Started dragging ${name}`);
    },
  });

  const [{ canDrop, isOver }, drop] = useDrop({
    accept: ItemTypes.RECIPE,
    drop: (item) => {
      console.log(`Dropped ${item.name} onto ${day}`);
      onDrop(day)(item);
    },
    collect: (monitor) => ({
      isOver: monitor.isOver(),
      canDrop: monitor.canDrop(),
    }),
  });

  const isActive = canDrop && isOver;

  console.log(`Rendered RecipeWidget for ${name} on ${day}`);

  return (
    <div
      ref={drop}
      className={`recipe-widget ${isActive ? "active" : ""}`}
      style={{ opacity: isDragging ? 0.5 : 1 }}
    >
      <div ref={drag} className="handle" />
      {name}
    </div>
  );
};

function TimeTable() {
  const [recipes, setRecipes] = useState({
    Monday: "Recipe 1",
    Tuesday: "",
    Wednesday: "",
    Thursday: "",
    Friday: "",
    Saturday: "",
    Sunday: "",
  });

  const onDrop = (day) => (item) => {
    console.log(`Dropping ${item.name} onto ${day}`);
    setRecipes((recipes) => ({
      ...recipes,
      [day]: item.name,
      [Object.keys(recipes).find((key) => recipes[key] === item.name)]: "",
    }));
  };

  console.log("Rendered TimeTable");

  return (
    <DndProvider backend={HTML5Backend}>
      <div>
        <h1>Time Table Content</h1>
        <div className="timetable-grid">
          {Object.keys(recipes).map((day) => (
            <div key={day} className="day">
              <div className="widgets">
                <div className="day-widget">{day}</div>
                {recipes[day] !== "" ? (
                  <RecipeWidget name={recipes[day]} day={day} onDrop={onDrop} />
                ) : null}
              </div>
            </div>
          ))}
        </div>
      </div>
    </DndProvider>
  );
}

export default TimeTable;
