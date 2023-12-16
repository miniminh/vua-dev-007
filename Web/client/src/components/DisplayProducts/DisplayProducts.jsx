import Box from '@mui/material/Box'
import CardActionArea from '@mui/material/CardActionArea'
import Grid from '@mui/material/Grid'
import Card from '@mui/material/Card'
import CardContent from '@mui/material/CardContent'
import CardMedia from '@mui/material/CardMedia'
import Typography from '@mui/material/Typography'
import Slider from 'react-slick'
import { SampleNextArrow, SamplePrevArrow } from './Arrow'
import 'slick-carousel/slick/slick.css'
import 'slick-carousel/slick/slick-theme.css'

function DisplayProducts({ data }) {
  const setting = {
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    nextArrow: <SampleNextArrow />,
    prevArrow: <SamplePrevArrow />
  }

  return (
    <div style={{ width: '100%'}}>
      <div style={{ paddingTop: '24px', display: 'flex', justifyContent: 'center', width: '100%', flexWrap: 'wrap'}}>
        {data.map((item) => (
            <Card sx={{
              maxWidth: 250,
              border: 'none',
              marginRight: '24px',
              marginBottom: '24px',
              boxShadow: 'none',
              '&:hover': {
                transform: 'scale(1.1)'
              }
            }}
            onClick = {() => {window.location.href = item.url}}
            >
              <CardActionArea sx ={{ transition: 'none', backgroundColor: '#c9c9c9'}} >
                <Box>
                  <Slider {...setting}>
                    {item.images.map((img, index) => (
                      <CardMedia key = {index}
                        component="img"
                        height="250"
                        width = "250"
                        image= {img}
                        alt={item.name}
                      />
                    ))}
                  </Slider>
                </Box>
                <CardContent>
                  <Typography gutterBottom variant="body1" component="div" sx = {{ fontSize: '18px', textTransform: 'none', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', fontWeight: '700' }}>
                    {item.name}
                  </Typography>
                  <Typography variant="body1" color="#333" sx={{fontSize: '14px', fontWeight: '600'}}>
                    {item.price} {item.currency}
                  </Typography>
                </CardContent>
              </CardActionArea>
            </Card>
        ))}
      </div>
    </div>
  )
}

export default DisplayProducts