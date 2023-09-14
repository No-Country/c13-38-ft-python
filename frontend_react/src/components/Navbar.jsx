import menu from "../assets/img/menu-puntos.svg"
import estrella from "../assets/img/estrella.svg"
import usuarios from "../assets/img/agregar-usuario.svg"
import usuario from "../assets/img/usuarios.svg"

function Navbar() {
    return (
        <nav class="bg-gray-200">
            <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
                <div class="relative flex h-16 items-center justify-between">
                    <div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
                        <div class="flex flex-shrink-0 items-center">
                            <h2 class=" rounded-md px-3 py-2 text-sm font-medium"> Nombre tablero </h2>
                        </div>


                        <div class="hidden sm:ml-6 sm:block">
                            <button type="button" class="relative flex rounded-full  text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800" id="user-menu-button" aria-expanded="false" aria-haspopup="true">
                                <img class="h-4 w-4 rounded-full" src={estrella} alt="" />
                            </button>
                        </div>

                        <div class="hidden sm:ml-6 sm:block">
                            <button type="button" class="relative flex rounded-full  text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800" id="user-menu-button" aria-expanded="false" aria-haspopup="true">
                                <img class="h-4 w-4 mx-2" src={usuario} alt="" />
                                <p>Visible para el espacio de trabajo</p>
                            </button>
                        </div>
                    </div>


                    <div class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
                        <button type="button" class="relative flex rounded-full  text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800 bg-principal" id="user-menu-button" aria-expanded="false" aria-haspopup="true">
                            <img class="h-4 w-4 mx-2" src={usuarios} alt="" />
                            <p>Compartir</p>
                        </button>


                        <div class="relative ml-3">
                            <div>
                                <button type="button" class="relative flex rounded-full  text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800" id="user-menu-button" aria-expanded="false" aria-haspopup="true">
                                    <img class="h-5 w-5 rounded-full" src={menu} alt="" />
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>


        </nav>
    );
}

export default Navbar;