

function Tablero({tableroInfo} ){
    return(
        <>
        <div className=" bg-red-100 "  style={{ width: 300}}>
            <h1>{tableroInfo.nombre_tablero}</h1>
        </div>
        </>
    )
}

export default Tablero;