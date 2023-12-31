// ImageUploadComponent.js
import { useState } from 'react'
import { Button, CircularProgress, Box } from '@mui/material'
import axios from 'axios'
import DisplayProducts from '../../components/DisplayProducts/DisplayProducts'
import { MuiFileInput } from 'mui-file-input'

const ImageUploadComponent = () => {
  const [selectedFile, setSelectedFile] = useState(null)
  const [uploading, setUploading] = useState(false)
  const [imageData, setImageData] = useState(null)
  const [previewUrl, setPreviewUrl] = useState(null)

  const handleFileChange = (file) => {
    console.log(file)
    setSelectedFile(file)

    const reader = new FileReader()
    reader.onload = () => {
      // Set the preview URL when the file is loaded
      setPreviewUrl(reader.result)
    }

    if (file) {
      reader.readAsDataURL(file)
    }
  }

  const handleUpload = async () => {
    if (selectedFile) {
      const formData = new FormData()
      formData.append('input', selectedFile)
      setUploading(true)
      try {
        const response = await axios.post('http://localhost:5050/suggest', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        setImageData(response.data) // Set received data to state for display
        console.log(response)
      } catch (error) {
        console.error('Error uploading image: ', error)
      } finally {
        setUploading(false)
      }
    }
  }

  return (
    <div style={{width: '100%', margin: '0 auto'}}>
      {!imageData ? (
        <Box
          sx={{
            background: 'rgba(255, 255, 255, 0.4)',
            boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.37)',
            backdropFilter: 'blur(3px)',
            WebkitBackdropFilter: 'blur(3px)',
            borderRadius: '10px',
            border: '1px solid rgba(255, 255, 255, 0.18)',
            padding: '20px',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            marginTop: '24px',
            width: '100%',
            maxWidth: '350px',
            marginLeft: 'auto',
            marginRight: 'auto'
          }}
        >
          <div style={{fontFamily: '"Roboto","Helvetica","Arial","sans-serif"', fontSize: '24px', marginBottom: '20px', fontWeight: '700', color: '#fff'}}>Vua Style</div>
          <MuiFileInput placeholder="Nhấp vào để thêm ảnh" value={selectedFile} onChange={handleFileChange} />
          {previewUrl && (
            <img
              src={previewUrl}
              alt="Preview"
              style={{
                width: '200px',
                height: 'auto',
                marginTop: '20px',
                borderRadius: '10px',
                boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.37)',
              }}
            />
          )}
          <Button
            variant="contained"
            color="primary"
            onClick={handleUpload}
            disabled={uploading || !selectedFile}
            sx={{ marginTop: '20px' }}
          >
            {uploading ? <CircularProgress size={24} /> : 'Nhận gợi ý'}
          </Button>
        </Box>
      ) : (
        <DisplayProducts data={imageData.data} />
      )}
    </div>
  )
}

export default ImageUploadComponent
