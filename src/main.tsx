import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
// This file renders root app, and connects it to the structure of the HTML file.

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
