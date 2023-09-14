import httpInstance from "./instanceHTTP";

async function crearTarjeta(accessToken, tituloTarjeta, listaId, descripcionTarjeta) {
  try {
    const response = await httpInstance.post(
      '/api/tarjeta/',
      {
        titulo_tarjeta: tituloTarjeta,
        lista_relacionada: listaId,
        descripcion_tarjeta: descripcionTarjeta,
      },
      {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      }
    );

    if (response.status === 201) {
      return response.data;
    } else {
      throw new Error('Error al crear la tarjeta');
    }
  } catch (error) {
    throw error;
  }
}

async function obtenerTarjeta(accessToken, tarjetaId) {
  try {
    const response = await httpInstance.get(`/api/tarjeta/${tarjetaId}/`, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });
    return response.data;
  } catch (error) {
    throw error;
  }
}

async function editarTarjeta(accessToken, tarjetaId, tituloTarjeta, listaId, descripcionTarjeta) {
  try {
    const response = await httpInstance.put(
      `/api/tarjeta/${tarjetaId}/`,
      {
        titulo_tarjeta: tituloTarjeta,
        lista_relacionada: listaId,
        descripcion_tarjeta: descripcionTarjeta,
      },
      {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      }
    );

    if (response.status === 200) {
      return response.data;
    } else {
      throw new Error('Error al editar la tarjeta');
    }
  } catch (error) {
    throw error;
  }
}

async function eliminarTarjeta(accessToken, tarjetaId) {
  try {
    const response = await httpInstance.delete(`/api/tarjeta/${tarjetaId}/`, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });

    if (response.status === 204) {
      return true; // Éxito en la eliminación
    } else {
      throw new Error('Error al eliminar la tarjeta');
    }
  } catch (error) {
    throw error;
  }
}

const tarjetaService = {
  crearTarjeta,
  obtenerTarjeta,
  editarTarjeta,
  eliminarTarjeta,
};

export default tarjetaService;
