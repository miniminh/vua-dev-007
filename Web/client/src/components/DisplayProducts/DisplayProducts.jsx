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
    <Box sx={{ flexGrow: 1, width: '100%', paddingRight: 2, paddingLeft: 4 }}>
      <Typography variant="body1" color="black" sx={{ fontSize: '28px', marginBottom: '24px', fontWeight: '700' }}>
        Sản phẩm gợi ý:
      </Typography>

      <Grid container spacing={1} columns={{ xs: 4, sm: 8, md: 12 }}>
        {data.map((item) => (
          <Grid item xs={2} sm={4} md={4} lg = {3} key={item.name}>
            <Card sx={{
              maxWidth: 335,
              border: 'none',
              boxShadow: 'none',
              '&:hover': {
                outline: '2px solid black'
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
                        height="350"
                        width = "350"
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
          </Grid>
        ))}
      </Grid>
    </Box>
  )
}

export default DisplayProducts