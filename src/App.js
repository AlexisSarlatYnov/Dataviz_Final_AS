import React from "react";
import { Grommet, Box, Text } from "grommet";

import MapBox from "./features/Map/MapBox";
import Pornhub from "./features/pornhub/pornhub";
import Covid_Cases from "./features/covid_data/Covid_Data";
import JVUSA from "./features/JVUSA/JVUSA.js";
import Insee_teletravail from "./features/Teletravail/teletravail.js";

const theme = {
  global: {
    font: {
      family: "Roboto",
      size: "18px",
      height: "20px",
    },
  },
};

function App() {
  return (
    <Grommet theme={theme} full>
      <Box justify="center">
        <Covid_Cases/>
        <Insee_teletravail/>
        <JVUSA/>
        <Pornhub/>
      </Box>
    </Grommet>
  );
}

export default App;
