$(document).ready(function () {
  const newUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  $.get(newUrl, function (data) {
    $('#hello').text(data.hello);
  });
});
