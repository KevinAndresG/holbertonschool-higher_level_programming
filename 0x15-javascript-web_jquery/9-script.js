
$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    for (i in data) {
      if (i === 'hello') {
        $('#hello').append(data[i]);
      }
    }
  });
});
