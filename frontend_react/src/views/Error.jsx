// Funcionando correctamente--------------------------------------------------

import { useNavigate } from 'react-router-dom';
function Error() {

    const navigate = useNavigate();

    const handleGoBackHome = () => {
        navigate('/home');
    };

    return (
        <main class="grid min-h-full place-items-center px-6 py-24 sm:py-32 lg:px-8 bg-principal">
            <div class="text-center">
                <p class="text-base font-semibold text-gray-50">404</p>
                <h1 class="mt-4 text-3xl font-bold tracking-tight text-gray-50 sm:text-5xl">Página no encontrada</h1>
                <p class="mt-6 text-base leading-7 text-gray-50">Lo siento, no pudimos encontrar la página que estás buscando.</p>
                <div class="mt-10 flex items-center justify-center gap-x-6">
                    <button
                        onClick={handleGoBackHome}
                        className="rounded-md bg-secundario px-3.5 py-2.5 text-sm font-semibold shadow-sm hover:bg-tercero focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
                        Volver al Inicio
                    </button>
                </div>
            </div>
        </main>
    );
}

export default Error;