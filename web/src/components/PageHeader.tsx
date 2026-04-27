/* import UserButton from "./UserButton" */
import MenuButton from "./MenuButton"
import SearchButton from "./SearchButton"
import LoginMenu from "./LoginMenu"


function PageHeader() {
    return(
        <div className="flex flex-row">
            <div className="basis-auto"><MenuButton /></div>
            <div className="basis-2/12"></div>
            <div className="basis-full"><input type="text" className="size-full h-auto my-1 rounded-full border text-lg pl-3" id="searchText" placeholder="Search Here"></input></div>
            <div className="basis-auto"><SearchButton /></div>
            <div className="basis-2/12"></div>
            <LoginMenu />
        </div>
    )
}

export default PageHeader