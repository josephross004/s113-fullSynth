function unicodeToChar(text) {
    return text.replace(/\\u[\dA-F]{4}/gi, 
           function (match) {
                return String.fromCharCode(parseInt(match.replace(/\\u/g, ''), 16));
           });
}

function run(text) {
     /*fs = require('fs');
     fs.truncate('conversion.txt',0,function(){console.log("done")})
     fs.writeFile('conversion.txt', unicodeToChar(text), function (err) {
     if (err) return console.log(err);
     console.log('Hello World > helloworld.txt');
     });*/
     return(unicodeToChar(text))
}
