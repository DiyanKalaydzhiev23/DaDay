import './App.css';
import { Routes, Route } from 'react-router-dom';

import Home from './components/Home/Home';
import Layout from './components/layout/Layout';
import Login from './components/Login/Login';
import MonthlyReport from './components/MonthlyReport/MonthlyReport';
import Register from './components/Register/Register';

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/monthly-report" element={<MonthlyReport />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </Layout>
  );
}

export default App;
