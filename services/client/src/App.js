import React, { useState, useEffect } from "react";
//import logo from "./logo.svg";
import "./App.css";
import Tree from "./Tree";
import { fetchTreeData } from "./utils";

function App() {
  const [treeData, setTreeData] = useState({});
  useEffect(() => {
    const getData = async () => {
      const data = await fetchTreeData();
      setTreeData(data);
    };
    getData();
  }, []);
  return (
    <div className="App">
      <Tree data={treeData} />
    </div>
  );
}

export default App;
