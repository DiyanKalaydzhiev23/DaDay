import './App.css';
import { Routes, Route } from 'react-router-dom';
import { Navigate } from 'react-router-dom';

import Layout from './components/layout/Layout';
import Login from './components/Login/Login';
import MonthlyReport from './components/MonthlyReport/MonthlyReport';
import Register from './components/Register/Register';

function App() {
  return (
    <Layout>
      <Routes>
        <Route exact path="/" element={<Navigate to="/login" />}/>
        <Route path="/monthly-report" element={<MonthlyReport />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </Layout>
  );
}

export default App;
