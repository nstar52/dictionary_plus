const URL = "http://localhost:3000";

fetch( URL ).then(response=>response.json()).then(json=>console.log(json));