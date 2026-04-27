
function PageFooter() {
    return(
        <div className="flex flex-row ">
            <div className="basis-10 bg-red-500"></div>
            <div className="basis-3/12 p-5">
                <div>Created By Cagox</div>
                <div><a href="https://react.dev/">Powered By React</a></div>
                <div><a href="https://www.typescriptlang.org/">Powered By TypeScript</a></div>
                <div><a href="https://tailwindcss.com/">Styled With Tailwind</a></div>
                <div><a href="https://github.com/cagox/FictionSite">See on GitHub</a></div>
            </div>
            <div className="basis-full bg-red-500"></div> {/* Spacer */}
            <div className="basis-3/12 p-5">
                <div>About</div>
                <div>Contact Us</div>
                <div>Help</div>
            </div>
            <div className="basis-10 bg-red-500"></div>
        </div>
    ) /* The red blocks are there to make the space holders visible while I design the page.*/
}

export default PageFooter