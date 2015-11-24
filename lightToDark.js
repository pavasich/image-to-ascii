window.onload = function() {
  var lightToDark = [
  '.',
  "'",
  'l',
  'I',
  'o',
  'e',
  'm',
  '&',
  '@',
  '#',
  'M'
  ]

  // for(var i = 0; i < lightToDark.length; i++) {
  //   s = '';
  //   for (var j = 0; j < 10; j++) {
  //     for (var x = 0; x < 10; x++)
  //       s += lightToDark[i]
  //     s += "\n"
  //   }
  //
  //   console.log(s);
  // }

  var image = new Image();
  image.src = '/home/pavasich/Downloads/me.png'+'?'+new Date().getTime();
  image.setAttribute('crossOrigin', 'anonymous');
  var canvas = document.getElementById('canvas');
  var cxt = canvas.getContext('2d');
  image.onload = function() {
    canvas.width = image.width;
    canvas.height = image.height;
    cxt.drawImage(image, 0, 0);
    var data = cxt.getImageData(0,0, image.width, image.height)
    console.log(data)
  }
}
