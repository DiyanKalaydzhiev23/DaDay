import './App.css';
import { Routes, Route } from 'react-router-dom';

import Layout from './components/layout/Layout';
import Home from './components/Home/Home';
import ReportChart from './components/MonthlyReport/ReportChart';

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/chart" element={<ReportChart />} />
      </Routes>
    </Layout>
  );
}

export default App;
