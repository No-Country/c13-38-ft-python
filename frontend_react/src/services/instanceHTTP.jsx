import axios from 'axios';

const API_BASE_URL = 'http://eduardovega04.pythonanywhere.com';
const axiosInstance = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});


export async function sendRequest(config) {
    try {
      const response = await axiosInstance(config);
      return response.data;
    } catch (error) {
      throw error;
    }
  }
  
export default axiosInstance;