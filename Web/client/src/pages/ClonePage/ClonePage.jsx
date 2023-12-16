// ImageUploadComponent.js
import { useState } from 'react'
import { Button, CircularProgress, Box } from '@mui/material'
import axios from 'axios'
import DisplayProducts from '../../components/DisplayProducts/DisplayProducts'

const ImageUploadComponent = () => {
  const [selectedFile, setSelectedFile] = useState(null)
  const [uploading, setUploading] = useState(false)
  const [imageData, setImageData] = useState(null)
  const [previewUrl, setPreviewUrl] = useState(null)

  const handleFileChange = (event) => {
    const file = event.target.files[0]
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
        const response = await axios.post('http://10.124.3.196:5050/test', formData, {
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
    <div>
      {!imageData ? (
        <Box
          sx={{
            background: 'rgba(255, 255, 255, 0.25)',
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
            width: 'fit-content',
            marginLeft: 'auto',
            marginRight: 'auto'
          }}
        >
          <input type="file" onChange={handleFileChange} />
          {previewUrl && (
            <img
              src={previewUrl}
              alt="Preview"
              style={{
                width: '230px',
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
            {uploading ? <CircularProgress size={24} /> : 'Upload'}
          </Button>
        </Box>
      ) : (
        <DisplayProducts data={imageData.data} />
      )}
    </div>
  )
}

export default ImageUploadComponent
