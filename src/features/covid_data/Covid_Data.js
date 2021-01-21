import React from "react";

import dataRaw from "../../covid_data.json";
import dataRawDeaths from "../../covid_data_deaths.json";
import dataRawRecov from "../../covid_data_recov.json";

import {Box, Text, Meter, Chart, Select} from "grommet";

import {LineChart, ReferenceLine, CartesianGrid, XAxis, YAxis, Tooltip, Legend, Line, Area, AreaChart, ComposedChart, BarChart, Bar, Cell} from "recharts";



const dataCases = new Array();
dataRaw.map(item => {
  dataCases.push(item)
});

const dataDeaths = new Array();
dataRawDeaths.map(item => {
  dataDeaths.push(item)
});

const dataRecov = new Array();
dataRawRecov.map(item => {
  dataRecov.push(item)
});

console.log(dataCases);

dataCases.shift();
dataCases.splice(8, dataCases.length - 8);

dataDeaths.shift();
dataDeaths.splice(8, dataDeaths.length - 8);

dataRecov.shift();
dataRecov.splice(8, dataRecov.length - 8);

const Covid_Cases = () => {
    return(
        <Box fill align="center">
            <Text >Top 8 Covid Cases By Country</Text>
            <BarChart width={1000} height={300} data={dataCases} margin={{top: 5, right: 30, left: 20, bottom: 5}}>
              <CartesianGrid strokeDasharray="3 3"/>
              <XAxis dataKey="Location"/>
              <YAxis/>
              <Tooltip/>
              <Legend />
              <Bar dataKey="Cases" fill="#067AE3" />
            </BarChart>
            <Text>Top 8 Covid Deaths By Country</Text>
            <BarChart width={1000} height={300} data={dataDeaths} margin={{top: 5, right: 30, left: 20, bottom: 5}}>
              <CartesianGrid strokeDasharray="3 3"/>
              <XAxis dataKey="Location"/>
              <YAxis/>
              <Tooltip/>
              <Legend />
              <Bar dataKey="Deaths" fill="#E31D06" />
            </BarChart>
            <Text>Top 8 Covid Recoveries By Country</Text>
            <BarChart width={1000} height={300} data={dataRecov} margin={{top: 5, right: 30, left: 20, bottom: 5}}>
              <CartesianGrid strokeDasharray="3 3"/>
              <XAxis dataKey="Location"/>
              <YAxis/>
              <Tooltip/>
              <Legend />
              <Bar dataKey="Recoveries" fill="#05AC16" />
            </BarChart>
        </Box>
    )}

export default Covid_Cases;








