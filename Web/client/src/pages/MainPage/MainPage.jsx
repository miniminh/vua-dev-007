import DisplayProducts from '../../components/DisplayProducts/DisplayProducts'
import Box from '@mui/material/Box'
function MainPage() {
  return (
    <Box sx = {{ display: 'flex', alignItems: 'center', overflowX: 'hidden', overflowY: 'auto' }}>
      <DisplayProducts />
    </Box>
  )
}

export default MainPage