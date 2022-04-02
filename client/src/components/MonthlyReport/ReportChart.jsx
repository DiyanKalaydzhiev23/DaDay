import React from 'react';
import { LineChart, Line, CartesianAxis, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from 'recharts';
import { formatDate } from '../../utils';

const ReportChart = ({ emotions }) => {
  let data = [];

  emotions.forEach(emotionObj => {
    data.push({name: formatDate(emotionObj.date), uv: Number(emotionObj.emotion) })
  });
  

  return (
    <>
      <ResponsiveContainer width={500} height={500}>
        <LineChart
          width={500}
          height={300}
          data={data}
        >
          <CartesianGrid strokeDasharray={"3 3"} />
          <XAxis dataKey="name" />
          <YAxis />
          <Line type="monotone" dataKey="pv" stroke="#8884d8" activeDot={{ r: 8 }} />
          <Line type="monotone" dataKey="uv" stroke="#82ca9d" />
        </LineChart>
      </ResponsiveContainer>
    </>
  );
}

export default ReportChart;