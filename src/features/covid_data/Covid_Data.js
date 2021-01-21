import React, {useRef, useEffect} from "react";
import {Runtime, Inspector} from "@observablehq/runtime";
import notebook from "7a24795d54ccd03f";

function Covid_Cases() {
    const ref = useRef();
  
    useEffect(() => {
      (new Runtime).module(notebook, name => {
        if (name === "chart") return Inspector.into(ref.current.querySelector(".chart"))();
      });
    }, []);
  
    return (
      <div className="Notebook" ref={ref}>
        <div className="chart"></div>
        <p>Credit: <a href="https://observablehq.com/d/7a24795d54ccd03f">Week 1: Cupcake Barchart by alexenfeu</a></p>
      </div>
    );
  }
  
  export default Covid_Cases;