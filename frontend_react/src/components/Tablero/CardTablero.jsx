
import { useNavigate } from 'react-router-dom';

function CardTablero({ title = "¿Desea crear un nuevo tablero?", id, espacioId  }) {
    const navigate = useNavigate();

    const handleClick = () => {
        if (id !== undefined && id !== null) {
            navigate(`/tablero/${id}`);
        } else {
            navigate('/create');
        }
    };

    return (
        <div className="cursor-pointer flex bg-gray-100 h-28 p-3 bg-neutral-200 rounded-lg border-l border-r border-b border-solid border-white justify-center items-center" onClick={handleClick}>
            <h3 className="text-center font-semibold text-sm">{title}</h3>
        </div>
    );
}

export default CardTablero;

