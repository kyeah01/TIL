# Use Google Translater by Node.js

## Installation

```bash
$ npm install google-translate --save
```

(package.json으로 받았다면 불필요)



## Usage Overview

```js
var googleTranslate = require('google-translate')(apiKey);

googleTranslate.translate('My name is Brandon', 'es', function(err, translation) {
  console.log(translation.translatedText);
  // =>  Mi nombre es Brandon
});

googleTranslate.detectLanguage('Gracias', function(err, detection) {
  console.log(detection.language);
  // =>  es
});
```





>[출처](https://www.npmjs.com/package/google-translate)