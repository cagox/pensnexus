

function LoginMenu(){


    return(
        <>
            <div className="basis-auto mt-3"><input name="userid" id="userid" placeholder="User ID"></input></div>
            <div className="basis-3"></div>
            <div className="basis-auto mt-3"><input name="password" id="password" placeholder="Password"></input></div>
            <div className="basis-3"></div>
            <div className="basis-auto"><button id="loginbutton" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full">Login</button></div>
        </>
    )

}

export default LoginMenu