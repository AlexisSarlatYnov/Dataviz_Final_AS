import React from "react";

import dataRaw from "../../pornhub_2019_2020.json";

import {Box, Text, Meter, Chart, Select, Heading} from "grommet";

import {LineChart, ReferenceLine, CartesianGrid, XAxis, YAxis, Tooltip, Legend, Line, Area, AreaChart, ComposedChart, BarChart, Bar, Cell} from "recharts";



const datas = new Array();
dataRaw.map(item => {
    item.date = new Date(item.date);
    let month = "";
    switch (item.date.getMonth() + 1) {
        case 1:
            month = 'Jan';
            break;
        case 2:
            month = 'Feb';
            break;
        case 3:
            month = 'Mar';
            break;
        case 4:
            month = 'Apr';
            break;
        case 5:
            month = 'May';
            break;
        case 6:
            month = 'Jun';
            break;
        case 7:
            month = 'Jul';
            break;
        case 8:
            month = 'Aug';
            break;
        case 9:
            month = 'Sep';
            break;
        case 10:
            month = 'Oct';
            break;
        case 11:
            month = 'Nov';
            break;
        case 12:
            month = 'Dec';
            break;
        default:
            break;
    }
    item.date = month + ' ' +(item.date.getFullYear()).toString();
    datas.push(item)
});


const Pornhub = () => {
    return(
        <Box fill align="center" justify="center">
            <Heading>Porn Data</Heading>
            <Text>Pornhub French Frequency Evolution</Text>
            <AreaChart width={1000} height={300} data={datas} syncId="ID1" margin={{top: 10, right: 30, left: 0, bottom: 0}}>
                <CartesianGrid strokeDasharray="4 4" />
                <XAxis dataKey="date" />
                <YAxis />
                <Tooltip />
                <Legend/>
                <Area type="monotone" dataKey="pornhub" stroke="#8884d8" fill="#8884d8" />
            </AreaChart>
        </Box>
    )}

export default Pornhub;








