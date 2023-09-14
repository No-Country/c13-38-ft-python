function CardNewProject(props) {
    const { title, subtitle, img , borde , onClick} = props;
    return (
        <>
            <a href="#" class="flex flex-col justify-center items-center block  w-1/2 py-6 px-8 bg-white rounded-lg  hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700   transform transition-transform hover:scale-105  hover:translate-y-2" onClick={onClick}>


                <div className={`flex justify-center border-2 ${borde} border-gray-400 rounded-lg w-36 h-36`}>
                    <img className="w-12 " src={img} alt="" />
                </div>


                <h5 class="mt-4 mb-2 text-sm font-bold tracking-tight text-gray-900 dark:text-white">{title}</h5>
                <p class="font-normal text-sm text-gray-700 dark:text-gray-400">{subtitle}</p>
            </a>
        </>
    )
}

export default CardNewProject