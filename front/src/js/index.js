function sendImage() {
  img = document.getElementById('image').files[0]
  var reader  = new FileReader()
  reader.readAsDataURL(img)
  reader.addEventListener('load', () => {
    postRequest('/image_editor', {img: reader.result})
  }, false);
}

function getRequest(url) {
  axios.get(url)
    .then(function(response) {
      console.log('Requested data: ', response.data)
    })
    .catch(function(error) {
      console.log('Error: ', error);
    });
}

function postRequest(url, params) {
  axios.post(url, params)
    .then(function(response) {
      console.log('Requested data: ', response.data)
      drawImage('data:image/png;base64,' + response.data)
    })
    .catch(function(error) {
      console.log('Error: ', error);
    });
}

function drawImage(src) {
  document.getElementById('previewImage').src = src
}

function legendClick() {
  var display = document.getElementById('s-img-close').style.display
  if (display === 'none' || display === '') {
    document.getElementById('s-img-menu').style.display = 'none'
    document.getElementById('s-img-close').style.display = 'initial'
    document.getElementById('s-side-menu').style.marginLeft = '0'
    document.getElementById('s-legend').style.backgroundColor = '#218c86'
  } else {
    document.getElementById('s-img-close').style.display = 'none'
    document.getElementById('s-img-menu').style.display = 'initial'
    document.getElementById('s-side-menu').style.marginLeft = '-71%'
    document.getElementById('s-legend').style.backgroundColor = 'lightseagreen'
  }
}
