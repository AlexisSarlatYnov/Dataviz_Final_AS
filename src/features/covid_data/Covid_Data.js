import React from "react";

import dataRaw from "../../covid_data.json";

import {Box, Text, Meter, Chart, Select} from "grommet";

import {LineChart, ReferenceLine, CartesianGrid, XAxis, YAxis, Tooltip, Legend, Line, Area, AreaChart, ComposedChart, BarChart, Bar, Cell} from "recharts";



const datas = new Array();
dataRaw.map(item => {
    datas.push(item)
});

console.log(datas);

datas.shift();
datas.splice(8, datas.length - 8);

const Covid_Cases = () => {
    return(
        <Box fill align="center" justify="center">
            <Text>Top 8 Cases, Deaths and Recoveries By Country</Text>
            <BarChart width={1000} height={300} data={datas} margin={{top: 5, right: 30, left: 20, bottom: 5}}>
              <CartesianGrid strokeDasharray="3 3"/>
              <XAxis dataKey="Location"/>
              <YAxis/>
              <Tooltip/>
              <Legend />
              <Bar dataKey="Cases" fill="#067AE3" />
              <Bar dataKey="Deaths" fill="#E31D06" />
              <Bar dataKey="Recoveries" fill="#05AC16" />
            </BarChart>
        </Box>
    )}

export default Covid_Cases;








