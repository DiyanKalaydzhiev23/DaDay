import './App.css';
import { Routes, Route } from 'react-router-dom';

import Layout from './components/layout/Layout';
import Home from './components/Home/Home';
import MonthlyReport from './components/MonthlyReport/MonthlyReport';
import Register from './components/Register/Register';

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/monthly-report" element={<MonthlyReport />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Layout>
  );
}

export default App;
