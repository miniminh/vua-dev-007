import Container from '@mui/material/Container'
import MainPage from './pages/MainPage/MainPage'
import ClonePage from './pages/ClonePage/ClonePage'
import { FaCrown } from "react-icons/fa";
function App() {
  return (
    <div style={{background: 'linear-gradient(132deg, rgba(215,30,235,1) 0%, rgba(29,9,121,1) 64%, rgba(255,255,255,1) 100%)', height: '100%', minHeight: '100vh'}}>
      <header style={{ backgroundColor: '#333', padding: '12px 20px', display: 'flex', justifyContent:'center', alignItems: 'center' }}>
        <FaCrown style={{fontSize: '32px', marginRight: '12px', color: 'yellow'}} />
        <span style={{fontFamily: '"Roboto","Helvetica","Arial","sans-serif"', fontSize: '24px', fontWeight: '700', color: '#fff'}}>
          VUA DEV 007
        </span>
        <FaCrown style={{fontSize: '32px', marginLeft: '10px', color: 'yellow'}}  />
      </header>
      <ClonePage />
    </div>
  )
}

export default App
