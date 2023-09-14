import React, { useState, useEffect, 
} from 'react';
import { useNavigate, useParams, useLocation } from 'react-router-dom';

import Sidebar from "../components/Sidebar";
import EspaciosTableros from "../components/Tablero/EspaciosTableros";
import espaciosService from "../services/espaciosService";


function VistaTableros() {
    const [username, setUsername] = useState('');
    const navigate = useNavigate();
    const { espacioId } = useParams();

    const location = useLocation();

    useEffect(() => {
        const token = localStorage.getItem('accessToken');
        if (!token) {
            navigate('/');
        }
        const storedUsername = localStorage.getItem('username');
        setUsername(storedUsername);
    }, [navigate]);

    useEffect(() => {
        const loadEspacioDetallado = async () => {
            try {
                const accessToken = localStorage.getItem('accessToken');
                const espacioDetallado = await espaciosService.getEspacioDetallado(accessToken, espacioId);
                
                // Utiliza la información detallada del espacio como necesites
                console.log('Información detallada del espacio:', espacioDetallado);
            } catch (error) {
                console.error('Error al obtener información detallada del espacio:', error);
            }
        };

        if (espacioId) {
            loadEspacioDetallado();
        }
    }, [espacioId]);

    return (
        <div className="flex">
            <Sidebar username={username} />
            <div className="flex-1 overflow-auto">
                <h1 className="text-xl font-bold text-primario text-center pt-10 mb-6">TUS TABLEROS</h1>
                <EspaciosTableros espacioId={espacioId} />
            </div>
        </div>
    );
}

export default VistaTableros;
