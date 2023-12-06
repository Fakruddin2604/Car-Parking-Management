// import Card from '@mui/material/Card';
// import CardContent from '@mui/material/CardContent';
// import CardMedia from '@mui/material/CardMedia';
// import Typography from '@mui/material/Typography';
// import CardHeader from '@mui/material/CardHeader';
// import { CardActionArea } from '@mui/material';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import image1 from "./images/1.jpg";
import image2 from "./images/2.jpg"
import image3 from "./images/3.jpg"
import image4 from "./images/4.jpg"
import image5 from "./images/5.jpg"
import image6 from "./images/6.jpg"
import image7 from "./images/7.jpg"
import image8 from "./images/8.jpg"
import image9 from "./images/9.jpg"
import image10 from "./images/10.jpg"
export default function HOME(){
  const [stringToSend, setStringToSend] = useState('');
  const [stringFromServer, setStringFromServer] = useState('');

  const sendStringToServer = async () => {
    try {
      // Send the string to the Flask server using Axios
      const response = await axios.post('http://localhost:5000/process-string', { string: stringToSend });
      // Get the processed string from the Flask server
      setStringFromServer(response.data.processed_string);
    } catch (error) {
      alert('Error sending data to server:', error);
    }
  };

    const handleImageClick = (event) => {
        const baseString = event.target.src;
    const fileName = baseString.split('/').pop();
    const actualFileName = `${fileName.split('.')[0]}.jpg`;
    // alert(actualFileName);
    setStringToSend(actualFileName);
    sendStringToServer();
}



    return (<>
    <div className="w3-card w3-responsive">
      <h1 className="w3-center">Car Number Detector </h1>
      <table className="w3-table-all w3-center">
        <tr>
          <td><img  onClick={handleImageClick} height="175px" width="300px" src={image1} alt="image1" /></td>
          <td><img  onClick={handleImageClick} height="175px" width="300px" src={image2} alt="image2" /></td>
          <td><img  onClick={handleImageClick} height="175px" width="300px" src={image3} alt="image3" /></td>
          <td><img  onClick={handleImageClick} height="175px" width="300px"  src={image4} alt="image4"/></td>
          <td><img  onClick={handleImageClick} height="175px" width="300px"  src={image5} alt="image5"/></td>
        </tr>
        <tr>
          <td><img  onClick={handleImageClick} height="175px" width="300px"  src={image6} alt="image6"/></td>
          <td><img  onClick={handleImageClick} height="175px" width="300px"  src={image7} alt="image7"/></td>
          <td><img  onClick={handleImageClick} height="175px" width="300px"  src={image8} alt="image8"/></td>
          <td><img  onClick={handleImageClick} height="175px" width="300px"  src={image9} alt="image9"/></td>
          <td><img  onClick={handleImageClick} height="175px" width="300px" src={image10} alt="image10"/></td>
        </tr>
      </table>
      <div>
      <p>Processed string from server: {stringFromServer}</p>
    </div>
    </div>
    </>)

}