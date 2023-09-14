import React, { useState, useEffect } from 'react';
import espaciosService from "../../services/espaciosService";

import CardEspacio from "../Espacios/CardEspacio"
import iconoSincronziar from "../../assets/img/sincronizar.png"


function EspaciosTrabajo() {

  const [espacios, setEspacios] = useState([]);

  

  useEffect(() => {
    async function fetchEspacios() {
      try {
        const accessToken = localStorage.getItem('accessToken');
        if (!accessToken) {
          throw new Error('Token de acceso no encontrado en localStorage');
        }
        const espaciosData = await espaciosService.getEspacios(accessToken);
        setEspacios(espaciosData);
      } catch (error) {
        console.error('Error al obtener espacios:', error.message);
      }
    }

    fetchEspacios();
  }, []);



  const eliminarEspacio = async (espacioId) => {
    try {
      const accessToken = localStorage.getItem('accessToken');
      if (!accessToken) {
        throw new Error('Token de acceso no encontrado en localStorage');
      }
  
      // Llama a la función eliminarEspacio del servicio
      await espaciosService.eliminarEspacio(accessToken, espacioId);
  
      // Actualiza el estado local eliminando el espacio de trabajo de la lista espacios
      setEspacios((prevEspacios) => prevEspacios.filter((espacio) => espacio.id !== espacioId));
    } catch (error) {
      console.error('Error al eliminar el espacio de trabajo:', error.message);
    }
  };
  


  return (
    <>

      <div className="flex items-center ml-10 ">
        <img className="w-4 mr-2" src={iconoSincronziar} alt="" />
        <h2 className="text-left">Espacios de trabajo de usuarios</h2>
      </div>

      <div className="grid grid-cols-5 gap-4 my-4 px-8 py-2">
      {espacios.length > 0 ? (
    espacios.map((espacio) => (
      <CardEspacio key={espacio.id} espacioId={espacio.id} title={espacio.nombre_espacio} onDelete={eliminarEspacio} />
      
    ))
  ) : (
    <p className='text-center'>No tienes espacios de trabajo.</p>
  )}
      </div>

      <p className="text-left ml-10">Ver todos los tableros cerrados</p>
    </>
  )
}

export default EspaciosTrabajo;