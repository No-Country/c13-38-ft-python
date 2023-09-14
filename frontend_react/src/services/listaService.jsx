import httpInstance from "./instanceHTTP";

async function crearLista(accessToken, nombreLista, tableroId) {
  try {
    const response = await httpInstance.post(
      '/api/lista/',
      { nombre_lista: nombreLista, tablero_relacionado: tableroId },
      {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      }
    );

    if (response.status === 201) {
      return response.data;
    } else {
      throw new Error('Error al crear la lista');
    }
  } catch (error) {
    throw error;
  }
}

async function editarLista(accessToken, listaId, nuevoNombre) {
  try {
    const response = await httpInstance.put(
      `/api/lista/${listaId}/`,
      { nombre_lista: nuevoNombre },
      {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      }
    );

    if (response.status === 200) {
      return response.data;
    } else {
      throw new Error('Error al editar la lista');
    }
  } catch (error) {
    throw error;
  }
}

async function eliminarLista(accessToken, listaId) {
  try {
    const response = await httpInstance.delete(`/api/lista/${listaId}/`, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });

    if (response.status === 204) {
      return true; // Éxito en la eliminación
    } else {
      throw new Error('Error al eliminar la lista');
    }
  } catch (error) {
    throw error;
  }
}

const listaService = {
  crearLista,
  editarLista,
  eliminarLista,
};

export default listaService;
