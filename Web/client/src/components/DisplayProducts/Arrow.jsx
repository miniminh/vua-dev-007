import ArrowForwardIcon from '@mui/icons-material/ArrowForward'
import ArrowBackIcon from '@mui/icons-material/ArrowBack'

const Arrow = ({ className, onClick, icon: Icon, marginLeft = 0 }) => {
  const handleArrowClick = (e) => {
    e.stopPropagation()
    onClick(e)
  }
  return (
    <Icon
      className={className}
      aria-label="previous"
      onClick={handleArrowClick}
      sx={{
        marginLeft: `${marginLeft}px`,
        position: 'absolute',
        zIndex: 1,
        top: '50%',
        right: 0,
        transform: 'translateY(-50%)',
        cursor: 'pointer',
        color: '#CCCCCC',
        borderRadius: '50%',
        backgroundColor: 'black',
        '&:hover': {
          backgroundColor: 'white',
          color: '#CCCCCC'
        },
        boxShadow: `${marginLeft !== 0 ? '-' : ''}3px 0px 5px rgba(0, 0, 0, 0.3)`,
        fontSize: '15px'
      }}
    />
  )
}

const SampleNextArrow = (props) => (
  <Arrow {...props} icon={ArrowForwardIcon} />
)

const SamplePrevArrow = (props) => (
  <Arrow {...props} icon={ArrowBackIcon} marginLeft={25} />
)

export { SampleNextArrow, SamplePrevArrow }
