import React from 'react'
import ReactDOM from 'react-dom/client'

import './index.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import Login from './views/Login.jsx'
import Home from './views/Home.jsx'
import Register from './views/Register.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />}></Route>
        <Route path="/home" element={<Home />} />
        <Route path="/register" element={<Register />} />
        
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
)
