// funcionando correctamente

import icono from "../assets/img/logoVertical.png"
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import authService from "../services/authService";

import Notification from '../components/Notification';

function Register() {

    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);

    const [registroExitoso, setRegistroExitoso] = useState(false);

    const navigate = useNavigate();


    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await authService.registerUser(username, email, password);
            console.log(response)
            if (response.success) {
                console.log('Registro exitoso');
                navigate('/');
            } else {
                console.error('Error en el registro:', response.error);
                setError(response.error);
            }
        } catch (error) {
            console.error('Error al registrar:', error.message);
            setError('Error al registrar');
        }
    };

    const irLogin = () => {
        navigate('/');
    };

    return (
        <div class="h-screen w-screen flex items-center justify-center bg-principal">

            <div class="w-64 h-64 bg-gradient-to-b rounded-full from-blue-500 to-black absolute z-0" style={{ left: 200, top: 15 }}>
            </div>


            <div class="w-44 h-44 bg-gradient-to-b from-blue-500 to-black absolute rounded-full z-0" style={{ right: 280, top: 400 }}>
            </div>

            <div class="flex rounded-xl border px-12  bg-black bg-opacity-10" style={{ height: 400, width: 700, backdropFilter: 'blur(20px)' }}>

                <div class="mx-auto my-auto px-6" style={{ width: 200 }}>
                    <img src={icono} alt="icono" />
                </div>

                <div class="flex min-h-full flex-col justify-center pr-6 py-4 lg:px-10" style={{ width: 350 }}>
                    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
                        <h1 class="mt-10 text-xl font-bold leading-9 tracking-tight text-gray-50">Registrate</h1>
                    </div>

                    <div class="sm:mx-auto sm:w-full sm:max-w-sm ">

                        <form class="space-y-4" action="#" method="POST" onSubmit={handleSubmit}>
                            <div>
                                <div class="mt-2">
                                    <input id="username" name="username" type="username" autocomplete="username" required class="block w-full rounded-md border-0 px-2 py-1.5 text-gray-50 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 bg-black bg-opacity-10" placeholder="Usuario" value={username}
                                        onChange={(e) => setUsername(e.target.value)}
                                    />
                                </div>
                            </div>

                            <div>
                                <div class="mt-2">
                                    <input id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 px-2 py-1.5 text-gray-50 shadow-sm ring-1 ring-inset ring-gray-300 placeholder text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 bg-black bg-opacity-10" placeholder="Correo Electronico" value={email}
                                        onChange={(e) => setEmail(e.target.value)} />
                                </div>
                            </div>

                            <div>
                                <div class="mt-2">
                                    <input id="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 px-2 py-1.5 text-gray-50 shadow-sm ring-1 ring-inset ring-gray-300 placeholder text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 bg-black bg-opacity-10" placeholder="Contraseña" value={password}
                                        onChange={(e) => setPassword(e.target.value)} />
                                </div>
                            </div>

                            {registroExitoso && (
                                <Notification type="success" message="Usuario creado con éxito" />
                            )}
                            {error && <Notification type="error" message={error} />}



                            <div>
                                <button type="submit" class="flex w-full justify-center rounded-md bg-acentuacion px-3 py-1.5 font-md leading-6 text-gray-50 shadow-sm hover:bg-tercero focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Registrar</button>
                            </div>
                        </form>

                        <p class="mt-7 mb-7 text-center text-sm text-gray-50">
                            Ya tienes cuenta?
                            <a href="#" class="font-semibold leading-6 text-acentuacion hover:text-indigo-500" onClick={irLogin}> Iniciar sesion</a>
                        </p>
                    </div>
                </div>



            </div>
        </div>

    );
}

export default Register;
