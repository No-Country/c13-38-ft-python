import { useNavigate } from 'react-router-dom';
import iconoEliminar from "../../assets/img/eliminar.svg"
import espaciosService from "../../services/espaciosService";

function CardEspacio({ title, espacioId, onDelete }) {
  const navigate = useNavigate();

  const handleDelete = async () => {
    
    onDelete(espacioId);
  };

  const handleClick = () => {
    navigate(`/espacios/${espacioId}`);
  };
  


  return (
    <div className="cursor-pointer bg-gray-100 h-28 p-3 bg-neutral-200 rounded-lg border-l border-r border-b border-solid border-white flex flex-col">
      <div className="flex justify-end cursor-pointer w-4" onClick={handleDelete}>
        <img className="text-center" src={iconoEliminar} alt="Cerrar" />
      </div>
      <div className="flex-grow flex justify-center items-center" onClick={handleClick}>
        <h3 className="font-semibold text-sm">{title}</h3>
      </div>
    </div>
  );
}

export default CardEspacio;