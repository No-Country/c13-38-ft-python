import { useNavigate } from 'react-router-dom';
import CardNewProject from "../components/CardNewProject"
import iconoAgregar from "../assets/img/mas.svg"
import iconoPM from "../assets/img/trello.svg"
import flecha from "../assets/img/flechaAtras.png"
import { useParams } from 'react-router-dom';

function CreateNewProject() {
    const { espacioId } = useParams();
    console.log(espacioId)
    const navigate = useNavigate();

    const goBack = () => {
        navigate(-1);
    };

    const handleCardClick = () => {
        navigate(`/new`);
      };


    return (
        <>

            <div className="h-screen flex flex-col justify-center items-center m-auto">
                <div className="cursor-pointer absolute top-0 left-0 m-4" onClick={goBack}>
                    <img src={flecha} alt="Flecha hacia atrás" className="w-8 h-8 mb-4" />
                </div>

                <h1 className="text-xl font-bold mb-4">Crear un tablero</h1>
                <p className=" mb-8">¿Como quieres empezar?</p>

                <div className="flex justify-around space-x-4">
                    <CardNewProject img={iconoAgregar} title="Tablero en blanco" subtitle="Empezar desde cero" borde="border-dashed" onClick={handleCardClick} />
                    <CardNewProject img={iconoPM} title="Usar una plantilla" subtitle="Desde plantilla" />
                </div>

            </div>

        </>
    )
}

export default CreateNewProject