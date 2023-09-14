

import httpInstance from "./instanceHTTP"


async function registerUser(username, email, password) {
  try {
    const response = await httpInstance.post('/api/registro/', {
      username,
      email,
      password,
    });

    if (response.data) {
      return { success: true, data: response.data };
    } else {
      throw new Error(response.data.error_message);
    }
  } catch (error) {
    throw new Error("Error al registrar:" ,error.message);
  }
}


async function login(username, password) {
  try {
    const response = await httpInstance.post('/api/token/', {
      username,
      password,
    });

    if (!response.data.access) {
      throw new Error('Credenciales incorrectas');
    }

    localStorage.setItem('accessToken', response.data.access);
    localStorage.setItem('refreshToken', response.data.refresh);
    localStorage.setItem('username', username);

    return response.data;
  } catch (error) {
    throw error;
  }
}



function logout() {
  localStorage.removeItem('accessToken');
  localStorage.removeItem('refreshToken');
  localStorage.removeItem('username');
}

const authService = {
  registerUser,
  login,
  logout,
};

export default authService;


