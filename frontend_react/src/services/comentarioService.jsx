import httpInstance from "./instanceHTTP";

async function crearComentario(accessToken, tarjetaId, textoComentario) {
  try {
    const response = await httpInstance.post(
      '/api/comentario/',
      {
        tarjeta_relacionada: tarjetaId,
        texto_comentario: textoComentario,
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
      throw new Error('Error al crear el comentario');
    }
  } catch (error) {
    throw error;
  }
}

async function crearRespuesta(accessToken, comentarioId, textoRespuesta) {
  try {
    const response = await httpInstance.post(
      '/api/respuesta/',
      {
        comentario_relacionado: comentarioId,
        texto_respuesta: textoRespuesta,
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
      throw new Error('Error al crear la respuesta');
    }
  } catch (error) {
    throw error;
  }
}

const comentarioService = {
  crearComentario,
  crearRespuesta,
};

export default comentarioService;
