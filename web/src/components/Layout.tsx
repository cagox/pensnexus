import { Outlet } from "react-router-dom";

import PageFooter from "./PageFooter"
import PageHeader from "./PageHeader"

function Layout() {

    return (
        <div className="container mx-auto rounded-lg" id="appContainer">
          <div className="grid">
            <PageHeader />
            <div className="min-h-96" id="contentArea"><Outlet /></div>
            <PageFooter />
          </div>
        </div>
      )

}

export default Layout