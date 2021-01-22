import React from "react";

import dataRaw from "../../insee_teletravail_1.json";

import dataRaw2 from "../../insee_teletravail_2.json";

import dataRaw3 from "../../insee_teletravail_2_3.json";

import {Box, Text, Meter, Chart, Select, Heading} from "grommet";

import {LineChart, Sector, PieChart, Pie, ReferenceLine, CartesianGrid, XAxis, YAxis, Tooltip, Legend, Line, Area, AreaChart, ComposedChart, BarChart, Bar, Cell} from "recharts";

const data_insee_teletravail_1 = new Array();
dataRaw.map(item => {
    data_insee_teletravail_1.push(item)
});

data_insee_teletravail_1.pop();

const data_insee_teletravail_2 = new Array();
dataRaw2.map(item => {
    data_insee_teletravail_2.push(item)
});

data_insee_teletravail_2.shift();

const data_insee_teletravail_3 = new Array();
dataRaw3.map(item => {
    data_insee_teletravail_3.push(item)
});

data_insee_teletravail_3.shift();

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#C60BD8'];

const Insee_teletravail = () => {
    return(
        <Box fill align="center">
            <Heading>Home Working Data</Heading>
            <Text>Percentage of usage of home working</Text>
            <PieChart width={400} height={400}>
                <Pie dataKey="PartEmploiPourcent" isAnimationActive={false} data={data_insee_teletravail_1} cx={200} cy={200} outerRadius={80} label >
                    {data_insee_teletravail_1.map((entry, index) => <Cell fill={COLORS[index % COLORS.length]}/>)}
                </Pie>
                <Tooltip />
            </PieChart>
            <Text color='#0088FE'>Maintien d’une activité sur site</Text>
            <Text color='#00C49F'>Recours généralisé au travail à domicile</Text>
            <Text color='#FFBB28'>Essor du travail à domicile</Text>
            <Text color='#FF8042'>Possibilité limitée de télétravail</Text>
            <Text color='#C60BD8'>Activité à l’arrêt</Text>
            <Text>Comparaison home working between 2019 and 2020</Text>
            <BarChart width={1000} height={300} data={data_insee_teletravail_1} margin={{top: 5, right: 30, left: 20, bottom: 5}}>
              <CartesianGrid strokeDasharray="3 3"/>
              <XAxis dataKey="typeEmploi"/>
              <YAxis/>
              <Tooltip/>
              <Legend />
              <Bar dataKey="Teletravail19Pourcent" fill="#05AC16" />
              <Bar dataKey="Teletravail20Pourcent" fill="#0B8FD8" />
            </BarChart>
            <Text>Comparaison home working in 2017 in percentage</Text>
            <BarChart width={1000} height={300} data={data_insee_teletravail_2} margin={{top: 5, right: 30, left: 20, bottom: 5}}>
              <CartesianGrid strokeDasharray="3 3"/>
              <XAxis dataKey="typeEmploi"/>
              <YAxis/>
              <Tooltip/>
              <Legend />
              <Bar dataKey="Ensembleen2017pourcent" fill="#05AC16" />
            </BarChart>
        </Box>
        )}

export default Insee_teletravail;
