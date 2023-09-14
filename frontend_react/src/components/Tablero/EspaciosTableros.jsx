

import React, { useState, useEffect } from 'react';
import tableroService from "../../services/tableroService";
import CardTablero from "./CardTablero";

function EspaciosTableros({espacioId}) {
  const [tableros, setTableros] = useState([]);

  useEffect(() => {
    async function fetchTableros() {
      try {
        const accessToken = localStorage.getItem('accessToken');
        if (!accessToken) {
          throw new Error('Token de acceso no encontrado en localStorage');
        }

        const tablerosData = await tableroService.getTableros(accessToken);
        setTableros(tablerosData);
      } catch (error) {
        console.error('Error al obtener tableros:', error.message);
      }
    }

    fetchTableros();
  }, []);

  return (
    <div className="grid grid-cols-5 gap-4 my-4 px-8 py-2">
      <CardTablero/>
      {tableros.map((tablero) => (
        <CardTablero key={tablero.id} title={tablero.nombre_tablero} id={tablero.id} espacioId={espacioId}/>
      ))}
    </div>
  );
}

export default EspaciosTableros;
