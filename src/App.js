import React from "react";
import { Grommet, Box, Text } from "grommet";

import MapBox from "./features/Map/MapBox";
import Pornhub from "./features/pornhub/pornhub";
import Covid_Cases from "./features/covid_data/Covid_Data";

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
      <Box fill align="center" justify="center">
        {/* <MapBox /> */}
        {/* <FinalProject/> */}
        {/* <Pornhub/> */}
        <Covid_Cases/>
      </Box>
    </Grommet>
  );
}

export default App;
