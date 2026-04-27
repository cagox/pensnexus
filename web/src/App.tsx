import { Routes, Route } from "react-router-dom"
import Layout from "./components/Layout.tsx"
import FrontPage from "./components/FrontPage.tsx"



function App() {

  return (
  <Routes>
    <Route element={<Layout />}>
      <Route index element={<FrontPage />} />
    </Route>
  </Routes>
  )
}

export default App
