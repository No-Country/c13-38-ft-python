import httpInstance from "./instanceHTTP"

async function getEspacios(accessToken) {
  try {
    const response = await httpInstance.get(`/api/espacio/`, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

async function createEspacio(nombreEspacio, accessToken) {
  try {
    const response = await httpInstance.post(
      '/api/espacio/',
      { nombre_espacio: nombreEspacio },
      {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      }
    );

    if (response.status === 201) {
      return response.data;
    } else {
      throw new Error('Error al crear el espacio');
    }
  } catch (error) {
    throw error;
  }
}



async function getEspacioDetallado(accessToken, espacioId) {
  try {
    const response = await httpInstance.get(`/api/espacio/${espacioId}/`, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });
    console.log(response.data)
    console.log(response)
    return response.data;
  } catch (error) {
    throw error;
  }
}


// Este se tendra para revision de si se llegase a poder o no
async function editarEspacio(accessToken, espacioId, nuevoNombre) {
  try {
    const response = await httpInstance.put(`/api/espacio/${espacioId}/`, {
      nombre_espacio: nuevoNombre,
    }, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });

    if (response.status === 200) {
      return response.data;
    } else {
      throw new Error('Error al editar el espacio');
    }
  } catch (error) {
    throw error;
  }
}

async function eliminarEspacio(accessToken, espacioId) {
  try {
    const response = await httpInstance.delete(`/api/espacio/${espacioId}/`, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });

    if (response.status === 204) {
      return true; // Éxito en la eliminación
    } else {
      throw new Error('Error al eliminar el espacio');
    }
  } catch (error) {
    throw error;
  }
}

const espaciosService = {
  getEspacios,
  createEspacio,
  getEspacioDetallado,
  editarEspacio,
  eliminarEspacio,
};

export default espaciosService;
