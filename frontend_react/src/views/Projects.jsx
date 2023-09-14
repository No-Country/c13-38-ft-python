import React, { useState, useEffect } from 'react';
import { useNavigate , useParams} from 'react-router-dom';

import Sidebar from "../components/Sidebar";
import Navbar from '../components/Navbar';
import Tablero from '../components/Tablero/Tablero';
import ServicioTablero from '../services/tableroService';

function Projects() {
    const [username, setUsername] = useState('');
    const [tableroInfo, setTableroInfo] = useState(null);
    const navigate = useNavigate();
    const { tableroId } = useParams();

    useEffect(() => {
        const token = localStorage.getItem('accessToken');
        if (!token) {
            navigate('/');
        }
        const storedUsername = localStorage.getItem('username');
        setUsername(storedUsername);
    }, [navigate]);


    useEffect(() => {
        // Verifica si hay un tableroId en la URL
        if (tableroId) {
            async function fetchTableroInfo() {
                try {
                    const accessToken = localStorage.getItem('accessToken');
                    const info = await ServicioTablero.getTableroDetallado(accessToken, tableroId);
                    setTableroInfo(info);
                } catch (error) {
                    console.error('Error al obtener información del tablero:', error);
                }
            }
            fetchTableroInfo();
        }
    }, [tableroId]);

    return (
        <>
            <div className="flex">
                <Sidebar username={username} />
                
                <div className="flex-1 overflow-auto">
                    <Navbar  />
                    {tableroInfo ? (
                        <Tablero tableroInfo={tableroInfo} className="h-full w-full"/>
                    ) : (
                        <p>Cargando información del tablero...</p>
                    )}
                </div>
            </div>


        </>
    )
}

export default Projects;