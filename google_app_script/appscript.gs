function doGet(e) {
  var image = e.parameter.image;
  var pythonScriptUrl = 'https://script.google.com/macros/d/{SCRIPT_ID}/exec';
  var options = {
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "payload": JSON.stringify({ "image": image })
  };
  UrlFetchApp.fetch(pythonScriptUrl, options);
}