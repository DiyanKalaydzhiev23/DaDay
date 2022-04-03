import './App.css';
import { Routes, Route } from 'react-router-dom';
import { Navigate } from 'react-router-dom';

import CreateNote from './components/Notes/CreateNote';
import Layout from './components/layout/Layout';
import Login from './components/Login/Login';
import MonthlyReport from './components/MonthlyReport/MonthlyReport';
import Register from './components/Register/Register';

function App() {
  const user = localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')) : null;
  
  return (
    <Layout>
      <Routes>
        <Route path="/" element={user ? <CreateNote /> : <Navigate to="/login" />}/>
        <Route path="/monthly-report" element={<MonthlyReport />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </Layout>
  );
}

export default App;
