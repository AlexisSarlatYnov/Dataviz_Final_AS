import React from "react";

import dataRaw from "../../JV_USA_19_20.json";

import {Box, Text, Meter, Chart, Select} from "grommet";

import {LineChart, Sector, PieChart, Pie, ReferenceLine, CartesianGrid, XAxis, YAxis, Tooltip, Legend, Line, Area, AreaChart, ComposedChart, BarChart, Bar, Cell} from "recharts";

const dataDiffYEAR19_20_millionVentesTotalJV = new Array();
dataRaw.map(item => {
    dataDiffYEAR19_20_millionVentesTotalJV.push(item)
});

dataDiffYEAR19_20_millionVentesTotalJV.pop();

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];

const JVUSA = () => {
    return(
    <Box direction="row" overfllow='auto'>
        <Box >
            <Text>Difference on total videogames millions dollars sales between 2019 and 2020</Text>
            <PieChart width={400} height={400}>
                <Pie dataKey="DiffYEAR19_20_millionVentesTotalJV" isAnimationActive={false} data={dataDiffYEAR19_20_millionVentesTotalJV} cx={200} cy={200} outerRadius={80} label >
                    {dataDiffYEAR19_20_millionVentesTotalJV.map((entry, index) => <Cell fill={COLORS[index % COLORS.length]}/>)}
                </Pie>
                <Tooltip />
            </PieChart>
            <Text color='#0088FE'>2019</Text>
            <Text color='#00C49F'>2020</Text>
        </Box>
        <Box >
            <Text>Difference on hardware videogames millions dollars sales between 2019 and 2020</Text>
            <PieChart width={400} height={400}>
                <Pie dataKey="DiffYEAR19_20_millionHardwareJV" isAnimationActive={false} data={dataDiffYEAR19_20_millionVentesTotalJV} cx={200} cy={200} outerRadius={80} label >
                    {dataDiffYEAR19_20_millionVentesTotalJV.map((entry, index) => <Cell fill={COLORS[index % COLORS.length]}/>)}
                </Pie>
                <Tooltip />
            </PieChart>
            <Text color='#0088FE'>2019</Text>
            <Text color='#00C49F'>2020</Text>
        </Box>
        <Box >
            <Text>Difference on complete videogames millions dollars sales between 2019 and 2020</Text>
            <PieChart width={400} height={400}>
                <Pie dataKey="DiffYEAR19_20_millionCompleteDLCJV" isAnimationActive={false} data={dataDiffYEAR19_20_millionVentesTotalJV} cx={200} cy={200} outerRadius={80} label >
                    {dataDiffYEAR19_20_millionVentesTotalJV.map((entry, index) => <Cell fill={COLORS[index % COLORS.length]}/>)}
                </Pie>
                <Tooltip />
            </PieChart>
            <Text color='#0088FE'>2019</Text>
            <Text color='#00C49F'>2020</Text>
        </Box>
        <Box >
            <Text>Difference on accessories videogames millions dollars sales between 2019 and 2020</Text>
            <PieChart width={400} height={400}>
                <Pie dataKey="DiffYEAR19_20_millionAccessoiresJV" isAnimationActive={false} data={dataDiffYEAR19_20_millionVentesTotalJV} cx={200} cy={200} outerRadius={80} label >
                    {dataDiffYEAR19_20_millionVentesTotalJV.map((entry, index) => <Cell fill={COLORS[index % COLORS.length]}/>)}
                </Pie>
                <Tooltip />
            </PieChart>
            <Text color='#0088FE'>2019</Text>
            <Text color='#00C49F'>2020</Text>
        </Box>
    </Box>
    )}

export default JVUSA;
